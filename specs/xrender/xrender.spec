# $Id$

# Authority: dag

Summary: X Render Extension.
Name: xrender
Version: 0.8.3
Release: 0
License: Free Software
Group: System Environment/Libraries
URL: http://freedesktop.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://freedesktop.org/~xlibs/release/xrender-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
This package contains header files and documentation for the X render
extension. Library and server implementations are separate.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_includedir}/X11/
%{__rm} -f %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_libdir}/pkgconfig/*.pc
#%{_libdir}/*.la

%changelog
* Fri Feb 27 2004 Dag Wieers <dag@wieers.com> - 0.8.3-0
- Initial package. (using DAR)
