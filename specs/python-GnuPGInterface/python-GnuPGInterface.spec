%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pkgname GnuPGInterface

Summary:	A Python module to interface with GnuPG
Name:		python-GnuPGInterface
Version:	0.3.2
Release:	2%{?dist}
License:	LGPLv2+
Group:		Development/Languages
URL:		http://py-gnupg.sourceforge.net/
Source:		http://downloads.sourceforge.net/py-gnupg/%{pkgname}-%{version}.tar.gz
BuildRequires:	python-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
GnuPGInterface is a Python module to interface with GnuPG. It
concentrates on interacting with GnuPG via filehandles, providing
access to control GnuPG via versatile and extensible means.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

# Correct some permissions
chmod 644 ChangeLog COPYING NEWS THANKS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog COPYING NEWS THANKS
%{python_sitelib}/%{pkgname}.py*

%changelog
* Tue Jan 04 2011 David Hrbáč <david@hrbac.cz> - 0.3.2-2
- initial rebuild

* Mon Sep 03 2007 Robert Scheck <robert@fedoraproject.org> 0.3.2-2
- Updated source URL to match with the guidelines (#265381)
- Use get_python_lib() macro according to the policy (#265381)

* Wed Aug 29 2007 Robert Scheck <robert@fedoraproject.org> 0.3.2-1
- Upgrade to 0.3.2
- Initial spec file for Fedora and Red Hat Enterprise Linux
