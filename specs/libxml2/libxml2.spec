# $Id$
# Authority: dries
# ExclusiveDist: el2 rh7 rh8 rh9 el3 fc1 fc2

#%define python_version %(python2 -c 'import sys; print sys.version[:3]')
%define python_version %(python -c 'import sys; print sys.version[:3]')

Summary: Library providing XML and HTML support
Name: libxml2
Version: 2.6.16
Release: 1.2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://xmlsoft.org/

Source: http://xmlsoft.org/sources/libxml2-%{version}.tar.gz
#Source: http://ftp.gnome.org/pub/GNOME/sources/libxml2/2.5/libxml2-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, python, python-devel

%description
This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select subnodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: libxml2 = %{version}-%{release}
Requires: zlib-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package python
Summary: Python bindings for the libxml2 library
Group: Development/Libraries
Requires: libxml2 = %{version}
Requires: %{_libdir}/python%{python_version}

%description python
The libxml2-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libxml2 library to manipulate XML files.

This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DTDs, either
at parse time or later once the document has been modified.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}
#%{__make} clean -C doc/examples

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/xmlcatalog.1.gz
%doc %{_mandir}/man1/xmllint.1.gz
%doc %{_mandir}/man3/libxml.3.gz
%{_bindir}/xmlcatalog
%{_bindir}/xmllint
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/xml2-config.1.gz
%doc doc/*.gif doc/*.html doc/*.png doc/html
%doc doc/libxml2-api.xml doc/tutorial
%doc doc/examples
#%doc %{_datadir}/doc/libxml2-python-%{version}/
%{_bindir}/xml2-config
%{_includedir}/libxml2/
%{_libdir}/xml2Conf.sh
%{_datadir}/aclocal/libxml.m4
%{_libdir}/*.so
### Needed by conglomerate, libgda, ... (?!)
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/python%{python_version}/site-packages/*.a
%exclude %{_libdir}/python%{python_version}/site-packages/*.la
%{_libdir}/pkgconfig/libxml-2.0.pc

%files python
%defattr(-, root, root, 0755)
%doc python/TODO python/libxml2class.txt
%doc doc/*.py doc/python.html python/tests/*.py
%{_libdir}/python%{python_version}/site-packages/*.py
%{_libdir}/python%{python_version}/site-packages/*.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.6.16-1.2
- Rebuild for Fedora Core 5.

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 2.6.16-1
- Updated to release 2.6.16.

* Wed Oct 08 2003 Dag Wieers <dag@wieers.com> - 2.5.11-1
- Re-added the libxml2.la file

* Tue Oct 07 2003 Dag Wieers <dag@wieers.com> - 2.5.11-0
- Initial package. (using DAR)
