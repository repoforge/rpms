# $Id$
# Authority: dag
# Upstream: Jan Morgenstern <jan$jm-music,de>

%define real_version 0.4.0b

Summary: Ncurses-based monitoring application for wireless network devices
Name: wavemon
Version: 0.4.0
Release: 0.b.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.janmorgenstern.de/projects-software.html

Source: http://www.janmorgenstern.de/wavemon-%{real_version}.tar.gz
#Source: http://www.wavemage.com/wavemon-%{real_version}.tar.bz2
Patch0: wavemon.c.diff
Patch1: wavemon-0.4.0b-gcc34.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: ncurses-devel

%description
wavemon is a wireless device monitoring application that allows you to
watch signal and noise levels, packet statistics, device configuration
and network parameters of your wireless network hardware. It has
currently only been tested with the Lucent Orinoco series of cards,
although it *should* work (though with varying features) with all
devices supported by the wireless kernel extensions by Jean Tourrilhes.

%prep
%setup -n %{name}-%{real_version}
%patch0 -p1
%patch1 -p1

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

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.0-0.b.2
- Rebuild for Fedora Core 5.

* Mon Jul 12 2004 Dag Wieers <dag@wieers.com> - 0.4.0-0.b
- Initial package. (using DAR)
