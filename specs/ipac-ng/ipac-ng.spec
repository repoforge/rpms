# $Id$
# Authority: dag

Summary: IP accounting tool
Name: ipac-ng
Version: 1.31
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://sourceforge.net/projects/ipac-ng/

Source: http://dl.sf.net/ipac-ng/ipac-ng-%{version}.tar.bz2
Patch0: ipac-ng-1.31-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mysql-devel, gdbm-devel, postgresql-devel
# Actually bison or byacc is required.
BuildRequires: flex, openssl-devel, zlib-devel, byacc
Requires: apache, iptables
#Provides: perl(ipac_cfg.pm)

%description
ipac is a package which is designed to gather, summarize and nicely
output the IP accounting data. ipac make summaries and graphs as ascii
text and/or images with graphs.

%prep
%setup
%patch0 -p1

%build
%configure \
	--enable-auth-server="localhost" \
	--enable-classic="no" \
	--enable-default-agent="iptables" \
	--enable-default-storage="sqlite" \
	--enable-detailed-logs="yes"
%{__make} %{?_smp_mflags} all

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -D -m0644 contrib/sample_configs/ipac.conf %{buildroot}%{_sysconfdir}/ipac-ng/ipac.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING README TODO contrib/ doc/*
%doc %{_mandir}/man8/fetchipac.8*
%doc %{_mandir}/man8/ipacsum.8*
%doc %{_mandir}/man8/ipac-convert.8*
%config(noreplace) %{_sysconfdir}/ipac-ng/
%{_sbindir}/fetchipac
%{_sbindir}/ipacsum
%{_sbindir}/ipac-convert

%changelog
* Wed Jan 18 2006 Dag Wieers <dag@wieers.com> - 1.31-1
- Initial package. (using DAR)
