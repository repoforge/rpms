# $Id$
# Authority: dag
# Upstream: Karl Runge <xvml$karlrunge,com>


%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh8:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}

Summary: VNC server for the current X11 session
Name: x11vnc
Version: 0.9.9
Release: 1%{?dist}
License: GPL
Group: User Interface/X
URL: http://www.karlrunge.com/x11vnc/

Source: http://dl.sf.net/libvncserver/x11vnc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libjpeg-devel, zlib-devel
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: xorg-x11-proto-devel, libXext-devel, libXtst-devel}

%description
x11vnc is to X Window System what WinVNC is to Windows, i.e. a server
which serves the current X Window System desktop via RFB (VNC)
protocol to the user.

Based on the ideas of x0rfbserver and on LibVNCServer, it has evolved
into a versatile and performant while still easy to use program.

%prep
%setup

%build
if pkg-config openssl; then
    export CFLAGS="%{optflags} $(pkg-config --cflags openssl)"
    export LDFLAGS="$LDFLAGS $(pkg-config --libs-only-L openssl)"
#%{?_without_modxorg:export LDFLAGS="$LDFLAGS -L/usr/X11R6/lib"}
fi
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man1/x11vnc.1*
%{_bindir}/x11vnc
%{_datadir}/applications/x11vnc.desktop
%{_datadir}/x11vnc/

%changelog
* Sat Dec 26 2009 Dag Wieers <dag@wieers.com> - 0.9.9-1
- Updated to release 0.9.9.

* Fri Jul 10 2009 Dag Wieers <dag@wieers.com> - 0.9.8-1
- Updated to release 0.9.8.

* Fri Apr 03 2009 Dag Wieers <dag@wieers.com> - 0.9.7-1
- Updated to release 0.9.7.

* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.9.6-1
- Updated to release 0.9.6.

* Sat Oct 25 2008 Dag Wieers <dag@wieers.com> - 0.9.5-1
- Updated to release 0.9.5.

* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Fri Oct 05 2007 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Tue Jun 19 2007 Dag Wieers <dag@wieers.com> - 0.9.2-1
- Updated to release 0.9.2.

* Sat May 26 2007 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Fri Apr 20 2007 Dag Wieers <dag@wieers.com> - 0.9-1
- Updated to release 0.9.

* Fri Feb 02 2007 Dag Wieers <dag@wieers.com> - 0.8.4-1
- Updated to release 0.8.4.

* Sun Dec 03 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.3-2
- libXtst-devel added, thanks to Walter Neumann.

* Wed Nov 15 2006 Dag Wieers <dag@wieers.com> - 0.8.3-1
- Updated to release 0.8.3.

* Fri Jul 14 2006 Dag Wieers <dag@wieers.com> - 0.8.2-1
- Updated to release 0.8.2.

* Fri Jun 09 2006 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Updated to release 0.8.1.

* Tue Feb 14 2006 Dag Wieers <dag@wieers.com> - 0.8-1
- Updated to release 0.8.

* Thu Jul 14 2005 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Updated to release 0.7.2.

* Fri Feb 25 2005 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Thu Dec 23 2004 Dag Wieers <dag@wieers.com> - 0.7-1
- Updated to release 0.7.

* Mon Aug 02 2004 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Initial package. (using DAR)
