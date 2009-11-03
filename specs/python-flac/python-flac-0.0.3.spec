# $Id: python-flac.spec 4303 2006-04-18 22:05:03Z dries $
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pyflac

Summary: Flac support for Python
Name: python-flac
Version: 0.0.3
Release: 1.2%{?dist}
License: UNKNOWN
Group: Development/Libraries
URL: http://www.sacredchao.net/quodlibet/browser/trunk/pyflac/

Source: http://www.sacredchao.net/~piman/software/pyflac-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel, flac-devel

Obsoletes: pyflac <= %{version}-%{release}
Provides: pyflac

%description
Flac support for Python.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README examples/
%{python_sitearch}/flac/

%changelog
* Tue Jul 19 2005 Dag Wieers <dag@wieers.com> - 0.0.3-1
- Initial package. (using DAR)
