# $Id$
# Authority: dag
# Upstream: Jörgen Scheibengruber <mfcn@gmx.de>

# Distcc: 0

Summary: GNOME applet that shows traffic on a network device
Name: netspeed_applet
Version: 0.9.2
Release: 0
License: GPL
Group: Applications/Internet
URL: http://mfcn.ilo.de/netspeed_applet/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.wh-hms.uni-ulm.de/~mfcn/shared/netspeed/netspeed_applet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, intltool
BuildRequires: libgnomeui-devel >= 2.0, libgtop2-devel >= 2.0
BuildRequires: scrollkeeper

Requires(post): scrollkeeper

%description
netspeed_applet is a little GNOME applet that shows the traffic on a
specified network device (for example eth0) in kbytes/s.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper/

%post
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_datadir}/gnome/help/netspeed_applet/
%{_libexecdir}/*
%{_libdir}/bonobo/servers/*
%{_datadir}/pixmaps/*
%{_datadir}/omf/netspeed_applet/

%changelog
* Sat Feb 07 2004 Dag Wieers <dag@wieers.com> - 0.9.2-0
- Updated to release 0.9.2.

* Thu Jan 08 2004 Dag Wieers <dag@wieers.com> - 0.9.1-0
- Updated to release 0.9.1.

* Sat Jun 28 2003 Dag Wieers <dag@wieers.com> - 0.9-0
- Updated to release 0.9.

* Thu Jan 30 2003 Dag Wieers <dag@wieers.com> - 0.8-0
- Initial package. (using DAR)
