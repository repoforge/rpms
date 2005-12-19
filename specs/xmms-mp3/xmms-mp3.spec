# $Id$
# Authority: matthias

Summary: XMMS plugin for mp3 playback.
Name: xmms-mp3
Version: 1.2.10
Release: 12
Epoch: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.xmms.org/
Source: http://www.xmms.org/files/1.2.x/xmms-%{version}.tar.bz2
Patch: xmms-1.2.10-gcc4.patch
Requires: xmms = 1.2.10
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk+-devel

%description
This is the mp3 plugin for XMMS that was removed from Fedora Core and Red Hat
Linux because the patented mp3 format itself is theoretically GPL incompatible.


%prep
%setup -n xmms-%{version}
%patch -p1 -b .gcc4


%build
%configure \
    --disable-opengl
%{__make}


%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 0755 ./Input/mpg123/.libs/libmpg123.so \
    %{buildroot}%{_libdir}/xmms/Input/libmpg123.so


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%dir %{_libdir}/xmms/Input/
%{_libdir}/xmms/Input/libmpg123.so


%changelog
* Tue Dec 20 2005 Matthias Saou <http://freshrpms.net/> 1:1.2.10-12
- Split off xmms-mp3 in a separate source package at last. Yes, we rebuild
  the entire xmms to get it... but it saves hacking out only the mpg123
  plugin source from the original tarball.

