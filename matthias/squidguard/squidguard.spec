# Authority: dag

### FIXME: configure has problems finding flex output using soapbox on RHEL3
# Soapbox: 0

%define rname squidGuard
%define dbhomedir %{_localstatedir}/lib/squidguard

Summary: Combined filter, redirector and access controller plugin for squid.
Name: squidguard
Version: 1.2.0
Release: 1
License: GPL
Group: System Environment/Daemons
URL: http://www.squidguard.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.teledanmark.no/pub/www/proxy/squidGuard/%{rname}-%{version}.tar.gz
Source1: guard-distrib.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: bison, flex, perl, lynx
%{?rhfc1:BuildRequires: db4-devel}
%{?rhel3:BuildRequires: db4-devel}
%{?rh90:BuildRequires: db4-devel}
%{?rh80:BuildRequires: db4-devel}
%{?rh73:BuildRequires: db3-devel}
%{?rhel21:BuildRequires: db3-devel}
Requires: squid
Obsoletes: squidGuard
Provides: squidGuard

%description
squidGuard is a combined filter, redirector and access controller
plugin for squid. squidGuard can be used to limit or block access
users to a list of webservers, based on keywords.

%prep
%setup -n %{rname}-%{version}

%{__perl} -pi -e '
		s|^(dbhome) .+$|$1 \@sg_dbhome\@|;
		s|^(logdir) .+$|$1 \@sg_logdir\@|;
	' samples/sample.conf.in

%{__cat} <<EOF >%{name}.logrotate
%{_localstatedir}/log/squid/squidguard.log {
	missingok
	copytruncate
	notifempty
}
EOF

%build
%configure \
	--with-sg-config="%{_sysconfdir}/squid/squidguard.conf" \
	--with-sg-logdir="%{_localstatedir}/log/squidguard" \
	--with-sg-dbhome="%{dbhomedir}"
%{__make} %{?_smp_mflags} \
	LIBS="-ldb"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 \
	%{buildroot}%{_datadir}/squidguard/ \
	%{buildroot}%{_sysconfdir}/squid/ \
	%{buildroot}%{_sysconfdir}/logrotate.d/ \
	%{buildroot}%{dbhomedir} \
	%{buildroot}%{_localstatedir}/log/squidguard/

%{__install} -m0644 samples/sample.conf %{buildroot}%{_sysconfdir}/squid/squidguard.conf
%{__install} -m0644 %{SOURCE1} samples/
%{__install} -m0644 %{name}.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/squidguard
%{__ln_s} -f squidGuard %{buildroot}%{_bindir}/squidguard

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc samples/sample.conf samples/squidGuard-simple.cgi samples/squidGuard.cgi
%doc samples/guard-distrib.tar.gz doc/*.txt doc/*.html doc/*.gif
%config(noreplace) %{_sysconfdir}/squid/
%config %{_sysconfdir}/logrotate.d/*
%{_bindir}/*
%{dbhomedir}
%{_localstatedir}/log/squidguard/

%changelog
* Sat Apr 12 2003 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Removed the default blacklists.

* Thu Jan 09 2003 Dag Wieers <dag@wieers.com> - 1.2.0-0
- Initial package. (using DAR)
