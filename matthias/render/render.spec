# $Id: render.spec,v 1.2 2004/02/28 02:39:00 dag- Exp $

# Authority: dag

Summary: X Render Extension.
Name: render
Version: 0.8
Release: 0
License: Free Software
Group: System Environment/Libraries
URL: http://freedesktop.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://freedesktop.org/~xlibs/release/render-%{version}.tar.gz
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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL README
%{_datadir}/doc/render/
%{_libdir}/pkgconfig/*.pc
#%{_includedir}/X11/extensions/

%changelog
* Fri Feb 27 2004 Dag Wieers <dag@wieers.com> - 0.8-0
- Initial package. (using DAR)
