# $Id$
# Authority: dag
# Upstream: Jeremy Chartier <jeremy,chartier$free,fr>

# Tag: test

### FIXME: Disabled snortalog as it does not provide an install script and it is too hard to setup properly.

%define real_version v2.4

Summary: Snort log analyzer
Name: snortalog
Version: 2.4.1
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://jeremy.chartier.free.fr/snortalog/

Source: http://jeremy.chartier.free.fr/snortalog/downloads/snortalog/snortalog_v%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
Requires: perl

%description
SnortALog is a powerfull perl script that summarizes snort logs making
it easy to view any attacks against your network.

SnortALog works with all versions of SNORT and is the only script who
can analyse snort's logs in all formats (Syslog, Fast and Full alerts).
Also, it is able to summarize Fw-1 (NG and 4.1), Netfilter and IPFilter
logs in a simmilar way.

%prep
%setup -c -n %{name}_%{real_version}

%{__perl} -pi.orig -e '
		s|^#(\$domains_file) = .+;|$1 = "%{_sysconfdir}/snortalog/domains";|;
		s|^#(\$hw_file) = .+;|$1 = "%{_sysconfdir}/snortalog/hw";|;
		s|^#(\$rules_file) = .+;|$1 = "%{_sysconfdir}/snortalog/rules";|;
		s|^(\$html_directory) = .+;|$1 = "%{_localstatedir}/www/snortalog/";|;
		s|^(\$dbm_directory) = .+;|$1 = "%{_localstatedir}/www/snortalog/";|;
		s|^(\$tmpout_file) = .+;|$1 = "%{_localstatedir}/www/snortalog/.snortalog.tmp";|;
	' snortalog.pl

%{__cat} <<EOF >snortalog.httpd
Alias /snortalog/ %{_localstatedir}/www/snortalog/

<Directory %{_localstatedir}/www/snortalog/>
#	DirectoryIndex index.php
	order deny,allow
	deny from all
	allow from 127.0.0.1
</Directory>

<FilesMatch "\.dbm$">
	order deny,allow
	deny from all
</FilesMatch>
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 snortalog.pl %{buildroot}%{_bindir}/snortalog
%{__install} -Dp -m0644 snortalog.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/snortalog.conf

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/snortalog/
%{__install} -p -m0644 domains hw rules %{buildroot}%{_sysconfdir}/snortalog/

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/www/snortalog/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.pdf CHANGES README
%config %{_sysconfdir}/snortalog/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf
%{_bindir}/snortalog
%dir %{_localstatedir}/www/snortalog/

%changelog
* Thu Jan 25 2007 Dag Wieers <dag@wieers.com> - 2.4.1-1
- Updated to release 2.3.1.

* Sun Dec 05 2004 Dag Wieers <dag@wieers.com> - 2.4.0-1
- Updated to release 2.4.0.

* Sun Dec 05 2004 Dag Wieers <dag@wieers.com> - 2.3.0-1
- Updated to release 2.3.0.

* Wed May 05 2004 Dag Wieers <dag@wieers.com> - 2.2.1-1
- Updated to release 2.2.1.

* Fri Mar 13 2004 Dag Wieers <dag@wieers.com> - 2.2.0-1
- Initial package. (using DAR)
