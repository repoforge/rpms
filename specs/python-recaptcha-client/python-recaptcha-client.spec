# $Id$
# Authority: yury
# Upstream: Ben Maurer <support$recaptcha,net>

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

Name: python-recaptcha-client
Version: 1.0.6
Release: 1%{?dist}
Summary: Python module for reCAPTCHA and reCAPTCHA Mailhide

Group: Development/Languages
License: MIT
URL: http://pypi.python.org/pypi/recaptcha-client
Source0: http://pypi.python.org/packages/source/r/recaptcha-client/recaptcha-client-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-setuptools

Requires: python-crypto

%description
Provides a CAPTCHA for Python using the reCAPTCHA service. Does not require
any imaging libraries because the CAPTCHA is served directly from reCAPTCHA.
Also allows you to securely obfuscate emails with Mailhide. This functionality
requires python-crypto. This library requires two types of API keys. If you'd
like to use the CAPTCHA, you'll need a key from
http://recaptcha.net/api/getkey. For Mailhide, you'll need a key from
http://mailhide.recaptcha.net/apikey.

%prep
%setup -n recaptcha-client-%{version}
sed -i 's/^from ez_setup/#from ez_setup/' setup.py
sed -i 's/^use_setuptools()/#use_setuptools()/' setup.py


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root, -)
%doc PKG-INFO
%{python_sitelib}/recaptcha/
%{python_sitelib}/recaptcha_client*-nspkg.pth
%{python_sitelib}/recaptcha_client*.egg-info/

%changelog
* Wed Sep 07 2011 Yury V. Zaytsev <yury@shurup.com> - 1.0.6-1
- Imported into RepoForge.
- Updated to release 1.0.6.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 30 2010 Stephen Gallagher <sgallagh@redhat.com> 1.0.5-4
- Rebuild for python 2.7

* Fri Mar 12 2010 Stephen Gallagher <sgallagh@redhat.com> 1.0.5-3
- Bump revision to chain-build ReviewBoard

* Thu Mar 11 2010 Stephen Gallagher <sgallagh@redhat.com> 1.0.5-2
- Conditionally define python_sitelib
- Remove CFLAGS from the build step (unneeded)
- Remove useless comment from %%files
- Update summary

* Tue Mar 09 2010 Stephen Gallagher <sgallagh@redhat.com> 1.0.5-1
- Specfile changes from package review

* Mon Dec 21 2009 Stephen Gallagher <sgallagh@redhat.com> 1.0.5-0
- First release

