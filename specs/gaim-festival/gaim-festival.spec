# $Id$
# Authority: dag
# Upstream: Sandindo Flores <saflores$hotmail,com>
# Upstream: Rishi Sharma <rishsharma$hotmail,com>

%define real_name festival-gaim

Summary: Voice plugin for gaim
Name: gaim-festival
Version: 0.78
Release: 1
License: GPL
Group: Applications/Internet
URL: http://festival-gaim.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/festival-gaim/festival-gaim-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gaim, pkgconfig, libtool
Requires: gaim, festival
Obsoletes: festival-gaim

%description
This plugin speak your incoming messages from gaim.
It use festival and is configurable.

%prep

%setup -n %{real_name}-%{version}

%build
%{__make} %{?_smp_mflags} \
	 FESTIVAL_VOICES_PATH="%{_datadir}/festival/voices" \
	 PLUGIN_VERSION="%{version}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}/gaim/
%makeinstall \
	PLUGIN_GAIM_PATH="%{buildroot}%{_libdir}/gaim"

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL LICENSE README THANKS
%{_libdir}/gaim/*

%changelog
* Mon Jul 19 2004 Dag Wieers <dag@wieers.com> - 0.78-1
- Updated to release 0.78.

* Tue May 18 2004 Dag Wieers <dag@wieers.com> - 0.77-1
- Updated to release 0.77.

* Wed Oct 08 2003 Dag Wieers <dag@wieers.com> - 0.68.2-0
- Updated to release 0.68.2.

* Fri Oct 03 2003 Dag Wieers <dag@wieers.com> - 0.68-0
- Initial package. (using DAR)
