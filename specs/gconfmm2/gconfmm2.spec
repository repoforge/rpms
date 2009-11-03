# $Id$
# Authority: dag

%define real_name gconfmm

Summary: C++ wrappers for GConf
Name: gconfmm2
Version: 2.0.1
Release: 0.2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://gtkmm.sourceforge.net/

Source: http://dl.sf.net/gtkmm/gconfmm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gtkmm2-devel >= 2.0, libsigc++-devel >= 1.2, glib2-devel >= 2.0
BuildRequires: atk-devel >= 1.0, pango-devel >= 1.0, gtk2-devel >= 2.0
BuildRequires: ORBit2-devel >= 2.0, GConf2-devel >= 1.2, gcc-c++

%description
C++ wrappers for GConf.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
	--enable-static \
	--enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig &>/dev/null

%postun
/sbin/ldconfig &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/gconfmm-2.0/
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/gconfmm-2.0/
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.1-0.2
- Rebuild for Fedora Core 5.

* Sat Mar 29 2003 Dag Wieers <dag@wieers.com> - 2.0.1-0
- Initial package. (using DAR)
