%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?pydir: %define pydir %(%{__python} -c "from distutils.sysconfig import get_config_vars; print get_config_vars()['LIBDEST']")}

Name:           python-json
Version:        3.4
%define version_munge %(sed 's/\\./_/g' <<< %{version})
Release:        3%{?dist}
Summary:        A JSON reader and writer for Python

Group:          Development/Languages
License:        LGPL
URL:            https://sourceforge.net/projects/json-py/
Source0:        http://dl.sourceforge.net/json-py/json-py-%{version_munge}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel

%description
json.py is an implementation of a JSON (http://json.org) reader and writer in
Python.

%prep
%setup -q -c
chmod a-x *

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{python_sitelib}
install -p -m 0644 json.py minjson.py $RPM_BUILD_ROOT%{python_sitelib}
%{__python} %{pydir}/compileall.py $RPM_BUILD_ROOT%{python_sitelib}
%{__python} -O %{pydir}/compileall.py $RPM_BUILD_ROOT%{python_sitelib}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc changes.txt jsontest.py license.txt readme.txt
%{python_sitelib}/*.py
%{python_sitelib}/*.py[co]

%changelog
* Sat Dec  9 2006 Luke Macken <lmacken@redhat.com> 3.4-3
- Rebuild for python 2.5

* Fri Sep  8 2006 Luke Macken <lmacken@redhat.com> 3.4-2
- Rebuild for FC6

* Fri Dec 30 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 3.4-1
- Initial RPM release
