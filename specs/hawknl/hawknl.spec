# Authority: dries
# Upstream: Phil Frisbie Jr <phil$hawksoft,com>

%define real_version 168

Summary: Portable network library
Name: hawknl
Version: 1.68
Release: 1%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://www.hawksoft.com/

Source: http://www.hawksoft.com/download/files/HawkNL%{real_version}src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
HawkNL (NL) is a fairly low level API, a wrapper over Berkeley/Unix Sockets
and Winsock. But NL also provides other features including support for many
OSs, groups of sockets, socket statistics, high accuracy timer, CRC functions,
macros to read and write data to packets with endian conversion, and support
for multiple network transports.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n hawknl%{version}
%{__cp} makefile.linux Makefile
sed -i 's;ln -s ..LIBDIR./;ln -s ;g' src/makefile.linux

%build
%{__make} %{?_smp_mflags} LIBDIR=%{_libdir} INCDIR=%{_includedir}

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_libdir} %{buildroot}/%{_includedir}
%makeinstall LIBDIR=%{buildroot}%{_libdir} INCDIR=%{buildroot}%{_includedir}

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%{_libdir}/libNL.so.*

%files devel
%defattr(-, root, root, 0755)
%doc samples/*
%{_libdir}/*NL.so
%{_libdir}/libNL.a
%{_includedir}/nl.h

%changelog
* Sun Jul 30 2006 Vincent Knecht <vknecht@users.sourceforge.net> - 1.68-1
- Initial packaging.
