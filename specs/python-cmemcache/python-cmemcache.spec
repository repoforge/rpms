# $Id$
# Authority: yury
# Upstream: Gijsbert de Haan <gijsbert,de,haan$gmail,com>

%{!?python_sitelib:  %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?python_abi:      %define python_abi %(%{__python} -c "import sys; print sys.version[:3]")}

%define modn   cmemcache
%define modv   0.95

Summary:       A Python extension for libmemcache
Name:          python-%{modn}
Version:       %{modv}
Release:       2%{?dist}
License:       GPL
Group:         Development/Libraries
Source0:       http://gijsbert.org/downloads/%{modn}/%{modn}-%{modv}.tar.bz2
URL:           http://gijsbert.org/%{modn}/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root
Provides:      python(%{modn}) = %{modv}
BuildRequires: libmemcache-devel
BuildRequires: python-devel >= 2.3.5 python-setuptools


%description
Python-cmemcache is a Python extension for libmemcache, the C API to the
memcached distributed memory object cache daemon. It is very similar to
python-memcache, except for some return codes, and faster.


%prep
%setup -q -n %{modn}-%{modv}


%build
%{__python} -c 'import setuptools; execfile("setup.py")' build


%install
[ -n "${RPM_BUILD_ROOT}" -a "${RPM_BUILD_ROOT}" != "/" ] && %{__rm} -rf ${RPM_BUILD_ROOT}
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}

%{__python} -c 'import setuptools; execfile("setup.py")' install \
	--skip-build -O1 --root ${RPM_BUILD_ROOT}


%clean
[ -n "${RPM_BUILD_ROOT}" -a "${RPM_BUILD_ROOT}" != "/" ] && %{__rm} -rf ${RPM_BUILD_ROOT}


%files
%defattr(-,root,root)
%doc COPYING INSTALL README VERSION *.{css,html}
%{python_sitearch}/_cmemcache.so
%{python_sitearch}/cmemcache.py*
%{python_sitearch}/*.egg-info


%changelog
* Sun Dec 27 2009 Yury V. Zaytsev <yury@shurup.com> - 0.95-2
- Ported over RPMForge.

* Fri Oct 31 2008 Peter Pramberger <peterpramb@member.fsf.org> - 0.95-1
- New version (0.95).

* Mon May 14 2007 peter.pramberger@member.fsf.org 0.91-2
- Created.
