# $Id$
# Authority: matthias

%define xmms_generaldir %(xmms-config --general-plugin-dir 2>/dev/null || echo %{_libdir}/xmms/General)

Summary: XMMS plugin to use special multimedia keys in GNOME or through acme
Name: xmms-acme
Version: 0.4.2
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.devin.com/xmms-xf86audio/
Source: http://www.devin.com/xmms-xf86audio/download/xmms-xf86audio-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xmms >= 1.0.0
BuildRequires: xmms-devel, glib-devel, gtk+-devel
Provides: xmms-xf86audio = %{version}-%{release}

%description
This plugin was written in response to demand from the users of Acme, GNOME2's
multimedia key manager.  While Acme manages the association of appropriate
keyboard scancodes with the media-control scancodes, it does not know how to
individually control the various media players.  Instead, it arranges the
mapping and expects those media players to listen for the XF86Audio keysyms.


%prep
%setup -n xmms-xf86audio-%{version}


%build
%{__make} %{?_smp_mflags} OPT="%{optflags} -fPIC"


%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m 0755 libxf86audio.so \
    %{buildroot}%{xmms_generaldir}/libxf86audio.so


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{xmms_generaldir}/libxf86audio.so


%changelog
* Mon Oct 25 2004 Matthias Saou <http://freshrpms.net/> 0.4.2-1
- Update to 0.4.2.

* Mon Jul  5 2004 Matthias Saou <http://freshrpms.net/> 0.4.1-3
- Fix for x86_64.

* Thu May 20 2004 Matthias Saou <http://freshrpms.net/> 0.4.1-2
- Removed explicit acme dependency as GNOME 2.6 has the key mapping built in.
- Removed explicit stripping, that goes into the debuginfo package.

* Tue Feb  3 2004 Matthias Saou <http://freshrpms.net/> 0.4.1-1
- Initial RPM package, called xmms-acme instead of xmms-xf86audio.

