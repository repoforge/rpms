# $Id$

# Authority: dries
# Upstream: Erick Calder <ecalder$cpan,org>

%define real_name X11-Keyboard
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Keyboard support functions for X11
Name: perl-X11-Keyboard
Version: 1.4
Release: 1
License: MIT
Group: Applications/CPAN
URL: http://search.cpan.org/dist/X11-Keyboard/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/E/EC/ECALDER/X11-Keyboard-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module make available certain keyboard functions useful to translate
keysyms and keycodes, when working with the X11::Protocol module.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/X11/Keyboard.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Initial package.
