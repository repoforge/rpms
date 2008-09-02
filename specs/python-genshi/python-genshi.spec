# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name Genshi

Summary: Python toolkit for generation of output for the web
Name: python-genshi
Version: 0.5.1
Release: 2
License: BSD
Group: Development/Libraries
URL: http://genshi.edgewall.org/wiki/

Source: http://ftp.edgewall.com/pub/genshi/Genshi-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: python >= 2.3, python-setuptools >= 0.6, python-devel
Requires: python >= 2.3, python-setuptools => 0.6

%description

Genshi is a Python library that provides an integrated set of components for
parsing, generating, and processing HTML, XML or other textual content for 
output generation on the web.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --single-version-externally-managed --optimize="1" --root="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING PKG-INFO README.txt doc/ examples/
%{python_sitearch}/genshi/
%{python_sitearch}/Genshi-%{version}-py*.egg-info/

%changelog
* Wed Aug 06 2008 Brandon Davidson <brandond@uoregon.edu> - 0.5.1-2
- Added egg-info files.

* Wed Jul 30 2008 Brandon Davidson <brandond@uoregon.edu> - 0.5.1-1
- Initial package.
