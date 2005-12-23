# $Id$
# Authority: matthias

Summary: Library to access the contents of an iPod
Name: libgpod
Version: 0.3.0
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://www.gtkpod.org/libgpod.html
Source: http://dl.sf.net/gtkpod/libgpod-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: glib2-devel, gettext, gcc-c++

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
%configure
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

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/gpod-1.0/
%{_libdir}/pkgconfig/libgpod-1.0.pc
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%changelog
* Mon Dec 19 2005 Matthias Saou <http://freshrpms.net/> 0.3.0-1
- Initial RPM release.

