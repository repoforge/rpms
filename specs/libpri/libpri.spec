# $Id$
# Authority: matthias

Summary: Implementation of the Primary Rate ISDN specification
Name: libpri
Version: 1.0.9
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://www.asterisk.org/
Source: http://ftp.digium.com/pub/libpri/libpri-%{version}.tar.gz
Patch: libpri-1.0.9-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Provides: %{name}-devel = %{version}-%{release}

%description
C implementation of the Primary Rate ISDN specification.
It was based on the Bellcore specification SR-NWT-002343 for National ISDN.
As of May 12, 2001, it has been tested work with NI-2, Nortel DMS-100, and
Lucent 5E Custom protocols on switches from Nortel and Lucent.


%prep
%setup
%patch -p1 -b .cflags
%{__perl} -pi -e 's|/usr/lib|%{_libdir}|g' Makefile


%build
export CFLAGS="%{optflags}"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_PREFIX=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE README TODO
%{_libdir}/*.so.*
# Included devel
%{_includedir}/*
%exclude %{_libdir}/*.a
%{_libdir}/*.so


%changelog
* Tue Aug 23 2005 Matthias Saou <http://freshrpms.net/> 1.0.9-1
- Initial RPM release.

