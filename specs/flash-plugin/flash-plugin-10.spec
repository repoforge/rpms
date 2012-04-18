# $Id: flash-plugin.spec 5067 2007-01-11 00:54:46Z dag $
# Authority: dag

# ExcludeDist: el2 rh7 rh9 el3 el4

### Disable stripping
%define __spec_install_post /usr/lib/rpm/brp-compress

%define real_name install_flash_player_10_linux

Summary: Macromedia Flash Player
Name: flash-plugin
Version: 10.3.183.16
%define real_version 10_3r183_16
Release: 0.1%{?dist}
License: Commercial
Group: Applications/Internet
URL: http://www.macromedia.com/downloads/

### More information wrt. downloads: http://kb2.adobe.com/cps/142/tn_14266.html
#Source0: http://fpdownload.macromedia.com/get/flashplayer/current/install_flash_player_10_linux.tar.gz
#Source0: http://fpdownload.macromedia.com/get/flashplayer/installers/archive/fp_%{version}_archive.zip
Source0: flashplayer%{real_version}_linux.tar.gz
Source1: README
Source2: LICENSE
Source3: homecleanup
Source4: setup
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: i386
Obsoletes: mozilla-flash <= %{version}-%{release}
#Requires: %{_libdir}/mozilla/plugins/

%description
Macromedia Flash Player

By downloading and installing this package you agree to the included LICENSE.

%prep
%setup -c %{real_name}
%{__install} -Dp -m0644 %{SOURCE1} LICENSE
%{__install} -Dp -m0644 %{SOURCE2} README

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 libflashplayer.so %{buildroot}%{_libdir}/flash-plugin/libflashplayer.so
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_libdir}/flash-plugin/LICENSE
%{__install} -Dp -m0644 %{SOURCE2} %{buildroot}%{_libdir}/flash-plugin/README
%{__install} -Dp -m0755 %{SOURCE3} %{buildroot}%{_libdir}/flash-plugin/homecleanup
%{__install} -Dp -m0755 %{SOURCE4} %{buildroot}%{_libdir}/flash-plugin/setup

%post
if [ $1 -eq 1 ]; then
    %{_libdir}/flash-plugin/setup install
elif [ $1 -eq 2 ]; then
    %{_libdir}/flash-plugin/setup upgrade
fi

%preun
if [ $1 -eq 0 ]; then
    %{_libdir}/flash-plugin/setup preun
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%{_libdir}/flash-plugin/

%changelog
* Thu Mar 15 2012 Dag Wieers <dag@wieers.com> - 10.3.183.16-0.1
- Updated to release 10.3.183.16.

* Fri Feb 17 2012 Dag Wieers <dag@wieers.com> - 10.3.183.15-0.1
- Updated to release 10.3.183.15.

* Wed Dec 14 2011 Dag Wieers <dag@wieers.com> - 10.3.183.11-0.1
- Updated to release 10.3.183.11.

* Thu Sep 22 2011 Dag Wieers <dag@wieers.com> - 10.3.183.10-0.1
- Updated to release 10.3.183.10.

* Thu Aug 11 2011 Dag Wieers <dag@wieers.com> - 10.3.183.5-0.1
- Updated to release 10.3.183.5.

* Sun Jun 19 2011 Dag Wieers <dag@wieers.com> - 10.3.181.26-0.1
- Updated to release 10.3.181.26.

* Thu Jun 09 2011 Dag Wieers <dag@wieers.com> - 10.3.181.22-0.1
- Updated to release 10.3.181.22.

* Fri May 13 2011 Dag Wieers <dag@wieers.com> - 10.3.181.14-0.1
- Updated to release 10.3.181.14.

* Tue Apr 19 2011 Dag Wieers <dag@wieers.com> - 10.2.159.1-0.1
- Updated to release 10.2.159.1.

* Wed Mar 23 2011 Dag Wieers <dag@wieers.com> - 10.2.153.1-0.1
- Updated to release 10.2.153.1.

* Thu Feb 10 2011 Dag Wieers <dag@wieers.com> - 10.2.152.27-0.1
- Updated to release 10.2.152.27.

* Fri Dec 03 2010 Dag Wieers <dag@wieers.com> - 10.1.102.65-0.1
- Updated to release 10.1.102.65.

* Tue Nov 09 2010 Dag Wieers <dag@wieers.com> - 10.1.102.64-0.1
- Updated to release 10.1.102.64.

* Thu Aug 12 2010 Dag Wieers <dag@wieers.com> - 10.1.82.76-0.1
- Updated to release 10.1.82.76.

* Sun Jun 13 2010 Dag Wieers <dag@wieers.com> - 10.1.53.64-0.1
- Updated to release 10.1.53.64.

* Sat Aug 08 2009 Dag Wieers <dag@wieers.com> - 10.0.32.18-0.2
- Fixed to use the real 10.0.32.18 tarball. (damn adobe, version your stuff!)

* Sat Aug 01 2009 Dag Wieers <dag@wieers.com> - 10.0.32.18-0.1
- Updated to release 10.0.32.18.

* Thu Apr 16 2009 Dag Wieers <dag@wieers.com> - 10.0.22.87-1
- Updated to release 10.0.22.87.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 10.0.15.3-1
- Updated to release 10.0.15.3.

* Mon Nov 03 2008 Dag Wieers <dag@wieers.com> - 10.0.12.36-2
- Include setup and homecleanup like upstream.

* Tue Oct 28 2008 Dag Wieers <dag@wieers.com> - 10.0.12.36-1
- Updated to release 10.0.12.36.

* Wed Apr 23 2008 Dag Wieers <dag@wieers.com> - 9.0.124.0-1
- Updated to release 9.0.124.0.

* Wed Dec 05 2007 Dag Wieers <dag@wieers.com> - 9.0.115.0-1
- Updated to release 9.0.115.0.

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
