# $Id$
# Authority: dries
# Upstream: <ml$andreas,silberstorff,de>

Summary: Video recorder
Name: kalva
Version: 0.8.75
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://developer.berlios.de/projects/kalva

Source: http://download.berlios.de/kalva/kalva-%{version}-no-i18n.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gcc-c++, gettext, flex

%description
Kalva is a KDE video recorder that is simple to use and easy to setup. You
can use it to schedule a single movie recording by choosing the date from a
calendar. A serial recording may be scheduled by choosing the days of the
week. You can store recording options in various profiles for different
hardware and quality levels. Kalva can import channellists from programs
like xawtv or xawtv4, and can generate a new one using scantv.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n kalva-%{version}-no-i18n

%build
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall perlbindir=%{buildroot}%{_bindir} perlmoddir=%{buildroot}%{_libdir}/tvapp

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_bindir}/kalva
%{_bindir}/tvapp.pl
%{_libdir}/kde3/scantvplugin.*
%{_libdir}/kde3/tv_stationsfilterplugin.*
%{_libdir}/kde3/xawtvrcfilterplugin.*
%{_libdir}/libkchlstfilterplugininterfaces.so.*
%{_libdir}/libkchlstfilterplugininterfaces.la
%{_libdir}/tvapp/
%{_datadir}/applications/kde/kalva.desktop
%{_datadir}/applnk/Multimedia/TV/kalva.desktop
%{_datadir}/apps/kalva/
%{_datadir}/apps/scantvplugin/
%{_datadir}/apps/tv_stationsfilterplugin/
%{_datadir}/apps/xawtvrcfilterplugin/
%{_datadir}/config.kcfg/kalva.kcfg
%{_datadir}/doc/HTML/*/kalva/
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/services/*.desktop
%{_datadir}/servicetypes/kchlstfilterplugin.desktop

%files devel
%{_includedir}/kchlstfilterplugin/
%{_libdir}/libkchlstfilterplugininterfaces.so

%changelog
* Mon Apr 03 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.75-1
- Updated to release 0.8.75.

* Sat Dec 10 2005 Dries Verachtert <dries@ulyssis.org> - 0.8.50-1
- Updated to release 0.8.50.

* Thu Nov 10 2005 Dries Verachtert <dries@ulyssis.org> - 0.8.49-1
- Initial package.
