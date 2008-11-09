# $Id$
# Authority: dag

Summary: Off-The-Record Messaging library and toolkit
Name: libotr
Version: 3.2.0
Release: 1
License: GPL, LGPL
Group: System Environment/Libraries
URL: http://www.cypherpunks.ca/otr/

Source: http://www.cypherpunks.ca/otr/libotr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Provides: libotr-toolkit = %{version}
Obsoletes: libotr-toolkit < %{version}
BuildRequires: libgcrypt-devel >= 1.2.0, libgpg-error-devel, gcc-c++

%description
Off-the-Record Messaging Library and Toolkit
This is a library and toolkit which implements Off-the-Record (OTR) Messaging.
OTR allows you to have private conversations over IM by providing Encryption,
Authentication, Deniability and Perfect forward secrecy.

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
    --disable-static \
    --with-pic
%{__make} %{?_smp_mflags} all

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" \
    LIBINSTDIR="%{_libdir}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README
%doc %{_mandir}/man1/otr_mackey.1*
%doc %{_mandir}/man1/otr_modify.1*
%doc %{_mandir}/man1/otr_parse.1*
%doc %{_mandir}/man1/otr_readforge.1*
%doc %{_mandir}/man1/otr_remac.1*
%doc %{_mandir}/man1/otr_sesskeys.1*
%doc %{_mandir}/man1/otr_toolkit.1*
%{_bindir}/otr_mackey
%{_bindir}/otr_modify
%{_bindir}/otr_parse
%{_bindir}/otr_readforge
%{_bindir}/otr_remac
%{_bindir}/otr_sesskeys
%{_libdir}/libotr.so.*

%files devel
%defattr(-, root, root, 0755)
%doc Protocol*
%{_datadir}/aclocal/libotr.m4
%{_includedir}/libotr/
%{_libdir}/libotr.so
%{_libdir}/pkgconfig/libotr.pc
%exclude %{_libdir}/libotr.la

%changelog
* Thu Nov 06 2008 Dag Wieers <dag@wieers.com> - 3.2.0-1
- Updated to release 3.2.0.

* Sat Oct 13 2007 Dag Wieers <dag@wieers.com> - 3.1.0-1
- Updated to release 3.1.0.

* Sun Mar 19 2006 Dries Verachtert <dries@ulyssis.org> - 3.0.0-2
- gcc-c++ buildrequirement added.

* Tue Mar 14 2006 Dag Wieers <dag@wieers.com> - 3.0.0-1
- Initial package. (using DAR)
