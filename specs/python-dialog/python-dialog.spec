# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name pythondialog

Summary: Python interface to the Unix dialog utility
Name: python-dialog
Version: 2.7
Release: 1%{?dist}
License: LGPL
Group: Development/Languages
URL: http://pythondialog.sourceforge.net/

Source: http://dl.sf.net/pythondialog/pythondialog-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel
Requires: dialog

%description
A Python interface to the Unix dialog utility, designed to provide
an easy, pythonic and as complete as possible way to use the dialog
features from Python code.

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
%doc AUTHORS COPYING DEBUGGING README TODO demo.py
%{python_sitelib}/dialog.py
%{python_sitelib}/dialog.pyc
%ghost %{python_sitelib}/dialog.pyo

%changelog
* Sun Aug 06 2006 Dag Wieers <dag@wieers.com> - 2.7-1
- Initial package. (using DAR)
