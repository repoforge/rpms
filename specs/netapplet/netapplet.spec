# $Id$
# Authority: dag

Summary: Network switching and control applet.
Name: netapplet
Version: 0.98.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.gnome.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://primates.ximian.com/~rml/netapplet/netapplet-%{version}.tar.gz
Patch0: netapplet-0.98.0-fc2.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.4.0, glib2-devel >= 2.4.0
BuildRequires: wireless-tools, gnome-keyring-devel
BuildRequires: perl(XML::Parser), intltool
Prereq: wireless-tools

%description
Network switching and control applet.

%prep
%setup
%patch0 -p1 -b .fc2

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -D -m0755 netdaemon %{buildroot}%{_initrddir}/netdaemon

%post
/sbin/chkconfig --add netdaemon
/etc/init.d/netdaemon restart &>/dev/null

%preun
if [ $1 -eq 0 ]; then
	/etc/init.d/netdaemon stop &>/dev/null
	/sbin/chkconfig --del netdaemon
fi

%postun
if [ $1 -ne 0 ]; then
	/etc/init.d/netdaemon restart &>/dev/null
fi

%files
%defattr(-, root, root, 0755)
%config %{_initrddir}/netdaemon
%{_bindir}/netapplet
%{_bindir}/netdaemon
%{_datadir}/applications/netapplet.desktop
%{_datadir}/icons/gnome/*/apps/*
%{_datadir}/netapplet/
%{_datadir}/pixmaps/netapplet.png

%changelog
* Sun Aug 28 2004 Dag Wieers <dag@wieers.com> - 0.98.0-1
- Initial package. (using DAR)
