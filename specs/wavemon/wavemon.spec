# $Id: _template.spec 765 2004-05-20 17:33:53Z dag $
# Authority: dag
# Upstream: Jan Morgenstern <jan$jm-music,de>

%define real_version 0.4.0b

Summary: Ncurses-based monitoring application for wireless network devices
Name: wavemon
Version: 0.4.0
Release: 0.b
License: GPL
Group: Applications/Internet
URL: http://www.janmorgenstern.de/projects-software.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.janmorgenstern.de/wavemon-%{real_version}.tar.gz
#Source: http://www.wavemage.com/wavemon-%{real_version}.tar.bz2
Patch: wavemon.c.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
wavemon is a wireless device monitoring application that allows you to
watch signal and noise levels, packet statistics, device configuration
and network parameters of your wireless network hardware. It has
currently only been tested with the Lucent Orinoco series of cards,
although it *should* work (though with varying features) with all
devices supported by the wireless kernel extensions by Jean Tourrilhes.

%prep
%setup -n %{name}-%{real_version}
%patch -p1

%build
%configure
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man{1,5}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Changelog COPYING README TODO
%doc %{_mandir}/man?/*
%{_bindir}/wavemon

%changelog -n wavemon
* Mon Jul 12 2004 Dag Wieers <dag@wieers.com> - 0.4.0-0.b
- Initial package. (using DAR)
