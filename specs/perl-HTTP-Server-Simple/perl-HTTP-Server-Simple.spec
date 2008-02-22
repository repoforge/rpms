# $Id$
# Authority: dries
# Upstream: Jesse Vincent <jesse+cpan$fsck,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Server-Simple

Summary: Simple standalone HTTP daemon
Name: perl-HTTP-Server-Simple
Version: 0.29
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Server-Simple/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-Server-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
HTTP::Server::Simple is a very simple standalone HTTP daemon with no non-core
module dependencies.  It's ideal for building a standalone http-based UI to
your existing tools.

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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/HTTP::Server::Simple.3pm*
%doc %{_mandir}/man3/HTTP::Server::Simple::*.3pm*
%dir %{perl_vendorlib}/HTTP/
%dir %{perl_vendorlib}/HTTP/Server/
%{perl_vendorlib}/HTTP/Server/Simple/
%{perl_vendorlib}/HTTP/Server/Simple.pm

%changelog
* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 0.29-1
- Updated to release 0.29.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.28-1
- Updated to release 0.28.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.27-1
- Updated to release 0.27.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.26-1
- Updated to release 0.26.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Updated to release 0.23.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Updated to release 0.20.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Updated to release 0.18.

* Sat Dec 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Initial package.
