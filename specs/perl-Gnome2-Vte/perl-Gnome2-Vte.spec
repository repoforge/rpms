# $Id$
# Authority: dries
# Upstream: Torsten Schönfeld <kaffeetisch$gmx,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gnome2-Vte

Summary: Interface to the Virtual Terminal Emulation library
Name: perl-Gnome2-Vte
Version: 0.09
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gnome2-Vte/

Source: http://www.cpan.org/modules/by-module/Gnome2/Gnome2-Vte-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl-ExtUtils-Depends
BuildRequires: perl-ExtUtils-PkgConfig
BuildRequires: perl-Glib
BuildRequires: perl-Gtk2
BuildRequires: pkgconfig
BuildRequires: gtk2-devel
BuildRequires: vte-devel
BuildRequires: zlib-devel
BuildRequires: perl(Cairo::Install::Files)

%description
This module allows you to use the Virtual Terminal Emulation library (libvte
for short) from Perl.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE README
%{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Gnome2/
%{perl_vendorarch}/Gnome2/Vte.pm
%{perl_vendorarch}/Gnome2/Vte/
%dir %{perl_vendorarch}/auto/Gnome2/
%{perl_vendorarch}/auto/Gnome2/Vte/

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.09-1
- Updated to version 0.09.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Updated to release 0.08.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Updated to release 0.06.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Updated to release 0.05.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Updated to release 0.04.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
