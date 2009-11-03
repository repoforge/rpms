# $Id$
# Authority: dries
# Upstream: Christoph 'delmonico' Neuroth <delmonico$gmx,net>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Generates fuzzy clock output
Name: fuzzyclock
Version: 0.3
Release: 2.2%{?dist}
License: GPL
Group: Applications/System
URL: http://home.gna.org/fuzzyclock/

Source: http://download.gna.org/fuzzyclock/src/fuzzyclock-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: python, python-devel

%description
Fuzzy Clock is a Python class and command line utility to generate
"fuzzy clock" output.

%prep
%setup

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/fuzzyclock
%{python_sitearch}/fuzzyclock.py*
%{python_sitearch}/fuzzyclock/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-2.2
- Rebuild for Fedora Core 5.

* Wed Dec 07 2005 Dag Wieers <dag@wieers.com> - 0.3-2
- Fixed RPM Group.

* Tue Nov 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Updated to release 0.3.

* Fri Nov 18 2005 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
