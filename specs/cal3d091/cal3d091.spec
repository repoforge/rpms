# $Id$
# Authority: dries
# Upstream: Bruno 'Beosil' Heidelberger <beosil$swileys,com>

%define real_name cal3d

Summary: Skeletal based character animation library
Name: cal3d091
Version: 0.9.1
Release: 1.2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://cal3d.sourceforge.net/

Source: http://dl.sf.net/cal3d/cal3d-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, autoconf, automake, doxygen, docbook-utils

%description
Cal3D is a skeletal based 3d character animation library written in C++ in a
platform/graphic API-independent way.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
bash autogen.sh
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
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_libdir}/libcal3d-*.so

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/cal3d/
%{_libdir}/libcal3d.so
%{_libdir}/pkgconfig/cal3d.pc
%exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.1-1.2
- Rebuild for Fedora Core 5.

* Thu Oct 06 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.1-1
- Initial package.
