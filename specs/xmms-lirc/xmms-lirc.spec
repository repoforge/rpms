# $Id$
# Authority: matthias

%define xmms_generaldir %(xmms-config --general-plugin-dir 2>/dev/null || echo %{_libdir}/xmms/General)
%define real_name       lirc-xmms-plugin

Summary: Plugin to use LIRC supported infrared devices in XMMS
Name: xmms-lirc
Version: 1.4
Release: 3%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.lirc.org/
Source: http://dl.sf.net/lirc/lirc-xmms-plugin-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xmms >= 1.0.0, glib >= 1.2.7, gtk+ >= 1.2.7, lirc
BuildRequires: xmms-devel, glib-devel >= 1.2.7, gtk+-devel >= 1.2.7, lirc


%description
LIRC (Linux Infrared Remote Control) plugin for XMMS (X Multimedia System).


%prep
%setup -n %{real_name}-%{version}


%build
./configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{xmms_generaldir}/liblirc.so
%exclude %{xmms_generaldir}/liblirc.la


%changelog
* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.4-3
- Rebuilt for Fedora Core 2.

* Wed Jan  7 2004 Matthias Saou <http://freshrpms.net/> 1.4-2
- Rebuilt for Fedora Core 1.

* Wed May 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.4.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.3.
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Wed Oct  9 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Fri May  3 2002 Matthias Saou <http://freshrpms.net/>
- Changed the xmms General dir to be expanded from xmms-config (cleaner).
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Fri Oct  5 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

