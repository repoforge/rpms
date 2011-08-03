# $Id$
# Authority: dag

%{?el5:%define _without_egg-info 1}
%{?el4:%define _without_egg-info 1}
%{?el3:%define _without_egg-info 1}
%{?el2:%define _without_egg-info 1}

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name dnspython

Summary: DNS toolkit for Python
Name: python-dns
Version: 1.5.0
Release: 2%{?dist}
License: BSD-like
Group: Development/Languages
URL: http://www.dnspython.org/

Source: http://www.dnspython.org/kits/%{version}/dnspython-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel

%description
dnspython is a DNS toolkit for Python. It supports almost all record
types. It can be used for queries, zone transfers, and dynamic
updates. It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set. The low level classes allow direct
manipulation of DNS zones, messages, names, and records.

%prep
%setup -n %{real_name}-%{version}

find examples/ -type f | xargs %{__chmod} a-x

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog LICENSE README TODO examples/
%{python_sitelib}/dns/
%{!?_without_egg_info:%{python_sitelib}/*.egg-info}

%changelog
* Wed Aug 03 2011 Steve Huff <shuff@vecna.org> - 1.5.0-2
- Update for el6 compatibility.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.5.0-1
- Updated to release 1.5.0.

* Mon Aug 14 2006 Dag Wieers <dag@wieers.com> - 1.4.0-1
- Initial package. (using DAR)
