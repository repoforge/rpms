# $Id$

# Authority: atrpms

Summary: Sophisticated file transfer program.
Name: lftp
Version: 2.6.12
Release: 0
License: GPL
Group: Applications/Internet
URL: http://lftp.yar.ru/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.yars.free.net/pub/software/unix/net/ftp/client/lftp/lftp-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: ncurses-devel, openssl-devel, pkgconfig, readline-devel

%description
LFTP is a sophisticated ftp/http file transfer program. Like bash, it has job
control and uses the readline library for input. It has bookmarks, built-in
mirroring, and can transfer several files in parallel. It is designed with
reliability in mind.

%prep
%setup

%build
%configure \
	--with-modules \
	--disable-static \
	--with-ssl
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__chmod} 0755 %{buildroot}%{_libdir}/lftp/*
%{__chmod} 0755 %{buildroot}%{_libdir}/lftp/%{version}/*.so

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/lftp/%{version}/*.{a,la}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc BUGS ChangeLog COPYING FAQ FEATURES README* NEWS THANKS TODO
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/lftp.conf
%{_bindir}/*
%{_datadir}/lftp/
%{_libdir}/lftp/

%changelog
* Sat Jan 24 2004 Dag Wieers <dag@wieers.com> - 2.6.12-0
- Updated to release 2.6.12.

* Mon Dec 15 2003 Dag Wieers <dag@wieers.com> - 2.6.10-0
- Updated to release 2.6.10.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 2.6.9-0
- Updated to release 2.6.9.

* Tue Oct 14 2003 Dag Wieers <dag@wieers.com> - 2.6.8-0
- Updated to release 2.6.8.

* Sun Oct 05 2003 Dag Wieers <dag@wieers.com> - 2.6.7-0
- Initial package. (using DAR)
