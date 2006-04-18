# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Python binding for the wireless (wifi) extensions
Name: python-wifi
Version: 0.2
Release: 1.2
License: LGPL
Group: Development/Libraries
URL: http://www.romanofski.de/downloads/pywifi

Source: http://www.romanofski.de/downloads/pywifi/%{version}/pywifi-%{version}.tar.gz
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
%setup -n pywifi

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 iwlibs.py %{buildroot}%{python_sitelib}/iwlibs.py
%{__install} -Dp -m0755 pyiwconfig %{buildroot}%{_bindir}/pyiwconfig
%{__install} -Dp -m0755 pyiwlist %{buildroot}%{_bindir}/pyiwlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog LICENSE NEWS README TODO
%{python_sitelib}/iwlibs.py
%{_bindir}/pyiwconfig
%{_bindir}/pyiwlist

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2-1.2
- Rebuild for Fedora Core 5.

* Tue May 24 2005 Dag Wieers <dag@wieers.com> - 0.2.0-1
- Initial package. (using DAR)
