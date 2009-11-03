# $Id$
# Authority: dries

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name Unipath

Summary: Object oriented pathname and filesystem access
Name: python-unipath
Version: 0.2.1
Release: 1%{?dist}
License: Python Software Foundation License
Group: Development/Libraries
URL: http://sluggo.scrapping.cc/python/unipath/

Source: http://sluggo.scrapping.cc/python/unipath/Unipath-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.0

%description
Unipath is package for doing pathname calculations and filesystem access in 
an object-oriented manner in Python. It's based on Jason Orendorff's path.py
 but does not adhere as strictly to the underlying functions' syntax, in 
order to provide more user convenience and higher-level functionality. 
Unipath is for Python 2.4 or higher. It comes with a test suite.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt *.html CHANGES
%{python_sitelib}/unipath/
%{python_sitelib}/Unipath-%{version}-*.egg-info

%changelog
* Tue Apr  7 2009 Dries Verachtert <dries@ulyssis.org> - 0.2.1-1
- Initial package.
