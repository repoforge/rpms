# $Id$
# Authority: shuff
# Upstream: Barry Scott <barryscott$tigris,org>

## ExcludeDist: el3 el4

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pysvn

Summary: Alternative Python interface to Subversion
Name: python-svn
Version: 1.7.1
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://pysvn.tigris.org/

Source: http://pysvn.barrys-emacs.org/source_kits/pysvn-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: neon-devel
BuildRequires: python-devel
BuildRequires: subversion-devel >= 1.6.5
Requires: neon 
Requires: python 
Requires: subversion >= 1.6.5

Obsoletes: pysvn
Provides: pysvn = %{version}

%description
The pysvn project's goal is to enable Tools to be written in Python that use Subversion.

Windows, Mac OS X, Linux and other unix platforms are supported.
pysvn Extension Features

    * Supports all svn client features
    * Supports svn transaction features required to write svn pre-commit hooks
    * Easy to learn and use
    * Python like interface
    * Good Documentation and examples
    * No need to understand the Subversion C API 

%prep
%setup -n %{real_name}-%{version}

%build
cd Source
CFLAGS="%{optflags}" %{__python} setup.py backport
CFLAGS="%{optflags}" %{__python} setup.py configure
%{__make}


%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{python_sitearch}/pysvn/
%{__install} Source/pysvn/__init__.py %{buildroot}%{python_sitearch}/pysvn/
%{__install} Source/pysvn/_pysvn*.so %{buildroot}%{python_sitearch}/pysvn/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL.html Docs/ Examples/
%{python_sitearch}/*

%changelog
* Tue Nov 03 2009 Steve Huff <shuff@vecna.org> - 1.7.1-1
- Renamed per RPMforge naming convention.

* Thu Oct 08 2009 Steve Huff <shuff@vecna.org> - 1.7.1-1
- Initial package.
