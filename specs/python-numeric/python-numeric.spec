# $Id$

# Authority: dag

%define real_name Numeric

Summary: Numerical Extension to Python
Name: python-numeric
Version: 23.1
Release: 0
License: UNKNOWN
Group: Development/Libraries
URL: http://www.pfdubois.com/numpy/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/numpy/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


Obsoletes: numpy

%description
Numerical Extension to Python with subpackages.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
%{__rm} -rf %{buildroot}
python setup.py install \
	--root="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Demo/
%{_libdir}/python*/site-packages/Numeric.pth
%{_libdir}/python*/site-packages/Numeric/
%{_includedir}/python*/Numeric/
