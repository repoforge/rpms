# $Id: $

# Authority: newrpms

Summary: A library to provide abstract access to various archives.  
Name:	 physfs
Version: 0.1.9
Release: 1
License: zlib License 
Group:   System Environment/Libraries
Source: %{name}-%{version}.tar.bz2
URL: http://www.icculus.org/physfs/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: ncurses-devel
BuildRequires: readline-devel
BuildRequires: zlib-devel

Packager: Rudolf Kastl <che666 at uni.de>
Vendor: http://newrpms.sunsite.dk/

%description
A library to provide abstract access to various archives. 
It is intended for use in video games. 
The programmer defines a "write directory" on the physical filesystem. 
No file writing done through the PhysicsFS API can leave that write directory.

%package -n %{name}-devel
Summary: Headers for developing programs that will use physfs
Group:   Development/Libraries
Requires: %{name} = %{version} zlib-devel

%description -n %{name}-devel
This package contains the headers that programmers will need to develop
applications which will use physfs

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot} install

rm -f $RPM_BUILD_ROOT%{_libdir}/lib%{name}.a

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig

%files -n %{name}
%defattr(-, root, root)
%doc CHANGELOG CREDITS INSTALL LICENSE TODO
%{_libdir}/*.so.*

%files -n %{name}-devel
%defattr(-, root, root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.so
 
%changelog
* Sun Oct 12 2003 Che
- initial rpm release 



