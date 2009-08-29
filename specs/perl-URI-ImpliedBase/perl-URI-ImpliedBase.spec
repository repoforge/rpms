# $Id$
# Authority: dag
# Upstream: Joe McMahon <mcmahon$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-ImpliedBase

Summary: Perl module to magically force all URIs to be absolute
Name: perl-URI-ImpliedBase
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-ImpliedBase/

Source: http://www.cpan.org/modules/by-module/URI/URI-ImpliedBase-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
# From yaml build_requires
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
BuildRequires: perl(Cwd)
BuildRequires: perl(Test::Simple) >= 0.44
BuildRequires: perl(URI)


%description
perl-URI-ImpliedBase is a Perl module to magically force all URIs
to be absolute.

This package contains the following Perl module:

    URI::ImpliedBase

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README Todo
%doc %{_mandir}/man3/URI::ImpliedBase.3pm*
%dir %{perl_vendorlib}/URI/
#%{perl_vendorlib}/URI/ImpliedBase/
%{perl_vendorlib}/URI/ImpliedBase.pm

%changelog
* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 0.07-1
- Updated to version 0.07.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Initial package. (using DAR)
