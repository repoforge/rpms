# $Id$
# Authority: matthias

%define xmms_generaldir %(xmms-config --general-plugin-dir)
%define xmms_datadir    %(xmms-config --data-dir)

Summary: XMMS plugin to use special keyboard multimedia keys
Name: xmms-itouch
Version: 0.1.2
Release: 5%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.saunalahti.fi/~syrjala/xmms-itouch/
Source: http://www.saunalahti.fi/~syrjala/xmms-itouch/xmms-itouch-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xmms >= 1.0.0, glib >= 1.2.7, gtk+ >= 1.2.7
BuildRequires: xmms-devel, glib-devel >= 1.2.7, gtk+-devel >= 1.2.7


%description
With this XMMS plugin you can take advantage of the multimedia (playback and
volume control) keys on your Logitech iTouch keyboard. When the plugin is
used you can use the keys regardless of the current input focus. The plugin
won't work if some other application (eg. xscreensaver) has grabbed the
keyboard.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install \
    libdir=%{buildroot}%{xmms_generaldir} \
    datadir=%{buildroot}%{xmms_datadir}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%config %{xmms_datadir}/xmms-itouch.config
%{xmms_generaldir}/libitouch.so
%exclude %{xmms_generaldir}/libitouch.la


%changelog
* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.1.2-5
- Rebuilt for Fedora Core 2.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.1.2-4
- Rebuilt for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sun Sep 29 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Mon Jul 15 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.1.2.

* Tue Jun 26 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

