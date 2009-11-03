# $Id$
# Authority: dag
# Upstream: Florent Rougon <flo@via.ecp.fr>

%define python_includedir %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_inc()')
%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pyxmms

Name: python-xmms
Summary: Python Interface to XMMS
Version: 2.04
Release: 1.2%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.via.ecp.fr/~flo/

Source: http://people.via.ecp.fr/~flo/2002/PyXMMS/dist/pyxmms-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, glib-devel, python-devel, xmms-devel
Requires: python >= %{python_version}

%description
A python (Python) interface to xmms (XMMS) consisting of all the
xmms_remote_* functions from libxmms plus some higher-level functions.
This should provide anything needed to control XMMS from an external
program.

%prep
%setup -n %{real_name}-%{version}
%{__rm} setup.cfg

%build
export CFLAGS="%{optflags}"
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%{python_sitearch}/xmms/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.04-1.2
- Rebuild for Fedora Core 5.

* Sun May 08 2005 Dag Wieers <dag@wieers.com> - 2.0.4-1
- Initial package. (using DAR)
