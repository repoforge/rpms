# $Id$

# Authority: dag

### FIXME: Makefiles don't allow -jX (parallel compilation)
# Distcc: 0

Summary: Graphical project management tool.
Name: planner
Version: 0.11
Release: 0
License: GPL
Group: Applications/Productivity
URL: http://planner.imendio.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source:	http://ftp.gnome.org/pub/GNOME/sources/planner/%{version}/planner-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gtk2-devel >= 2.0.3, libgnomeui-devel >= 2.0.1, libglade2-devel >= 2.0.0
BuildRequires: libgnomecanvas >= 2.0.1, libbonoboui-devel >= 2.0.1
BuildRequires: intltool, libgnomeprint22, libgnomeprintui22

#BuildRequires: libmrproject-devel >= %{name}-%{version}
BuildRequires: scrollkeeper

Requires(post): scrollkeeper
#Requires: libmrproject >= %{name}-%{version}

Obsoletes: mrproject <= 0.10, libmrproject <= 0.10

%description
Planner is a visual project management application which allows users to
manage several aspects of a project, including schedule tracking using
Gantt charts.

You should install Planner if you wish to manage schedules, allocate
resources, and track the progress of your projects.

%prep
%setup

%build
intltoolize
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
#	MRP_PLUGINDIR="%{buildroot}%{_libdir}/planner/plugins" \
#	MRP_VIEWDIR="%{buildroot}%{_libdir}/planner/views"
%find_lang %{name}
%find_lang planner-libplanner
%{__cat} planner-libplanner.lang >>%{name}.lang

#desktop-file-install --vendor gnome --delete-original \
#	--add-category X-Red-Hat-Base                 \
#	--add-category Application                    \
#	--dir %{buildroot}%{_datadir}/applications    \
#	%{buildroot}%{_datadir}/applications/mrproject.desktop

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper/
%{__rm} -f %{buildroot}%{_libdir}/planner{,/file-modules,/storage-modules,/views,/plugins}/*.la \
		%{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig &>/dev/null
scrollkeeper-update -q || :

%postun
/sbin/ldconfig &>/dev/null
scrollkeeper-update -q || :

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_datadir}/gnome/help/planner/
%{_bindir}/*
%{_libdir}/*.so
%{_libdir}/planner/
%{_datadir}/planner/
%{_datadir}/application-registry/*.applications
%{_datadir}/applications/*.desktop
#%{_datadir}/gnome-2.0/ui/*.ui
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*
%{_includedir}/planner-1.0/
%{_libdir}/pkgconfig/*.pc
%{_datadir}/omf/planner/

%changelog
* Thu Dec 04 2003 Dag Wieers <dag@wieers.com> - 0.11-0
- Changed package name from mrproject to planner.
- Updated to release 0.11.

* Sat Sep 13 2003 Dag Wieers <dag@wieers.com> - 0.10-0
- Updated to release 0.10.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 0.9.1-0
- Updated to release 0.9.1.

* Thu Jan 23 2003 Dag Wieers <dag@wieers.com> - 0.8-0
- Initial package. (using DAR)
