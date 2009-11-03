# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

Summary: Network provisioning tool for Xen and Bare Metal Machines 
Name: koan
Version: 0.5.0
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://cobbler.et.redhat.com/

Source: http://cobbler.et.redhat.com/download/koan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.2
Requires: python >= 2.2
Requires: mkinitrd
Requires: syslinux

%description
Koan stands for kickstart-over-a-network and allows for both network
provisioning of new virtualized guests and destructive re-provisioning
of any existing system. For use with a boot-server configured with
'cobbler'

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
%doc AUTHORS COPYING CHANGELOG README NEWS
%doc %{_mandir}/man1/koan.1*
%{_bindir}/koan
%{python_sitelib}/koan/
%ghost %{python_sitelib}/koan/*.pyo

%changelog
* Mon Jul 02 2007 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Updated to release 0.5.0.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.3.1-1
- Initial package. (using DAR)
