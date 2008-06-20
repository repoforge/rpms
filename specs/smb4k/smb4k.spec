# $Id$
# Authority: dries

# Screenshot: http://smb4k.berlios.de/shots/0.3.0/Smb4K-0.3.0-1.png

# ExcludeDist: el3 fc1

%{?dtag: %{expand: %%define %dtag 1}}

Summary: SMB (samba) share browser for KDE
Name: smb4k
Version: 0.9.6
Release: 1
License: GPL
Group: Applications/Internet
URL: http://smb4k.berlios.de/

Source: http://download.berlios.de/smb4k/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, kdelibs-devel
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
%configure LDFLAGS="-L$QTLIB"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source "/etc/profile.d/qt.sh"
%{__make} install DESTDIR="%{buildroot}"
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
%{_bindir}/smb4k_cat
%{_bindir}/smb4k_mv
%{_libdir}/kde3/konqsidebar*
%{_libdir}/kde3/libsmb4k*
%{_libdir}/libsmb4k*
%{_datadir}/applications/kde/smb4k.desktop
%{_datadir}/apps/konqsidebartng/add/smb4k_add.desktop
%{_datadir}/apps/smb4k/
%{_datadir}/apps/smb4knetworkbrowserpart/
%{_datadir}/apps/smb4ksharesiconviewpart/
%{_datadir}/apps/smb4kshareslistviewpart/
%{_datadir}/config.kcfg/smb4k.kcfg
%{_datadir}/icons/crystalsvg/*/apps/smb4k.png

%changelog
* Thu Jun 19 2008 Dries Verachtert <dries@ulyssis.org> - 0.9.6-1
- Updated to release 0.9.6.

* Mon Jun  9 2008 Dries Verachtert <dries@ulyssis.org> - 0.9.5-1
- Updated to release 0.9.5.

* Sun Apr 27 2008 Dries Verachtert <dries@ulyssis.org> - 0.9.4-1
- Updated to release 0.9.4.

* Mon Feb 25 2008 Dries Verachtert <dries@ulyssis.org> - 0.9.3-1
- Updated to release 0.9.3.

* Sun Jan 20 2008 Dries Verachtert <dries@ulyssis.org> - 0.9.2-1
- Updated to release 0.9.2.

* Tue Jan  1 2008 Dries Verachtert <dries@ulyssis.org> - 0.9.1-1
- Updated to release 0.9.1.

* Sun Dec 16 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.0-1
- Updated to release 0.9.0.

* Thu Nov 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.7-1
- Updated to release 0.8.7.

* Wed Nov 11 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.6-1
- Updated to release 0.8.6.

* Fri Sep 28 2007 Dag Wieers <dag@wieers.com> - 0.8.5-1
- Updated to release 0.8.5.

* Mon Jul 16 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.4-1
- Updated to release 0.8.4.

* Wed May 09 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.3-1
- Updated to release 0.8.3.

* Mon Apr 16 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.1-1
- Updated to release 0.8.1.

* Sat Dec 23 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.0-1
- Updated to release 0.8.0.

* Sun Nov 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.5-1
- Updated to release 0.7.5.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.4-1
- Updated to release 0.7.4.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.3-1
- Updated to release 0.7.3.

* Fri Aug 04 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.2-1
- Updated to release 0.7.2.

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
