# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name pytimeago

Summary: Human-oriented representation of time deltas
Name: python-timeago
Version: 0.0
Release: 1.r11%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://adomas.org/pytimeago/

Source: http://adomas.org/pytimeago/pytimeago.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel
Obsoletes: pytimeago < %{version}-%{release}
Provides: pytimeago = %{version}-%{release}

%description
pytimeago is a small Python library that transforms the numerical
difference between timestamps into human-readable strings like
"3h ago" or "5 months ago". Such functionality is often present in
email, issue tracking and other applications that display a number
of items to the user. It is practical to briefly describe the age
of a certain item.

%prep
%setup -c

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
		keywords=["timestamps", "time-delta", "time difference"],
		packages=['pytimeago'],
		package_dir={'pytimeago': 'pytimeago'},
#		py_modules=["pytimeago"],
	)

if __name__ == "__main__": main()
EOF

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{python_sitelib}/pytimeago/
%ghost %{python_sitelib}/pytimeago/*.pyo

%changelog
* Mon Aug 14 2006 Dag Wieers <dag@wieers.com> - 0.0-1.r11
- Initial package. (using DAR)
