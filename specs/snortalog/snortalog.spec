# $Id$

# Authority: dag
# Upstream: Jeremy Chartier <jeremy.chartier@free.fr>

%define rversion v2.2

Summary: Snort log analyzer
Name: snortalog
Version: 2.2.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://jeremy.chartier.free.fr/snortalog/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://jeremy.chartier.free.fr/snortalog/snortalog_v%{version}.tgz
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
%setup -n %{name}_%{rversion}

%{__perl} -pi.orig -e '
		s|^#(\$domains_file) = .+;|$1 = "%{_sysconfdir}/snortalog/domains";|;
		s|^#(\$hw_file) = .+;|$1 = "%{_sysconfdir}/snortalog/hw";|;
		s|^#(\$rules_file) = .+;|$1 = "%{_sysconfdir}/snortalog/rules";|;
		s|^(\$html_directory) = .+;|$1 = "%{_localstatedir}/www/snortalog/";|;
		s|^(\$dbm_directory) = .+;|$1 = "%{_localstatedir}/www/snortalog/";|;
		s|^(\$tmpout_file) = .+;|$1 = "%{_localstatedir}/www/snortalog/.snortalog.tmp";|;
	' snortalog.pl

%{__cat} <<EOF >snortalog.conf
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
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_sysconfdir}/snortalog/ \
			%{buildroot}%{_localstatedir}/www/snortalog/ \
			%{buildroot}%{_sysconfdir}/httpd/conf.d/
%{__install} -m0755 snortalog.pl %{buildroot}%{_bindir}/snortalog
%{__install} -m0644 domains hw rules %{buildroot}%{_sysconfdir}/snortalog/
%{__install} -m0644 snortalog.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README *.pdf
%config %{_sysconfdir}/snortalog/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf
%{_bindir}/*
%dir %{_localstatedir}/www/snortalog/

%changelog
* Fri Mar 13 2004 Dag Wieers <dag@wieers.com> - 2.2.0-1
- Initial package. (using DAR)
