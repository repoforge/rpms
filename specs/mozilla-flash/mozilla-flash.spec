# $Id$
# Authority: dag

Summary: Macromedia Flash Player
Name: mozilla-flash
Version: 7.0.25
Release: 1
License: Commercial
Group: Applications/Internet
URL: http://www.macromedia.com/downloads/

Source: http://macromedia.rediris.es/rpmsource/flash-plugin-7.0.25.tar.gz
#Source: http://fpdownload.macromedia.com/get/shockwave/flash/english/linux/7.0r25/install_flash_player_7_linux.tar.gz
Source1: http://macromedia.rediris.es/rpmsource/LICENSE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: i386
#Requires: %{_libdir}/mozilla/plugins/

%description
Macromedia Flash Player

By downloading and installing this package you agree to the included LICENSE:

	http://macromedia.rediris.es/rpmsource/LICENSE


%prep
%setup -c
%{__install} -D -m0644 %{SOURCE1} %{_builddir}/%{name}-%{version}/LICENSE

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 install_flash_player_7_linux/libflashplayer.so %{buildroot}%{_libdir}/mozilla/plugins/libflashplayer.so
%{__install} -D -m0755 install_flash_player_7_linux/flashplayer.xpt %{buildroot}%{_libdir}/mozilla/plugins/flashplayer.xpt

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc install_flash_player_7_linux/Readme.* LICENSE
%{_libdir}/mozilla/plugins/

%changelog
* Sun Jun 27 2004 Dag Wieers <dag@wieers.com> - 7.0.25-1
- Initial package. (using DAR)
