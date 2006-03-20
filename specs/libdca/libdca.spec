# $Id$
# Authority: matthias

Summary: DTS Coherent Acoustics decoder
Name: libdca
Version: 0.0.2
Release: 3
License: GPL
Group: System/Library
URL: http://www.videolan.org/libdca.html
Source: http://debian.unnet.nl/pub/videolan/libdts/%{version}/libdts-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# Only a static lib, but two binaries too, so provide devel in the main
Provides: %{name}-devel = %{version}-%{release}
Requires: pkgconfig

%description
Free library for decoding DTS Coherent Acoustics streams.


%prep
%setup -n libdts-%{version}


%build
# Force PIC as applications fail to recompile against the lib on x86_64 without
export CFLAGS="%{optflags} -fPIC"
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc doc/libdts.txt
%{_bindir}/dtsdec
%{_bindir}/extract_dts
%{_includedir}/dts.h
%{_libdir}/libdts.a
%{_libdir}/libdts_pic.a
%{_libdir}/pkgconfig/libdts.pc
%{_mandir}/man1/dtsdec.1*
%{_mandir}/man1/extract_dts.1*


%changelog
* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.0.2-3
- Release bump to drop the disttag number in FC5 build.

* Fri Dec  9 2005 Matthias Saou <http://freshrpms.net/> 0.0.2-2
- Force -fPIC, as applications fail to recompile against the lib on x86_64
  without.

* Thu Aug 25 2005 Matthias Saou <http://freshrpms.net/> 0.0.2-1
- Initial RPM release.

