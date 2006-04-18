# $Id$
# Authority: dag

Summary: DVD backup tool
Name: lxdvdrip
Version: 1.40
Release: 1.2
License: GPL
Group: Applications/Multimedia
URL: http://lxdvdrip.berlios.de/

Source: http://download.berlios.de/lxdvdrip/lxdvdrip-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: dvdauthor, dvdbackup, dvd+rw-tools, mplayer, streamdvd, transcode

%description
lxdvdrip is a tool to make a copy from a Video DVD for private use.  It
automates the process of ripping, authoring, preview and burning a DVD.

%prep
%setup -n %{name}

%{__perl} -pi.orig -e 's|(-ldvdread)|$1 -ldl|g' Makefile */Makefile

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"
%{__make} %{?_smp_mflags} -C vamps \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 lxdvdrip %{buildroot}%{_bindir}/lxdvdrip
%{__install} -Dp -m0755 mpgtx/mpgtx %{buildroot}%{_bindir}/mpgtx
%{__install} -Dp -m0755 vamps/vamps %{buildroot}%{_bindir}/vamps
%{__install} -Dp -m0644 doc-pak/lxdvdrip.conf.EN %{buildroot}%{_sysconfdir}/lxdvdrip.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc-pak/*
%config(noreplace) %{_sysconfdir}/lxdvdrip.conf
%{_bindir}/lxdvdrip
%{_bindir}/mpgtx
%{_bindir}/vamps

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.40-1.2
- Rebuild for Fedora Core 5.

* Fri Dec 03 2004 Dag Wieers <dag@wieers.com> - 1.40-1
- Initial package. (using DAR)
