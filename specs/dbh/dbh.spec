# $Id$
# Authority: dries

Summary: Create multidimensional binary trees on disk
Name: dbh
Version: 4.5.0
Release: 1%{?dist}
License: LGPL/QPL
Group: Development/Libraries
URL: http://dbh.sourceforge.net/

Source: http://dl.sf.net/dbh/dbh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: 

%description
Disk based hashes is a method to create multidimensional binary trees on disk. 
This library permits the extension of the database concept to a plethora of 
electronic data, such as graphical information.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libdbh*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/dbh*.h
%{_libdir}/libdbh.a
%{_libdir}/libdbh.so
%{_libdir}/pkgconfig/dbh.pc
%exclude %{_libdir}/libdbh.la

%changelog
* Thu May 25 2006 Dries Verachtert <dries@ulyssis.org> - 4.5.0-1
- Initial package.
