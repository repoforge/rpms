# $Id$
# Authority: dag
# Upstream: Dave Rolsky, <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-FromHash

Summary: Perl module that implements the fantastic new URI::FromHash
Name: perl-URI-FromHash
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-FromHash/

Source: http://www.cpan.org/modules/by-module/URI/URI-FromHash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
perl-URI-FromHash is a Perl module that implements the fantastic
new URI::FromHash.

This package contains the following Perl module:

    URI::FromHash

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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/URI::FromHash.3pm*
%dir %{perl_vendorlib}/URI/
#%{perl_vendorlib}/URI/FromHash/
%{perl_vendorlib}/URI/FromHash.pm

%changelog
* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 0.03-1
- Updated to version 0.03.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
