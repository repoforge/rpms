# $Id$
# Authority: dag

%define pyver %(python2 -c 'import sys; print sys.version[:3]')

Summary: Python's own image processing library
Name: python-imaging
Version: 1.1.4
Release: 1
License: Distributable
Group: Development/Libraries
URL: http://www.pythonware.com/products/pil/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.pythonware.com/downloads/Imaging-%{version}.tar.gz
Source1: Imaging-doc.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildPreReq: libjpeg-devel >= 6b, zlib-devel >= 1.1.2, libpng-devel >= 1.0.1, tk
Requires: python >= %{pyver}, libjpeg >= 6b, zlib >= 1.1.2, libpng >= 1.0.1
Obsoletes: PIL <= %{version}
Provides: PIL = %{version}-%{release}

%description
The Python Imaging Library (PIL) adds image processing capabilities 
to your Python interpreter.

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.

%prep
%setup -n Imaging-%{version} -a1
find -type f | xargs fgrep -l /usr/local | xargs -r perl -pi.orig -e 's|/usr/local|%{_prefix}|g'

%build
cd libImaging
%configure
%{__make} \
	OPT="%{optflags}"
cd -

python2 setup.py build_ext -i
#%{__make} -f Makefile.pre.in boot
#%{__make} \
#	OPT="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0644 PIL.pth %{buildroot}%{_libdir}/python%{pyver}/site-packages/PIL.pth
%{__install} -D -m0755 _imaging.so %{buildroot}%{_libdir}/python%{pyver}/lib-dynload/_imaging.so
%{__install} -D -m0755 _imagingtk.so %{buildroot}%{_libdir}/python%{pyver}/lib-dynload/_imagingtk.so
%{__cp} -av  PIL/* %{buildroot}%{_libdir}/python%{pyver}/site-packages/
%{__cp} -av  libImaging/*.h %{buildroot}%{_includedir}/python%{pyver}/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES* CONTENTS README handbook/ Images/ notes/ Sane/ Scripts/
%{_libdir}/python*/lib-dynload/*
%{_libdir}/python*/site-packages/*
%{_includedir}/python*/*.h

%changelog
* Mon Dec 08 2003 Dag Wieers <dag@wieers.com> - 1.1.4-1
- Fixed python location for RHFC1. (Ian Burrell)

* Mon Jun 30 2003 Dag Wieers <dag@wieers.com> - 1.1.4-0
- Updated to release 1.1.4.

* Sat Jan 04 2003 Dag Wieers <dag@wieers.com> - 1.1.3-0
- Initial package. (using DAR)
