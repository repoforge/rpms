# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name pysnmp

Summary: SNMP engine written in Python
Name: python-pysnmp
Version: 4.1.14a
Release: 1%{?dist}
License: BSD
Group: Development/Libraries
URL: http://pysnmp.sourceforge.net/

Source: http://dl.sf.net/pysnmp/pysnmp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-setuptools

Requires: net-snmp

%description
This is a Python implementation of SNMP v.1/v.2c engine. It's
general functionality is to assemble/disassemble SNMP messages
from/into given SNMP Object IDs along with associated values.
PySNMP also provides a few transport methods specific to TCP/IP
networking.

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
%defattr(-, root, root, -)
%doc CHANGES LICENSE README THANKS TODO docs/ examples/
%{_bindir}/*%{real_name}*
%{python_sitelib}/%{real_name}/
%{python_sitelib}/%{real_name}*.egg-info

%changelog
* Thu Sep 15 2011 Dag Wieers <dag@wieers.com> - 4.1.14a-1
- Initial package. (using DAR)
