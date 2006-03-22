# $Id$
# Authority: dries
# Upstream: Kevin Meltzer <perlguy$perlguy,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-Htpasswd

Summary: Manage Unix crypt-style password file
Name: perl-Apache-Htpasswd
Version: 1.7
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-Htpasswd/

Source: http://search.cpan.org/CPAN/authors/id/K/KM/KMELTZ/Apache-Htpasswd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module comes with a set of methods to use with htaccess password
files. These files (and htaccess) are used to do Basic Authentication on
a web server.

The passwords file is a flat-file with login name and their associated
crypted password. You can use this for non-Apache files if you wish, but
it was written specifically for .htaccess style files.
	
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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Apache/Htpasswd.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.7-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.7-1
- Updated to release 1.7.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.6.0-1
- Updated to release 1.6.0.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.5.9-1
- Initial package.

