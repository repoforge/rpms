# $Id$
# Authority: dag

### FIXME: Added desktop file

Summary: Wireless network sssistant
Name: wlassistant
Version: 0.5.4a
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://wlassistant.sourceforge.net/

Source: http://dl.sf.net/wlassistant/wlassistant-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel >= 3.2.0
BuildRequires: gcc-c++, libstdc++-devel, libart_lgpl-devel, wireless-tools
BuildRequires: libpng-devel, zlib-devel, gettext
Requires: kdelibs, wireless-tools, libstdc++, libgcc, libart_lgpl, libpng, zlib, sudo
Obsoletes: wirelessassisstant, wlassisant
Provides: wirelessassisstant

%description
Wireless profile managing application that allows you to scan for wireless
networks and connect to them.
Connecting to encrypted networks is not supported YET.
It uses wireless-tools as it's backend, so they need to be installed.

%prep
%setup

%build
source /etc/profile.d/qt.sh
%configure \
%ifarch amd64 x86_64 ia32e ppc64 s390x
	--enable-libsuffix=64 \
%endif
	--with-qt-dir="$QTDIR"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /etc/profile.d/qt.sh
%{__make} install DESTDIR="%{buildroot}"

%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/wlassistant
%{_datadir}/applnk/Utilities/wlassistant.desktop
%{_datadir}/icons/*/*x*/apps/wlassistant.png

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.4a-1.2
- Rebuild for Fedora Core 5.

* Fri Dec 02 2005 Dag Wieers <dag@wieers.com> - 0.5.4a-1
- Initial package. (using DAR)
