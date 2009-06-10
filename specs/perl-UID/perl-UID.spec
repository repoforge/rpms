# $Id$
# Authority: dag
# Upstream: David Green <plato$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UID

Summary: Define unique identifier objects that can be used like a kind of keyword
Name: perl-UID
Version: 0.24
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UID/

Source: http://www.cpan.org/authors/id/P/PL/PLATO/UID-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)

%description
Define unique identifier objects that can be used like a kind of keyword.

This package contains the following Perl module:

    UID

%prep
%setup -n %{real_name}-%{version}

%build
#%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
#%{__make} %{?_smp_mflags}
%{__perl} Build.PL
./Build

%install
%{__rm} -rf %{buildroot}
#%{__make} pure_install
PERL_INSTALL_ROOT="%{buildroot}" ./Build install installdirs="vendor"

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/UID.3pm*
#%{perl_vendorlib}/UID/
%{perl_vendorlib}/UID.pm

%changelog
* Wed Jun 10 2009 Christoph Maser <cmr@financial.com> - 0.24-1
- Updated to version 0.24.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.21-1
- Initial package. (using DAR)
