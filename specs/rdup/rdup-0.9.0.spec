# $Id: rdup.spec 6655 2009-01-19 18:31:00Z dag $
# Authority: dag
# Upstream: Miek Gieben <rdup@miek.nl>

Summary: Prints filenames for backup
Name: rdup
Version: 0.9.0
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://www.miek.nl/projects/rdup/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.miek.nl/projects/rdup/rdup-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel
BuildRequires: libattr-devel
#BuildRequires: openssh-client
#BuildRequires: perl-File-Copy-Recursive

%description
rdup is a utility inspired by rsync and the plan9 way of doing backups.
rdup it self does not backup anything, it only print a list of absolute
filenames to standard output. Auxilary scripts are needed that act on
this list and implement the backup strategy.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog DEPENDENCIES DESIGN LICENSE README todo
%doc %{_mandir}/man1/rdup.1*
#%doc %{_mandir}/man1/rdup-cp.1*
#%doc %{_mandir}/man1/rdup-crypt.1*
#%doc %{_mandir}/man1/rdup-dump.1*
#%doc %{_mandir}/man1/rdup-gpg.1*
#%doc %{_mandir}/man1/rdup-gzip.1*
#%doc %{_mandir}/man1/rdup-hist.1*
#%doc %{_mandir}/man1/rdup-mirror.1*
#%doc %{_mandir}/man1/rdup-purge.1*
#%doc %{_mandir}/man1/rdup-restore.1*
#%doc %{_mandir}/man1/rdup-simple.1*
#%doc %{_mandir}/man1/rdup-snap.1*
#%doc %{_mandir}/man1/rdup-snap-link.1*
#%doc %{_mandir}/man1/rdup-snapshot.1*
%doc %{_mandir}/man1/rdup-tr.1*
%doc %{_mandir}/man1/rdup-up.1*
%doc %{_mandir}/man7/rdup-backups.7*
%{_bindir}/rdup
#%{_bindir}/rdup-cp
#%{_bindir}/rdup-crypt
#%{_bindir}/rdup-dump
#%{_bindir}/rdup-gpg
#%{_bindir}/rdup-gzip
#%{_bindir}/rdup-hist
#%{_bindir}/rdup-mirror
#%{_bindir}/rdup-purge
#%{_bindir}/rdup-restore
#%{_bindir}/rdup-simple
#%{_bindir}/rdup-snap
#%{_bindir}/rdup-snap-link
#%{_bindir}/rdup-snapshot
%{_bindir}/rdup-up
%{_datadir}/rdup/
%{_libdir}/rdup/

%changelog
* Mon Mar 02 2009 Dag Wieers <dag@wieers.com> - 0.9.0-1
- Updated to release 0.9.0.

* Sun Feb 22 2009 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Sun Feb 08 2009 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Fri Jan 02 2009 Dag Wieers <dag@wieers.com> - 0.6.4-1
- Updated to release 0.6.4.

* Tue Jun 03 2008 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Updated to release 0.6.0.

* Sun Mar 30 2008 Dag Wieers <dag@wieers.com> - 0.5.7-1
- Updated to release 0.5.7.

* Tue Mar 18 2008 Dag Wieers <dag@wieers.com> - 0.5.6-1
- Updated to release 0.5.6.

* Fri Feb 15 2008 Dag Wieers <dag@wieers.com> - 0.5.5-1
- Updated to release 0.5.5.

* Thu Jan 24 2008 Dag Wieers <dag@wieers.com> - 0.5.4-1
- Updated to release 0.5.4.

* Fri Sep 28 2007 Dag Wieers <dag@wieers.com> - 0.5.2-1
- Updated to release 0.5.2.

* Mon Jun 25 2007 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Updated to release 0.5.1.

* Sat May 19 2007 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Updated to release 0.5.0.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.3.9-1
- Updated to release 0.3.9.

* Sun Mar 18 2007 Dag Wieers <dag@wieers.com> - 0.3.8-1
- Updated to release 0.3.8.

* Tue Feb 13 2007 Dag Wieers <dag@wieers.com> - 0.3.7-1
- Updated to release 0.3.7.

* Mon Jan 29 2007 Dag Wieers <dag@wieers.com> - 0.3.6-1
- Updated to release 0.3.6.

* Thu Dec 28 2006 Dag Wieers <dag@wieers.com> - 0.3.5-1
- Initial package. (using DAR)
