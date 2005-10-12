# $Id$
# Authority: dries
# Upstream: Richard Clamp <richardc$unixbeard,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Server-HTTP

Summary: Foundation of a POE HTTP Daemon
Name: perl-POE-Component-Server-HTTP
Version: 0.07
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Server-HTTP/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Server-HTTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module is a foundation of a POE HTTP Daemon.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Server/
%{perl_vendorlib}/POE/Component/Server/HTTP.pm
%{perl_vendorlib}/POE/Component/Server/HTTP/

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Updated to release 0.06.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.05
- Initial package.
