# $Id$

# Authority: dag
# Upstream: <libxmlplusplus-general@lists.sourceforge.net>

Summary: C++ interface for working with XML files.
Name: libxml++
Version: 0.26.0
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://libxmlplusplus.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/libxmlplusplus/libxml++-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libxml2-devel >= 2.5.1

%description
libxml++ is a C++ interface for working with XML files, using libxml
(gnome-xml) to parse and write the actual XML files. It has a simple
but complete API.

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
#%{__make} -C docs/reference

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc examples/
#{_bindir}/xml++-config
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libxml++-1.0/
#{_datadir}/aclocal/*.m4

%changelog
* Mon Jan 05 2004 Dag Wieers <dag@wieers.com> - 0.26.0-0
- Updated to release 0.26.0.

* Thu Sep 11 2003 Dag Wieers <dag@wieers.com> - 0.25.0-0
- Initial package. (using DAR)
