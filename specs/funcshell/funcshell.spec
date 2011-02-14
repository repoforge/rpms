# $Id$
# Authority: shuff
# Upstream: Silas Sewell <silas$sewell,ch>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Shell interface to Func
Name: funcshell
Version: 0.0.1
Release: 1%{?dist}
License: MIT
Group: Applications/System
URL: https://github.com/silas/funcshell/

Source: https://github.com/downloads/silas/funcshell/funcshell-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-setuptools
Requires: func
Requires: python-cly

%description
funcshell takes a similar approach to features as Func; it allows developers to
easily extend and customize its functionality using a plugin system. It also
assumes the most useful commands will be the ones you write yourself. That
being said, funcshell currently comes with both the command and service module.

Features:

* advanced client selection (you can use + and - to add/remove hosts/groups)
* tab completion
* persistent history
* a command sub-shell
* quick help (just hit the "?" key)

%prep
%setup

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE
%{_bindir}/*
%{python_sitelib}/funcshell/
%{python_sitelib}/funcshell*.egg-info

%changelog
* Mon Feb 14 2011 Steve Huff <shuff@vecna.org> - 0.0.1-1
- Initial package.
