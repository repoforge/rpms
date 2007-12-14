# $Id$
# Authority: dries
# Upstream: Yingyao Zhou <easydatabase$yahoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Table

Summary: Table data types
Name: perl-Data-Table
Version: 1.51
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Table/

Source: http://www.cpan.org/modules/by-module/Data/Data-Table-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Data type related to database tables, spreadsheets, CSV/TSV files,
HTML table displays, etc.

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
%doc Changes MANIFEST README Table.html
%doc %{_mandir}/man3/Data::Table.3pm*
%dir %{perl_vendorlib}/Data/
#%{perl_vendorlib}/Data/Table/
%{perl_vendorlib}/Data/Table.pm
%{perl_vendorlib}/auto/Data/Table

%changelog
* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 1.51-1
- Updated to release 1.51.

* Sat Sep 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.50-1
- Updated to release 1.50.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.49-1
- Updated to release 1.49.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.47-1
- Updated to release 1.47.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.43-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.43-1
- Initial package.
