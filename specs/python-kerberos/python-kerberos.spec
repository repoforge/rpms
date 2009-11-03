# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name PyKerberos
%define real_version svn1735

Summary: High-level python wrapper for Kerberos (GSSAPI) operations
Name: python-kerberos
Version: 0.0
Release: 0.svn1735.1%{?dist}
License: Apache License
Group: System Environment/Libraries
URL: http://trac.calendarserver.org/projects/calendarserver/browser/PyKerberos/

### svn co http://svn.macosforge.org/repository/collaboration/PyKerberos/trunk
Source: PyKerberos-%{real_version}.tar.gz
Patch1: PyKerberos-svn1735-includes.patch
Patch2: PyKerberos-svn1735-delegation.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel

Obsoletes: PyKerberos <= %{version}-%{release}
Provides: PyKerberos = %{version}-%{release}

%description
python-kerberos is a high-level wrapper for Kerberos (GSSAPI) operations.
The goal is to avoid having to build a module that wraps the entire
Kerberos.framework, and instead offer a limited set of functions that do what
is needed for client/server Kerberos authentication based on
<http://www.ietf.org/rfc/rfc4559.txt>.

%prep
%setup -n %{real_name}-0.1735
%patch1 -p0 -b .includes
%patch2 -p0 -b .delegation

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
#%{__install} -Dp -m0644 build/lib*/kerberos.so %{buildroot}%{python_archlib}/kerberos.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README.txt test.py
%{python_sitearch}/kerberos.so

%changelog
* Mon Oct 15 2007 Dag Wieers <dag@wieers.com> - 0.0-0.1735.1
- Initial package. (using DAR)
