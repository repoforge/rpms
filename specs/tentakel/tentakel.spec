# $Id$
# Authority: dag
# Upstream: Sebastian Stark <cran$users,sourceforge,net>

Summary: program that executes the same command on many hosts in parallel
Name: tentakel
Version: 2.1.3
Release: 1
License: GPL
Group: Applications/Internet
URL: http://tentakel.biskalar.de/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/tentakel/tentakel-%{version}.tgz
Patch: tentakel-2.1.3-setup.py.patch
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
%patch -p0

%build
%{__make}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	PREFIX="%{buildroot}%{_prefix}" \
	sharedoc="doc-rpm"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README TODO tentakel.1.html tentakel.conf.example
%doc %{_mandir}/man1/tentakel.1*
%{_bindir}/tentakel
%{_libdir}/python*/site-packages/lekatnet/

%changelog
* Mon Sep 27 2004 Dag Wieers <dag@wieers.com> - 2.1.3-1
- Initial package. (using DAR)
