# $Id$
# Authority: dag
# Upstream: Rob Caelers <robc@krandor.org>

Summary: Tool to recover from or prevent Repetitive Strain Injury
Name: workrave
Version: 1.6.1
Release: 1
License: GPL
Group: Applications/System
URL: http://workrave.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/workrave/workrave-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libsigc++-devel, gnet2-devel, glib2-devel
BuildRequires: gtkmm2-devel

%description
Workrave is a program that assists in the recovery and prevention of
Repetitive Strain Injury (RSI). The program frequently alerts you to
take micro-pauses, rest breaks and restricts you to your daily limit.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Workrave RSI Prevention
Comment=Recover or prevent Repetitive Strain Injury.
Icon=workrave/workrave-icon-small.png
Exec=workrave
Terminal=false
Type=Application
Categories=GNOME;Application;Utility;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor gnome                \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%config %{_sysconfdir}/sound/events/*
%{_bindir}/*
%{_libexecdir}/*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/applications/*.desktop
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/pixmaps/workrave/
%{_datadir}/sounds/workrave/
%{_datadir}/workrave/

%changelog
* Fri May 14 2004 Dag Wieers <dag@wieers.com> - 1.6.1-1
- Updated to release 1.6.1.

* Sat May 01 2004 Dag Wieers <dag@wieers.com> - 1.6.0-1
- Updated to release 1.6.0.

* Tue Nov 04 2003 Dag Wieers <dag@wieers.com> - 1.4.1-0
- Updated to release 1.4.1.

* Mon Sep 08 2003 Dag Wieers <dag@wieers.com> - 1.4.0-0
- Updated to release 1.4.0.

* Wed Mar 26 2003 Dag Wieers <dag@wieers.com> - 1.2.2-0
- Updated to release 1.2.2. (using DAR)

* Fri Nov 01 2002 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Updated to release 1.0.0.

* Wed Oct 30 2002 Dag Wieers <dag@wieers.com>
- Initial package.
