# $Id$

# Authority: dries
# Upstream: 
# Screenshot: http://www.dooglio.net/VncSelector/screenshot.png

Summary: Manage a list of currently active VNC server sessions
Name: vncselector
Version: 1.6
Release: 1
License: GPL
Group: User Interface/Desktops
URL: http://www.dooglio.net/VncSelector/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# Source: http://www.dooglio.net/VncSelector/VncSelector_%{version}.tar.gz
# Source: http://dl.sf.net/vncselector/VncSelector_1.6.tar.gz
Source: http://vncselector.sourceforge.net/VncSelector_%{version}.tar.gz
BuildRequires: fltk-devel, gcc-c++, XFree86-devel, autoconf, automake
Requires: fltk

%description
VncSelector allows a user to manage his/her list of currently active VNC
server sessions. This can be useful in a thin client situation (run from
.Xsession, for example). 

%prep
%{__rm} -rf %{buildroot}
%setup -n VncSelector_%{version}

%build
%{__make} -f Makefile.cvs
%{__perl} -npi -e "s/xtightvncviewer/vncviewer/g;" src/VncOptions.cxx
%{__perl} -npi -e "s/tightvncserver/vncserver/g;" src/VncOptions.cxx
%configure LDFLAGS="-L/lib -L/usr/lib -L/usr/X11R6/lib"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 755 src/vncselector %{buildroot}%{_bindir}/vncselector

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_bindir}/*

%changelog
* Sat Oct 02 2004 Dries Verachtert <dries@ulyssis.org> 1.6-1
- update to version 1.6.

* Mon May 24 2004 Dries Verachtert <dries@ulyssis.org> 1.2-1
- first packaging for Fedora Core 1
