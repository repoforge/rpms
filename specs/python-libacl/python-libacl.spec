# $Id$
# Authority: dag
# Upstream: Iustin Pop <iusty$k1024,org>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pylibacl

Summary: POSIX.1e ACLs for python
Name: python-libacl
Version: 0.2.1
Release: 1.2%{?dist}
License: GPL
Group: Development/Libraries
URL: http://pylibacl.sourceforge.net/

Source: http://dl.sf.net/pylibacl/pylibacl-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: pylibacl <= %{version}-%{release}
BuildRequires: python >= 2.2, libacl-devel, python-devel
Requires: python >= 2.2, libacl

%description
python-libacl is a C extension module for Python which implements
POSIX ACLs manipulation. It is a wrapper on top of the systems's
acl C library - see acl(5).

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
%doc *.html *.txt BENCHMARK IMPLEMENTATION MANIFEST PLATFORMS README
%{python_sitearch}/posix1e.so
%exclude %{_docdir}/pylibacl-%{version}/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.1-1.2
- Rebuild for Fedora Core 5.

* Sun Sep 11 2005 Dag Wieers <dag@wieers.com> - 0.2.1-1
- Initial package. (using DAR)
