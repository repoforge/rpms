# $Id$
# Authority: matthias
# Upstream: Dan Dennedy <ddennedy$users,sf,net>
# Upstream: <libdv-dev$lists,sourceforge,net>

### EL6 ships with libdv-1.0.0-8.1.el6
### EL5 ships with libdv-0.104-4.fc6.1
### EL4 ships with libdv-0.103-1
# ExclusiveDist: el2 el3 el4

Summary: Codec for DV video, used by most digital camcorders
Name: libdv
Version: 0.102
Release: 3%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://libdv.sourceforge.net/
Source: http://dl.sf.net/libdv/libdv-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk+-devel >= 1.2.4, pkgconfig >= 0.9.0
# libtool, *sigh*
BuildRequires: gcc-c++

%description
The Quasar DV codec (libdv) is a software codec for DV video, the encoding
format used by most digital camcorders, typically those that support the
IEEE 1394 (a.k.a. FireWire or i.Link) interface. Libdv was developed
according to the official standards for DV video: IEC 61834 and SMPTE 314M.


%package tools
Summary: Basic tools to manipulate Digital Video streams
Group: Applications/Multimedia
Requires: %{name} = %{version}

%description tools
This package contains some basic programs to display and encode
digital video streams. This programs uses the Quasar DV codec (libdv),
a software codec for DV video, the encoding format used by most
digital camcorders, typically those that support the IEEE 1394
(a.k.a. FireWire or i.Link) interface.


%package devel
Summary: Development file for programs which use the libdv library
Group: Development/Libraries
Requires: %{name} = %{version}, gtk+-devel >= 1.2.4, pkgconfig >= 0.9.0

%description devel
The Quasar DV codec (libdv) is a software codec for DV video, the encoding
format used by most digital camcorders, typically those that support the
IEEE 1394 (a.k.a. FireWire or i.Link) interface. Libdv was developed
according to the official standards for DV video: IEC 61834 and SMPTE 314M.

This is the libraries, include files and other resources that are used to
incorporate libdv into applications.


%prep
%setup


%build
%configure --program-prefix=%{?_program_prefix}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPY* NEWS README* TODO
%{_libdir}/*.so.*

%files tools
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libdv/
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Mon May 10 2004 Dag Wieers <dag@wieers.com> - 0.102-3
- Split off the libdv-tools subpackage.
- Increased release to 3 to be in sync with dag.

* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 0.102-1
- Update to 0.102, which has a newer library version.

* Tue Feb 24 2004 Matthias Saou <http://freshrpms.net/> 0.101-2
- Add missing gtk+-devel dependency on the devel package.

* Tue Feb 24 2004 Matthias Saou <http://freshrpms.net/> 0.101-1
- Update to 0.101.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.99-3
- Rebuild for Fedora Core 1.

* Tue Aug 12 2003 Matthias Saou <http://freshrpms.net/>
- Added gtk+-devel build dep.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Exclude .la files.

* Thu Jan 23 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.

* Thu Sep 26 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Thu Aug  1 2002 Matthias Saou <http://freshrpms.net/>
- Spec file rewrite from the one included with the sources.

