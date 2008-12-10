# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Discovery-based unittest extension for Python
Name: python-nose
Version: 0.10.4
Release: 1
License: LGPL
Group: Development/Languages
URL: http://somethingaboutorange.com/mrl/projects/nose/

Source: http://somethingaboutorange.com/mrl/projects/nose/nose-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-setuptools
Requires: python-setuptools

%description
nose: a discovery-based unittest extension.

nose provides an alternate test discovery and running process for unittest,
one that is intended to mimic the behavior of py.test as much as is
reasonably possible without resorting to too much magic.

%prep
%setup -n nose-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}" \
    --single-version-externally-managed --install-data="%{_datadir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGELOG lgpl.txt NEWS README.txt
%doc %{_mandir}/man1/nosetests.1.gz
%{_bindir}/nosetests
%{python_sitelib}/nose-%{version}-py*.egg-info
%{python_sitelib}/nose/

%changelog
* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.10.4-1
- Initial package. (based on fedora)
