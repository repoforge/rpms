# $Id$
# Authority: dag


%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define pyver %(%{__python} -c 'import sys; print sys.version[:3]' || echo 2.0)

Summary: Python's own image processing library
Name: python-imaging
Version: 1.1.6
Release: 2%{?dist}
License: Distributable
Group: Development/Libraries
URL: http://www.pythonware.com/products/pil/

Source: http://effbot.org/downloads/Imaging-%{version}.tar.gz
Patch0: python-imaging-no-xv.patch
Patch1: python-imaging-lib64.patch
Patch2: python-imaging-giftrans.patch
Patch3: python-imaging-1.1.6-sane-types.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel, gtk+-devel
BuildRequires: libjpeg-devel, libpng-devel, freetype-devel, zlib-devel
Requires: python >= %{pyver}
Obsoletes: PIL <= %{version}
Provides: PIL = %{version}-%{release}

%description
The Python Imaging Library (PIL) adds image processing capabilities
to your Python interpreter.

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.

%prep
%setup -n Imaging-%{version}
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1 -b .sane-types

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

### Clean up buildroot
for script in %{buildroot}%{_bindir}/*.py; do
	%{__mv} -f $script %{buildroot}%{_bindir}/$(basename $script .py)
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES* CONTENTS Images/ README Sane/ Scripts/
%{_bindir}/pilconvert
%{_bindir}/pildriver
%{_bindir}/pilfile
%{_bindir}/pilfont
%{_bindir}/pilprint
%{python_sitearch}/PIL.pth
%{python_sitearch}/PIL/

%changelog
* Wed Jun 13 2007 Dag Wieers <dag@wieers.com> - 1.1.6-2
- Added patches from Fedora.
- Fixed a problem where png support was disabled for x86_64. (Paul Casteels)

* Thu May 31 2007 Dag Wieers <dag@wieers.com> - 1.1.6-1
- Updated to release 1.1.6.
- Rename the python scripts in %%{_bindir} without .py.

* Mon Aug 14 2006 Dag Wieers <dag@wieers.com> - 1.1.5-1
- Updated to release 1.1.5.

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
