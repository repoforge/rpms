# $Id$

# Authority: dag

Summary: Displays a given file anywhere on your X root window.
Name: root-tail
Version: 0.9
Release: 0
License: GPL
Group: System Environment/Base
URL: http://goof.com/pcg/marc/root-tail.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://goof.com/pcg/marc/data/root-tail-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: XFree86-devel

%description
Displays a given file anywhere on your X11 root window with a transparent
background. It was made because I'm very lazy and this was easier than
making a new rxvt pixmap each time I changed my background to simulate
that transparent effect.

%prep
%setup

%build
xmkmf -a
export CFLAGS="%{optflags}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/
%{__install} -m0755 root-tail %{buildroot}%{_bindir}
%{__install} -m0644 root-tail.man %{buildroot}%{_mandir}/man1/root-tail.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 0.9-0
- Updated to release 0.9.

* Sun Feb 22 2004 Dag Wieers <dag@wieers.com> - 0.2-1
- Fixed a problem with the manpage install. (Evgeney Dushistov)

* Wed Oct 08 2003 Dag Wieers <dag@wieers.com> - 0.2-0
- Initial package. (using DAR)
