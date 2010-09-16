# $Id$
# Authority: yury
# Upstream: http://trac-hacks.org/wiki/AccountManagerPlugin

%define svn_revision 7737
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_version %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_version()')

Summary: Account Manager Plugin for Trac
Name: trac-accountmanager
Version: 0.12.0.r%{svn_revision}
Release: 3%{?dist}
License: GPL
Group: Development/Tools
URL: http://trac-hacks.org/wiki/AccountManagerPlugin

# http://trac-hacks.org/changeset/%{svn_revision}/accountmanagerplugin/trunk?old_path=%2F&old=%{svn_revision}&format=zip
Source: accountmanagerplugin_r%{svn_revision}.zip
Patch0: accountmanagerplugin-0.12-attribute.patch

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
%patch0 -p0 -b .attribute

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
* Thu Sep 16 2010 Yury V. Zaytsev <yury@shurup.com> - 0.12.0.r7737-3
- Renamed the package.

* Mon Aug 16 2010 Yury V. Zaytsev <yury@shurup.com> - 0.12.0.r7737-2
- Added missing attribute patch (see http://trac-hacks.org/ticket/4040).
- Various tweaks.

* Thu Aug 05 2010 Christoph Maser <cmr@financial.com> - 0.12.0.r7737-1
- Initial package. (using DAR)
