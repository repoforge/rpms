# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name pyparsing

Summary: Object-oriented approach to text processing
Name: python-parsing
Version: 1.4.11
Release: 1%{?dist}
License: MIT
Group: Development/Libraries
URL: http://pyparsing.wikispaces.com/

Source: http://dl.sf.net/pyparsing/pyparsing-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel

Obsoletes: pyparsing <= %{version}-%{release}
Provides: pyparsing = %{version}-%{release}

%description
pyparsing is a module that can be used to easily and directly configure syntax
definitions for any number of text parsing applications.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build
%{__mv} pyparsingClassDiagram.PNG pyparsingClassDiagram.png

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES README *.html pyparsingClassDiagram.* docs/ examples/ htmldoc/
%{python_sitelib}/pyparsing.py
%{python_sitelib}/pyparsing.pyc
%ghost %{python_sitelib}/pyparsing.pyo

%changelog
* Mon Jul 14 2008 Dag Wieers <dag@wieers.com> - 1.4.11-1
- Initial package. (using DAR)
