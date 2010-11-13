# $Id$
# Authority: dag

Summary: Qt Cryptographic Architecture
Name: qca
Version: 1.0
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://delta.affinix.com/qca/

Source: http://delta.affinix.com/download/qca/qca-%{version}.tar.bz2
Patch0: qca-1.0-mach.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel >= 1:3.0

%description
QCA aims to provide a straightforward and cross-platform crypto API, using Qt
datatypes and conventions. QCA separates the API from the implementation,
using plugins known as Providers.

The advantage of this model is to allow applications to avoid linking to or
explicitly depending on any particular cryptographic library. This allows one
to easily change or upgrade crypto implementations without even needing to
recompile the application.

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
%patch0 -p0 -b .mach
%{__perl} -pi.orig -e 's|target\.path=\$PREFIX/lib|target.path=\$PREFIX/%{_lib}|g' qcextra

%build
source %{_sysconfdir}/profile.d/qt.sh
./configure --prefix="%{_prefix}" --qtdir="$QTDIR"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README TODO
%{_libdir}/libqca.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/qca.h
%{_libdir}/libqca.so

%changelog
* Wed Jun 06 2007 Dag Wieers <dag@wieers.com> - 1.0-1
- initial package. (using DAR)
