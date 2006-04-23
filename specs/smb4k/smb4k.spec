# $Id$
# Authority: dries

# Screenshot: http://smb4k.berlios.de/shots/0.3.0/Smb4K-0.3.0-1.png

# ExcludeDist: el3 fc1

%{?dist: %{expand: %%define %dist 1}}

Summary: SMB (samba) share browser for KDE
Name: smb4k
Version: 0.7.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://smb4k.berlios.de/

Source: http://download.berlios.de/smb4k/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel, kdelibs-devel, gcc, make
BuildRequires: gcc-c++, qt-devel, fam-devel, fam, kdebase-devel
BuildRequires: autoconf, automake
%{?fc3:BuildRequires:libselinux-devel}
%{?fc2:BuildRequires:libselinux-devel}
Requires: kdelibs, fam

%description
Smb4K is an SMB share browser for KDE. It uses the Samba software suite for
an easy access to the SMB shares of your local network neighborhood.

%prep
%setup

%build
source "/etc/profile.d/qt.sh"
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source "/etc/profile.d/qt.sh"
%{__make} install \
	DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc %{_docdir}/HTML/en/smb4k
%{_includedir}/smb4k*.h
%{_bindir}/smb4k
%{_bindir}/smb4k_kill
%{_bindir}/smb4k_mount
%{_bindir}/smb4k_umount
%{_libdir}/kde3/konqsidebar*
%{_libdir}/libsmb4k*
%{_datadir}/applications/kde/smb4k.desktop
%{_datadir}/apps/konqsidebartng/add/smb4k_add.desktop
%{_datadir}/apps/smb4k
%{_datadir}/icons/crystalsvg/*/apps/smb4k.png

%changelog
* Sun Apr 23 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.0-1
- Updated to release 0.7.0.

* Fri Apr 21 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.10-1
- Updated to release 0.6.10.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.9-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.9-1
- Updated to release 0.6.9.

* Wed Mar 01 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.8-1
- Updated to release 0.6.8.

* Mon Feb 06 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.7-1
- Updated to release 0.6.7.

* Mon Jan 09 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.5-1
- Updated to release 0.6.5.

* Wed Nov 02 2005 Dries Verachtert <dries@ulyssis.org> 0.6.4-1
- Updated to release 0.6.4.

* Fri Sep 09 2005 Dries Verachtert <dries@ulyssis.org> 0.6.3-1
- Updated to release 0.6.3.

* Tue Aug 30 2005 Dries Verachtert <dries@ulyssis.org> 0.6.2-1
- Updated to release 0.6.2.

* Mon Aug 1 2005 Dries Verachtert <dries@ulyssis.org> 0.6.1-1
- Updated to release 0.6.1.

* Sat Jun 18 2005 Dries Verachtert <dries@ulyssis.org> 0.6.0-1
- Updated to release 0.6.0.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> 0.5.2-1
- Updated to release 0.5.2.

* Thu Feb 03 2005 Dries Verachtert <dries@ulyssis.org> 0.5.1-1
- Updated to release 0.5.1.

* Tue Jan 11 2005 Dries Verachtert <dries@ulyssis.org> 0.5.0-1
- Updated to release 0.5.0.

* Wed Sep 01 2004 Dries Verachtert <dries@ulyssis.org> 0.4.1-1
- Update to version 0.4.1.

* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 0.3.1-1
- first packaging for Fedora Core 1
