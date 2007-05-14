%define rkhVer 1.2.8
%define rpmRel 3

Summary: Host-based tool to scan for rootkits, backdoors and local exploits
Name: rkhunter
Version: 1.2.9
Release: 1
License: GPL
Group: Applications/System
URL: http://www.rootkit.nl/

Source: http://dl.sf.net/rkhunter/rkhunter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: /bin/sh, coreutils, binutils, modutils, findutils, grep, mktemp
Requires: e2fsprogs, procps, lsof, prelink, iproute, net-tools, wget
Requires: perl, perl(strict), perl(IO::Socket), mailx

%description
Rootkit Hunter scans files and systems for known and unknown rootkits,
backdoors, and sniffers.  The package contains one shell script, a few
text-based databases, and optional Perl modules.  It should run on almost
every Unix clone.  This tool scans for rootkits, backdoors and local
exploits by running tests like: 

	MD5 hash compare,
	Look for default files used by rootkits,
	Wrong file permissions for binaries,
	Look for suspected strings in LKM and KLD modules,
	Look for hidden files,
	Optional scan within plaintext and binary files,
	Software version checks and
	Application tests

%prep
%setup -n %{name}-%{version}/files

%{__perl} -pi.0001 -e '
		s|^#(INSTALLDIR=).+$|$1%{_prefix}|;
		s|^#(MAIL-ON-WARNING=).+$|$1root\@localhost|;
		s|^#(TMPDIR=).+$|$1%{_var}/%{name}/tmp|;
		s|^#(DBDIR=).+$|$1%{_var}/%{name}/db|;
	' rkhunter.conf

%{__perl} -pi.orig -e 's| /usr/man| %{_mandir}|g' rkhunter

%{__cat} <<EOF >rkhunter.logrotate
%{_localstatedir}/log/rkhunter.log {
	weekly
	notifempty
	create 640 root root
}
EOF

%build

%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m0750 rkhunter %{buildroot}%{_bindir}/rkhunter

%{__install} -Dp -m0644 rkhunter.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/rkhunter
%{__install} -Dp -m0640 rkhunter.conf %{buildroot}%{_sysconfdir}/rkhunter.conf
#%{__install} -Dp -m0640 rkhunter.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/rkhunter
#%{__install} -Dp -m0750 01-rkhunter %{buildroot}%{_sysconfdir}/cron.daily/01-rkhunter

%{__install} -d -m0750 %{buildroot}%{_localstatedir}/rkhunter/db/
%{__install} -p -m640 *.dat %{buildroot}%{_localstatedir}/rkhunter/db/

%{__install} -d -m0755 %{buildroot}%{_mandir}/man8/
%{__install} -p -m0644 -p development/*.8 %{buildroot}%{_mandir}/man8/

%{__install} -d -m0755 %{buildroot}%{_prefix}/lib/rkhunter/scripts/
%{__install} -p -m0750 *.pl check_*.sh %{buildroot}%{_prefix}/lib/rkhunter/scripts/

%{__install} -d -m0750 %{buildroot}%{_localstatedir}/rkhunter/tmp/

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/
touch %{buildroot}%{_localstatedir}/log/rkhunter.log
%{__chmod} 0640 %{buildroot}%{_localstatedir}/log/rkhunter.log

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG LICENSE README WISHLIST
%doc %{_mandir}/man8/*.8*
%config(noreplace) %{_sysconfdir}/rkhunter.conf
#%config(noreplace) %{_sysconfdir}/sysconfig/rkhunter
#%config %{_sysconfdir}/cron.daily/01-rkhunter
%config %{_sysconfdir}/logrotate.d/rkhunter
%{_bindir}/rkhunter
%{_prefix}/lib/rkhunter/
%{_localstatedir}/rkhunter/
%ghost %{_localstatedir}/log/rkhunter.log

%changelog
* Mon May 14 2007 Dag Wieers <dag@wieers.com> - 1.2.9-1
- Initial package. (using DAR)
