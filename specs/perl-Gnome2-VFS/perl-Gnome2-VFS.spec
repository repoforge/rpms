# $Id$
# Authority: dag
# Upstream: Torsten Schönfeld <kaffeetisch$gmx,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gnome2-VFS

Summary: Perl interface to the 2.x series of the GNOME VFS library
Name: perl-Gnome2-VFS
Version: 1.081
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
#URL: http://gtk2-perl.sourceforge.net/
URL: http://search.cpan.org/dist/Gnome2-VFS/

Source: http://www.cpan.org/modules/by-module/Gnome2/Gnome2-VFS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgnomeui-devel >= 2.0.0
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: perl(Glib)
BuildRequires: perl(Gtk2)
Requires: perl >= 2:5.8.0

%description
Perl bindings to the 2.x series of the Gnome widget set.  This module allows
you to write graphical user interfaces in a perlish and object-oriented way,
freeing you from the casting and memory management in C, yet remaining very
close in spirit to original API.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE MANIFEST MANIFEST.SKIP META.yml NEWS README copyright.pod examples/
%doc %{_mandir}/man3/Gnome2::VFS.3pm*
%doc %{_mandir}/man3/Gnome2::VFS::*.3pm*
%dir %{perl_vendorarch}/Gnome2/
%{perl_vendorarch}/Gnome2/VFS/
%{perl_vendorarch}/Gnome2/VFS.pm
%dir %{perl_vendorarch}/auto/Gnome2/
%{perl_vendorarch}/auto/Gnome2/VFS/

%changelog
* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 1.081-1
- Updated to release 1.081.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.080-1
- Updated to release 1.080.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 1.061-2
- Cosmetic cleanup.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.061-1
- Updated to release 1.061.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.060-1
- Updated to release 1.060.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.041-1
- Updated to release 1.041.

* Tue Mar 30 2004 Dag Wieers <dag@wieers.com> - 1.001-1
- Updated to release 1.001.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
