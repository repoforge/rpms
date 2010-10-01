# $Id$
# Authority: dag

# ExclusiveDist: el2 el3 el5

Summary: GNU Scientific Library for numerical analysis
Name: gsl
Version: 1.14
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.gnu.org/software/gsl/

Source: ftp://ftp.gnu.org/gnu/gsl/gsl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: binutils
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: make
BuildRequires: pkgconfig

%description
The GNU Scientific Library (GSL) is a collection of routines for
numerical analysis, written in C.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: /sbin/install-info
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info %{_infodir}/gsl-ref.info.gz %{_infodir}/dir || :

%preun devel
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/gsl-ref.info.gz %{_infodir}/dir || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%doc %{_mandir}/man1/gsl-histogram.1*
%doc %{_mandir}/man1/gsl-randist.1*
%{_bindir}/gsl-histogram
%{_bindir}/gsl-randist
%{_libdir}/*so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/gsl-config.1*
%doc %{_mandir}/man3/*.3*
%doc %{_infodir}/*info*
%exclude %{_infodir}/dir
%{_bindir}/gsl-config*
%dir %{_datadir}/aclocal/
%{_datadir}/aclocal/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gsl.pc
%exclude %{_libdir}/*.la

%changelog
* Fri Oct 01 2010 Steve Huff <shuff@vecna.org> - 1.14-1
- Updated to release 1.14.
- Captured build dependencies explicitly.

* Tue Jul 14 2009 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Fri Jul 06 2007 Dag Wieers <dag@wieers.com> - 1.9-1
- Initial package. (using DAR)
