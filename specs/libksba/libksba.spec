# $Id$
# Authority: dag
# Upstream: <gnupg-devel$gnupg,org>

# Distcc: 0

Summary: X.509 library
Name: libksba
Version: 0.4.7
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://www.gnupg.org/

Source: ftp://ftp.gnupg.org/gcrypt/alpha/libksba/libksba-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
KSBA is a library designed to build software based
on the X.509 and CMS protocols.

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
%configure
%{__make} %{?_smp_mflags}
%{__make} check

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%post devel
install-info %{_infodir}/ksba.info.gz %{_infodir}/dir

%postun devel
if [ $1 -eq 0 ]; then
  install-info --delete %{_infodir}/ksba.info.gz %{_infodir}/dir
fi

%files 
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README* THANKS TODO VERSION
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_infodir}/*.info*
%{_bindir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
%{_datadir}/aclocal/*.m4
%exclude %{_libdir}/*.la

%changelog
* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 0.4.6-1
- Initial package. (using DAR)
