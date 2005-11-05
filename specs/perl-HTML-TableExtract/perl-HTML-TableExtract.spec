# $Id$
# Authority: dries
# Upstream: Matt Sisk <sisk$mojotoad,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-TableExtract

Summary: Extracts the text contained in tables within an HTML document
Name: perl-HTML-TableExtract
Version: 2.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-TableExtract/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSISK/HTML-TableExtract-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
HTML::TableExtract is a module that simplifies the extraction
of information contained in tables within HTML documents.

Tables of note may be specified using Headers, Depth, Count,
or some combination of the three.

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
%{perl_vendorlib}/HTML/TableExtract.pm

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.06-1
- Updated to release 2.06.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Initial package.
