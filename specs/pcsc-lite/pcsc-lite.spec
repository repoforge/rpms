# $Id$
# Authority: dag

### EL6 ships with pcsc-lite-1.5.2-6.el6
### EL5 ships with pcsc-lite-1.4.4-4.el5_5
# ExclusiveDist: el2 rh7 rh9 el3 el4

Summary: PC/SC Lite smart card framework and applications
Name: pcsc-lite
Version: 1.3.3
Release: 1%{?dist}
License: BSD
Group: System Environment/Daemons
URL: http://pcsclite.alioth.debian.org/

### Source is a fixed address per file, substituting version doesn't work.
Source: https://alioth.debian.org/download.php/1565/pcsc-lite-1.3.3.tar.gz
Patch0: pcsc-lite-docinst.patch
Patch1: pcsc-lite-1.3.0-rpath64.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libusb-devel >= 0.1.7, doxygen
Requires: /sbin/chkconfig, initscripts
Requires: pcsc-ifd-handler

%description
The purpose of PC/SC Lite is to provide a Windows(R) SCard interface in a very
small form factor for communicating to smartcards and readers. PC/SC Lite uses
the same winscard API as used under Windows(R). This package includes the
PC/SC Lite daemon, a resource manager that coordinates communications with
smart card readers and smart cards that are connected to the system, as well
as other command line tools.

%package libs
Summary: PC/SC Lite libraries
Group: System Environment/Libraries
Provides: libpcsc-lite = %{version}-%{release}

%description libs
PC/SC Lite libraries.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name}-libs = %{version}-%{release}
Requires: pkgconfig
Provides: libpcsc-lite-devel = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%description devel
PC/SC Lite development files.

%package doc
Summary: PC/SC Lite developer documentation
Group: Documentation

%description doc
PC/SC Lite developer documentation.

%prep
%setup
%patch0 -p0 -b .docinst
%patch1 -p1 -b .rpath64

%{__cat} <<EOF >README-reader.conf.d
All *.conf files in this directory are merged into %{_sysconfdir}/reader.conf
by %{_sbindir}/update-reader.conf.
EOF

%build
%configure \
	--disable-dependency-tracking \
	--disable-static \
	--enable-runpid="%{_localstatedir}/run/pcscd.pid" \
	--enable-confdir="%{_sysconfdir}" \
	--enable-ipcdir="%{_localstatedir}/run" \
	--enable-usbdropdir="%{_libdir}/pcsc/drivers"
%{__make} %{?_smp_mflags}

doxygen doc/doxygen.conf
%{__rm} -f doc/api/*.{map,md5}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_libdir}/pcsc/drivers/
%{__install} -Dp -m0755 etc/pcscd.init %{buildroot}%{_initrddir}/pcscd
%{__install} -Dp -m0644 README-reader.conf.d %{buildroot}%{_sysconfdir}/reader.conf.d/README
touch %{buildroot}%{_sysconfdir}/reader.conf

%{__rm} -f %{buildroot}%{_sysconfdir}/reader.conf.d/reader.conf

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/chkconfig --add pcscd

%preun
if [ $1 -eq 0 ] ; then
	/sbin/service pcscd stop &>/dev/null || :
	/sbin/chkconfig --del pcscd
fi

%postun
if [ $1 -ge 1 ]; then
	/sbin/service pcscd condrestart &>/dev/null || :
fi

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog* COPYING DRIVERS HELP NEWS README SECURITY TODO
%doc %{_mandir}/man1/formaticc.1*
%doc %{_mandir}/man5/reader.conf.5*
%doc %{_mandir}/man8/pcscd.8*
%doc %{_mandir}/man8/update-reader.conf.8*
%dir %{_sysconfdir}/reader.conf.d/
%doc %{_sysconfdir}/reader.conf.d/README
%ghost %config %{_sysconfdir}/reader.conf
%config %{_initrddir}/pcscd
%{_libdir}/pcsc/
%{_sbindir}/pcscd
%{_sbindir}/update-reader.conf

%files libs
%defattr(-, root, root, 0755)
%{_libdir}/libpcsclite.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/PCSC/
%exclude %{_libdir}/libpcsclite.la
%{_libdir}/libpcsclite.so
%{_libdir}/pkgconfig/libpcsclite.pc

%files doc
%defattr(-, root, root, 0755)
%doc doc/api/ doc/*.pdf doc/example/pcsc_demo.c

%changelog
* Fri Jan 26 2007 Dag Wieers <dag@wieers.com> - 1.3.3-1
- Initial package. (using DAR)
