# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{!?dist: %define ft2build 1}
%{?fc3: %define ft2build 1}
%{?fc2: %define ft2build 1}
%{?yd4: %define ft2build 1}

%define pyver %(%{__python} -c 'import sys; print sys.version[:3]' || echo 2.0)

Summary: Python's own image processing library
Name: python-imaging
Version: 1.1.4
Release: 2
License: Distributable
Group: Development/Libraries
URL: http://www.pythonware.com/products/pil/
Source: http://effbot.org/downloads/Imaging-%{version}.tar.gz
Patch: python-imaging-1.1.4-setup.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python >= %{pyver}
BuildRequires: python, python-devel, gtk+-devel
BuildRequires: libjpeg-devel, libpng-devel, freetype-devel, zlib-devel
Obsoletes: PIL <= %{version}
Provides: PIL = %{version}-%{release}

%description
The Python Imaging Library (PIL) adds image processing capabilities 
to your Python interpreter.

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.


%prep
%setup -n Imaging-%{version}
%patch -p1 -b .setup
%{__perl} -pi -e 's|/usr/local|%{_prefix}|' \
    Setup.in Scripts/*.py libImaging/Makefile.in libImaging/configure
%{?ft2build:%{__perl} -pi.orig -e 's|^(#include <freetype/freetype.h>)$|#include <ft2build.h>\n$1|' _imagingft.c}


%build
pushd libImaging
    %configure
    %{__make} OPT="%{optflags}"
popd
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CHANGES* CONTENTS README Images/ Sane/ Scripts/
%{_libdir}/python*/site-packages/PIL.pth
%{_libdir}/python*/site-packages/PIL/


%changelog
* Thu Oct 21 2004 Matthias Saou <http://freshrpms.net/> 1.1.4-2
- Further spec file updates.
- Build without tcl/tk... which shouldn't harm for a python/gtk module!

* Mon Oct 18 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.1.4-2.fdr.1: adapted for Fedora

* Sat Oct 16 2004 Johan Dahlin <johan@fluendo.com> - 1.1.4-2
- stole dags spec
- remove includes
- install in PIL/ with .pth
- install freetype bindings
- don't depend on doc package

* Mon Dec 08 2003 Dag Wieers <dag@wieers.com> - 1.1.4-1
- Fixed python location for RHFC1. (Ian Burrell)

* Mon Jun 30 2003 Dag Wieers <dag@wieers.com> - 1.1.4-0
- Updated to release 1.1.4.

* Sat Jan 04 2003 Dag Wieers <dag@wieers.com> - 1.1.3-0
- Initial package. (using DAR)
