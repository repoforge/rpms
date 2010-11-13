# $Id$
# Authority: dag

### EL6 ships with python-ethtool-0.3-5.1.el6
# ExclusiveDist: el2 el3 el4 el5

%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%{?el4:%define _without_iff_dynamic 1}

Summary: Ethernet settings python bindings
Name: python-ethtool
Version: 0.3
Release: 2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://git.kernel.org/?p=linux/kernel/git/acme/python-ethtool.git

Source: http://userweb.kernel.org/~acme/python-ethtool/%{name}-%{version}.tar.bz2
Patch0: python-ethtool-0.3-iff-dynamic.patch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel

%description
Python bindings for the ethtool kernel interface, that allows querying and
changing of ethernet card settings, such as speed, port, autonegotiation, and
PCI locations.

%prep
%setup

%{?_without_iff_dynamic:%patch0 -p0}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%{__install} -Dp -m0755 pethtool.py %{buildroot}%{_sbindir}/pethtool
%{__install} -Dp -m0755 pifconfig.py %{buildroot}%{_sbindir}/pifconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING
%{_sbindir}/pethtool
%{_sbindir}/pifconfig
%{python_sitearch}/ethtool.so
#%{python_sitearch}/*.egg-info

%changelog
* Tue Mar 10 2009 Dag Wieers <dag@wieers.com> - 0.3-2
- Added IFF_DYNAMIC patch for pifconfig too.

* Tue Mar 10 2009 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
