# $Id$
# Authority: dag
# Upstream: Karl Runge <xvml$karlrunge,com>

Summary: VNC server for the current X11 session
Name: x11vnc
Version: 0.7.1
Release: 1
License: GPL
Group: User Interface/X
URL: http://www.karlrunge.com/x11vnc/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source:	http://dl.sf.net/libvncserver/x11vnc-%{version}.tar.gz
# Source0-md5: b03ba2f34355a4e3c2e0420af2065703
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: XFree86-devel, libjpeg-devel, zlib-devel

%description
x11vnc is to X Window System what WinVNC is to Windows, i.e. a server
which serves the current X Window System desktop via RFB (VNC)
protocol to the user.

Based on the ideas of x0rfbserver and on LibVNCServer, it has evolved
into a versatile and performant while still easy to use program.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man1/x11vnc.1*
%{_bindir}/x11vnc
%{_datadir}/x11vnc/

%changelog
* Fri Feb 25 2005 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Thu Dec 23 2004 Dag Wieers <dag@wieers.com> - 0.7-1
- Updated to release 0.7.

* Mon Aug 02 2004 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Initial package. (using DAR)
