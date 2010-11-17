# $Id$
# Authority: shuff

Summary: Host-based tool to scan for rootkits, backdoors and local exploits
Name: rkhunter
Version: 1.3.8
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.rootkit.nl/projects/rootkit_hunter.html

Source: http://downloads.sourceforge.net/project/rkhunter/rkhunter/%{version}/rkhunter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: /bin/sh
Requires: binutils
Requires: coreutils
Requires: e2fsprogs
Requires: findutils
Requires: grep
Requires: iproute
Requires: lsof
Requires: mailx
Requires: mktemp
Requires: modutils
Requires: net-tools
Requires: perl
Requires: perl(IO::Socket)
Requires: perl(strict)
Requires: prelink
Requires: procps
Requires: wget

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
%setup

### FIXME: installer has /usr/local as default prefix for RPM
%{__perl} -pi.orig -e 's|PREFIX="\${RPM_BUILD_ROOT}/usr/local"|PREFIX="\${RPM_BUILD_ROOT}%{_prefix}"|g' installer.sh

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
RPM_BUILD_ROOT="%{buildroot}" ./installer.sh --layout RPM --install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root 0755)
%doc files/ACKNOWLEDGMENTS files/CHANGELOG files/FAQ files/LICENSE files/README 
%doc %{_mandir}/man8/rkhunter.8*
%config(noreplace) %{_sysconfdir}/rkhunter.conf
%{_bindir}/rkhunter
%{_libdir}/rkhunter/
%{_localstatedir}/lib/rkhunter/
%exclude %{_docdir}
 
%changelog
* Wed Nov 17 2010 Steve Huff <shuff@vecna.org> - 1.3.8-1
- Updated to version 1.3.8.

* Mon May 31 2010 Christoph Maser <cmaser@gmx.de> - 1.3.6-1
- Updated to version 1.3.6.

* Tue May 05 2009 Christoph Maser <cmr@financial.com> - 1.3.4-1
- Updated to release 1.3.4.

* Tue Dec 23 2008 Christoph Maser <cmr@financial.com> - 1.3.2-1
- Updated to release 1.3.2.
- Use --layout RPM from installer.sh.
- Patch installer to use "/usr" prefix in RPM mode.

* Thu May 17 2007 Dag Wieers <dag@wieers.com> - 1.2.9-2
- Fixed the INSTALLDIR location in rkhunter.conf. (Phil Schaffner)

* Mon May 14 2007 Dag Wieers <dag@wieers.com> - 1.2.9-1
- Initial package. (using DAR)
