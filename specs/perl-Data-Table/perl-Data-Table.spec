# $Id$
# Authority: dries
# Upstream: Yingyao Zhou <easydatabase$yahoo,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Table

Summary: Table data types
Name: perl-Data-Table
Version: 1.47
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Table/

Source: http://search.cpan.org/CPAN/authors/id/E/EZ/EZDB/Data-Table-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Data/Table.pm
%{perl_vendorlib}/auto/Data/Table

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.47-1
- Updated to release 1.47.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.43-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.43-1
- Initial package.
