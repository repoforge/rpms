# $Id$

# Authority: dag

Summary: CableCrypt Decoder for Linux
Name: cabletv
Version: 1.3.9
Release: 0
Group: Applications/Multimedia
License: Freeware
URL: http://sector17.tvand.net/cabletv/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://sector17.tvand.net/cabletv/download/cabletv-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: nasm
#BuildRequires: liblirc-devel 

Requires: xawtv

%description
CableTV is a CableCrypt decoder for Linux. It has been tested with BT878 cards 
under kernel 2.2.x and 2.4.0-testx, and provides full decryption of Wiener 
Telekabel Telekino (Austria), but reported to work with many stations over 
europe. It works yet only with PAL. Chroma and polarity inversion is supported. 
Supports color MMX decoding and b/w x86 assembler decoding.

%prep
%setup

%build
%{__perl} -pi -e 's#prefix=/usr/local#prefix=%{_prefix}#' Makefile
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir} \
	%{buildroot}%{_prefix}/X11R6/lib/X11/app-defaults

%{__install} cabletv %{buildroot}%{_bindir}
#%{__install} v4l-conf %{buildroot}%{_bindir}
%{__install} CableTV.ad %{buildroot}%{_prefix}/X11R6/lib/X11/app-defaults/CableTV

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
