# $Id$
# Authority: shuff
# Upstream: Jelmer Vernooij <jelmer$samba,org>

%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

%define real_name fastimport
%define vtag 0.9.0
%define devtag 0
%define real_version %{vtag}dev%{devtag}
%define rev 298
%define tarball_version %{real_version}-r%{rev}

Summary: Python VCS fastimport/fsatexport parser
Name: python-fastimport
Version: %{vtag}.%{devtag}
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://launchpad.net/python-fastimport/

Source: http://www.vecna.org/software/python-fastimport/python-fastimport-%{tarball_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.4

Provides: fastimport
Obsoletes: fastimport <= %{version}-%{release}

%description
python-fastimport provides a Python library for handling imports from various VCS formats.

%prep
%setup -n %{name}-%{tarball_version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING.txt
%{python_sitelib}/fastimport/

%changelog
* Tue Dec 21 2010 Steve Huff <shuff@vecna.org> - 0.9.0.0-1
- Initial package.
