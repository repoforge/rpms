# $Id$
# Authority: rudolf
# Upstream: Steve Jankowski <steve$qstat,org>

%define real_version 25c

Summary: Real-time Game Server Status for Quake servers
Name: qstat
Version: 2.5
Release: 0.c
License: Artistic
Group: Applications/Internet
URL: http://www.qstat.org/

Source: http://www.qstat.org/qstat%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
QStat is a command-line program that gathers real-time statistics
from Internet game servers. Most supported games are of the first
person shooter variety (Quake, Half-Life, etc)

%prep
%setup -n %{name}%{real_version}

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 qstat %{buildroot}%{_bindir}/qstat
%{__install} -Dp -m0644 qstat.cfg %{buildroot}%{_sysconfdir}/qstat.cfg

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES.txt contrib.cfg info/* qstatdoc.html
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*

%changelog
* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 2.5-0.c
- Initial package. (using DAR)
