# $Id$
# Authority: dag
# Upstream: Sandindo Flores <saflores$hotmail,com>
# Upstream: Rishi Sharma <rishsharma$hotmail,com>

%define real_name festival-gaim

Summary: Voice plugin for gaim
Name: gaim-festival
Version: 1.00
Release: 3.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://festival-gaim.sourceforge.net/

Source: http://dl.sf.net/festival-gaim/festival-gaim-%{version}.tar.gz
Patch0: gaim-festival-1.00-voice-selection.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gaim-devel, pkgconfig, libtool, gtk2-devel
Requires: gaim, festival
Obsoletes: festival-gaim

%description
This plugin speak your incoming messages from gaim.
It use festival and is configurable.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

%{__perl} -pi.orig -e 's|-march=\w+||g' Makefile

%build
%{__make} %{?_smp_mflags} \
	 FESTIVAL_VOICES_PATH="%{_datadir}/festival/voices" \
	 PLUGIN_VERSION="%{version}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}/gaim/
%makeinstall \
	PLUGIN_GAIM_PATH="%{buildroot}%{_libdir}/gaim"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL LICENSE README THANKS
%dir %{_libdir}/gaim/
%{_libdir}/gaim/festival.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.00-3.2
- Rebuild for Fedora Core 5.

* Tue Mar 22 2005 Dag Wieers <dag@wieers.com> - 1.00-3
- Rebuild against gaim 1.2.0-0.

* Sat Jan 22 2005 Dag Wieers <dag@wieers.com> - 1.00-2
- Added voice selection fix. (David L Norris)

* Thu Sep 23 2004 Dag Wieers <dag@wieers.com> - 1.00-1
- Updated to release 1.00.

* Mon Jul 19 2004 Dag Wieers <dag@wieers.com> - 0.78-1
- Updated to release 0.78.

* Tue May 18 2004 Dag Wieers <dag@wieers.com> - 0.77-1
- Updated to release 0.77.

* Wed Oct 08 2003 Dag Wieers <dag@wieers.com> - 0.68.2-0
- Updated to release 0.68.2.

* Fri Oct 03 2003 Dag Wieers <dag@wieers.com> - 0.68-0
- Initial package. (using DAR)
