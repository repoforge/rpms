# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name Numeric

Summary: Numerical Extension to Python
Name: python-numeric
Version: 23.1
Release: 0
License: UNKNOWN
Group: Development/Libraries
URL: http://www.pfdubois.com/numpy/

Source: http://dl.sf.net/numpy/Numeric-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python, python-devel

Obsoletes: numpy

%description
Numerical Extension to Python with subpackages.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install \
	--root="%{buildroot}" \
	--prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Demo/
%{python_sitearch}/Numeric.pth
%{python_sitearch}/Numeric/
%{_includedir}/python*/Numeric/
