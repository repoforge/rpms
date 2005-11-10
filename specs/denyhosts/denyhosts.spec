# $Id$
# Authority: dries
# Upstream:  Phil Schwartz <phil_schwartz$users,sourceforge,net>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name DenyHosts

Summary: Scan ssh server logs and block hosts
Name: denyhosts
Version: 1.1.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://denyhosts.sourceforge.net/

Source: http://dl.sf.net/denyhosts/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: python

%description
DenyHosts is a script intended to help Linux system administrators thwart 
ssh server attacks. DenyHosts scans an ssh server log, updates 
/etc/hosts.deny after a configurable number of failed attempts from a 
rogue host is determined, and alerts the administrator of any suspicious 
logins.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}" --prefix="%{_prefix}"
%{__rm} -Rf %{buildroot}%{_datadir}/denyhosts

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG.txt daemon-control-dist denyhosts.cfg-dist LICENSE.txt README.txt
%{_bindir}/denyhosts.py
%{python_sitearch}/DenyHosts/

%changelog
* Wed Nov 09 2005 Dries Verachtert <dries@ulyssis.org> - 1.1.1-1
- Updated to release 1.1.1.

* Tue Sep 27 2005 Dries Verachtert <dries@ulyssis.org> - 1.1.0-1
- Updated to release 1.1.0.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.3-1
- Initial package.
