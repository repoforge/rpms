# $Id$
# Authority: shuff
# Upstream: Michael D. Adams <mdadams$ece.uvic.ca>

%define real_name jasper

Summary: Reference implementation of the JPEG-2000 Part-1 standard
Name: libjasper
Version: 1.900.1
Release: 1%{?dist}
License: Modified BSD
Group: System Environment/Libraries
URL: http://www.ece.uvic.ca/~mdadams/jasper/

Source: http://www.ece.uvic.ca/~mdadams/jasper/software/jasper-%{version}.zip
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-%{dist}-%{arch}-XXXXXX)

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: binutils
BuildRequires: freeglut-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: libjpeg-devel
BuildRequires: libtool
BuildRequires: libICE-devel
BuildRequires: libSM-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXi-devel
BuildRequires: libXmu-devel
BuildRequires: libXt-devel
BuildRequires: make
BuildRequires: rpm-macros-rpmforge

%description
JasPer is a collection of software (i.e., a library and application programs)
for the coding and manipulation of images.  This software can handle image data
in a variety of formats.  One such format supported by JasPer is the JPEG-2000
format defined in ISO/IEC 15444-1:2000.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
    --disable-dependency-tracking \
    --enable-shared \
    --disable-static \
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
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/jasper/
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Thu Jul 08 2010 Steve Huff <shuff@vecna.org> - 1.900.1-1
- Initial package.
