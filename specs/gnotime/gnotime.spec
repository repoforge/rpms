# $Id$

# Authority: dag
# Upstream: Linas Vepstas <linas@linas.org>

Summary: GNOME Time Tracker.
Name: gnotime
Version: 2.1.7
Release: 0
License: GPL
Group: Applications/Productivity
URL: http://gttr.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gttr/gnotime-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libgnome-devel >= 2.0, libgnomeui-devel >= 2.0.3, guile-devel

%description
The GNOME Time Tracker is a desktop utility for tracking the amount
of time spent on projects, and generating configurable reports and
invoices based on that time.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}-2.0
%{__rm} -rf %{buildroot}%{_datadir}/gnome/help/gtt

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}-2.0.lang
%defattr (-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man1/*
%doc %{_datadir}/gnome/help/gnotime/
%{_bindir}/*
%{_datadir}/gnotime/
%{_datadir}/gnome/apps/Applications/*.desktop

%changelog
* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 2.1.7-0
- Updated to release 2.1.7.

* Mon May 05 2003 Dag Wieers <dag@wieers.com> - 2.1.6-0
- Updated to release 2.1.6.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 2.1.5-0
- Updated to release 2.1.5.

* Mon Jan 06 2003 Dag Wieers <dag@wieers.com> - 2.1.4-0
- Initial package. (using DAR)
