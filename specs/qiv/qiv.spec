# $Id$
# Authority: dag
# Upstream: Adam Kopacz <adam,k$klografx,de>

Summary: Quick Image Viewer
Name: qiv
Version: 2.0
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.klografx.net/qiv/

Source: http://www.klografx.net/qiv/download/qiv-%{version}-src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: imlib-devel, gtk+-devel

%description
Quick Image Viewer (qiv) is a very small and fast GDK/Imlib image
viewer designed to replace the classic image viewers like xv or
xloadimage. It features setting an image as an x11 background with a
user-definable background color, fullscreen viewing, a screensaver mode,
brightness/contrast/gamma correction, real transparency, zoom, slideshow,
and more.

%prep
%setup

%{__cat} <<'EOF' >qiv.sh
#!/bin/sh
### http://bugs.xmms.org/show_bug.cgi?id=1907.
exec env XLIB_SKIP_ARGB_VISUALS=1 %{_libexecdir}/qiv "$@"
EOF

%build
%{__perl} -pi.orig -e 's|/var/tmp|%{_tmppath}|' Makefile
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 qiv %{buildroot}%{_libexecdir}/qiv
%{__install} -Dp -m0755 qiv.sh %{buildroot}%{_bindir}/qiv
%{__install} -Dp -m0644 qiv.1 %{buildroot}%{_mandir}/man1/qiv.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README* intro.jpg qiv-command.example
%doc %{_mandir}/man1/qiv.1*
%{_bindir}/qiv
%{_libexecdir}/qiv

%changelog
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
