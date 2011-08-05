# $Id$
# Authority: dag

%{?el5:%define _without_egg-info 1}
%{?el4:%define _without_egg-info 1}
%{?el3:%define _without_egg-info 1}
%{?el2:%define _without_egg-info 1}

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name PyYAML

Summary: Python package implementing YAML parser and emitter
Name: python-yaml
Version: 3.09
Release: 2%{?dist}
License: GPL
Group: Development/Libraries
URL: http://pyyaml.org/wiki/PyYAML

Source: http://pyyaml.org/download/pyyaml/PyYAML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.2
Requires: python >= 2.2

Provides: PyYAML = %{name}-%{version}
Obsoletes: PyYAML <= %{name}-%{version}

%description
PyYAML is a YAML parser and emitter for the Python programming language. 

YAML is a data serialization format designed for human readability
and interaction with scripting languages.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README examples/
%{python_sitearch}/yaml/
%{!?_without_egg-info:%{python_sitearch}/*.egg-info}

%changelog
* Fri Aug 05 2011 Steve Huff <shuff@vecna.org> - 3.09-2
- Made the package arch-specific.
- Added egg-info support for el6.

* Mon May 17 2010 Dag Wieers <dag@wieers.com> - 3.09-1
- Updated to release 3.09.

* Wed Oct  8 2008 Dries Verachtert <dries@ulyssis.org> - 3.06-1
- Updated to release 3.06.

* Sun May 13 2007 Dag Wieers <dag@wieers.com> - 3.05-1
- Initial package. (using DAR)
