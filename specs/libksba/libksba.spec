# $Id$
# Authority: dag
# Upstream: <gnupg-devel$gnupg,org>

### RHEL 5.4 ships with libksba-1.0.2-6.el5
# ExclusiveDist: el3 el4

Summary: X.509 library
Name: libksba
Version: 0.4.7
Release: 1.2
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
%configure --disable-static
%{__make} %{?_smp_mflags}
%{__make} check

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
install-info %{_infodir}/ksba.info.gz %{_infodir}/dir

%postun devel
if [ $1 -eq 0 ]; then
  install-info --delete %{_infodir}/ksba.info.gz %{_infodir}/dir
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README* THANKS TODO VERSION
%{_libdir}/libksba.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_infodir}/*.info*
%{_bindir}/ksba-config
%{_datadir}/aclocal/ksba.m4
%{_includedir}/ksba.h
%{_libdir}/libksba.so
%exclude %{_libdir}/libksba.la

%changelog
* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 0.4.7-1
- Initial package. (using DAR)
