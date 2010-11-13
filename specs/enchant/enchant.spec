# $Id$
# Authority: dag

### EL6 ships with enchant-aspell-1.5.0-4.el6
# ExclusiveDist: el2 el3 el4 el5

Summary: Cross-platform abstract layer to spellchecking
Name: enchant
Version: 1.3.0
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.abisource.com/projects/enchant/

Source: http://www.abisource.com/downloads/enchant/%{version}/enchant-%{version}.tar.gz
BuildRequires: glib2-devel >= 2.0.0, aspell-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Enchant is a cross-platform abstract layer to spellchecking.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
	--disable-ispell
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING.LIB README
%doc %{_mandir}/man1/enchant.1*
%{_bindir}/*
%{_libdir}/lib*.so.*
%dir %{_libdir}/enchant/
%{_libdir}/enchant/*.so
%{_datadir}/enchant/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/enchant/
%{_libdir}/*.a
%{_libdir}/*.so
%dir %{_libdir}/enchant/
%{_libdir}/enchant/*.a
%{_libdir}/pkgconfig/enchant.pc
%exclude %{_libdir}/*.la
%exclude %{_libdir}/enchant/*.la

%changelog
* Mon Jun 25 2007 Dag Wieers <dag@wieers.com> - 1.3.0-1
- Initial package. (using DAR)
