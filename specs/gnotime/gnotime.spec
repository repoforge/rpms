# $Id$
# Authority: dag
# Upstream: Linas Vepstas <linas$linas,org>

Summary: Tracks and reports time spent
Name: gnotime
Version: 2.2.2
Release: 1%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://gttr.sourceforge.net/

Source: http://dl.sf.net/gttr/gnotime-%{version}.tar.gz
Patch0: gnotime-qof-0.7.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: gtkhtml3-devel
BuildRequires: guile-devel
BuildRequires: intltool
BuildRequires: libgnome-devel >= 2.0
BuildRequires: libgnomeui-devel >= 2.0.3
BuildRequires: qof-devel >= 0.7.0
BuildRequires: scrollkeeper
BuildRequires: autoconf
Requires: GConf2
Requires: scrollkeeper

%description
A combination of stop-watch, diary, consultant billing system, and project
manager.  Gnotime allows you to track the amount of time you spend on a task,
associate a memo with it, set a billing rate, print an invoice, as well as
track the status of other projects.

Some people may remember Gnotime in its previous incarnations as GTT
(Gnome Time Tracker) when it was part of the Gnome Utils package.  It has
been split out, renamed, and greatly enhanced since then.

%prep
%setup
%patch0 -p1

%build
autoconf
%configure \
    --disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}-2.0

%clean
%{__rm} -rf %{buildroot}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%files -f %{name}-2.0.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man?/*
%doc %{_datadir}/gnome/help/gnotime/
%config %{_sysconfdir}/gconf/schemas/gnotime.schemas
%{_bindir}/gnotime
%{_datadir}/applications/gnotime.desktop
%{_datadir}/gnotime/
#%{_datadir}/gnome/apps/Applications/*.desktop
#exclude %{_datadir}/gnome/help/gtt/
%{_datadir}/omf/gnotime/
%{_includedir}/gnotime/
%exclude %{_libdir}/libqofsql.a
%exclude %{_libdir}/libqofsql.la
%{_libdir}/libqofsql.so.*
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Wed Feb 01 2006 Dag Wieers <dag@wieers.com> - 2.2.2-1
- Updated to release 2.2.2.

* Wed Apr 28 2004 Dag Wieers <dag@wieers.com> - 2.2.0-1
- Updated to release 2.2.0.

* Wed Apr 21 2004 Dag Wieers <dag@wieers.com> - 2.1.9-1
- Updated to release 2.1.9.

* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 2.1.8-1
- Updated to release 2.1.8.

* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 2.1.7-0
- Updated to release 2.1.7.

* Mon May 05 2003 Dag Wieers <dag@wieers.com> - 2.1.6-0
- Updated to release 2.1.6.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 2.1.5-0
- Updated to release 2.1.5.

* Mon Jan 06 2003 Dag Wieers <dag@wieers.com> - 2.1.4-0
- Initial package. (using DAR)
