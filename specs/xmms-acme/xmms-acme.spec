# $Id: xmms-acme.spec,v 1.1 2004/02/26 17:54:31 thias Exp $

%define xmmsgeneraldir %(xmms-config --general-plugin-dir)

Summary: A useful plugin for XMMS to use special multimedia keys through acme
Name: xmms-acme
Version: 0.4.1
Release: 1.fr
License: GPL
Group: Applications/Multimedia
URL: http://www.devin.com/xmms-xf86audio/
Source: http://www.devin.com/xmms-xf86audio/download/xmms-xf86audio-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xmms >= 1.0.0, acme
BuildRequires: xmms-devel, glib-devel, gtk+-devel
Provides: xmms-xf86audio = %{version}-%{release}

%description
This plugin was written in response to demand from the users of Acme, GNOME2's
multimedia key manager.  While Acme manages the association of appropriate
keyboard scancodes with the media-control scancodes, it does not know how to
individually control the various media players.  Instead, it arranges the
mapping and expects those media players to listen for the XF86Audio keysyms.

%prep
%setup -q -n xmms-xf86audio-%{version}

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -D -m 0755 libxf86audio.so %{buildroot}%{xmmsgeneraldir}/libxf86audio.so
strip %{buildroot}%{xmmsgeneraldir}/* || :

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc COPYING README
%{xmmsgeneraldir}/libxf86audio.so

%changelog
* Tue Feb  3 2004 Matthias Saou <http://freshrpms.net/> 0.4.1-1.fr
- Initial RPM package, called xmms-acme instead of xmms-xf86audio.

