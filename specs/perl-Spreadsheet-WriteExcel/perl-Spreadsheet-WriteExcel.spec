# $Id$
# Authority: dries
# Upstream: John McNamara <plan9$eircom,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Spreadsheet-WriteExcel

Summary: Write formatted text and numbers to a cross-platform Excel binary file
Name: perl-Spreadsheet-WriteExcel
Version: 2.16
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Spreadsheet-WriteExcel/

Source: http://search.cpan.org/CPAN/authors/id/J/JM/JMCNAMARA/Spreadsheet-WriteExcel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man?/*
%{_bindir}/chartex
%{perl_vendorlib}/Spreadsheet/WriteExcel.pm
%{perl_vendorlib}/Spreadsheet/WriteExcel

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.16-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.16-1
- Updated to release 2.16.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 2.15-1
- Updated to release 2.15.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.14-1
- Updated to release 2.14.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.12-1
- Initial package.
