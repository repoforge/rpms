# $Id$
# Authority: dries
# Upstream: Enrico Sorcinelli <enrys$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-SessionManager

Summary: Mod_perl 1.0/2.0 session manager extension
Name: perl-Apache-SessionManager
Version: 1.03
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-SessionManager/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-SessionManager-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This package is an HTTP session manager.
Apache::SessionManager is a mod_perl module that helps
session management of a web application. This simple module is a
wrapper around Apache::Session persistence framework for session data.
It creates a session object and makes it available to all other handlers
transparenlty by putting it in pnotes.

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
%{perl_vendorlib}/Apache/SessionManager.pm
%{perl_vendorlib}/Apache/SessionManager

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
