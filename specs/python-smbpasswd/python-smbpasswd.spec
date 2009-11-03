# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Python SMB Password Hash Generator Module
Name: python-smbpasswd
Version: 1.0.1
Release: 1%{?dist}
License: GPL
Group: Development/Languages
URL: http://barryp.org/software/py-smbpasswd/

Source: http://barryp.org/software/py-smbpasswd/files/py-smbpasswd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel

%description
python-smbpasswd is a python module able to generate LANMAN and NT password
hashes suiteable for use with Samba.

%prep
%setup -n py-smbpasswd-%{version}
%{__chmod} 0644 smbpasswd.c

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
 
%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README.txt
%{python_sitearch}/smbpasswd.so

%changelog
* Mon Aug 14 2006 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Initial package. (using DAR)
