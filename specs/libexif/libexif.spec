# $Id$

Name: libexif
Summary: EXIF image tag library
Version: 0.5.12
Release: 2.fr
License: GPL
URL: http://libexif.sourceforge.net/
Source: http://dl.sf.net/libexif/%{name}-%{version}.tar.gz
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc ChangeLog README
%{_libdir}/*.so*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc

%changelog
* Mon Nov  5 2003 Matthias Saou <http://freshrpms.net/> 0.5.12-2.fr
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

