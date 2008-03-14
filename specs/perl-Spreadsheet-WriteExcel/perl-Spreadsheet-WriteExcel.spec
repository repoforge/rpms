# $Id$
# Authority: dries
# Upstream: John McNamara <plan9$eircom,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Spreadsheet-WriteExcel

Summary: Write to a cross platform Excel binary file
Name: perl-Spreadsheet-WriteExcel
Version: 2.21
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Spreadsheet-WriteExcel/

Source: http://www.cpan.org/modules/by-module/Spreadsheet/Spreadsheet-WriteExcel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The Spreadsheet::WriteExcel module can be used to create a cross-
platform Excel binary file. Multiple worksheets can be added to a
workbook and formatting can be applied to cells. Text, numbers,
formulas, hyperlinks and images can be written to the cells.

TThe Excel file produced by this module is compatible with 97,
2000, 2002 and 2003.

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
find doc/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL MANIFEST META.yml README doc/ examples/
%doc %{_mandir}/man1/chartex.1*
%doc %{_mandir}/man3/Spreadsheet::WriteExcel.3pm*
%doc %{_mandir}/man3/Spreadsheet::WriteExcel::*.3pm*
%{_bindir}/chartex
%dir %{perl_vendorlib}/Spreadsheet/
%{perl_vendorlib}/Spreadsheet/WriteExcel/
%{perl_vendorlib}/Spreadsheet/WriteExcel.pm

%changelog
* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 2.21-1
- Updated to release 2.21.

* Mon Oct 22 2007 Dries Verachtert <dries@ulyssis.org> - 2.20-1
- Updated to release 2.20.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.18-1
- Updated to release 2.18.

* Tue May 24 2006 Dries Verachtert <dries@ulyssis.org> - 2.17-1
- Updated to release 2.17.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.16-1
- Updated to release 2.16.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 2.15-1
- Updated to release 2.15.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.14-1
- Updated to release 2.14.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.12-1
- Initial package.
