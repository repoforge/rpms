# $Id$
# Authority: dag

### Already in xorg package
# ExclusiveDist: el2 rh7 rh9 el3 fc1 fc2

Summary: X Render Extension
Name: xrender
Version: 0.8.3
Release: 0
License: Free Software
Group: System Environment/Libraries
URL: http://freedesktop.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://freedesktop.org/~xlibs/release/xrender-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: render

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
%{__rm} -f %{buildroot}%{_libdir}/libXrender.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL
%{_libdir}/libXrender.a
%{_libdir}/libXrender.so
%{_libdir}/libXrender.so.*
%{_libdir}/pkgconfig/xrender.pc
#%{_libdir}/libXrender.la

%changelog
* Fri Feb 27 2004 Dag Wieers <dag@wieers.com> - 0.8.3-0
- Initial package. (using DAR)
