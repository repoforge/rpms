# $Id$
# Authority: dag

### This package fixes bugs in the RHEL 5.2 pygobject2
### EL6 ships with pygobject2-2.20.0-5.el6
### EL5 ships with pygobject2-2.12.1-5.el5
%{?el5:# Tag: rfx}
# ExclusiveDist: el5

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pygobject

Summary: Python bindings for GObject
Name: pygobject2
Version: 2.12.2
Release: 0.1%{?dist}
License: LGPL
Group: Development/Languages
URL: http://www.pygtk.org/

Source: http://ftp.gnome.org/pub/GNOME/sources/pygobject/2.12/pygobject-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: automake >= 1.6.3-5
BuildRequires: glib2-devel >= 2.8
BuildRequires: libtool
BuildRequires: python2-devel >= 2.3.5
Requires: glib2 >= 2.8
Requires: python2 >= 2.3.5

%description
pygobject2 provides a convenient wrapper for the GObject library
for use in Python programs.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pygobject2-doc = %{version}-%{release}
Requires: glib2-devel
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package doc
Summary: Documentation files for pygobject2
Group: Development/Languages

%description doc
This package contains documentation files for pygobject2.

%prep
%setup -n pygobject-%{version}

%build
%configure \
    --disable-docs \
    --disable-static \
    --enable-thread
export tagname="CC"
%{__make} LIBTOOL="/usr/bin/libtool"

%install
%{__rm} -rf %{buildroot}
export tagname="CC"
%{__make} install DESTDIR="%{buildroot}" LIBTOOL="/usr/bin/libtool"

### Clean up examples/
%{__rm} examples/Makefile*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README examples/
%dir %{python_sitearch}/gtk-2.0/
%{python_sitearch}/gtk-2.0/dsextras.*
%{python_sitearch}/gtk-2.0/gobject/
%{python_sitearch}/pygtk.*

%files devel
%defattr(-, root, root, 0755)
%dir %{_includedir}/pygtk-2.0/
%{_includedir}/pygtk-2.0/pygobject.h
%{_libdir}/pkgconfig/pygobject-2.0.pc

%files doc
%defattr(644, root, root, 755)
%doc %{_datadir}/gtk-doc/html/pygobject/
%{_datadir}/pygobject/

%changelog
* Wed Dec 17 2008 Dag Wieers <dag@wieers.com> - 2.12.2-0.1
- Updated to release 2.12.2.

* Thu Jan 18 2007 Matthew Barnes <mbarnes@redhat.com> - 2.12.1-5.el5
- Add subpackage pygobject2-doc (RH bug #222169).

* Thu Jan 11 2007 Matthew Barnes <mbarnes@redhat.com> - 2.12.1-4.el5
- Use the python_sitearch macro instead of python_sitelib (RH bug #222169).

* Sun Sep 24 2006 Matthew Barnes <mbarnes@redhat.com> - 2.12.1-3.fc6
- Require glib2-devel for the -devel package.

* Fri Sep 22 2006 Matthew Barnes <mbarnes@redhat.com> - 2.12.1-2.fc6
- Define a python_sitelib macro for files under site_packages.
- Spec file cleanups.

* Tue Sep  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.12.1-1.fc6
- Update to 2.12.1
- Require pkgconfig for the -devel package

* Sun Aug 27 2006 Matthias Clasen <mclasen@redhat.com> - 2.11.4-1.fc6
- Update to 2.11.4
- Use pre-built docs

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.11.3-1.fc6
- Update to 2.11.3

* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.11.2-2.fc6
- BR libxslt

* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.11.2-1.fc6
- Update to 2.11.2

* Wed Jul 19 2006 Jesse Keating <jkeating@redhat.com> - 2.11.0-2
- rebuild

* Wed Jul 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.11.0-1
- Update to 2.11.0

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.10.1-3
- rebuild
- Add missing br libtool

* Fri May 19 2006 John (J5) Palmieri <johnp@redhat.com> - 2.10.1-2
- Cleanup

* Fri May 12 2006 John (J5) Palmieri <johnp@redhat.com> - 2.10.1-1
- Initial package
