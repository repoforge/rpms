# Authority: dag

%define rname pychm

Summary: Python package to handle CHM files.
Name: python-chm
Version: 0.8.0
Release: 0
License: GPL
Group: Development/Libraries
URL: http://gnochm.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/gnochm/pychm-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: python, chmlib-devel
Requires: python, chmlib

%description
The python chm package provides three modules, chm, chmlib and extra,
which provide access to the API implemented by the C library chmlib
and some additional classes and functions. They are used to access
MS-ITSS encoded files - Compressed Html Help files (.chm).

%prep
%setup -n %{rname}-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install \
	--root="%{buildroot}" \
	--record=INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING NEWS README
%{_libdir}/python*/site-packages/chm/

%changelog
* Tue Feb 24 2004 Dag Wieers <dag@wieers.com> - 0.8.0-0
- Updated to release 0.8.0.

* Mon Feb 09 2004 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Initial package. (using DAR)
