# $Id$
# Authority: dag

Summary: C# bindings for the Gecko engine
Name: gecko-sharp
Version: 0.6
Release: 1%{?dist}
License: MPL/LGPL
Group: Development/Tools
URL: http://monodevelop.com/

Source: http://www.go-mono.com/packagers/gecko-sharp/gecko-sharp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: mozilla

%description
C# bindings for the Gecko engine

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/webshot
%{_libdir}/gecko-sharp/
%dir %{_libdir}/mono/
%dir %{_libdir}/mono/gac/
%{_libdir}/mono/gac/gecko-sharp/
%{_libdir}/mono/gecko-sharp/
%{_libdir}/pkgconfig/gecko-sharp.pc

%changelog
* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 0.6-1
- Initial package. (using DAR)
