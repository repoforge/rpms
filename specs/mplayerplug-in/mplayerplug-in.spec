# $Id$
# Authority: atrpms
# Upstream: Kevin DeKorte <kdekorte$users,sf,net>
# Upstream: <mplayerplug-in-devel$lists,sf,net>

%define mversion %(rpm -q mozilla-devel --qf "%%{epoch}:%%{version}")

Summary: Browser plugin for mplayer
Name: mplayerplug-in
Version: 2.65
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://mplayerplug-in.sf.net/

Source: http://dl.sf.net/mplayerplug-in/mplayerplug-in-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: XFree86-devel, mozilla-devel, glib2-devel, gtk2-devel, mozilla-devel

Obsoletes: mozilla-mplayer <= %{version}-%{release}
Requires: mplayer, mozilla = %{mversion}

%description
mplayerplug-in is a browser plugin that uses mplayer to play videos
in your browser.

%prep
%setup -n %{name}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 mplayerplug-in.so %{buildroot}%{_libdir}/mozilla/plugins/mplayerplug-in.so
%{__install} -D -m0755 mplayerplug-in.xpt %{buildroot}%{_libdir}/mozilla/components/mplayerplug-in.xpt
%{__install} -D -m0644 mplayerplug-in.conf %{buildroot}%{_sysconfdir}/mplayerplug-in.conf
%{__install} -D -m0644 mplayerplug-in.types %{buildroot}%{_sysconfdir}/mplayerplug-in.types

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog INSTALL README TODO
%config(noreplace) %{_sysconfdir}/mplayerplug-in.conf
%config(noreplace) %{_sysconfdir}/mplayerplug-in.types
%{_libdir}/mozilla/plugins/mplayerplug-in.so
%{_libdir}/mozilla/components/mplayerplug-in.xpt

%changelog
* Sat Jun 19 2004 Dag Wieers <dag@wieers.com> - 2.65-1
- Updated to release 2.65.

* Thu Apr 22 2004 Dag Wieers <dag@wieers.com> - 2.60-2
- Moved mozilla-devel from Obsolets to BuildRequires, duh. (Kevin DeKorte)

* Wed Apr 21 2004 Dag Wieers <dag@wieers.com> - 2.60-1
- Renamed package back to mplayerplug-in.
- Updated to release 2.60.

* Fri Oct 10 2003 Dag Wieers <dag@wieers.com> - 0.95-1
- Disabled using MIME-types and fix config files.

* Mon Oct 06 2003 Dag Wieers <dag@wieers.com> - 0.95-0
- Updated to release 0.95.

* Thu Sep 11 2003 Dag Wieers <dag@wieers.com> - 0.91-0
- Updated to release 0.91.

* Sun Apr 20 2003 Dag Wieers <dag@wieers.com> - 0.71-0
- Initial package. (using DAR)
