# $Id$
# Authority: dag

Summary: Control operation of a CD-ROM when playing audio CDs
Name: libcdaudio
Version: 0.99.12p2
Release: 12%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://libcdaudio.sourceforge.net/

Source: http://dl.sf.net/libcdaudio/libcdaudio-%{version}.tar.gz
Patch0: libcdaudio-0.99.12-buffovfl.patch
Patch1: libcdaudio-0.99.12p2-libdir.patch
Patch2: libcdaudio-0.99-CAN-2005-0706.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
libcdaudio is a library designed to provide functions to control
operation of a CD-ROM when playing audio CDs.  It also contains
functions for CDDB and CD Index lookup.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
%configure \
  --disable-static \
  --enable-dependency-tracking \
  --enable-threads
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/%{name}-config
%{_datadir}/aclocal/%{name}.m4
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libcdaudio.pc
%exclude %{_libdir}/*.la

%changelog
* Sat Dec 27 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.99.12p2-11
- Fix CVE-2005-0706.

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.99.12p2-10
- took COPYING out of doc (it is simply wrong)
- fixed license tag

* Fri Dec 29 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.99.12p2-8
- Change Group tag.
- Fix libcdaudio-config for libdir != %%{_prefix}/lib.

* Wed Dec 27 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.99.12p2-7
- Update to 0.99.12p2.

* Tue Sep 13 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Patch to fix buffer overflow by Brian C. Huffman
  <huffman@graze.net>.

* Sat Jul 23 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.99.12.

* Wed May 14 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.
