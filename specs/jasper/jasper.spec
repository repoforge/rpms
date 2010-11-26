# $Id$
# Authority: shuff
# Upstream: Michael D. Adams <mdadams$ece.uvic.ca>

### EL6 already ships with jasper-1.900.1-15.el6
# ExclusiveDist: el2 el3 el4 el5

%{?el4:%define _without_modxorg 1}

%{?el3:%define _without_freeglut 1}
%{?el3:%define _without_modxorg 1}

%{?el2:%define _without_freeglut 1}
%{?el2:%define _without_modxorg 1}

Summary: Reference implementation of the JPEG-2000 Part-1 standard
Name: jasper
Version: 1.900.1
Release: 2%{?dist}
License: Modified BSD
Group: System Environment/Libraries
URL: http://www.ece.uvic.ca/~mdadams/jasper/

Source: http://www.ece.uvic.ca/~mdadams/jasper/software/jasper-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Provides: libjasper = %{version}-%{release}
Obsoletes: libjasper <= %{version}-%{release}

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: binutils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: libjpeg-devel
BuildRequires: libtool
BuildRequires: make
%{!?_without_modxorg:BuildRequires: libICE-devel, libSM-devel, libX11-devel, libXext-devel, libXi-devel, libXmu-devel, libXt-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_freeglut:BuildRequires: freeglut-devel}
%{?_without_freeglut:BuildRequires: glut-devel}


%description
JasPer is a collection of software (i.e., a library and application programs)
for the coding and manipulation of images.  This software can handle image data
in a variety of formats.  One such format supported by JasPer is the JPEG-2000
format defined in ISO/IEC 15444-1:2000.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

Provides: libjasper-devel = %{version}-%{release}
Obsoletes: libjasper-devel <= %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
    --disable-dependency-tracking \
    --disable-static \
    --enable-shared \
    --with-x
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYRIGHT INSTALL LICENSE NEWS README doc/
%doc %{_mandir}/man1/imgcmp.1*
%doc %{_mandir}/man1/imginfo.1*
%doc %{_mandir}/man1/jasper.1*
%doc %{_mandir}/man1/jiv.1*
%{_bindir}/imgcmp
%{_bindir}/imginfo
%{_bindir}/jasper
%{_bindir}/jiv
%{_bindir}/tmrdemo
%{_libdir}/libjasper.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/jasper/
%{_libdir}/libjasper.so
%exclude %{_libdir}/libjasper.la

%changelog
* Thu Nov 25 2010 Dag Wieers <dag@wieers.com> - 1.900.1-2
- Renamed libjasper to jasper.

* Thu Jul 08 2010 Steve Huff <shuff@vecna.org> - 1.900.1-1
- Initial package.
