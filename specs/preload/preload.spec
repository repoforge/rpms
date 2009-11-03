# $Id$
# Authority: shuff
# Upstream: Behdad Esfahbod <behdad$behdad,org>

# stock RHEL5 optflags cause problems
%define optflags -g -O2 -Wall -ansi

Summary: Adaptive readahead daemon
Name: preload
Version: 0.6.3
Release: 1%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://preload.sourceforge.net/
Source: http://downloads.sourceforge.net/project/preload/preload/0.6.4/preload-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, autoconf, automake, pkgconfig >= 0.9.0
BuildRequires: glib2-devel >= 2.6
BuildRequires: help2man
Requires: logrotate

Provides: %{_sbindir}/preload

%description
preload is an adaptive readahead daemon. It monitors applications that users
run, and by analyzing this data, predicts what applications users might run,
and fetches those binaries and their dependencies into memory for faster
startup times.

%prep
%setup

%build
%configure --disable-dependency-tracking
%{__make} -j1 %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/ INSTALL NEWS README README-alpha
%doc THANKS TODO
%dir %{_sysconfdir}/logrotate.d
%{_sysconfdir}/logrotate.d/*
%config(noreplace) %{_sysconfdir}/preload.conf
%dir %{_sysconfdir}/sysconfig
%config(noreplace) %{_sysconfdir}/sysconfig/preload
%dir %{_initrddir}
%{_initrddir}/preload
%{_mandir}/man?/*
%dir %{_var}/lib
%{_var}/lib/preload
%dir %{_var}/log
%exclude %{_var}/log/preload.log
%{_sbindir}/*

%changelog
* Sun Nov 01 2009 Steve Huff <shuff@vecna.org> - 0.6.3-1
- Initial package.
