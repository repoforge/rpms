# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Python binding for the wireless (wifi) extensions
Name: python-wifi
Version: 0.3
Release: 1
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

### Fix permissions on examples and tests
%{__chmod} a+x docs/*.py examples/*.py tests/*.py

%build
#%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
#%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
#%{__install} -Dp -m0644 iwlibs.py %{buildroot}%{python_sitelib}/iwlibs.py
#%{__install} -Dp -m0755 pyiwconfig %{buildroot}%{_bindir}/pyiwconfig
#%{__install} -Dp -m0755 pyiwlist %{buildroot}%{_bindir}/pyiwlist
%{__install} -d -m0755 %{buildroot}%{python_sitelib}/pythonwifi/
%{__install} -Dp -m0755 pythonwifi/*.py %{buildroot}%{python_sitelib}/pythonwifi/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE README docs/ examples/ tests/
%{python_sitelib}/pythonwifi/

%changelog
* Sun Jul 09 2006 Dag Wieers <dag@wieers.com> - 0.3-1
- Updated to release 0.3.

* Tue May 24 2005 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
