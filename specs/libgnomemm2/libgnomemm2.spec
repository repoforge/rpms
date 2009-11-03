# $Id$
# Authority: matthias

%define real_name libgnomemm

Summary: C++ wrappers for libgnome, for use with gtkmm
Name: libgnomemm2
Version: 2.0.1
Release: 0%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://gtkmm.sourceforge.net/

Source: http://dl.sf.net/gtkmm/libgnomemm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtkmm2-devel >= 2.0, libsigc++ >= 1.2, glib2-devel >= 2.0
BuildRequires: atk-devel >= 1.0, pango-devel >= 1.0, gtk2-devel >= 2.0
BuildRequires: freetype-devel >= 2.0, libxml2 >= 2.0
BuildRequires: libgnome >= 2.0, ORBit2 >= 2.0

%description
libgnomemm provides C++ wrappers for libgnome, for use with gtkmm.

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

### Ckean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig &>/dev/null

%postun
/sbin/ldconfig &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libgnomemm-2.0/
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/libgnomemm-2.0/
%{_libdir}/pkgconfig/*.pc
#exclude %{_libdir}/*.la

%changelog
* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 2.0.1-0
- Updated to release 2.0.1.

* Sat Mar 29 2003 Dag Wieers <dag@wieers.com> - 1.3.10-0
- Initial package. (using DAR)
