# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Relying party support for the Yadis service discovery protocol
Name: python-yadis
Version: 1.1.0
Release: 1%{?dist}
License: LGPL
Group: Development/Languages
URL: http://www.openidenabled.com/yadis/libraries/python/

Source: http://www.openidenabled.com/resources/downloads/python-openid/python-yadis-%{version}.tar.gz
Patch0: python-yadis-1.0.1-silencepyflakes.patch
Patch1: python-yadis-1.1.0-silencepyflakes+elementtree.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
#BuildRequires: epydoc, pyflakes
BuildRequires: python-devel, PyXML, python-urljr, python-elementtree
Requires: python-elementtree, PyXML, python-urljr

%description
python-yadis implements relying party support for the Yadis service
discovery protocol. The protocol was developed for use by
decentralized URL-based identity systems, but is useful for
advertising services provided by or on behalf of a certain URL.

%prep
%setup
%patch1 -p0

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
 
%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README doc/ examples/
%{python_sitelib}/yadis/
%ghost %{python_sitelib}/yadis/*.pyo

%changelog
* Tue Jul 10 2007 Dag Wieers <dag@wieers.com> - 1.1.0-1
- Initial package. (using DAR)
