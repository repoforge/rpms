# $Id$
# Authority: dries
# Upstream: Benoit Rouits <brouits$free,fr>

Summary: POP3 client library
Name: libspopc
Version: 0.7.4
Release: 1
License: GPL
Group: Development/Libraries
URL: http://brouits.free.fr/libspopc/

Source: http://brouits.free.fr/libspopc/releases/libspopc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
libspopc is an easy-to-use POP3 client library that Its primary goal is to 
provide an easy and quick way to host a POP3 client in a program. It is 
fully reentrant (when built with -D_RENTRANT) and implements the client 
side of RFC 1939. It can download email headers and delete emails remotely 
without actualy downloading the entire message.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_libdir} %{buildroot}%{_includedir}
%{__make} install DESTDIR=%{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog README
%{_libdir}/libspopc-*.so

%files devel
#%doc %{_mandir}/man?/*
%{_includedir}/libspopc.h
%exclude %{_libdir}/*.a
%{_libdir}/libspopc.so
#%exclude %{_libdir}/*.la

%changelog
* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.7.4-1
- Updated to release 0.7.4.

* Thu Jan 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.7-1
- Initial package.
