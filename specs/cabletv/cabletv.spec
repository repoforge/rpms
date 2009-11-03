# $Id$
# Authority: dag

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
%{?yd3:%define _without_modxorg 1}

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
Release: 0.2%{?dist}
Group: Applications/Multimedia
License: Freeware
URL: http://sector17.tvand.net/cabletv/

Source: http://sector17.tvand.net/cabletv/download/cabletv-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: nasm
#BuildRequires: liblirc-devel
Requires: xawtv
%if 0%{?_without_modxorg:1}
%{?_without_xorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU}
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGLU}
%else
BuildRequires: mesa-libGLU-devel, libXaw-devel, libXt-devel 
%endif

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

%{__install} -Dp cabletv %{buildroot}%{_bindir}/cabletv
#%{__install} -Dp v4l-conf %{buildroot}%{_bindir}/v4l-conf
%{__install} -Dp CableTV.ad %{buildroot}%{_prefix}/X11R6/lib/X11/app-defaults/CableTV

#%{__make} install prefix="%{buildroot}%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc cabletv.sample Modeline.sample README
%{_bindir}/*
#%{_bindir}/v4l-conf
%{_prefix}/X11R6/lib/X11/app-defaults/CableTV

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.9-0.2
- Rebuild for Fedora Core 5.

* Sat Feb 08 2003 Dag Wieers <dag@wieers.com> - 1.3.9-0
- Initial package. (using DAR)
