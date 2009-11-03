# $Id$
# Authority: dag
# Upstream: <aide-devel@lists.sourceforge.net>

Summary: Advanced intrusion detection environment
Name: aide
Version: 0.11
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.cs.tut.fi/~rammer/aide.html

Source: http://dl.sf.net/aide/aide-%{version}.tar.gz
Source1: aide.conf
Source2: README.quickstart
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildrequires: flex, bison, m4
Buildrequires: mhash-devel, zlib-devel

### Postgresql support doesn't build.
#Buildconflicts: postgresql-devel

%description
AIDE (Advanced Intrusion Detection Environment) is a file integrity
checker and intrusion detection program.

%prep
%setup

%{__perl} -pi.orig -e 's|^C(PP)?FLAGS=.+$||' configure
%{__perl} -pi.orig -e 's|%{_sysconfdir}/aide.db|%{_localstatedir}/lib/aide.db|' config.h
%{__perl} -pi.orig -e 's|<prefix>/etc/aide.db|%{_localstatedir}/lib/aide.db|' doc/aide.1
%{__perl} -pi.orig -e 's|<prefix>/etc/aide.conf|%{_sysconfdir}/aide.conf|' doc/aide.1

%build
%configure \
	--with-config_file="%{_sysconfdir}/aide.conf" \
	--with-zlib \
	--with-mhash \
	--enable-mhash
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" \
	bindir="%{_sbindir}"
%{__install} -Dp -m0600 %{SOURCE1} %{buildroot}%{_sysconfdir}/aide.conf
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/aide/

%{__install} -p -m0644 %{SOURCE2} README.quickstart

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ./doc/manual.html AUTHORS ChangeLog COPYING NEWS README* Todo contrib/
%doc %{_mandir}/man?/aide.*

%defattr(0600, root, root, 0755)
%config(noreplace) %{_sysconfdir}/aide.conf

%defattr(0700, root, root, 0755)
%{_sbindir}/aide

%defattr(0700, root, root, 0700)
%{_localstatedir}/lib/aide/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.11-1.2
- Rebuild for Fedora Core 5.

* Mon Feb 20 2006 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Tue Nov 23 2004 Dag Wieers <dag@wieers.com> - 0.10-2
- Cosmetic changes and re-added %%changelog.

* Fri Nov 28 2003 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.10-0.fdr.1
- Update to 0.10 release.
- memleaks patch merged upstream.
- rootpath patch merged upstream.
- fstat patch not needed anymore.
- Updated URL.

* Thu Nov 13 2003 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.10-0.fdr.0.2.cvs20031104
- Added buildreq m4 to work around incomplete deps of bison package.

* Tue Nov 04 2003 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.10-0.fdr.0.1.cvs20031104
- Only tar.gz available upstream.
- byacc not needed when bison -y is available.
- Installed Russian manual pages.
- Updated with changes from CVS (2003-11-04).
- getopt patch merged upstream.
- bison-1.35 patch incorporated upstream.

* Tue Sep 09 2003 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.9-0.fdr.0.2.20030902
- Added fixes for further memleaks.

* Sun Sep 07 2003 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.9-0.fdr.0.1.20030902
- Initial package version.
