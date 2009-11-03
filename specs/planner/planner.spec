# $Id$
# Authority: dag

# ExcludeDist: el4


%{?fc1:%define _without_shared_mime 1}
%{?el3:%define _without_shared_mime 1}
%{?rh9:%define _without_shared_mime 1}

Summary: Graphical project management tool
Name: planner
Version: 0.12.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://planner.imendio.org/

Source: http://ftp.imendio.com/pub/imendio/planner/src/planner-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.0.3, libgnomeui-devel >= 2.0.1, libglade2-devel >= 2.0.0
BuildRequires: libgnomecanvas >= 2.0.1, libbonoboui-devel >= 2.0.1, libgsf-devel
BuildRequires: intltool, libgnomeprint22, libgnomeprintui22, gcc-c++
BuildRequires: libgnomeprintui22-devel, python-devel
%{!?_without_shared_mime:BuildRequires: shared-mime-info}

BuildRequires: scrollkeeper

Requires(post): scrollkeeper

Obsoletes: mrproject <= 0.10, libmrproject <= 0.10

%description
Planner is a visual project management application which allows users to
manage several aspects of a project, including schedule tracking using
Gantt charts.

You should install Planner if you wish to manage schedules, allocate
resources, and track the progress of your projects.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n python-planner
Summary: Python library for planner
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description -n python-planner
Python library for planner.

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
#%find_lang planner-libplanner
#%{__cat} planner-libplanner.lang >>%{name}.lang

#desktop-file-install --vendor gnome --delete-original \
#	--add-category X-Red-Hat-Base                 \
#	--add-category Application                    \
#	--dir %{buildroot}%{_datadir}/applications    \
#	%{buildroot}%{_datadir}/applications/mrproject.desktop

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/planner{,/file-modules,/storage-modules,/views,/plugins}/*.la

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig &>/dev/null
scrollkeeper-update -q || :
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :

%postun
/sbin/ldconfig &>/dev/null
scrollkeeper-update -q || :
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING examples/*.planner NEWS README*
%doc %{_datadir}/gnome/help/planner/
%{_bindir}/planner
%{_libdir}/libplanner-1.so.*
%{_libdir}/planner/
%{_datadir}/planner/
%{_datadir}/application-registry/planner.applications
%{_datadir}/applications/planner.desktop
#%{_datadir}/gnome-2.0/ui/*.ui
%{_datadir}/mime-info/planner.*
%{!?_without_shared_mime:%{_datadir}/mime/application/x-planner.xml}
%{!?_without_shared_mime:%exclude %{_datadir}/mime/XMLnamespaces}
%{!?_without_shared_mime:%exclude %{_datadir}/mime/globs}
%{!?_without_shared_mime:%exclude %{_datadir}/mime/magic}
%{_datadir}/mime/packages/planner.xml
%{_datadir}/pixmaps/gnome-application-x-planner.png
%{_datadir}/pixmaps/gnome-planner.png
%{_datadir}/pixmaps/planner/
%{_datadir}/omf/planner/
%exclude %{_docdir}/planner/
%exclude %{_localstatedir}/scrollkeeper/

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/libplanner/
%exclude %{_libdir}/libplanner-1.la
%{_libdir}/libplanner-1.so
%{_libdir}/pkgconfig/libplanner-1.pc
%{_includedir}/planner-1.0/

%files -n python-planner
%defattr(-, root, root, 0755)
%exclude %{_libdir}/python*/site-packages/gtk-2.0/planner.la
%{_libdir}/python*/site-packages/gtk-2.0/planner.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.12.1-1.2
- Rebuild for Fedora Core 5.

* Mon Aug 30 2004 Dag Wieers <dag@wieers.com> - 0.12.1-1
- Updated to release 0.12.1.

* Fri Jul 09 2004 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Thu Dec 04 2003 Dag Wieers <dag@wieers.com> - 0.11-0
- Changed package name from mrproject to planner.
- Updated to release 0.11.

* Sat Sep 13 2003 Dag Wieers <dag@wieers.com> - 0.10-0
- Updated to release 0.10.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 0.9.1-0
- Updated to release 0.9.1.

* Thu Jan 23 2003 Dag Wieers <dag@wieers.com> - 0.8-0
- Initial package. (using DAR)
