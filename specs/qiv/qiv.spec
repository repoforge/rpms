# $Id$

# Authority: dag

# Upstream: Adam Kopacz <adam.k@klografx.de>

Summary: Quick Image Viewer
Name: qiv
Version: 1.9
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.klografx.net/qiv/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.klografx.net/qiv/download/%{name}-%{version}-src.tgz
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

%build
%{__perl} -pi.orig -e 's|/var/tmp|%{_tmppath}|' Makefile
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1
%{__install} -m0755 qiv %{buildroot}%{_bindir}
%{__install} -m0644 qiv.1 %{buildroot}%{_mandir}/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README* intro.jpg qiv-command.example
%doc %{_mandir}/man?/*
%{_bindir}/*
     
%changelog
* Sun Dec 14 2003 Dag Wieers <dag@wieers.com> - 1.9-1
- Updated to release 1.9.

* Thu Jun 05 2003 Dag Wieers <dag@wieers.com> - 1.9-0.pre13
- Updated to release 1.9-pre13.
- Cleaned up SPEC file.

* Mon Dec 16 2002 Dag Wieers <dag@wieers.com> - 1.8-0
- Updated to release 1.8.

* Fri May 18 2001 Dag Wieers <dag@wieers.com>
- Initial package.
