# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Python binding for the wireless (wifi) extensions
Name: python-wifi
Version: 0.3
Release: 2%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://www.romanofski.de/downloads/pywifi

Source: http://www.romanofski.de/downloads/pywifi/%{version}/python-wifi-%{version}.linux-i686.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.0
Requires: python >= 2.0
Obsoletes: pywifi <= %{version}

%description
Pywifi is a Python library that provides currently read access to
information about a W-Lan card's capabilities, like the wireless
extensions written in C.

%prep
%setup -n %{name}

%{__cat} <<'EOF' >setup.py
import os, string, sys
from distutils.core import setup

def main():
	setup(
		name="%{name}",
		version="%{version}",
		description="%{summary}",
		author="Dag Wieers",
		author_email="dag@wieers.com, http://dag.wieers.com/, dag.wieers@gmail.com",
		maintainer="Dag Wieers",
		maintainer_email="dag@wieers.com",
		url="%{url}",
		license="%{license}",
		platforms="UNIX",
		long_description="""%{description}""",
		keywords=["wireless extensions", "wifi", "iwlibs"],
		packages=['pythonwifi'],
		package_dir={'pythonwifi': 'pythonwifi'},
#		py_modules=["pythonwifi"],
	)

if __name__ == "__main__": main()
EOF

### Fix permissions on examples and tests
%{__chmod} a+x docs/*.py examples/*.py tests/*.py

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE README docs/ examples/ tests/
%{python_sitelib}/pythonwifi/
%ghost %{python_sitelib}/pythonwifi/*.pyo

%changelog
* Tue Aug 08 2006 Dag Wieers <dag@wieers.com> - 0.3-2
- Added own setup.py.

* Sun Jul 09 2006 Dag Wieers <dag@wieers.com> - 0.3-1
- Updated to release 0.3.

* Tue May 24 2005 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
