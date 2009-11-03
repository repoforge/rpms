# $Id$
# Authority: dag

Summary: Library for binary I/O classes in C++
Name: libbinio
Version: 1.4
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://libbinio.sourceforge.net/

Source: http://dl.sf.net/libbinio/libbinio-%{version}.tar.gz
Patch0: libbinio-1.4-texinfo.patch
Patch1: libbinio-1.4-pkgconfigurl.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: info
BuildRequires: texinfo

%description
This binary I/O stream class library presents a platform-independent
way to access binary data streams in C++. The library is hardware 
independent in the form that it transparently converts between the 
different forms of machine-internal binary data representation.
It further employs no special I/O protocol and can be used on
arbitrary binary data sources.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: info

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_infodir}/dir/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info %{_infodir}/libbinio.info.gz %{_infodir}/dir || :

%preun devel
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/libbinio.info.gz %{_infodir}/dir || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL* NEWS README TODO
%{_libdir}/libbinio.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_infodir}/libbinio.info*
%{_includedir}/libbinio/
%{_libdir}/libbinio.so
%{_libdir}/pkgconfig/libbinio.pc
%exclude %{_libdir}/libbinio.la

%changelog
* Wed Jul 15 2009 Dag Wieers <dag@wieers.com> - 1.4-1
- Initial package. (using DAR)
