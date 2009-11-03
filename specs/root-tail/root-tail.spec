# $Id$
# Authority: dag
# Upstream: Marc Lehmann <chris,moore$mail,com>


%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh8:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}

Summary: Displays a given file anywhere on your X root window
Name: root-tail
Version: 1.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://root-tail.plan9.de/

Source: http://goof.com/pcg/marc/data/root-tail-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: imake, libXext-devel}

%description
Displays a given file anywhere on your X11 root window with a transparent
background. It was made because I'm very lazy and this was easier than
making a new rxvt pixmap each time I changed my background to simulate
that transparent effect.

%prep
%setup

%build
xmkmf -a
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 root-tail %{buildroot}%{_bindir}/root-tail
%{__install} -Dp -m0644 root-tail.man %{buildroot}%{_mandir}/man1/root-tail.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Updated to release 1.2.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1-1.2
- Rebuild for Fedora Core 5.

* Thu Apr 08 2004 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Fri Apr 02 2004 Dag Wieers <dag@wieers.com> - 0.95-1
- Updated to release 0.95.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 0.9-0
- Updated to release 0.9.

* Sun Feb 22 2004 Dag Wieers <dag@wieers.com> - 0.2-1
- Fixed a problem with the manpage install. (Evgeney Dushistov)

* Wed Oct 08 2003 Dag Wieers <dag@wieers.com> - 0.2-0
- Initial package. (using DAR)
