# $Id$
# Authority: dag

### EL6 ships with python-genshi-0.5.1-7.1.el6
# ExclusiveDist: el2 el3 el4 el5

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name Genshi

Summary: Python toolkit for generation of output for the web
Name: python-genshi
Version: 0.6
Release: 1%{?dist}
License: BSD
Group: Development/Libraries
URL: http://genshi.edgewall.org/wiki/

Source: http://ftp.edgewall.com/pub/genshi/Genshi-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch: noarch
BuildRequires: python >= 2.4
BuildRequires: python-devel >= 2.4
BuildRequires: python-setuptools >= 0.6
Requires: python >= 2.4
Requires: python-setuptools => 0.6

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
%{__python} setup.py install --single-version-externally-managed --optimize="1" --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING PKG-INFO README.txt doc/ examples/
%{python_sitelib}/genshi/
%{python_sitelib}/Genshi-%{version}-py*.egg-info/

%changelog
* Mon Jun 14 2010 Dag Wieers <dag@wieers.com> - 0.6-1
- Updated to release 0.6.

* Wed Aug 06 2008 Brandon Davidson <brandond@uoregon.edu> - 0.5.1-2
- Added egg-info files.

* Wed Jul 30 2008 Brandon Davidson <brandond@uoregon.edu> - 0.5.1-1
- Initial package.
