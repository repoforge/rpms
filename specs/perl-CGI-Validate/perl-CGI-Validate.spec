# $Id$
# Authority: dries
# Upstream: Byron Brummer <zenin$bawdycaste,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Validate

Summary: Advanced CGI form parser and type validation
Name: perl-CGI-Validate
Version: 2.000
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Validate/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Validate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The basic concept of this module is to combine the best features of the
CGI and Getopt::Long modules. The CGI module is great for parsing,
building, and rebuilding forms, however it lacks any real error checking
abilitys such as misspelled form input names, the data types received
from them, missing values, etc. This however, is something that the
Getopt::Long module is vary good at doing. So, basicly this module is a
layer that collects the data using the CGI module and passes it to
routines to do type validation and name consistency checks all in one
clean try/catch style block.

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
%{perl_vendorlib}/CGI/Validate.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.000-1
- Initial package.
