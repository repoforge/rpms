# $Id$
# Authority: dag
# Upstream: <info$littlecms,com>

%{?dtag: %{expand: %%define %dtag 1}}

%{?el3:%define _without_python 1}
%{?rh9:%define _without_python 1}
%{?rh7:%define _without_python 1}
%{?el2:%define _without_python 1}

Summary: Open Source color management engine
Name: lcms
Version: 1.15
Release: 1.2%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://www.littlecms.com/

Source: http://www.littlecms.com/lcms-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libjpeg-devel, libtiff-devel, zlib-devel
%{!?_without_python:BuildRequires: python-devel >= 2.0, gcc-c++, swig, libtool}
Obsoletes: liblcms <= %{version}

%description
lcms is an Open Source color management engine. It implements a standalone
CMM engine and allows fast transforms between ICC profiles. It does not need
ICM or ColorSync to work.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: liblcms-devel <= %{version}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n python-lcms
Summary: Python bindings for the lcms color management engine
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: liblcms-python <= %{version}

%description -n python-lcms
python-lcms is a Python module that interfaces to the lcms color management
engine.

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}" \
%{!?_without_python:--with-python}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null || :

%postun
/sbin/ldconfig 2>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README*
%{_mandir}/man1/icc2ps.1*
%{_mandir}/man1/icclink.1*
%{_mandir}/man1/jpegicc.1*
%{_mandir}/man1/tifficc.1*
%{_mandir}/man1/wtpt.1*
%{_bindir}/icc2ps
%{_bindir}/icclink
%{_bindir}/icctrans
%{_bindir}/jpegicc
%{_bindir}/tiffdiff
%{_bindir}/tifficc
%{_bindir}/wtpt
%{_libdir}/liblcms.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*
%{_includedir}/icc34.h
%{_includedir}/lcms.h
%{_libdir}/liblcms.a
%exclude %{_libdir}/liblcms.la
%{_libdir}/liblcms.so
%{_libdir}/pkgconfig/lcms.pc

%if %{!?_without_python:1}0
%files -n python-lcms
%defattr(-, root, root, 0755)
%{_libdir}/python*/site-packages/lcms.py
%exclude %{_libdir}/python*/site-packages/_lcms.a
%exclude %{_libdir}/python*/site-packages/_lcms.la
%{_libdir}/python*/site-packages/_lcms.so
%endif

%changelog
* Mon Nov 28 2005 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Updated to release 1.15.

* Wed Jan 19 2005 Dag Wieers <dag@wieers.com> - 1.14-1
- Initial package. (using DAR)
