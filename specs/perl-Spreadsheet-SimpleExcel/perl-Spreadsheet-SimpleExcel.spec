# $Id$
# Authority: dries
# Upstream: Renee Baecker <module$renee-baecker,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Spreadsheet-SimpleExcel

Summary: Show excel-files on the web
Name: perl-Spreadsheet-SimpleExcel
Version: 1.9
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Spreadsheet-SimpleExcel/

Source: http://www.cpan.org/modules/by-module/Spreadsheet/Spreadsheet-SimpleExcel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module is used to show data in excel-files in the web. It can be used
to provide the results of a database query as an excel-file. It does not provide
cell-formats yet, but the module will be extended within the next weeks.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Spreadsheet::SimpleExcel.3pm*
%dir %{perl_vendorlib}/Spreadsheet/
#%{perl_vendorlib}/Spreadsheet/SimpleExcel/
%{perl_vendorlib}/Spreadsheet/SimpleExcel.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.9-1
- Updated to release 1.9.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.1-1
- Updated to release 1.1.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Initial package.
