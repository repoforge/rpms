# $Id$
# Authority: dag
# Upstream: Lennart Poettering <mzvscyhtq$0pointer,de>
# Upstream: <ifplugd-discuss$mail,0pointer,de>

%define _sbindir /sbin

Summary: Activates network interfaces on cable plug
Name: ifplugd
Version: 0.28
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://0pointer.de/lennart/projects/ifplugd/

Source: http://0pointer.de/lennart/projects/ifplugd/ifplugd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libdaemon-devel, pkgconfig >= 0.9.0, lynx, gcc-c++

%description
ifplugd is a lightweight Linux daemon which configures the network
automatically when a cable is plugged in and deconfigures it when
the cable is pulled. It is primarily intended for usage with laptops.

It relies on the distribution's native network configuration subsystem,
and is thus not very intrusive.

%prep
%setup

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e 's|\@SYSINITDIR\@|\$(DESTDIR)\$(sysconfdir)/rc.d/init.d|' conf/Makefile.in

%{__perl} -pi.orig -e 's|^(INTERFACES)=.*$|$1="auto"|' conf/ifplugd.conf

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/chkconfig --add ifplugd

%preun
if [ $1 -eq 0 ]; then
        /sbin/service ifplugd stop &>/dev/null || :
        /sbin/chkconfig --del ifplugd
fi

%postun
/sbin/service ifplugd condrestart &>/dev/null || :

%files
%defattr(-, root, root, 0755)
%doc LICENSE README doc/NEWS doc/README.html doc/SUPPORTED_DRIVERS
%doc %{_mandir}/man?/ifplug*
%config(noreplace) %{_sysconfdir}/ifplugd/
%config %{_initrddir}/ifplugd
%{_sbindir}/ifplug*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.28-1.2
- Rebuild for Fedora Core 5.

* Sat Jun 04 2005 Dag Wieers <dag@wieers.com> - 0.28-1
- Updated to release 0.28.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 0.27-1
- Updated to release 0.27.

* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 0.26-1
- Updated to release 0.26.

* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 0.25-1
- Updated to release 0.25.

* Wed Apr 21 2004 Dag Wieers <dag@wieers.com> - 0.24-1
- Updated to release 0.24.

* Sun Apr 18 2004 Dag Wieers <dag@wieers.com> - 0.23-1
- Initial package. (using DAR)
