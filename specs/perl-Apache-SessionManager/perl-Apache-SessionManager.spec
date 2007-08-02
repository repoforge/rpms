# $Id$
# Authority: dries
# Upstream: Enrico Sorcinelli <enrys$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-SessionManager

Summary: Mod_perl 1.0/2.0 session manager extension
Name: perl-Apache-SessionManager
Version: 1.03
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-SessionManager/

Source: http://search.cpan.org/CPAN/authors/id/E/EN/ENRYS/Apache-SessionManager-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

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
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Apache/SessionManager.pm
%{perl_vendorlib}/Apache/SessionManager

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.03-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
