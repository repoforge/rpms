# $Id: oidentd.spec,v 1.1 2004/02/26 17:54:30 thias Exp $

Summary: An implementation of the RFC1413 identification server.
Name: oidentd
Version: 2.0.7
Release: 2.fr
License: GPL
Group: System Environment/Daemons
URL: http://ojnk.sourceforge.net/
Source0: http://download.sourceforge.net/ojnk/oidentd-%{version}.tar.gz
Source1: identd.init
Source2: identd.spoof
Source3: oidentd.users
Provides: identd = %{version}
Prereq: /sbin/chkconfig /etc/init.d /sbin/service
BuildRequires: byacc
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Conflicts: pidentd

%description
The oidentd package contains identd, which implements the RFC1413
identification server.  Identd looks up specific TCP/IP connections
and returns either the user name or other information about the
process that owns the connection.

Install oidentd if you need to look up information about specific
TCP/IP connections.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall
install -D -m 755 %{SOURCE1} %{buildroot}/etc/init.d/identd
install -D -m 640 %{SOURCE2} %{buildroot}%{_sysconfdir}/identd.spoof
install -D -m 640 %{SOURCE3} %{buildroot}%{_sysconfdir}/oidentd.users

%clean
rm -rf %{buildroot}

%post
/sbin/chkconfig --add identd

%preun
if [ $1 = 0 ]; then
    /sbin/service identd stop > /dev/null 2>&1
    /sbin/chkconfig --del identd
fi

%postun
if [ "$1" -ge "1" ]; then
    /sbin/service identd condrestart > /dev/null 2>&1
fi

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog* COPYING* NEWS README TODO doc/rfc1413
%{_sbindir}/oidentd
%attr(0640, root, nobody) %config(noreplace) %{_sysconfdir}/identd.spoof
%attr(0640, root, nobody) %config(noreplace) %{_sysconfdir}/oidentd.users
%attr(0755, root, root) %config /etc/init.d/identd
%{_mandir}/man?/*

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 2.0.7-2.fr
- Rebuild for Fedora Core 1.

* Tue Jul 15 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.7.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sun Sep 29 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Thu Aug 22 2002 Matthias Saou <http://freshrpms.net/>
- Fixed the init script's status, thanks to Jørn for spotting this.

* Wed Aug 21 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.4.

* Fri May  3 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Tue Jan  8 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.3.
- Fix user in %files for "-".

* Sun Dec 30 2001 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.2.

* Thu Oct  4 2001 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.1.

* Mon Oct  1 2001 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.0.

* Sat Sep 15 2001 Matthias Saou <http://freshrpms.net/>
- Update to 1.9.9.1.

* Mon Aug 27 2001 Matthias Saou <http://freshrpms.net/>
- Update to 1.9.9 (complete program rewrite).
- Added new docs and manpages.

* Tue Apr 24 2001 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup and rebuilt for Red Hat 7.1.

* Tue Jan  2 2001 Matthias Saou <http://freshrpms.net/>
- Added a Conflicts: for pidentd
- Quick cleanup
- Fixed o-r modes
- Changed the uid/gid in the initscript

* Wed Dec 27 2000 Matthias Saou <http://freshrpms.net/>
- Initial RPM release

