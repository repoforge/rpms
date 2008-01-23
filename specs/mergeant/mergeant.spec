# $Id$
# Authority: dag
# Upstream: Jorge Ferrer <jferrer$ieeesb,etsit,upm,es>

# Distcc: 0

Summary: Database administration tool
Name: mergeant
Version: 0.62
Release: 1.2
License: GPL
Group: Applications/Databases
URL: http://www.gnome-db.org/

Source: http://ftp.gnome.org/pub/GNOME/sources/mergeant/%{version}/mergeant-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgda-devel, libgnomedb-devel, gettext
BuildRequires: scrollkeeper, gcc-c++, libgnomeprint22-devel
BuildRequires: libgnomeprintui22-devel, perl(XML::Parser), intltool
Requires(post): scrollkeeper

%description
Mergeant is a database admin tool working with libgnomedb and libgda.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
### FIXME: Set proper MERGEANT_Helpdir, Applicationsdir and Pixmapdir in Makefiles
%{__perl} -pi.orig -e '
		s| = /usr/share/| = \$(datadir)/|;
		s| = /usr/lib/| = \$(libdir)/|;
	' Makefile */Makefile doc/*/Makefile
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%post
/sbin/ldconfig 2>/dev/null
scrollkeeper-update -q || :

%postun
/sbin/ldconfig 2>/dev/null
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING examples/ NEWS README TODO
%doc %{_datadir}/gnome/help/mergeant/
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/applications/*.desktop
%{_datadir}/application-registry/*.applications
%{_datadir}/mime-info/*
%{_datadir}/mergeant/
%{_datadir}/pixmaps/*
%{_datadir}/omf/mergeant/
%{_libdir}/bonobo/servers/*.server

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/libmergeant/
%{_includedir}/libmergeant/
%{_libdir}/*.a
%{_datadir}/omf/libmergeant/
%exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.62-1.2
- Rebuild for Fedora Core 5.

* Thu Nov 10 2005 Dries Verachtert <dries@ulyssis.org> - 0.62-1
- Updated to release 0.62.

* Mon Jul 18 2005 Dries Verachtert <dries@ulyssis.org> - 0.61-1
- Updated to release 0.61.

* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 0.50-1
- Updated to release 0.50.

* Fri Jun 13 2003 Dag Wieers <dag@wieers.com> - 0.12.1-0
- Initial package. (using DAR)
