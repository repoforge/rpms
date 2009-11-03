# $Id$
# Authority: dag
# Upstream: Iustin Pop <iusty$k1024,org>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pyxattr

Summary: Extended attributes for python
Name: python-xattr
Version: 0.2
Release: 1.2%{?dist}
License: GPL
Group: Development/Libraries
URL: http://pyxattr.sourceforge.net/

Source: http://dl.sf.net/pyxattr/pyxattr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: pyxattr <= %{version}-%{release}
BuildRequires: python >= 2.2, libattr-devel, python-devel
Requires: python >= 2.2, libattr

%description
python-xattr is a C extension module for Python which implements
extended attributes manipulation. It is a wrapper on top of the
attr C library - see attr(5).

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
%doc *.html *.txt MANIFEST README
%{python_sitearch}/xattr.so
%exclude %{_docdir}/pyxattr-%{version}/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2-1.2
- Rebuild for Fedora Core 5.

* Sun Sep 11 2005 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
