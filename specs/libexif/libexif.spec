# $Id$
# Authority: matthias
# Upstream: <libexif-devel$lists,sf,net>

### EL6 ships with libexif-0.6.16-4.1.el6
### EL5 ships with libexif-0.6.13-4.0.2.el5_1.1
### EL4 ships with libexif-0.5.12-5.1.0.2.el4_6.1
# ExclusiveDist: el2 el3

### Beware FC3 comes with older libexif !
# Tag: rft

Name: libexif
Summary: EXIF image tag library
Version: 0.6.9
Release: 1%{?dist}
License: GPL
URL: http://libexif.sourceforge.net/
Source: http://dl.sf.net/libexif/libexif-%{version}.tar.gz
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++

%description
Most digital cameras produce EXIF files, which are JPEG files with extra tags
that contain information about the image. The EXIF library allows you to parse
an EXIF file and read the data from those tags.


%package devel
Summary: The files needed for libexif application development
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig

%description devel
The libexif-devel package contains the libraries and include files
that you can use to develop libexif applications.

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

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Jul 15 2004 Matthias Saou <http://freshrpms.net/> 0.6.9-1
- Update to 0.6.9.

* Mon Nov  5 2003 Matthias Saou <http://freshrpms.net/> 0.5.12-2
- Rebuild for Fedora Core 1.

* Tue Aug  5 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.12.

* Thu Jul 24 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.10.
- The lang file is back from %%{name}-8 to %%{name}.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.9.
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Tue Jan 21 2003 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup based on the one made by "tack".

