# $Id$
# Authority: dries

Summary: C++ client API for PostgreSQL
Name: libpqxx
Version: 2.2.3
Release: 1
License: BSD
Group: System Environment/Libraries
URL: http://pqxx.tk/

Source: ftp://gborg.postgresql.org/pub/libpqxx/stable/libpqxx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel, postgresql-devel, postgresql-libs, gcc-c++

%description
C++ client API for PostgreSQL. The standard front-end (in the sense of
"language binding") for writing C++ programs that use PostgreSQL. Supersedes
older libpq++ interface. Requires an up-to-date C++ compiler, like gcc 2.95
or better.

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
%configure \
	--enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__mkdir_p} %{buildroot}/pqxx
%{__mv} %{buildroot}%{_includedir}/* %{buildroot}/pqxx/
%{__mv} %{buildroot}/pqxx %{buildroot}%{_includedir}/

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libpqxx.pc

%files devel
%defattr(-, root, root, 0755)
%doc doc/html/*
%{_includedir}/pqxx/*
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> - 2.2.3-1
- Initial package.
