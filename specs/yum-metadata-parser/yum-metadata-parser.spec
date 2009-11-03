# $Id$
# Authority: dag

### Ironically, yum 2.4 needs sqlite2, while this needs sqlite3
# ExclusiveDist:
# ExcludeDist: el4

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Fast metadata parser for yum
Name: yum-metadata-parser
Version: 1.0
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://linux.duke.edu/projects/yum/

Source: http://linux.duke.edu/projects/yum/download/yum-metadata-parser/yum-metadata-parser-%{version}.tar.gz
Patch0: yum-metadata-parser-1.0-quiet.patch
Patch1: yum-metadata-parser-1.0-files.patch
Patch2: yum-metadata-parser-1.0-locationbase.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, python-devel, glib2-devel, libxml2-devel, sqlite-devel >= 3.0

%description
Fast metadata parser for yum implemented in C.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog README
%{python_sitelib}/_sqlitecache.so
%{python_sitelib}/sqlitecachec.py
%{python_sitelib}/sqlitecachec.pyc
%ghost %{python_sitelib}/sqlitecachec.pyo

%changelog
* Wed Feb 14 2007 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
