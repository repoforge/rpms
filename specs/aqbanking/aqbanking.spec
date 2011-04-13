# $Id$
# Authority: dag

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define qtver qt
%{?el5:%define qtver qt3}
%{?el4:%define qtver qt3}
%{?el3:%define qtver qt3}
%{?el2:%define qtver qt3}

Name: aqbanking
Summary: Library for online banking functions and financial data import/export
Version: 4.2.4
Release: 1%{?dist}
# Download is PHP form at http://www.aquamaniac.de/sites/download/packages.php
License: GPLv2+
Group: System Environment/Libraries
URL: http://www.aquamaniac.de/aqbanking/

Source: aqbanking-%{version}.tar.gz
Patch2: aqbanking-3.7.2-pkgconfig.patch
Patch3: aqbanking-2.1.0-conflict.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext
BuildRequires: gmp-devel
BuildRequires: gwenhywfar-devel >= 3.10.0
BuildRequires: libtool
BuildRequires: %{qtver}-devel
BuildRequires: qt4-devel
Obsoletes: aqhbci <= 1.0.3
Obsoletes: g2banking < 3.7.2-1
Obsoletes: python-aqbanking

%description 
The intention of AqBanking is to provide a middle layer between the
program and the various Online Banking libraries (e.g. AqHBCI). The
first backend which is already supported is AqHBCI, a library which
implements a client for the German HBCI (Home Banking Computer
Interface) protocol. Additionally, Aqbanking provides various plugins
to simplify import and export of financial data. Currently there are
import plugins for the following formats: DTAUS (German financial
format), SWIFT (MT940 and MT942).

%package devel
Summary: Development headers for Aqbanking
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gwenhywfar-devel
Requires: pkgconfig
# for %{_datadir}/aclocal
Requires: automake
Obsoletes: aqhbci-devel <= 1.0.3
Obsoletes: g2banking-devel < 3.7.2-1 

%description devel
This package contains aqbanking-config and header files for writing and
compiling programs using Aqbanking.

%package -n qbanking
Summary: Qt3 bindings for Aqbanking
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: aqhbci-qt-tools <= 1.0.3
Obsoletes: kbanking < 3.7.2-1 

%description -n qbanking
This package contains the qbanking KDE bindings for the Aqbanking
online banking library.

%package -n qbanking-devel
Summary: Development headers for qbanking
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}
Requires: qbanking = %{version}-%{release}
Requires: %{qtver}-devel
Obsoletes: kbanking-devel < 3.7.2-1 

%description -n qbanking-devel
This package contains qbanking-config and header files for writing and
compiling programs using the qbanking bindings for Aqbanking.

%package -n q4banking
Summary: Qt4 bindings for Aqbanking
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
%{?_qt4_version:Requires:qt4 >= %{_qt4_version}}

%description -n q4banking
%{summary}.

%package -n q4banking-devel
Summary: Development files for q4banking
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}
Requires: q4banking = %{version}-%{release}
Requires: qt4-devel
%description -n q4banking-devel
%{summary}.


%prep
%setup
%patch2 -p1 -b .pkgconfig
%patch3 -p1 -b .conflict

%build
if [[ -z "$QTDIR" ]]; then
    source /etc/profile.d/qt.sh
fi

%configure \
  --disable-static \
  --enable-qt4 \
  --with-frontends="qbanking q4banking" \
  --with-qt4-includes="%{_qt4_headerdir}" \
  --with-qt4-libs="%{_qt4_libdir}" \
  --with-qt4-moc="moc-qt4" \
  --with-qt4-uic="uic-qt4"

%{__make} LIBTOOL="/usr/bin/libtool"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" LIBTOOL="/usr/bin/libtool"
%find_lang %{name}

%{__make} -C tutorials clean
%{__rm} -rf tutorials/.deps/ tutorials/Makefile*

%{__install} -d -m0755 %{buildroot}%{_docdir}/aqbanking-%{version}/
%{__mv} %{buildroot}%{_docdir}/{aqbanking,aqhbci} %{buildroot}%{_docdir}/aqbanking-%{version}/
%{__mv} AUTHORS README COPYING ChangeLog NEWS %{buildroot}%{_docdir}/aqbanking-%{version}/

### Fix multilib errors. (RHbz #602879)
sed -i 's|** Created:.*|** Created |g' %{buildroot}%{_includedir}/q4banking/*.ui.h

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post -n qbanking -p /sbin/ldconfig
%postun -n qbanking -p /sbin/ldconfig
%post -n q4banking -p /sbin/ldconfig
%postun -n q4banking -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc %{_docdir}/aqbanking-%{version}/
%{_bindir}/aqbanking-cli
%{_bindir}/aqhbci-tool4
%dir %{_datadir}/aqbanking/
%dir %{_datadir}/aqbanking/frontends/
%{_datadir}/aqbanking/backends/
%{_datadir}/aqbanking/bankinfo/
%{_datadir}/aqbanking/imexporters/
%{_libdir}/libaq*.so.*
%dir %{_libdir}/aqbanking/
%dir %{_libdir}/aqbanking/plugins/
%dir %{_libdir}/aqbanking/plugins/*/
%dir %{_libdir}/aqbanking/plugins/*/debugger/
%dir %{_libdir}/aqbanking/plugins/*/debugger/*/
%dir %{_libdir}/aqbanking/plugins/*/frontends/
%{_libdir}/aqbanking/plugins/*/bankinfo/
%{_libdir}/aqbanking/plugins/*/imexporters/
%{_libdir}/aqbanking/plugins/*/providers/
%{_libdir}/gwenhywfar/plugins/*/dbio/*

%files devel
%defattr(-, root, root, 0755)
%doc doc/0[12]* tutorials
%{_bindir}/aqbanking-config
%{_bindir}/hbcixml3
%{_datadir}/aclocal/aqbanking.m4
%{_includedir}/aq*/
%{_libdir}/libaq*.so
%{_libdir}/pkgconfig/aqbanking.pc
%exclude %{_libdir}/lib*.a
%exclude %{_libdir}/lib*.la

%files -n qbanking
%defattr(-, root, root, 0755)
%{_bindir}/qb-help8
%{_datadir}/aqbanking/frontends/qbanking/
%{_datadir}/aqbanking/i18n/
%{_libdir}/aqbanking/plugins/*/debugger/aqhbci/aqhbci-qt3-debug
%{_libdir}/aqbanking/plugins/*/debugger/aqhbci/qt_debug.xml
%{_libdir}/aqbanking/plugins/*/frontends/qbanking
%{_libdir}/aqbanking/plugins/*/wizards/qt3*
%{_libdir}/libqbanking.so.*

%files -n qbanking-devel
%defattr(-, root, root, 0755)
%{_includedir}/qbanking/
%{_libdir}/libqbanking.so

%files -n q4banking
%defattr(-, root, root, 0755)
%{_bindir}/q4b-help1
%{_datadir}/aqbanking/frontends/q4banking/
%{_libdir}/aqbanking/plugins/*/debugger/aqhbci/aqhbci-qt4-debug
%{_libdir}/aqbanking/plugins/*/debugger/aqhbci/qt4_debug.xml
%{_libdir}/aqbanking/plugins/*/frontends/q4banking
%{_libdir}/aqbanking/plugins/*/wizards/qt4*
%{_libdir}/libq4banking.so.1*

%files -n q4banking-devel
%defattr(-, root, root, 0755)
%{_includedir}/q4banking/
%{_libdir}/libq4banking.so

%changelog
* Thu Mar 24 2011 Dag Wieers <dag@wieers.com> - 4.2.4-1
- Initial package. (based on fedora)
