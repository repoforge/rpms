# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}


Summary: CableCrypt Decoder for Linux
Name: cabletv
Version: 1.3.9
Release: 0
Group: Applications/Multimedia
License: Freeware
URL: http://sector17.tvand.net/cabletv/

Source: http://sector17.tvand.net/cabletv/download/cabletv-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: nasm
#BuildRequires: liblirc-devel 
Requires: xawtv
%{?_without_xorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU}
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGLU}
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
CableTV is a CableCrypt decoder for Linux. It has been tested with BT878 cards 
under kernel 2.2.x and 2.4.0-testx, and provides full decryption of Wiener 
Telekabel Telekino (Austria), but reported to work with many stations over 
europe. It works yet only with PAL. Chroma and polarity inversion is supported. 
Supports color MMX decoding and b/w x86 assembler decoding.

%prep
%setup

%build
%{__perl} -pi.orig -e 's|(prefix)=/usr/local|$1=%{_prefix}|' Makefile
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%{__install} -D cabletv %{buildroot}%{_bindir}/cabletv
#%{__install} -D v4l-conf %{buildroot}%{_bindir}/v4l-conf
%{__install} -D CableTV.ad %{buildroot}%{_prefix}/X11R6/lib/X11/app-defaults/CableTV

#%{__make} install prefix="%{buildroot}%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Modeline.sample cabletv.sample
%{_bindir}/*
#%{_bindir}/v4l-conf
%{_prefix}/X11R6/lib/X11/app-defaults/CableTV

%changelog
* Sat Feb 08 2003 Dag Wieers <dag@wieers.com> - 1.3.9-0
- Initial package. (using DAR)
