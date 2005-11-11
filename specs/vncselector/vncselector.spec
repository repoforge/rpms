# $Id$

# Authority: dries
# Upstream: 
# Screenshot: http://www.dooglio.net/VncSelector/screenshot.png

# DistExclude: el3

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}

Summary: Manage a list of currently active VNC server sessions
Name: vncselector
Version: 1.6.1
Release: 2
License: GPL
Group: User Interface/Desktops
URL: http://www.dooglio.net/VncSelector/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# Source: http://www.dooglio.net/VncSelector/VncSelector_%{version}.tar.gz
Source: http://dl.sf.net/vncselector/vncselector_%{version}.tar.gz
# Source: http://vncselector.sourceforge.net/VncSelector_%{version}.tar.gz
BuildRequires: fltk-devel, gcc-c++, autoconf, automake
BuildRequires: libtool
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}
Requires: fltk

%description
VncSelector allows a user to manage his/her list of currently active VNC
server sessions. This can be useful in a thin client situation (run from
.Xsession, for example). 

%prep
%{__rm} -rf %{buildroot}
%setup -n %{name}_%{version}

%build
%{__perl} -npi -e "s/xtightvncviewer/vncviewer/g;" src/VncOptions.cxx
%{__perl} -npi -e "s/tightvncserver/vncserver/g;" src/VncOptions.cxx
%configure LDFLAGS="-L/lib -L/usr/lib -L/usr/X11R6/lib"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m 755 src/vncselector %{buildroot}%{_bindir}/vncselector

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_bindir}/*

%changelog
* Tue Nov 08 2005 Dries Verachtert <dries@ulyssis.org> 1.6.1-2
- Source url fixed.

* Fri Oct 28 2005 Dries Verachtert <dries@ulyssis.org> 1.6.1-1
- update to version 1.6.1.

* Sat Oct 02 2004 Dries Verachtert <dries@ulyssis.org> 1.6-1
- update to version 1.6.

* Mon May 24 2004 Dries Verachtert <dries@ulyssis.org> 1.2-1
- first packaging for Fedora Core 1
