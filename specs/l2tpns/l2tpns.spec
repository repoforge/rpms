# $Id$
# Authority: dag

Summary: High-speed clustered L2TP LNS
Name: l2tpns
Version: 2.1.20
Release: 1%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://sourceforge.net/projects/l2tpns/

Source: http://dl.sf.net/l2tpns/l2tpns-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libcli-devel >= 1.8.5

%description
l2tpns is a layer 2 tunneling protocol network server (LNS).  It
supports up to 65535 concurrent sessions per server/cluster plus ISP
features such as rate limiting, walled garden, usage accounting, and
more.

%prep
%setup

%{__perl} -pi.orig \
	-e 's|/lib\b|/%{_lib}/|g;' \
	-e 's|-o root -g root ||g;' \
	Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes COPYING INSTALL INTERNALS THANKS Docs/*.html
%doc %{_mandir}/man5/startup-config.5*
%doc %{_mandir}/man8/l2tpns.8*
%doc %{_mandir}/man8/nsctl.8*
%config(noreplace) %{_sysconfdir}/l2tpns/
%{_libdir}/l2tpns/
%{_sbindir}/l2tpns
%{_sbindir}/nsctl

%changelog
* Fri Aug 04 2006 Dag Wieers <dag@wieers.com> - 2.1.20-1
- Initial package. (using DAR)
