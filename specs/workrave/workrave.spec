# $Id$
# Authority: dag
# Upstream: Rob Caelers <robc$krandor,org>


%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

%define desktop_vendor rpmforge

Summary: Tool to recover from or prevent Repetitive Strain Injury
Name: workrave
Version: 1.8.5
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://workrave.sourceforge.net/

Source: http://dl.sf.net/workrave/workrave-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libsigc++-devel, gnet2-devel, glib2-devel >= 2.12, gcc-c++
BuildRequires: gtkmm2-devel, libgnomeuimm26-devel, gettext
BuildRequires: gnome-panel-devel

%{!?_without_modxorg:BuildRequires: libXmu-devel, libXt-devel}

%description
Workrave is a program that assists in the recovery and prevention of
Repetitive Strain Injury (RSI). The program frequently alerts you to
take micro-pauses, rest breaks and restricts you to your daily limit.

%prep
%setup

%{__cat} <<EOF >workrave.desktop
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
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	workrave.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README TODO
%config %{_sysconfdir}/sound/events/*
%{_bindir}/workrave
%{_libexecdir}/*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/applications/%{desktop_vendor}-workrave.desktop
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/pixmaps/workrave/
%{_datadir}/sounds/workrave/
%{_datadir}/workrave/

%changelog
* Mon Sep 24 2007 Dag Wieers <dag@wieers.com> - 1.8.5-1
- Updated to release 1.8.5.

* Fri May 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.8.3-1
- Updated to release 1.8.3.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.8.2-1
- Updated to release 1.8.2.

* Tue Nov 08 2005 Dries Verachtert <dries@ulyssis.org> - 1.8.1-2
- gnome-panel-devel added to buildreqs.

* Fri Nov 04 2005 Dries Verachtert <dries@ulyssis.org> - 1.8.1-1
- Updated to release 1.8.1.

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
