# $Id$
# Authority: matthias

Summary: DTS Coherent Acoustics decoder library
Name: libdca
Version: 0.0.5
Release: 1
License: GPLv2+
Group: System Environment/Libraries
URL: http://www.videolan.org/libdca.html

Source: http://download.videolan.org/pub/videolan/libdca/%{version}/libdca-%{version}.tar.bz2
Patch0: libdca-0.0.5-relsymlinks.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Free library for decoding DTS Coherent Acoustics streams.

%package tools
Summary: Tools from the DTS Coherent Acoustics decoder
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}

%description tools
Tools from the DTS Coherent Acoustics decoder.

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
%patch0 -p1 -b .relsymlinks

%build
### Force PIC as applications fail to recompile against the lib on x86_64 without
export CFLAGS="%{optflags} -fPIC"
%configure --disable-static
### Get rid of the /usr/lib64 RPATH on 64bit (as of 0.0.5)
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
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
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc doc/libdca.txt
%{_libdir}/libdca.so.*

%files tools
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/dcadec.1*
%doc %{_mandir}/man1/dtsdec.1*
%doc %{_mandir}/man1/extract_dca.1*
%doc %{_mandir}/man1/extract_dts.1*
%{_bindir}/dcadec
%{_bindir}/dtsdec
%{_bindir}/extract_dca
%{_bindir}/extract_dts

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/dca.h
%{_includedir}/dts.h
%{_libdir}/libdca.so
%{_libdir}/pkgconfig/libdca.pc
%{_libdir}/pkgconfig/libdts.pc
%exclude %{_libdir}/libdca.la

%changelog
* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 0.0.5-1
- Update to 0.0.5.
- Patch to have relative symlinks created.
- Split out tools to fix inter-repo problems.
- Split out devel now that a shared library is produced by default.
- Pass --disable-static (it does disable libdca.a).

* Mon Sep 18 2006 Matthias Saou <http://freshrpms.net/> 0.0.2-4
- Use the source from videolan.org as it is available again.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.0.2-3
- Release bump to drop the disttag number in FC5 build.

* Fri Dec  9 2005 Matthias Saou <http://freshrpms.net/> 0.0.2-2
- Force -fPIC, as applications fail to recompile against the lib on x86_64
  without.

* Thu Aug 25 2005 Matthias Saou <http://freshrpms.net/> 0.0.2-1
- Initial RPM release.

