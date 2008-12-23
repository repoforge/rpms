# $Id$
# Authority: dries
# Upstream: brian d foy <bdfoy$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Business-ISBN-Data

Summary: Data pack for Business::ISBN
Name: perl-Business-ISBN-Data
Version: 20081020
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Business-ISBN-Data/

Source: http://www.cpan.org/modules/by-module/Business/Business-ISBN-Data-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a data pack for Business::ISBN.  You can update
the ISBN data without changing the version of Business::ISBN.
Most of the interesting stuff is in Business::ISBN.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Business::ISBN::Data.3*
%dir %{perl_vendorlib}/Business/
%dir %{perl_vendorlib}/Business/ISBN/
#%{perl_vendorlib}/Business/ISBN/Data/
%{perl_vendorlib}/Business/ISBN/Data.pm

%changelog
* Mon Dec 22 2008 Dag Wieers <dag@wieers.com> - 20081020-1.
- Updated to release 20081020.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Updated to release 1.14.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Updated to release 1.13.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Updated to release 1.10.

* Sun Mar  6 2005 Dries Verachtert <dries@ulyssis.org> - 1.09-1
- Initial package.
