# $Id: $

# Authority: dries
# Upstream: Björn Augustsson <d3august $ dtek , chalmers , se>
# Screenshot: http://www.dtek.chalmers.se/~d3august/xt/bigshot.jpg

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}

Summary: Graphical version of the traceroute program
Name: xtraceroute
Version: 0.9.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.dtek.chalmers.se/~d3august/xt/index.html

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.dtek.chalmers.se/~d3august/xt/dl/xtraceroute-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bind-utils, traceroute, gettext, gtk2-devel, gtk+-devel
BuildRequires: gdk-pixbuf-devel, gtkglarea
%{?_without_xorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU, XFree86-Mesa-libGL}
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGLU, xorg-x11-Mesa-libGL}

%description
Xtraceroute is a graphical version of the traceroute program, which traces
the route your IP packets travel to their destination. It displays the
routes on a rotating globe, as a series of yellow lines between 'sites',
shown as small balls of different colors. 

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall xtraceroutedatadir=%{buildroot}%{_datadir}/xtraceroute
%find_lang %{name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/xtraceroute
# %{_datadir}/applications/*.desktop

%changelog
* Tue Sep 14 2004 Dries Verachtert <dries@ulyssis.org> - 0.9.1-1
- Initial package.
