# $Id$
# Authority: dag
# Distcc: 0

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define _bindir /usr/X11R6/bin

Summary: heXoNet RFB (remote control for the X Window System)
Name: rfb
Version: 0.6.1
Release: 4
License: GPL
Group: User Interface/Desktops
URL: http://www.hexonet.de/software/rfb/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://download.hexonet.com/software/rfb/%{name}-%{version}.tar.gz
Patch: rfb-0.6.1-rpmoptflags.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libxclass
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{?fc3:BuildRequires: compat-gcc-c++}
%{?fc2:BuildRequires: compat-gcc-c++}
%{?fc1:BuildRequires: compat-gcc-c++}
%{?el3:BuildRequires: compat-gcc-c++}
%{?rh9:BuildRequires: compat-gcc-c++}
%{?rh8:BuildRequires: compat-gcc-c++}

### Fix problem with apt requiring compat-gcc-c++ (Panu)
Requires: compat-libstdc++

%description
The heXoNet RFB Software package includes many different projects. The
goal of this package is to provide a comprehensive collection of
rfb-enabled tools and applications. One application, x0rfbserver, was,
and maybe still is, the only complete remote control solution for the
X Window System.

%prep
%setup
%patch0 -p1

%{__cat} <<EOF >x0rfbserver.desktop
[Desktop Entry]
Name=Run VNC Server
Comment=Make current X session available via VNC
Icon=redhat-system_tools.png
Exec=x0rfbserver
Terminal=false
Type=Application
Categories=GNOME;System;Application;
EOF

%{__cat} <<EOF >xvncconnect.desktop
[Desktop Entry]
Name=Run VNC Viewer
Comment=Connect to a VNC server
Icon=redhat-system_tools.png
Exec=xvncconnect
Terminal=false
Type=Application
Categories=GNOME;System;Application;
EOF

%build
### FIXME: Workaround for RH80 and RH9
%{?fc3:export CXXFLAGS="&>/dev/null; g++296 -D\$(USE_ZLIB) `xc-config --cflags` -I../include -finline-functions -funroll-loops %{optflags}"}
%{?fc2:export CXXFLAGS="&>/dev/null; g++296 -D\$(USE_ZLIB) `xc-config --cflags` -I../include -finline-functions -funroll-loops %{optflags}"}
%{?fc1:export CXXFLAGS="&>/dev/null; g++296 -D\$(USE_ZLIB) `xc-config --cflags` -I../include -finline-functions -funroll-loops %{optflags}"}
%{?el3:export CXXFLAGS="&>/dev/null; g++296 -D\$(USE_ZLIB) `xc-config --cflags` -I../include -finline-functions -funroll-loops %{optflags}"}
%{?rh9:export CXXFLAGS="&>/dev/null; g++296 -D\$(USE_ZLIB) `xc-config --cflags` -I../include -finline-functions -funroll-loops %{optflags}"}
%{?rh8:export CXXFLAGS="&>/dev/null; g++296 -D\$(USE_ZLIB) `xc-config --cflags` -I../include -finline-functions -funroll-loops %{optflags}"}
%{?fc1:export CXX="g++296"}
%{?el3:export CXX="g++296"}
%{?rh9:export CXX="g++296"}
%{?rh8:export CXX="g++296"}
%{__make} %{?_smp_mflags} depend all

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1 \
			%{buildroot}%{_bindir}
%{__install} -m0644 man/man1/* %{buildroot}%{_mandir}/man1
%{__install} -s -m0755 x0rfbserver/x0rfbserver %{buildroot}%{_bindir}
%{__install} -s -m0755 xvncconnect/xvncconnect %{buildroot}%{_bindir}
%{__install} -s -m0755 xrfbviewer/{xrfbviewer,xplayfbs} %{buildroot}%{_bindir}
%{__install} -s -m0755 rfbcat/rfbcat %{buildroot}%{_bindir}

%if %{?_without_freedesktop:1}0
	%{__install} -D -m0644 x0rfbserver.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/x0rfbserver.desktop
	%{__install} -D -m0644 xvncconnect.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/xvncconnect.desktop
%else
        install -d -m0755 %{buildroot}%{_datadir}/applications
        desktop-file-install --vendor "gnome"              \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
                x0rfbserver.desktop xvncconnect.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL README rfm_fbs.1.0.html
%doc %{_mandir}/man?/*
%{_bindir}/*
%{?_without_freedesktop:%{_datadir}/gnome/apps/Utilities/*.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/*.desktop}

%changelog
* Mon Jan 19 2004 Dag Wieers <dag@wieers.com> - 0.6.1-4
- Added desktop-files.
- Added requirements for compat-libstdc++.

* Tue Dec 02 2003 Dag Wieers <dag@wieers.com> - 0.6.1-3
- Rebuild against libxclass-0.8.2.

* Sat Apr 05 2003 Dag Wieers <dag@wieers.com> - 0.6.1-2
- Statically linked to libxclass, removing xclass dependency.

* Sun Dec 15 2002 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Initial package. (using DAR)
