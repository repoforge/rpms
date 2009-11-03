# $Id$
# Authority: dries
# Upstream: Erick Calder <ecalder$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name X11-Keyboard

Summary: Keyboard support functions for X11
Name: perl-X11-Keyboard
Version: 1.4
Release: 1.2%{?dist}
License: MIT
Group: Applications/CPAN
URL: http://search.cpan.org/dist/X11-Keyboard/

Source: http://www.cpan.org/modules/by-module/X11/X11-Keyboard-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module make available certain keyboard functions useful to translate
keysyms and keycodes, when working with the X11::Protocol module.

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
%dir %{perl_vendorlib}/X11/
%{perl_vendorlib}/X11/Keyboard.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Initial package.
