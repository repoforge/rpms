# $Id$
# Authority: rudolf
# Upstream: Steve Jankowski <steve$qstat,org>

Summary: Real-time Game Server Status for Quake servers
Name: qstat
Version: 2.11
Release: 1%{?dist}
License: Artistic
Group: Applications/Internet
URL: http://www.qstat.org/

Source: http://dl.sf.net/qstat/qstat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
QStat is a command-line program that gathers real-time statistics
from Internet game servers. Most supported games are of the first
person shooter variety (Quake, Half-Life, etc)

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog CHANGES.txt contrib.cfg LICENSE.txt qstatdoc.html info/*.txt
%config(noreplace) %{_sysconfdir}/qstat.cfg
%{_bindir}/qstat

%changelog
* Thu Dec 27 2007 Jim <quien-sabe@metaorg.com> - 2.11-1
- Updated to release 2.11.

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 2.5-0.c
- Initial package. (using DAR)
