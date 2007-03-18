# $Id$
# Authority: dag

Summary: Prints filenames for backup
Name: rdup
Version: 0.3.8
Release: 1
License: GPL
Group: Applications/File
URL: http://www.miek.nl/projects/rdup/

Source: http://www.miek.nl/projects/rdup/rdup-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel, libattr-devel
#BuildRequires: openssh-client, perl-File-Copy-Recursive

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
%doc AUTHORS ChangeLog DEPENDENCIES DESIGN LICENSE README todo hdup/
%doc %{_mandir}/man1/rdup-crypt.1*
%doc %{_mandir}/man1/rdup-gzip.1*
%doc %{_mandir}/man8/rdup-backups.8*
%doc %{_mandir}/man8/rdup-cp.8*
%doc %{_mandir}/man8/rdup-dump.8*
%doc %{_mandir}/man8/rdup-mirror.8*
%doc %{_mandir}/man8/rdup-restore.8*
%doc %{_mandir}/man8/rdup-snap.8*
%doc %{_mandir}/man8/rdup-snap-link.8*
%doc %{_mandir}/man8/rdup-snapshot.8*
%doc %{_mandir}/man8/rdup.8*
%{_sbindir}/rdup
%{_sbindir}/rdup-cp
%{_sbindir}/rdup-crypt
%{_sbindir}/rdup-dump
%{_sbindir}/rdup-gzip
%{_sbindir}/rdup-mirror
%{_sbindir}/rdup-restore
%{_sbindir}/rdup-snap
%{_sbindir}/rdup-snap-link
%{_sbindir}/rdup-snapshot
%{_datadir}/rdup/

%changelog
* Sun Mar 18 2007 Dag Wieers <dag@wieers.com> - 0.3.8-1
- Updated to release 0.3.8.

* Tue Feb 13 2007 Dag Wieers <dag@wieers.com> - 0.3.7-1
- Updated to release 0.3.7.

* Mon Jan 29 2007 Dag Wieers <dag@wieers.com> - 0.3.6-1
- Updated to release 0.3.6.

* Thu Dec 28 2006 Dag Wieers <dag@wieers.com> - 0.3.5-1
- Initial package. (using DAR)
