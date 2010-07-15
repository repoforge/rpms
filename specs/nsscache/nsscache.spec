# $Id$
# Authority: shuff
# Upstream: Jamie Wilkinson <jaq$google,com>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(0)')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Asynchronously synchronise local NSS databases with remote directory services
Name: nsscache
Version: 0.8.8
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://code.google.com/p/nsscache/

Source: http://nsscache.googlecode.com/files/nsscache-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: python
BuildRequires: rpm-macros-rpmforge

Requires: python
Requires: libnss-cache

%description
nsscache is a Python library and a commandline frontend to that library that
synchronises a local NSS cache against a remote directory service, such as
LDAP. 

%prep
%setup

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

# install the man pages
%{__install} -m0755 -d %{buildroot}/%{_mandir}/man1
%{__install} -m0755 nsscache.1 %{buildroot}/%{_mandir}/man1
%{__install} -m0755 -d %{buildroot}/%{_mandir}/man5
%{__install} -m0755 nsscache.conf.5 %{buildroot}/%{_mandir}/man5

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING THANKS
%doc nsscache.cron
%doc %{_mandir}/man?/*
%{_bindir}/*
%exclude %{_bindir}/runtests*
%config(noreplace) %{_sysconfdir}/nsscache.conf
%{python_sitelib}/*
%exclude %{python_sitelib}/*/*_test.py*
%exclude %{python_sitelib}/*/*/*_test.py*

%changelog
* Thu Jul 15 2010 Steve Huff <shuff@vecna.org> - 0.8.8-1
- Initial package.
