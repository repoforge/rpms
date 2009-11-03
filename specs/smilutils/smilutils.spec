# $Id$
# Authority: dag

Summary: Collection of command line tools for SMIL manipulation
Name: smilutils
Version: 0.3.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://users.pandora.be/acp/kino/smilutils.html

Source: http://kino.schirmacher.de/filemanager/download/14/smilutils-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libxml2-devel, gtk+-devel, gdk-pixbuf-devel, gcc-c++
Buildrequires: libraw1394-devel, libavc1394-devel, libdv-devel
BuildRequires: libquicktime-devel, SDL-devel, imlib2-devel, libpng-devel

%description
Tools: smil2raw, smil2yuv, and smil2wav.

%package devel
Summary: Header files, libraries and development documentation for %{name}
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
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README*
%doc %{_mandir}/man1/*.1*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so

%changelog
* Fri Dec 19 2003 Dag Wieers <dag@wieers.com> - 0.3.0-1
- Fixed a problem with the shared libraries. (Miguel Lemos)

* Wed Dec 17 2003 Dag Wieers <dag@wieers.com> - 0.3.0-0
- Initial package. (using DAR)
