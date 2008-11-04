# $Id$
# Authority: dag

Summary: Tool to extract InstallShield cabinet files
Name: unshield
Version: 0.5.1
Release: 1
License: MIT
Group: Applications/Communications
URL: http://synce.sourceforge.net/

Source: http://dl.sf.net/synce/unshield-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libtool
BuildRequires: zlib-devel

%description
unshield is a tool to extract InstallShield cabinet (CAB) files.

Cabinet (.CAB) files are a form of archive, which is used by
the InstallShield installer software.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure --disable-rpath --disable-static
%{__make} %{?_smp_mflags} LIBTOOL="%{_bindir}/libtool"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%doc %{_mandir}/man1/unshield.1.gz
%{_bindir}/unshield
%{_libdir}/libunshield.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libunshield.h
%{_libdir}/libunshield.so
%{_libdir}/pkgconfig/libunshield.pc
%exclude %{_libdir}/libunshield.a
%exclude %{_libdir}/libunshield.la

%changelog
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Initial package. (using DAR)
