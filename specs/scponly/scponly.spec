# $Id$
# Authority: dag
# Upstream: <scponly$lists,ccs,neu,edu>

Summary: Limited shell for secure file transfers
Name: scponly
Version: 4.6
Release: 4%{?dist}
License: GPL
Group: System Environment/Shells
URL: http://sublimation.org/scponly/wiki/

Source: http://sublimation.org/scponly/scponly-%{version}.tgz
Patch0: scponly-4.6-rsync.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: openssh >= 3.4, openssh-server, openssh-clients, rsync
BuildRequires: openssh >= 3.4, openssh-server, openssh-clients, rsync

%description
scponly is an alternative 'shell' for system administrators
who would like to provide access to remote users to both
read and write local files without providing any remote
execution priviledges. Functionally, it is best described
as a wrapper to the "tried and true" ssh suite of applications.

%prep
%setup
%patch0 -p1 -b .rsync
### FIXME: Remove ownership changes from Makefile
%{__perl} -pi.orig -e 's|-o 0 -g 0||g' Makefile*
### Change /usr/local from the docs to /usr.
%{__perl} -pi -e 's|%{_prefix}/local/|%{_prefix}/|g' scponly.8* INSTALL README

%build
%configure \
    --enable-chrooted-binary \
    --enable-rsync-compat \
    --enable-scp-compat \
    --enable-winscp-compat
%{__make} %{?_smp_mflags} OPTS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHOR BUILDING-JAILS.TXT CHANGELOG CONTRIB COPYING INSTALL README TODO
%doc setup_chroot.sh build_extras/setup_chroot.sh*
%doc %{_mandir}/man8/scponly.8*
%config(noreplace) %{_sysconfdir}/scponly/
%{_bindir}/scponly
%{_sbindir}/scponlyc

%changelog
* Sun May 27 2007 Dag Wieers <dag@wieers.com> - 4.6-4
- Added chrooted binary.

* Mon Mar 27 2006 Matthias Saou <http://freshrpms.net/> 4.6-3
- Enable rsync and scp/winscp compatibility.
- Add change from Extras to fix /usr/local in docs.
- Include (ugly) patch to fix long rsync options (may be missing options).

* Thu Mar 09 2006 Dag Wieers <dag@wieers.com> - 4.6-2
- Use make install and added %%{_sysconfdir}/scponly/debuglevel.
- Added setup_chroot helper scripts as documentation.

* Tue Feb 21 2006 Matthias Saou <http://freshrpms.net/> 4.6-1
- Update to 4.6.

* Tue May 10 2005 Dag Wieers <dag@wwieers.com> - 4.1-1
- Updated to release 4.1.

* Thu Mar 03 2005 Dag Wieers <dag@wwieers.com> - 4.0-1
- Initial package. (using DAR)

