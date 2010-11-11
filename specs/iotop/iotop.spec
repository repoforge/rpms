# $Id$
# Authority: dag

### EL6 ships with iotop-0.3.2-3.el6
### ExclusiveDist: el5

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Per process I/O bandwidth monitor
Name: iotop
Version: 0.3
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://guichaz.free.fr/iotop/

Source: http://guichaz.free.fr/iotop/files/iotop-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.5
Requires: python >= 2.5

%description
Iotop is a Python program with a top like UI used to show of behalf of which
process is the I/O going on.

%prep
%setup

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING NEWS THANKS
%doc %{_mandir}/man1/iotop.1*
%{_bindir}/iotop
%{python_sitelib}/iotop/
%exclude %{python_sitelib}/*.egg-info/

%changelog
* Fri May 08 2009 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
