# $Id$

# Authority: dries
# Upstream: Torsten Schönfeld <kaffeetisch$gmx,de>

%define real_name Gnome2-Vte
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Interface to the Virtual Terminal Emulation library
Name: perl-Gnome2-Vte
Version: 0.04
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gnome2-Vte/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/T/TS/TSCH/Gnome2-Vte-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl-ExtUtils-Depends, perl-ExtUtils-PkgConfig
BuildRequires: perl-Glib, perl-Gtk2, pkgconfig, gtk2-devel, vte-devel
BuildRequires: zlib-devel

%description
This module allows you to use the Virtual Terminal Emulation library (libvte
for short) from Perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README LICENSE ChangeLog
%{_mandir}/man3/*
%{perl_vendorarch}/Gnome2/Vte.pm
%{perl_vendorarch}/Gnome2/Vte
%{perl_vendorarch}/auto/Gnome2/Vte/Vte.bs
%{perl_vendorarch}/auto/Gnome2/Vte/Vte.so

%changelog
* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Updated to release 0.04.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
