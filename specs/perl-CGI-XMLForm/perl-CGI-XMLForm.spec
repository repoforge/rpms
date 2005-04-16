# $Id$
# Authority: dries
# Upstream: Matt Sergeant <matt$sergeant,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-XMLForm

Summary: Extension of CGI.pm which reads/generates formated XML
Name: perl-CGI-XMLForm
Version: 0.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-XMLForm/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSERGEANT/CGI-XMLForm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module can either create form field values from XML based
on XQL style queries (full XQL is _not_ supported - this module
is designed for speed), or it can create XML from form values.
There are 2 key functions: toXML and readXML.
	
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
%{perl_vendorlib}/CGI/XMLForm.pm
%{perl_vendorlib}/CGI/XMLForm
%{perl_vendorlib}/CGI/example.pl
%{perl_vendorlib}/auto/CGI/XMLForm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Initial package.
