# $Id$
# Authority: dag

%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pymad

Name: python-mad
Summary: Python Wrapper for the MPEG Audio Decoder Library
Version: 0.5.4
Release: 1.2%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://spacepants.org/src/pymad/

Source: http://spacepants.org/src/pymad/download/pymad-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel, libmad-devel
Requires: python >= %{python_version}

%description
This module makes the mad (MAD MP3 decoder) library available to python
(Python) programs. It provides a high-level API to the MAD functions,
that make reading audio data from an MPEG stream simple.

%prep
%setup -n %{real_name}-%{version}

%build
export CFLAGS="%{optflags}"
%{__python} config_unix.py --prefix="%{_prefix}"
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README THANKS
%{python_sitearch}/madmodule.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.4-1.2
- Rebuild for Fedora Core 5.

* Fri Jul 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.4-1
- Update to release 0.5.4.

* Sun May 08 2005 Dag Wieers <dag@wieers.com> - 0.5.3-1
- Initial package. (using DAR)
