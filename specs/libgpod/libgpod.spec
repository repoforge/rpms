# $Id$
# Authority: matthias

### EL6 ships with libgpod-0.7.2-6.el6
# ExclusiveDist: el2 el3 el4 el5

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Library to access the contents of an iPod
Name: libgpod
Version: 0.4.0
Release: 0%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.gtkpod.org/libgpod.html
Source: http://dl.sf.net/gtkpod/libgpod-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk2-devel, glib2-devel, gettext, intltool, perl(XML::Parser)
BuildRequires: taglib-devel, python-devel, python-eyed3, swig

%description
Libgpod is a library to access the contents of an iPod. It supports playlists,
smart playlists, playcounts, ratings, podcasts etc.


%package devel
Summary: Development files for the libgpod library
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig

%description devel
Libgpod is a library to access the contents of an iPod. It supports playlists,
smart playlists, playcounts, ratings, podcasts etc.

This package contains the files required to develop programs that will use
libgpod.


%prep
%setup


%build
%configure --disable-static
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%{_libdir}/*.so.*
%{python_sitelib}/gpod/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/gpod-1.0/
%{_libdir}/pkgconfig/libgpod-1.0.pc
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_datadir}/gtk-doc/html/libgpod/


%changelog
* Mon Sep 25 2006 Matthias Saou <http://freshrpms.net/> 0.4.0-0
- Update to 0.4.0 since FC6 only contains 0.3.0.
- Add taglib support.
- Disable building static library.
- Include new python bindings.
- Add gtk2-devel build req. for gdk-pixbuf-2.0.pc and enable ArtworkDB.

* Tue Mar 14 2006 Matthias Saou <http://freshrpms.net/> 0.3.2-0
- Update to 0.3.2.

* Mon Dec 19 2005 Matthias Saou <http://freshrpms.net/> 0.3.0-1
- Initial RPM release.

