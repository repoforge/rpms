# $Id$
# Authority: dries
# Upstream: Ave Wrigley <Ave,Wrigley$itn,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Robot

Summary: Configurable web traversal engine
Name: perl-WWW-Robot
Version: 0.026
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Robot/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Robot-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This distribution contains a module which provides a web traversal engine
for use in web robots and the like. This is a beta release; the API is
open to change until a 1.000 release.

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
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/WWW/Robot.pm

%changelog
* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 0.026-1
- Updated to version 0.026.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.025-1
- Updated to release 0.025.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.024-1
- Updated to release 0.024.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.023-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.023-1
- Initial package.
