# $Id$
# Authority: yury
# Upstream: Rune F. Halvorsen <runefh$gmail,com>

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

%global real_name anyjson

Name: python-anyjson
Version: 0.3.1
Release: 2%{?dist}
Summary: Wraps the best available JSON implementation available
Group: Development/Languages
License: BSD
URL: http://pypi.python.org/pypi/anyjson

Source0: http://pypi.python.org/packages/source/a/%{real_name}/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-setuptools

%description
Anyjson loads whichever is the fastest JSON module installed and
provides a uniform API regardless of which JSON implementation is used.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGELOG LICENSE PKG-INFO README
%{python_sitelib}/%{real_name}/
%{python_sitelib}/%{real_name}*.egg-info

%changelog
* Wed Sep 28 2011 Yury V. Zaytsev <yury@shurup.com> - 0.3.1-2
- Imported into RepoForge with minor changes.

* Sun Apr 03 2011 Fabian Affolter <fabian@bernewireless.net> - 0.3.1-1
- Updated to new upstream version 0.3.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Fabian Affolter <fabian@bernewireless.net> - 0.3-1
- Updated to new upstream version 0.3

* Sat Jul 31 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jul 03 2010 Fabian Affolter <fabian@bernewireless.net> - 0.2.4-1
- Initial package
