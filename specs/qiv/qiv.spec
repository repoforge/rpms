# $Id$
# Authority: dag
# Upstream: Adam Kopacz <adam,k$klografx,de>

Summary: Quick Image Viewer
Name: qiv
Version: 2.2.3
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://spiegl.de/qiv/

Source: http://spiegl.de/qiv/download/qiv-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel
BuildRequires: imlib-devel

%description
Quick Image Viewer (qiv) is a very small and fast GDK/Imlib image
viewer designed to replace the classic image viewers like xv or
xloadimage. It features setting an image as an x11 background with a
user-definable background color, fullscreen viewing, a screensaver mode,
brightness/contrast/gamma correction, real transparency, zoom, slideshow,
and more.

%prep
%setup

%build
%{__perl} -pi.orig -e '
        s|/var/tmp|%{_tmppath}|g;
        s|/lib\b|/%{_lib}|g;
    ' Makefile
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 qiv %{buildroot}%{_bindir}/qiv
%{__install} -Dp -m0644 qiv.1 %{buildroot}%{_mandir}/man1/qiv.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README* intro.jpg qiv-command.example
%doc %{_mandir}/man1/qiv.1*
%{_bindir}/qiv

%changelog
* Mon Feb 22 2010 Dag Wieers <dag@wieers.com> - 2.2.3-1
- Updated to release 2.2.3-1

* Sat May 05 2007 Dag Wieers <dag@wieers.com> - 2.0-2
- Workaround for http://bugs.xmms.org/show_bug.cgi?id=1907.

* Sat May 22 2004 Dag Wieers <dag@wieers.com> - 2.0-1
- Updated to release 2.0.

* Sun Dec 14 2003 Dag Wieers <dag@wieers.com> - 1.9-1
- Updated to release 1.9.

* Thu Jun 05 2003 Dag Wieers <dag@wieers.com> - 1.9-0.pre13
- Updated to release 1.9-pre13.
- Cleaned up SPEC file.

* Mon Dec 16 2002 Dag Wieers <dag@wieers.com> - 1.8-0
- Updated to release 1.8.

* Fri May 18 2001 Dag Wieers <dag@wieers.com>
- Initial package.
