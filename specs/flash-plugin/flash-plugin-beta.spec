# $Id$
# Authority: dag

# Tag: test

# ExcludeDist: rh7 el2

### Disable stripping
%define __spec_install_post /usr/lib/rpm/brp-compress

%define real_name flash-player-plugin
%define real_version 051508

Summary: Macromedia Flash Player
Name: flash-plugin
Version: 10.0.1.218
Release: 1
License: Commercial
Group: Applications/Internet
URL: http://www.macromedia.com/downloads/

Source0: http://download.macromedia.com/pub/labs/flashplayer10/flashplayer10_install_linux_%{real_version}.tar.gz
Source1: http://macromedia.rediris.es/rpmsource/LICENSE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: i386
Obsoletes: mozilla-flash <= %{version}-%{release}
#Requires: %{_libdir}/mozilla/plugins/

%description
Macromedia Flash Player

By downloading and installing this package you agree to the included LICENSE:

    http://macromedia.rediris.es/rpmsource/LICENSE


%prep
%setup -n install_flash_player_10_linux/
%{__install} -Dp -m0644 %{SOURCE1} LICENSE

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 libflashplayer.so %{buildroot}%{_libdir}/mozilla/plugins/libflashplayer.so
#%{__install} -Dp -m0755 flashplayer.xpt %{buildroot}%{_libdir}/mozilla/plugins/flashplayer.xpt

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE
%{_libdir}/mozilla/plugins/

%changelog
* Sat May 17 2008 Dag Wieers <dag@wieers.com> - 10.0.1.218-1
- Updated to release beta 051508.

* Wed Apr 23 2008 Dag Wieers <dag@wieers.com> - 9.0.124.0-1
- Updated to release 9.0.124.0.

* Wed Dec 05 2007 Dag Wieers <dag@wieers.com> - 9.0.115.0-1
- Updated to release 9.0.115.0.

* Tue Aug 28 2007 Dag Wieers <dag@wieers.com> - 9.0.48.082207-1
- Updated to release beta 082207.

* Thu Jul 19 2007 Dag Wieers <dag@wieers.com> - 9.0.48.0-1
- Updated to release 9.0.48.0.

* Wed Jan 17 2007 Dag Wieers <dag@wieers.com> - 9.0.31.0-1
- Updated to release 9.0.31.0.

* Wed Jan 10 2007 Dag Wieers <dag@wieers.com> - 7.0.69-1
- Updated to release 7.0.69.

* Tue Sep 12 2006 Dag Wieers <dag@wieers.com> - 7.0.68-1
- Updated to release 7.0.68.
- Renamed package from mozilla-flash to flash-plugin.

* Wed Mar 15 2006 Dag Wieers <dag@wieers.com> - 7.0.63-1
- Updated to release 7.0.63.

* Sat Nov 26 2005 Dag Wieers <dag@wieers.com> - 7.0.61-1
- Updated to release 7.0.61.

* Sun Jun 27 2004 Dag Wieers <dag@wieers.com> - 7.0.25-1
- Initial package. (using DAR)
