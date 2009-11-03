# $Id$
# Authority: dag
# Upstream: Lennart Poettering <mzvscyhtq$0pointer,de>
# Upstream: <ifplugd-discuss$mail,0pointer,de>

Summary: Roaming daemon for wireless NICs supporting the Linux wireless extensions
Name: waproamd
Version: 0.6
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://0pointer.de/lennart/projects/waproamd/

Source: http://0pointer.de/lennart/projects/waproamd/waproamd-%{version}.tar.gz
Patch: waproamd-0.6-chkconfig.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libdaemon-devel, lynx, pkgconfig

%description
WapRoamD is a roaming daemon for wireless IEEE 802.11 NICs supporting the
Linux wireless extensions. It is intended to configure the WEP keys according
to the networks found.  WapRoamD is intended to be used together with ifplugd.
Whenever an association succeeds, ifplugd detects it and runs further
configuration commands for it.

%prep
%setup
%patch -p1

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e 's|\${DESTDIR}/\${sysvinitdir}|\$(DESTDIR)\$(sysconfdir)/rc.d/init.d|' conf/Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/chkconfig --add waproamd

%preun
if [ $1 -eq 0 ]; then
        /sbin/service waproamd stop &>/dev/null || :
        /sbin/chkconfig --del waproamd
fi

%postun
/sbin/service waproamd condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/*.css doc/README.* LICENSE
%doc %{_mandir}/man?/*
%{_mandir}/man8/*
%config %{_initrddir}/waproamd
%config(noreplace) %{_sysconfdir}/waproamd/
%{_sbindir}/waproamd

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 15 2004 Dag Wieers <dag@wieers.com> - 0.6-1
- Initial package. (using DAR)
