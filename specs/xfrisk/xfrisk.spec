# $Id$
# Authority: dag
# Upstream: <xfrisk-devel$tuxick,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

Summary: Multi-user network version of the classic "Risk"
Name: xfrisk
Version: 1.2
Release: 0.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://tuxick.net/xfrisk/

Source: http://tuxick.net/xfrisk/files/XFrisk-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: Xaw3d-devel
%{!?_without_modxorg:BuildRequires: libX11-devel, Xaw3d-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

Obsoletes: XFrisk

%description
XFrisk is a computer version of the classic Risk board game. It is
a multiplayer game played on a TCP/IP network, uses the X11 window
system for graphics and runs on most UNIX and UNIX-like platforms.

%prep
%setup -n XFrisk

%build
%{__make} %{?_smp_mflags} \
	PREFIX="%{_prefix}" \
	BINDIR="%{_bindir}" \
	LIBDIR="%{_libdir}/xfrisk"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	BINDIR="%{buildroot}%{_bindir}" \
	LIBDIR="%{buildroot}%{_libdir}/xfrisk"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS ChangeLog COPYING FAQ README.NEW TODO
%{_bindir}/*
%{_libdir}/xfrisk/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-0.2
- Rebuild for Fedora Core 5.

#- Updated URL and Source-tag. (Anthony Joseph Seward)

* Sat Feb 15 2003 Dag Wieers <dag@wieers.com> - 1.2-0
- Initial package. (using DAR)
