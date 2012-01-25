# $Id$
# Authority: dag

### EL6 ships with python-pyasn1-0.0.12a-1.el6
# DistExclusive: el2 el3 el4 el5

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name pyasn1

Summary: ASN.1 tools for Python
Name: python-pyasn1
Version: 0.0.12a
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://pyasn1.sourceforge.net/

Source: http://dl.sf.net/pyasn1/pyasn1-%{version}.tar.gz
Patch1: python-pyasn1-0.0.12a-any.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-setuptools

%description
This project is dedicated to implementation of ASN.1 types (concrete syntax)
and codecs (transfer syntaxes) for Python programming environment. ASN.1
compiler is planned for implementation in the future.

%prep
%setup -n %{real_name}-%{version}
%patch1 -p1

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README doc/notes.html examples/
%{python_sitelib}/*

%changelog
* Thu Sep 15 2011 Dag Wieers <dag@wieers.com> - 0.0.12a-1
- Initial package (using DAR)
