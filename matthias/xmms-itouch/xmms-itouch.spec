# $Id: xmms-itouch.spec,v 1.1 2004/02/26 17:54:31 thias Exp $

%define xmmsgeneraldir %(xmms-config --general-plugin-dir)
%define xmmsdatadir    %(xmms-config --data-dir)

Summary: A useful plugin for XMMS to use special keyboard multimedia keys
Name: xmms-itouch
Version: 0.1.2
Release: 4.fr
License: GPL
Group: Applications/Multimedia
URL: http://www.saunalahti.fi/~syrjala/xmms-itouch/
Source: http://www.saunalahti.fi/~syrjala/xmms-itouch/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xmms >= 1.0.0, glib >= 1.2.7, gtk+ >= 1.2.7
BuildPrereq: xmms-devel

%description
With this XMMS plugin you can take advantage of the multimedia (playback and
volume control) keys on your Logitech iTouch keyboard. When the plugin is
used you can use the keys regardless of the current input focus. The plugin
won't work if some other application (eg. xscreensaver) has grabbed the
keyboard.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install \
    libdir=%{buildroot}%{xmmsgeneraldir} \
    datadir=%{buildroot}%{xmmsdatadir}
strip %{buildroot}%{xmmsgeneraldir}/* || :

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING README
%exclude %{xmmsgeneraldir}/libitouch.la
%{xmmsgeneraldir}/libitouch.so
%config %{xmmsdatadir}/xmms-itouch.config

%changelog
* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.1.2-4.fr
- Rebuilt for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sun Sep 29 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Mon Jul 15 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.1.2.

* Tue Jun 26 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

