# $Id$
# Authority: dag
# Upstream: Sebastian Stark <cran$users,sourceforge,net>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: program that executes the same command on many hosts in parallel
Name: tentakel
Version: 2.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://tentakel.biskalar.de/

Source: http://dl.sf.net/tentakel/tentakel-%{version}.tgz
Patch0: tentakel-2.1.3-setup.py.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
Requires: python
BuildRequires: python

%description
Tentakel is a program that executes the same command on many hosts in parallel
using SSH. It is designed to be easily extendable. The output of the remote
command can be controlled by means of format strings.

%prep
%setup
%patch0 -p0

%build
%{__make}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	PREFIX="%{buildroot}%{_prefix}" \
	sharedoc="doc-rpm"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}/tentakel-*/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc PLUGINS README TODO tentakel.1.html tentakel.conf.example
%doc %{_mandir}/man1/tentakel.1*
%{_bindir}/tentakel
%{python_sitelib}/lekatnet/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.2-1.2
- Rebuild for Fedora Core 5.

* Tue Mar 22 2005 Dag Wieers <dag@wieers.com> - 2.2-1
- Updated to release 2.2.

* Mon Sep 27 2004 Dag Wieers <dag@wieers.com> - 2.1.3-1
- Initial package. (using DAR)
