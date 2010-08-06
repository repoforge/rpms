# $Id$

%define real_version trunk-r8337
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_version %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_version()')


Summary: Account Manager Plugin for Trac
Name: TracAcccountManager
Version: 0.12.0.trunk_r8337
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://trac-hacks.org/wiki/AccountManagerPlugin

Source: accountmanagerplugin_%{real_version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python
BuildRequires: python-setuptools
Requires: python
Requires: trac

%description
The AccountManagerPlugin offers several features for managing trac user accounts:

    * allow users to register new accounts
    * login via an HTML form instead of using HTTP authentication
    * allow existing users to change their passwords or delete their accounts 
    * send a new password to users who’ve forgotten their password
    * administration of user accounts 

%prep
cd %{_builddir}
rm -rf accountmanagerplugin/trunk
unzip %{SOURCE0}
cd %{_builddir}/accountmanagerplugin/trunk
chmod -R a+rX,g-w,o-w .

%build
cd %{_builddir}/accountmanagerplugin/trunk
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
cd %{_builddir}/accountmanagerplugin/trunk
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"


%files
%defattr(-, root, root, 0755)
%{python_sitelib}/acct_mgr/
%{python_sitelib}/TracAccountManager-0.2.1dev-py%{python_version}.egg-info/


%changelog
* Thu Aug 05 2010 Christoph Maser <cmr@financial.com>
- Initial package. (using DAR)
