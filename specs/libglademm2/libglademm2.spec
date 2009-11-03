# $Id$
# Authority: matthias

Summary: The C++ interface for the libglade user interface library
Name: libglademm2
Version: 2.0.1
Release: 2%{?dist}
License: GPL
Group: System Environment/Libraries
Source: http://dl.sf.net/gtkmm/libglademm-%{version}.tar.gz
URL: http://gtkmm.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: libglade2 >= 1.99.11, gtkmm2 >= 2.0.2
BuildRequires: gcc-c++, libglade2-devel >= 1.99.11, gtkmm2-devel >= 2.0.2

%description
The C++ interface for the libglade user interface library.


%package devel
Summary: Development libraries and headers for libglademm2
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libglade2-devel >= 1.99.11, gtkmm2-devel >= 2.0.2

%description devel
Development files for libglademm2, the C++ interface for the libglade user
interface library.


%prep
%setup -n libglademm-%{version}

%build
%configure --enable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
# Clean up docs
%{__rm} -rf examples/*/.deps

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc examples
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/libglademm-2.0
%{_libdir}/pkgconfig/*

%changelog
* Thu Nov 13 2003 Matthias Saou <http://freshrpms.net/> 2.0.1-2.fr
- Rebuild for Fedora Core 1.

* Thu May  8 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

