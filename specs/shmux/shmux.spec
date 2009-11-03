# $Id$
# Authority: dag
# Upstream: Christophe Kalt <shmux$taranis,org>

Summary: Program for executing the same command on many hosts in parallel
Name: shmux
Version: 1.0.2
Release: 1%{?dist}
License: BSD-like
Group: System Environment/Shells
URL: http://web.taranis.org/shmux/

Source: http://web.taranis.org/shmux/dist/shmux-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: fping

%description
shmux is program for executing the same command on many hosts in parallel.
For each target, a child process is spawned by shmux, and a shell on the
target obtained one of the supported methods: rsh, ssh, or sh. The output
produced by the children is received by shmux and either output in turn to
the user, or written to files for later processing.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES INSTALL LICENSE mcmd.sh
%doc %{_mandir}/man1/shmux.1*
%{_bindir}/shmux
%{_datadir}/shmux/

%changelog
* Mon Dec 22 2008 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Mon Aug 27 2007 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Thu Aug 31 2006 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Fri Aug 11 2006 Dag Wieers <dag@wieers.com> - 1.0-0.b10
- Updated to release 1.0b10.

* Fri Jul 07 2006 Dag Wieers <dag@wieers.com> - 1.0-0.b9
- Updated to release 1.0b9.

* Fri Jun 30 2006 Dag Wieers <dag@wieers.com> - 1.0-0.b8.1
- Updated to release 1.0b8.

* Tue May 23 2006 Dag Wieers <dag@wieers.com> - 1.0-0.b7.1
- Updated to release 1.0b7 (for real now).

* Mon Mar 07 2005 Dag Wieers <dag@wieers.com> - 1.0-0.b6.1
- Updated to release 1.0b6 (for real now).

* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 1.0-0.b6
- Updated to release 1.0b6.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 1.0-0.b5
- Updated to release 1.0b5.

* Sun Aug 08 2004 Dag Wieers <dag@wieers.com> - 1.0-0.b4
- Updated to release 1.0b4.

* Wed Jul 07 2004 Dag Wieers <dag@wieers.com> - 1.0-0.b3
- Updated to release 1.0b3.

* Tue Jun 08 2004 Dag Wieers <dag@wieers.com> - 0.13-0.b
- Updated to release 0.13b.

* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 0.12-0.b
- Updated to release 0.12b.

* Mon Dec 31 2003 Dag Wieers <dag@wieers.com> - 0.11-0.a
- Updated to release 0.11a.

* Mon Jun 23 2003 Dag Wieers <dag@wieers.com> - 0.10-0.a
- Updated to release 0.10a.

* Mon May 05 2003 Dag Wieers <dag@wieers.com> - 0.9-0.a
- Updated to release 0.9a.

* Fri May 02 2003 Dag Wieers <dag@wieers.com> - 0.8-0
- Updated to release 0.8a.

* Tue Apr 29 2003 Dag Wieers <dag@wieers.com> - 0.7-0
- Updated to release 0.7a. (using DAR)

* Wed Aug 14 2002 Dag Wieers <dag@wieers.com> - 0.3-0
- Initial package.
