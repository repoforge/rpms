# $Id$
# Authority: dag

%define usbdropdir %(pkg-config libpcsclite --variable="usbdropdir" 2>/dev/null)

Summary: ACS ACR 38 USB (acr38u) Smartcard Reader driver for PCSC-lite
Name: pcsc-lite-acr38u
%define real_version 100709
Version: 1.7.9
Release: 2%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://www.acs.com.hk/acr38_driversmanual.asp

Source: http://www.acs.com.hk/download/ACR38_LINUX_%{real_version}_P.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pcsc-lite-devel >= 1.3.1
Requires: pcsc-lite >= 1.3.1

Provides: pcsc-ifd-handler
Provides: acr38u = %{version}-%{release}
Obsoletes: acr38u <= %{version}-%{release}

%description
CCID ACR38u Smart Card reader driver for PCSC-lite.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n ACR38_LINUX_%{real_version}_P

%build
%configure \
	--disable-dependency-tracking \
	--disable-static \
	--enable-usbdropdir="%{buildroot}%{usbdropdir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post
/sbin/ldconfig
if [ $1 -eq 1 ]; then
	%{_initrddir}/pcscd try-restart &>/dev/null || :
fi

%postun
/sbin/ldconfig
%{_initrddir}/pcscd try-restart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README* doc/README*
%dir %{usbdropdir}/
%{usbdropdir}/ACR38UDriver.bundle/
%{_libdir}/libacr38ucontrol.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*
%{_includedir}/ACS38DrvTools.h
%exclude %{_libdir}/libacr38ucontrol.la
%{_libdir}/libacr38ucontrol.so
%{_prefix}/lib/pkgconfig/libacr38ucontrol.pc

%changelog
* Fri Feb 09 2007 Dag Wieers <dag@wieers.com> - 1.7.9-2
- Added missing so symlink.
- Run ldconfig in %%post and %%postun.

* Fri Jan 26 2007 Dag Wieers <dag@wieers.com> - 1.7.9-1
- Initial package. (using DAR)
