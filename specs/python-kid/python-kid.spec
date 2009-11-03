# $Id$
# Authority: dag

%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name kid

Summary: Simple and pythonic XML template language
Name: python-kid
Version: 0.9.6
Release: 1%{?dist}
License: MIT
Group: Development/Libraries
URL: http://www.lesscode.org/projects/kid/

Source0: http://www.kid-templating.org/dist/%{version}/dist/kid-%{version}.tar.gz
Source1: http://cheeseshop.python.org/packages/2.4/s/setuptools/setuptools-0.6c6-py2.4.egg
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.2, python-elementtree
Requires: python >= %{python_version},  python-elementtree

%description
Kid is a simple Python based template language for generating and
transforming XML vocabularies. Kid was spawned as a result of a kinky love
triangle between XSLT, TAL, and PHP.

%prep
%setup -n %{real_name}-%{version}
%{__cp} -v %{SOURCE1} .

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING HISTORY README doc/ examples/
%{_bindir}/kid
%{_bindir}/kidc
%{python_sitelib}/kid/
%exclude %{python_sitelib}/kid-0.9.6-py*.egg-info/

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.9.6-1
- Updated to release 0.9.6.

* Mon May 09 2005 Dag Wieers <dag@wieers.com> - 0.6.3-1
- Initial package. (using DAR)
