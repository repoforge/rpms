# $Id$
# Authority: dries


%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

%{!?dtag:%define _with_lesstif 1}
%{?el5:%define _with_openmotif 1}
%{?fc6:%define _with_lesstif 1}
%{?fc5:%define _with_openmotif 1}
%{?fc4:%define _with_openmotif 1}
%{?fc3:%define _with_lesstif 1}
%{?el4:%define _with_openmotif 1}
%{?el3:%define _with_openmotif 1}
%{?el2:%define _with_lesstif 1}

%define desktop_vendor rpmforge

Summary: Screen lock and screen saver.
Name: xlockmore
Version: 5.28
Release: 1%{?dist}
License: BSD
Group: Amusements/Graphics
URL: http://www.tux.org/~bagleyd/xlockmore.html

Source: http://www.tux.org/~bagleyd/xlock/xlockmore-%{version}/xlockmore-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, esound-devel, gtk2-devel, pam-devel
BuildRequires: desktop-file-utils
%{?_with_lesstif:BuildRequires: lesstif-devel}
%{?_with_openmotif:BuildRequires: openmotif-devel}
%if 0%{?_without_modxorg:1}
%{?_without_xorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU}
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGLU}
%else
BuildRequires: mesa-libGLU-devel
%endif

%description
A screen locker and screen saver.

%prep
%setup

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure

%{__cat} <<EOF >xlockmore.desktop
[Desktop Entry]
Name=Xlock
Comment=Screen Saver
Encoding=UTF-8
Icon=gnome-lockscreen.png
Exec=xlock
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;Graphics;
EOF

%{__cat} <<EOF >xlock.pam
#%PAM-1.0
auth		required	pam_stack.so service=system-auth
account		required	pam_stack.so service=system-auth
password	required	pam_stack.so service=system-auth
session		required	pam_stack.so service=system-auth
EOF


%build
%configure \
	--with-crypt \
	--enable-pam \
        --disable-setuid \
	--enable-syslog
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 xlock/xlock %{buildroot}%{_bindir}/xlock
%{__install} -Dp -m0755 xmlock/xmlock %{buildroot}%{_bindir}/xmlock
%{__install} -Dp -m0644 xlock/xlock.man %{buildroot}%{_mandir}/man1/xlock.1
%{__install} -Dp -m0644 xlock/XLock.ad %{buildroot}%{_libdir}/X11/app-defaults/XLock
%{__install} -Dp -m0644 xmlock/XmLock.ad %{buildroot}%{_libdir}/X11/app-defaults/XmLock
%{__install} -Dp -m0644 xlock.pam %{buildroot}%{_sysconfdir}/pam.d/xlock

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install \
	--vendor %{desktop_vendor}                 \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	xlockmore.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man1/xlock.1*
%config(noreplace) %{_sysconfdir}/pam.d/xlock
%{_bindir}/xlock
%{_bindir}/xmlock
%{_libdir}/X11/app-defaults/XLock
%{_libdir}/X11/app-defaults/XmLock
%{_datadir}/applications/%{desktop_vendor}-xlockmore.desktop

%changelog
* Sun Jul 12 2009 Dries Verachtert <dries@ulyssis.org> - 5.28-1
- Updated to release 5.28.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 5.18-2.2
- Rebuild for Fedora Core 5.

* Thu Jul 28 2005 Dries Verachtert <dries@ulyssis.org> - 5.18-2
- Fixed the name of the desktop file (thanks to Erik Williamson)

* Mon Jun 20 2005 Dries Verachtert <dries@ulyssis.org> - 5.18-1
- Update to release 5.18.

* Tue Mar 22 2005 Dag Wieers <dag@wieers.com> - 5.15-2
- Fixed garbage from /etc/pam.d/xlock. (Zamil M. Cavalcanti)

* Thu Feb 24 2005 Adrian Reber <adrian@lisas.de> - 5.15-1
- update to 5.15
- build with pam support
- added .desktop file

* Sun Dec 12 2004 Dries Verachtert <dries@ulyssis.org> 5.14.1-1
- Update to release 5.14.1.

* Thu Oct 28 2004 Dries Verachtert <dries@ulyssis.org> 5.13-1
- update to release 5.13

* Thu May 27 2004 Dries Verachtert <dries@ulyssis.org> 5.12-1
- update to 5.12

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 5.10-2
- cleanup of spec file

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 5.10-1
- first packaging for Fedora Core 1
