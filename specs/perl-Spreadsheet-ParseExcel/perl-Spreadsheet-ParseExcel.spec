# $Id$
# Authority: dag
# Upstream: Kawai Takanori

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Spreadsheet-ParseExcel

Summary: Get information from Excel file
Name: perl-Spreadsheet-ParseExcel
Version: 0.56
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Spreadsheet-ParseExcel/

Source: http://search.cpan.org/CPAN/authors/id/J/JM/JMCNAMARA/Spreadsheet-ParseExcel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::File)
BuildRequires: perl(IO::Scalar)
BuildRequires: perl(OLE::Storage_Lite) >= 0.19
BuildRequires: perl(Scalar::Util)
Requires: perl(IO::File)
Requires: perl(IO::Scalar)
Requires: perl(OLE::Storage_Lite) >= 0.19
Requires: perl(Scalar::Util)

%filter_from_requires /^perl*/d
%filter_setup


%description
Get information from Excel file.

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
%doc Changes MANIFEST META.yml README README_Japan.htm
%doc %{_mandir}/man3/Spreadsheet::ParseExcel.3pm*
%doc %{_mandir}/man3/Spreadsheet::ParseExcel::*.3pm*
%dir %{perl_vendorlib}/Spreadsheet/
%{perl_vendorlib}/Spreadsheet/ParseExcel/
%{perl_vendorlib}/Spreadsheet/ParseExcel.pm

%changelog
* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 0.56-1
- Updated to version 0.56.

* Thu Oct 22 2009 Christoph Maser <cmr@financial.com> - 0.55-1
- Updated to version 0.55.

* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 0.54-1
- Updated to version 0.54.

* Thu Jun 18 2009 Christoph Maser <cmr@financial.com> - 0.49-1
- Updated to version 0.49.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.32-1
- Updated to release 0.32.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.31-1
- Initial package. (using DAR)
