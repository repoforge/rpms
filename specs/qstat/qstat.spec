# Authority: newrpms
%define rversion 25c

Summary: Real-time Game Server Status for Quake servers.
Name: qstat
Version: 2.5
Release: 0.c
License: Artistic
Group: Applications/Internet
URL: http://www.qstat.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.qstat.org/%{name}%{rversion}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
QStat is a command-line program that gathers real-time statistics
from Internet game servers. Most supported games are of the first
person shooter variety (Quake, Half-Life, etc)

%prep
%setup -n %{name}%{rversion}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sysconfdir} \
			%{buildroot}%{_bindir}
%{__install} -m755 qstat %{buildroot}%{_bindir}
%{__install} -m644 qstat.cfg %{buildroot}%{_sysconfdir}

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
