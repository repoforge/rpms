# $Id$
# Authority: dries

Summary: Screen lock and screen saver.
Name: xlockmore
Version: 5.15
Release: 1
License: BSD
Group: Amusements/Graphics
URL: http://www.tux.org/~bagleyd/xlockmore.html

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.tux.org/~bagleyd/latest/xlockmore-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: XFree86-devel, gcc-c++, esound-devel, gtk2-devel
BuildRequires: openmotif-devel, openmotif
%{?fc3:BuildRequires: xorg-x11-Mesa-libGL, xorg-x11-Mesa-libGLU}
%{?fc2:BuildRequires: xorg-x11-Mesa-libGL, xorg-x11-Mesa-libGLU}
%{?fc1:BuildRequires: XFree86-Mesa-libGL, XFree86-Mesa-libGLU}

%description
A screen locker and screen saver.

%prep
%setup

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure
%{__cat} <<EOF >%{name}.desktop
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

%build
%configure \
	--with-crypt  --enable-pam --enable-syslog \
        --disable-setuid
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 xlock/xlock %{buildroot}%{_bindir}/xlock
%{__install} -D -m0755 xmlock/xmlock %{buildroot}%{_bindir}/xmlock
%{__install} -D -m0644 xlock/xlock.man %{buildroot}%{_mandir}/man1/xlock.1
%{__install} -D -m0644 xlock/XLock.ad %{buildroot}%{_libdir}/X11/app-defaults/XLock
%{__install} -D -m0644 xmlock/XmLock.ad %{buildroot}%{_libdir}/X11/app-defaults/XmLock

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/pam.d
%{__cat} > %{buildroot}%{_sysconfdir}/pam.d/xlock << EOF
#%PAM-1.0
auth       required     pam_stack.so service=system-auth
account    required     pam_stack.so service=system-auth
password   required     pam_stack.so service=system-auth
session    required     pam_stack.so service=system-auth
EOF

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man1/xlock.1*
%{_bindir}/xlock
%{_bindir}/xmlock
%{_libdir}/X11/app-defaults/XLock
%{_libdir}/X11/app-defaults/XmLock
%config(noreplace) %{_sysconfdir}/pam.d/xlock
%{_datadir}/applications/*.desktop

%changelog
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
