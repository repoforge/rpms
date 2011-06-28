# $Id$
# Authority: shuff
# Upstream: <wwwsearch-general$lists,sourceforge,net>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name mechanize

Name: python-mechanize
Version: 0.2.5
Release: 1%{?dist}
Summary: Python port of WWW::Mechanize
Group: Development/Languages
License: GPL
URL: http://wwwsearch.sourceforge.net/mechanize/

Source: http://pypi.python.org/packages/source/m/mechanize/mechanize-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: python-setuptools 

Provides: mechanize = %{version}-%{release}

%description
Stateful programmatic web browsing in Python, after Andy Lester's Perl module
WWW::Mechanize.

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
%{python_sitelib}/*

%changelog
* Tue Jun 28 2011 Steve Huff <shuff@vecna.org> - 0.2.5-1
- Initial package.
