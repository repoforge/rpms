# Authority: atrpms
# Dists: rh90

Summary: Library providing XML and HTML support.
Name: libxml2
Version: 2.5.11
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://ftp.gnome.org/pub/GNOME/sources/libxml2/2.5/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.gnome.org/pub/GNOME/sources/libxml2/2.5/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
This library lets you manipulate XML files. It includes support to
read, modify, and write XML and HTML files. It has DTD support,
including parsing and validation, even with complex DTDs. The output
can be a simple SAX stream or an in-memory DOM like representation.
In this case you can use the built-in XPath and XPointer
implementation to select subnodes or ranges. A flexible Input/Output
mechanism is available, with existing HTTP and FTP modules and
combined to an URI library.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package python
Summary: Python scripts for %{name}.
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description python
Python files for %{name}

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
### Needed by conglomerate, libgda, ... (?!)
#%{__rm} -f %{buildroot}%{_libdir}/*.la
%{__rm} -f %{buildroot}%{_libdir}/python2.2/site-packages/*.la

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

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
%doc %{_datadir}/doc/libxml2-python-%{version}/
%{_bindir}/xml2-config
%{_includedir}/libxml2/
%{_libdir}/xml2Conf.sh
%{_datadir}/aclocal/*.m4
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/python2.2/site-packages/*.a
%{_libdir}/pkgconfig/*.pc

%files python
%defattr(-, root, root, 0755)
%{_libdir}/python2.2/site-packages/*.py
%{_libdir}/python2.2/site-packages/*.so

%changelog
* Wed Oct 08 2003 Dag Wieers <dag@wieers.com> - 2.5.11-1
- Re-added the libxml2.la file

* Tue Oct 07 2003 Dag Wieers <dag@wieers.com> - 2.5.11-0
- Initial package. (using DAR)
