Summary: Portable mail access library
Name: libetpan
Version: 0.38
Release: 1
License: BSD
Group: System Environment/Libraries
URL: http://www.etpan.org/
Source: http://dl.sf.net/libetpan/libetpan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: openssl-devel, db4-devel, cyrus-sasl-devel

%description
The purpose of this mail library is to provide a portable, efficient middleware
for different kinds of mail access. When using the drivers interface, the
interface is the same for all kinds of mail access, remote and local mailboxes.


%package devel
Summary: Development files for the libetpan mail access library
Group: Development/Libraries
Requires: %{name} = %{version}
Requires: openssl-devel, db4-devel, cyrus-sasl-devel

%description devel
The purpose of this mail library is to provide a portable, efficient middleware
for different kinds of mail access. When using the drivers interface, the
interface is the same for all kinds of mail access, remote and local mailboxes.

This package contains the files required to develop applications that will use
the libetpan library.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
# Fix execution bit on the library so that it gets properly stripped
%{__chmod} +x %{buildroot}%{_libdir}/*.so.*


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYRIGHT NEWS TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/API.html doc/DOCUMENTATION doc/README.html
%{_bindir}/libetpan-config
%{_includedir}/libetpan/
%{_includedir}/libetpan.h
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%changelog
* Wed Aug  3 2005 Matthias Saou <http://freshrpms.net/> 0.38-1
- Initial RPM release.

