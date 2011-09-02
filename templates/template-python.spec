# $Id$
# Authority: shuff
# Upstream: 

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name NNAAMMEE

Name: python-nnaammee
Version: 
Release: 1%{?dist}
Summary: 
Group: Development/Languages
License: GPL
URL: http://pypi.python.org/pypi/NNAAMMEE

Source: 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-setuptools

Provides: nnaammee = %{version}-%{release}

%description

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README TODO
%{python_sitelib}/*
# if arch-specific
# %{python_sitearch}/*

%changelog
* Tue Jun 28 2011 Steve Huff <shuff@vecna.org> - 0.0.1-1
- Initial package.
