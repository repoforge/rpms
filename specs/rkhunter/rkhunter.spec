# $Id$
# Authority: dag
# Tag: test

Summary: Host-based tool to scan for rootkits, backdoors and local exploits
Name: rkhunter
Version: 1.3.2
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
%setup -n %{name}-%{version}

# FIXME: installer has /usr/local as default prefix for RPM
%{__perl} -pi.orig -e 's|PREFIX="\${RPM_BUILD_ROOT}/usr/local"|PREFIX="\${RPM_BUILD_ROOT}/usr/"|g' installer.sh

%{__cat} <<EOF >rkhunter.logrotate
%{_localstatedir}/log/rkhunter.log {
	weekly
	notifempty
	create 640 root root
}
EOF

%build

%install
RPM_BUILD_ROOT=%{buildroot} ./installer.sh --layout RPM --install 

%clean
%{__rm} -rf %{buildroot}

%files
%{_sysconfdir}/rkhunter.conf
%{_bindir}/rkhunter
%{_libdir}/rkhunter/scripts/check_modules.pl
%{_libdir}/rkhunter/scripts/check_port.pl
%{_libdir}/rkhunter/scripts/check_update.sh
%{_libdir}/rkhunter/scripts/filehashmd5.pl
%{_libdir}/rkhunter/scripts/filehashsha1.pl
%{_libdir}/rkhunter/scripts/readlink.sh
%{_libdir}/rkhunter/scripts/showfiles.pl
%{_libdir}/rkhunter/scripts/stat.pl
%{_defaultdocdir}/rkhunter-1.3.2/ACKNOWLEDGMENTS
%{_defaultdocdir}/rkhunter-1.3.2/CHANGELOG
%{_defaultdocdir}/rkhunter-1.3.2/FAQ
%{_defaultdocdir}/rkhunter-1.3.2/LICENSE
%{_defaultdocdir}/rkhunter-1.3.2/README
%{_defaultdocdir}/rkhunter-1.3.2/WISHLIST
%{_mandir}/man8/rkhunter.8.gz
/var/lib/rkhunter/db/backdoorports.dat
/var/lib/rkhunter/db/defaulthashes.dat
/var/lib/rkhunter/db/i18n/cn
/var/lib/rkhunter/db/i18n/en
/var/lib/rkhunter/db/i18n/zh
/var/lib/rkhunter/db/i18n/zh.utf8
/var/lib/rkhunter/db/md5blacklist.dat
/var/lib/rkhunter/db/mirrors.dat
/var/lib/rkhunter/db/os.dat
/var/lib/rkhunter/db/programs_bad.dat
/var/lib/rkhunter/db/programs_good.dat
/var/lib/rkhunter/db/suspscan.dat
%dir /var/lib/rkhunter/tmp


 
%changelog
* Tue Dec 23 2008 Christoph Maser <cmr@financial.com> - 1.3.2 - 1
- Update to 1.3.2
- use --layout RPM from installer.sh
- patch installer to use "/usr" prefix in RPM mode

* Thu May 17 2007 Dag Wieers <dag@wieers.com> - 1.2.9-2
- Fixed the INSTALLDIR location in rkhunter.conf. (Phil Schaffner)

* Mon May 14 2007 Dag Wieers <dag@wieers.com> - 1.2.9-1
- Initial package. (using DAR)
