# $Id$
# Authority: dries

Summary: Screen lock and screen saver.
Name: xlockmore
Version: 5.14.1
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
a screen locker and screen saver.
You will need to do a chmod +s /usr/bin/xlock if you want to use all the
options.

%prep
%setup

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure

%build
%configure \
	--with-crypt
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 xlock/xlock %{buildroot}%{_bindir}/xlock
%{__install} -D -m0755 xmlock/xmlock %{buildroot}%{_bindir}/xmlock
%{__install} -D -m0644 xlock/xlock.man %{buildroot}%{_mandir}/man1/xlock.1
%{__install} -D -m0644 xlock/XLock.ad %{buildroot}%{_libdir}/X11/app-defaults/XLock
%{__install} -D -m0644 xmlock/XmLock.ad %{buildroot}%{_libdir}/X11/app-defaults/XmLock

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

%changelog
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
