# $Id$
# Authority: dag
# Upstream: Linas Vepstas <linas$linas,org>

Summary: Graphical Time Tracker
Name: gnotime
Version: 2.2.0
Release: 1
License: GPL
Group: Applications/Productivity
URL: http://gttr.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gttr/gnotime-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgnome-devel >= 2.0, libgnomeui-devel >= 2.0.3, guile-devel
#BuildRequires: gtkhtml3-devel >= 3.1.0
# from configure output: checking for libgtkhtml-3.1 >= 3.0.0... 
BuildRequires: gtkhtml3-devel

%description
The GNOME Time Tracker is a desktop utility for tracking the amount
of time spent on projects, and generating configurable reports and
invoices based on that time.

%prep
%setup

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
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
%defattr (-, root, root, 0755)
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
%exclude %{_libdir}/libqof.a
%exclude %{_libdir}/libqof.la
%{_libdir}/libqof.so.*
%exclude %{_libdir}/libqofsql.a
%exclude %{_libdir}/libqofsql.la
%{_libdir}/libqofsql.so.*
%exclude %{_localstatedir}/scrollkeeper/

%changelog
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
