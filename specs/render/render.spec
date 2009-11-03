# $Id$

# Authority: dag

Summary: X Render Extension
Name: render
Version: 0.8
Release: 0.2%{?dist}
License: Free Software
Group: System Environment/Libraries
URL: http://freedesktop.org/

Source: http://freedesktop.org/~xlibs/release/render-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


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
%{_docdir}/render/
%{_libdir}/pkgconfig/render.pc
#%{_includedir}/X11/extensions/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8-0.2
- Rebuild for Fedora Core 5.

* Fri Feb 27 2004 Dag Wieers <dag@wieers.com> - 0.8-0
- Initial package. (using DAR)
