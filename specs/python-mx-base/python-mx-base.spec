# $Id$
# Authority: dag

# Tag: rft

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name egenix-mx-base

Summary: mx-base libraries for Python
Name: python-mx-base
Version: 2.0.4
Release: 0.2%{?dist}
License: Egenix.com Public License
Group: Development/Libraries
URL: http://www.lemburg.com/files/python/eGenix-mx-Extensions.html

Source: http://www.egenix.com/files/python/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: python, python-devel
Requires: python
Provides: mx
Conflicts: mx

%description
The mx Extension Series are a collection of
Python extensions written in ANSI C and Python
which provide a large spectrum of useful additions
to everyday Python programming.

The BASE package includes the Open Source subpackages
of the series and is needed by all other add-on
packages of the series.

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
%doc mx/*/Doc/ mx/DateTime/COPYRIGHT mx/DateTime/LICENSE mx/Doc/ README
%{python_sitearch}/mx/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.4-0.2
- Rebuild for Fedora Core 5.

* Sat Aug 02 2003 Dag Wieers <dag@wieers.com> - 2.0.4-0
- Initial package. (using DAR)
