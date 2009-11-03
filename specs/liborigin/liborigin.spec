# $Id$
# Authority: dries

%define real_version 20060616
%define libversion 0.20060616

Summary: Library for reading OriginLab OPJ project files
Name: liborigin
Version: 0.20060616
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://sourceforge.net/projects/liborigin/

Source: http://dl.sf.net/liborigin/liborigin-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
A library for reading OriginLab OPJ project files.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{real_version}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir} %{buildroot}%{_includedir} %{buildroot}%{_libdir}
%{__install} opj2dat %{buildroot}%{_bindir}/opj2dat
%{__install} liborigin.so %{buildroot}%{_libdir}/liborigin.so.%{libversion}
%{__ln_s} liborigin.so.%{libversion} %{buildroot}%{_libdir}/liborigin.so
%{__install} OPJFile.h %{buildroot}%{_includedir}/OPJFile.h

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/opj2dat
%{_libdir}/liborigin.so.%{libversion}

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/OPJFile.h
%{_libdir}/liborigin.so

%changelog
* Thu Aug 03 2006 Dries Verachtert <dries@ulyssis.org> - 20060616-1
- Initial package.
