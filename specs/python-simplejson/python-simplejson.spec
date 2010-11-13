# $Id$
# Authority: dag

### EL6 ships with python-simplejson-2.0.9-3.1.el6
# ExclusiveDist: el2 el3 el4 el5

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Simple, fast, extensible JSON encoder/decoder for Python
Name: python-simplejson
Version: 2.0.5
Release: 1%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://code.google.com/p/simplejson/

Source: http://cheeseshop.python.org/packages/source/s/simplejson/simplejson-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel
BuildRequires: python-setuptools
BuildRequires: python-nose

%description
simplejson is a simple, fast, complete, correct and extensible
JSON <http://json.org> encoder and decoder for Python 2.3+.  It is
pure Python code with no dependencies.

simplejson was formerly known as simple_json, but changed its name to
comply with PEP 8 module naming guidelines.

The encoder may be subclassed to provide serialization in any kind of
situation, without any special support by the objects to be serialized
(somewhat like pickle).

The decoder can handle incoming JSON strings of any specified encoding
(UTF-8 by default).

%prep
%setup -n simplejson-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}" \
    --single-version-externally-managed

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc docs LICENSE.txt
%{python_sitearch}/simplejson-%{version}-py*.egg-info
%{python_sitearch}/simplejson/

%changelog
* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 2.0.5-1
- Initial package. (based on fedora)
