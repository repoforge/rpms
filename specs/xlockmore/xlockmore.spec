# $Id: $

# Authority: dries

Summary: Screen lock and screen saver.
Name: xlockmore
Version: 5.12
Release: 1
License: BSD
Group: Amusements/Graphics
URL: http://www.tux.org/~bagleyd/xlockmore.html

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.tux.org/~bagleyd/latest/xlockmore-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: XFree86-devel, gcc-c++, esound-devel, gtk2-devel, openmotif-devel, openmotif
%{?fc2:BuildRequires: xorg-x11-Mesa-libGL, xorg-x11-Mesa-libGLU}
%{?fc1:BuildRequires: XFree86-Mesa-libGL, XFree86-Mesa-libGLU}

%description
a screen locker and screen saver.
You will need to do a chmod +s /usr/bin/xlock if you want to use all the
options.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__install} -d -m 755 %{buildroot}/%{_bindir}
%{__install} -d -m 755 %{buildroot}/%{_datadir}/man/man1
%{__install} -d -m 755 %{buildroot}/%{_libdir}/X11/app-defaults
%{__install} -c -s -o root -m 755 xlock/xlock %{buildroot}/%{_bindir}
%{__install} -c -m 644 xlock/xlock.man %{buildroot}/%{_datadir}/man/man1/xlock.1
%{__install} -c -m 644 xlock/XLock.ad %{buildroot}/%{_libdir}/X11/app-defaults/XLock
%{__install} -c xmlock/xmlock %{buildroot}/%{_bindir}
%{__install} -c -m 644 xmlock/XmLock.ad %{buildroot}/%{_libdir}/X11/app-defaults/XmLock

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc README
%{_bindir}/xlock
%{_bindir}/xmlock
%{_libdir}/X11/app-defaults/XLock
%{_libdir}/X11/app-defaults/XmLock
%{_datadir}/man/man1/xlock.1.gz

%changelog
* Thu May 27 2004 Dries Verachtert <dries@ulyssis.org> 5.12-1
- update to 5.12

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 5.10-2
- cleanup of spec file

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 5.10-1
- first packaging for Fedora Core 1
