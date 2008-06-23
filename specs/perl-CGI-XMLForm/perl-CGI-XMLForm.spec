# $Id$
# Authority: dries
# Upstream: Matt Sergeant <matt$sergeant,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-XMLForm

Summary: Extension of CGI.pm which reads/generates formated XML
Name: perl-CGI-XMLForm
Version: 0.10
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-XMLForm/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-XMLForm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

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
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

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
