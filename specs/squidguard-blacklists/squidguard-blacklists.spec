# $Id$
# Authority: dag
# Upstream: Dag Wieers <dag$wieers,com>

### DB files are different depending on version of db3/db4
##Dist: nodist

### FIXME: TODO: Add a tool that updates blacklists and reconfigs squidguards.

%define dbhomedir %{_localstatedir}/lib/squidguard

Summary: Regularly updated blacklists for use with squidguard
Name:    squidguard-blacklists
Version: 1.3
Release: 1%{?dist}
Epoch:   1
License: GPL
Group:   System Environment/Libraries
URL:     http://www.squidguard.org

Source0: ftp://ftp.univ-tlse1.fr/pub/reseau/cache/squidguard_contrib/blacklists.tar.gz
Source1: http://www.ingrid.org/~harada/filtering/dmozlists/dmozlists-ages-adult-20020930.tar.gz
Source2: http://squidguard.mesd.k12.or.us/blacklists.tgz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: squidguard = 1.3
Requires: squidguard = 1.3

%description
Regularly updated blacklists for use with squidguard.

%prep
%{__rm} -rf %{_builddir}/%{name}-%{version}/

%setup -n %{name}-%{version}/univtlse -T -D -c -b0
%setup -n %{name}-%{version}/dmoz -T -D -c -b1
%setup -n %{name}-%{version}/k12 -T -D -c -b2

cd %{_builddir}/%{name}-%{version}/

### Create logrotate file
%{__cat} <<EOF >squidguard-blacklists.logrotate
%{_localstatedir}/log/squidguard/*.log {
	missingok
	copytruncate
	notifempty
}
EOF

### Clean up univtlse blacklists
%{__mv} -f univtlse/blacklists/* univtlse/
%{__rm} -f univtlse/ads univtlse/aggressive univtlse/drugs univtlse/mail univtlse/porn univtlse/proxy univtlse/violence
%{__rm} -rf univtlse/blacklists/

### Clean up dmoz blacklists
%{__mv} -f dmoz/dmozlists/* dmoz/
%{__rm} -rf dmoz/dmozlists/

### Clean up k12 blacklists
%{__mv} -f k12/blacklists/* k12/
%{__rm} -rf k12/blacklists/

### Clean up empty blacklists and remove symlinks
find . -size 0 -exec %{__rm} -f {} \;
find . -type l -exec %{__rm} -f {} \;

%build

%install
%{__rm} -rf %{buildroot}
cd %{_builddir}/%{name}-%{version}/

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/squid/local/{bad,good}/ \
			%{buildroot}%{_localstatedir}/log/squidguard/

%{__install} -Dp -m0644 squidguard-blacklists.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/squidguard-blacklists

### Creating uniq blacklists, default squidguard configfile and temporary configfile for generating databases
(
	echo -e "### This config-file is part of the squidguard-blacklists RPM package."
	echo -e "### More information about this package at:\n###\thttp://dag.wieers.com/home-made/squidguard/\n\n"
	echo -e "### Path configuration\ndbhome %{dbhomedir}\nlogdir %{_localstatedir}/log/squidguard\n"
	echo -e "### Generated blacklist definitions"
	echo -e "dbhome %{buildroot}%{dbhomedir}\nlogdir %{buildroot}%{_localstatedir}/log/squidguard\n\n" >&3
	for name in ads:publicite adult:porn aggressive:agressif audio-video drugs:drogue forums gambling hacking mail proxy:redirector:strict_redirector violence warez; do
		%{__mkdir} -p %{buildroot}%{dbhomedir}/${name/:*}/
		echo -e "### Group '${name/:*}' containing entries for '${name//:/, }'\ndest ${name/:*} {\n\tlogfile ${name/:*}.log\n"
		echo -e "dest ${name//:*} {\n\tlogfile ${name/:*}.log\n" >&3
		echo -e "\tdomainlist\t${name/:*}/domains\n\turllist\t\t${name/:*}/urls\n\texpressionlist\t${name/:*}/expressions\n}\n"
		echo -e "\tdomainlist\t${name/:*}/domains\n\turllist\t\t${name/:*}/urls\n}\n" >&3
		for list in ${name//:/ }; do
			find */$list/ -type f -name "domains" -exec sort {} >>%{buildroot}%{dbhomedir}/${name/:*}/domains.t \;
			find */$list/ -type f -name "urls" -exec sort {} >>%{buildroot}%{dbhomedir}/${name/:*}/urls.t \;
			find */$list/ -type f -name "expressions" -exec sort {} >>%{buildroot}%{dbhomedir}/${name/:*}/expressions.t \;
		done
		for file in %{buildroot}%{dbhomedir}/${name/:*}/*.t; do
			sort $file | uniq >${file/%.t}
			%{__rm} -f $file
		done
	done
	echo -e "### Define your local blacklists here"
	echo -e "dest bad {\n\tlogfile localbad.log\n\n\tdomainlist\tlocal/bad/domains\n\turllist\t\tlocal/bad/urls\n\texpressionlist\tlocal/bad/expressions\n}\n"
	echo -e "dest good {\n\tdomainlist\tlocal/good/domains\n\turllist\t\tlocal/good/urls\n\texpressionlist\tlocal/good/expressions\n}\n"
	echo -e "### ACL definition\nacl {\n\tdefault {\n\t\tpass good !bad !adult !aggressive !audio-video !hacking !warez any\n#\t\tredirect 302:http://localhost/access-denied.html?url=%u\n\t}\n}"
	echo -e "acl {\n\tdefault {\n\t\tpass any\n\t}\n}" >&3
) >%{buildroot}%{_sysconfdir}/squid/squidguard-blacklists.conf 3>temp.conf

### Generating databases
squidGuard -d -c temp.conf -C all

### Create 'local' demo files
touch %{buildroot}%{_sysconfdir}/squid/local/{bad,good}/{domains,expressions,urls}
%{__ln_s} -f %{_sysconfdir}/squid/local/ %{buildroot}%{dbhomedir}/
echo -e "users.pandora.be\nerrors.pandora.be\nusers.pandora.be" >>%{buildroot}%{_sysconfdir}/squid/local/good/domains
echo '\.(ra?m|wma|mp2|mpv2|mp3|asx)($|\?)' >>%{buildroot}%{_sysconfdir}/squid/local/bad/expressions
echo '\.(mpe?g?|wmv|mov|movie|qt|avi|dvd?|divx)($|\?)' >>%{buildroot}%{_sysconfdir}/squid/local/bad/expressions

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, squid, squid, 0755)
%config %{_sysconfdir}/squid/squidguard-blacklists.conf
%config %{_sysconfdir}/logrotate.d/*

%defattr(600, squid, squid, 0700)
%config(noreplace) %{_sysconfdir}/squid/local/
%{dbhomedir}/
%dir %{_localstatedir}/log/squidguard/
%ghost %{_localstatedir}/log/squidguard/*.log

%changelog
* Tue Mar 30 2010 Yury V. Zaytsev <yury@shurup.com> - 1.3-1
- Updated blacklists and hopefully fixed deps loop.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 20050528-1.2
- Rebuild for Fedora Core 5.

* Tue May 31 2005 Dag Wieers <dag@wieers.com> - 20050528-1
- Updated to release 20050528.

* Wed Jan 12 2005 Dag Wieers <dag@wieers.com> - 20050108-1
- Updated to release 20050108.

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 20040918-1
- Updated to release 20040918.

* Tue Mar 23 2004 Dag Wieers <dag@wieers.com> - 20040318-1
- Updated to release 20040318.
- Fixed problem with multiple blacklists per destination. (Tom Gordon)

* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 20040309-1
- Updated to release 20040309.

* Mon Sep 22 2003 Dag Wieers <dag@wieers.com> - 20030922-0
- Updated to release 20030922.

* Mon Aug 04 2003 Dag Wieers <dag@wieers.com> - 20030804-1
- Updated to release 20030804.
- Added local black and whitelist for overriding.
- Disabled local black and white lists by default.
- FIXME: still problem when installing files that used to be directories !

* Wed Mar 26 2003 Dag Wieers <dag@wieers.com> - 20030317-1
- Updated to release 20030317.
- Added debnpaf blacklists.

* Thu Jan 30 2003 Dag Wieers <dag@wieers.com> - 20030127-1
- Creating prebuilt databases automatically.

* Mon Jan 27 2003 Dag Wieers <dag@wieers.com> - 20030127-0
- Added dmozlists and univ-tlse blacklists.
- Updated to release 20030127.

* Thu Jan 09 2003 Dag Wieers <dag@wieers.com> - 20030105-0
- Initial package. (using DAR)
