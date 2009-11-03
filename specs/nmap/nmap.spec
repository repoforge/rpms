# $Id$
# Authority: matthias
# Upstream: <nmap-dev$insecure,org>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}

%{?el4:%define _without_python24 1}
%{?el3:%define _without_python24 1}

%define desktop_vendor rpmforge

Summary: Network exploration tool and security scanner
Name: nmap
Version: 5.00
Release: 1%{?dist}
Epoch: 2
License: GPL
Group: Applications/System
URL: http://www.insecure.org/nmap/

Source: http://download.insecure.org/nmap/dist/nmap-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libpcap
BuildRequires: openssl-devel
BuildRequires: pcre-devel
%{!?_without_python24:BuildRequires: python-devel >= 2.4}
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
Nmap is a utility for network exploration or security auditing.  It supports
ping scanning (determine which hosts are up), many port scanning techniques
(determine what services the hosts are offering), and TCP/IP fingerprinting
(remote host operating system identification). Nmap also offers flexible target
and port specification, decoy scanning, determination of TCP sequence
predictability characteristics, reverse-identd scanning, and more.

%package frontend
Summary: Graphical frontend for nmap
Group: Applications/System
Requires: nmap = %{epoch}:%{version}

%description frontend
This package includes zenmap, a graphical frontend for nmap. The nmap package
must be installed before installing nmap-frontend.

%prep
%setup

%build
%configure \
    --enable-ipv6
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%if %{!?_without_python24:1}0
%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --delete-original \
    --vendor %{desktop_vendor}                 \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/zenmap.desktop \
    %{buildroot}%{_datadir}/applications/zenmap-root.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING* HACKING docs/*.txt docs/*.xml docs/README
%doc %{_mandir}/man1/ncat.1*
%{!?_without_python24:%doc %{_mandir}/man1/ndiff.1*}
%doc %{_mandir}/man1/nmap.1*
%{_bindir}/ncat
%{!?_without_python24:%{_bindir}/ndiff}
%{_bindir}/nmap
%{_datadir}/ncat/
%{_datadir}/nmap/

%if %{!?_without_python24:1}0
%files frontend
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/zenmap.1*
%{_bindir}/nmapfe
%{_bindir}/uninstall_zenmap
%{_bindir}/xnmap
%{_bindir}/zenmap
%{_datadir}/applications/%{desktop_vendor}-zenmap.desktop
%{_datadir}/applications/%{desktop_vendor}-zenmap-root.desktop
%{_datadir}/zenmap/
%{python_sitelib}/radialnet/
%{python_sitelib}/zenmapCore/
%{python_sitelib}/zenmapGUI/
%endif

%changelog
* Fri Jul 17 2009 Dag Wieers <dag@wieers.com> - 5.00-1
- Updated to release 5.00.

* Thu Dec 13 2007 Dag Wieers <dag@wieers.com> - 4.50-1
- Updated to release 4.50.

* Sun Dec 10 2006 Dag Wieers <dag@wieers.com> - 4.20-1
- Updated to release 4.20.

* Thu Jun 29 2006 Dag Wieers <dag@wieers.com> - 4.11-1
- Updated to release 4.11.

* Wed Jun 14 2006 Dag Wieers <dag@wieers.com> - 4.10-1
- Updated to release 4.10.

* Mon Apr 24 2006 Matthias Saou <http://freshrpms.net/> 4.03-1
- Update to 4.03.

* Sun Feb 12 2006 Dag Wieers <dag@wieers.com> - 4.01-2
- Updated release to fix the checksum problems (how lame).

* Sun Feb 12 2006 Dag Wieers <dag@wieers.com> - 4.01-1
- Updated to release 4.01.

* Tue Jan 31 2006 Dag Wieers <dag@wieers.com> - 4.00-1
- Updated to release 4.00.

* Tue Sep 13 2005 Matthias Saou <http://freshrpms.net/> 3.93-0
- Update to 3.93.

* Thu Sep  8 2005 Matthias Saou <http://freshrpms.net/> 3.90-0
- Update to 3.90.

* Mon Feb 07 2005 Dag Wieers <dag@wieers.com> - 3.81-1
- Updated to release 3.81.

* Tue Oct 19 2004 Matthias Saou <http://freshrpms.net/> 3.75-0
- Update to 3.75.

* Mon Sep  6 2004 Matthias Saou <http://freshrpms.net/> 3.70-2
- Fix menu entry (TryExec vs. Exec).

* Wed Sep  1 2004 Matthias Saou <http://freshrpms.net/> 3.70-1
- Update to 3.70.
- Enable IPv6.

* Thu Jul 15 2004 Matthias Saou <http://freshrpms.net/> 3.55-1
- Update to 3.55.

* Wed May  5 2004 Matthias Saou <http://freshrpms.net/> 3.50-1
- Update to 3.50.
- Minor spec cleanups.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 3.48-2
- Rebuild for Fedora Core 1.
- Added openssl support, it works at last!

* Mon Oct  6 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.48.
- Added proper build requirements, still no openssl though.

* Tue Sep 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.45.

* Mon Jun 30 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.30.

* Thu Jun 19 2003 Matthias Saou <http://freshrpms.net/>
- Added epoch in the frontend's requirement to make rpm 4.2.1 happy.

* Tue Jun 17 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.28.

* Sun Apr 27 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.26.

* Tue Apr 22 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.25.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Fri Mar 21 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.20.
- Spec file cleanup.
- Added desktop entry.

* Thu Jan  9 2003 Harald Hoyer <harald@redhat.de> 3.0-3
- nmap-3.00-nowarn.patch added

* Mon Nov 18 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches
- remove old desktop file from $$RPM_BUILD_ROOT so rpm won't complain

* Thu Aug  1 2002 Harald Hoyer <harald@redhat.de>
- version 3.0

* Mon Jul 29 2002 Harald Hoyer <harald@redhat.de> 2.99.2-1
- bumped version

* Fri Jul 26 2002 Harald Hoyer <harald@redhat.de> 2.99.1-2
- bumped version to 2.99RC1

* Fri Jul 19 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- add an epoch

* Mon Jul  1 2002 Harald Hoyer <harald@redhat.de> 2.54.36-1
- removed desktop file
- removed "BETA" name from version
- update to BETA36

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed May 22 2002 Harald Hoyer <harald@redhat.de> 2.54BETA34-1
- update to 2.54BETA34

* Mon Mar 25 2002 Harald Hoyer <harald@redhat.com>
- more recent version (#61490)

* Mon Jul 23 2001 Harald Hoyer <harald@redhat.com>
- buildprereq for nmap-frontend (#49644)

* Sun Jul 22 2001 Heikki Korpela <heko@iki.fi>
- buildrequire gtk+

* Tue Jul 10 2001 Tim Powers <timp@redhat.com>
- fix bugs in desktop file (#48341)

* Wed May 16 2001 Tim Powers <timp@redhat.com>
- updated to 2.54BETA22

* Mon Nov 20 2000 Tim Powers <timp@redhat.com>
- rebuilt to fix bad dir perms

* Fri Nov  3 2000 Tim Powers <timp@redhat.com>
- fixed nmapdatadir in the install section, forgot lto include
  $RPM_BUILD_ROOT in the path

* Thu Nov  2 2000 Tim Powers <timp@redhat.com>
- update to nmap-2.54BETA7 to possibly fix bug #20199
- use the desktop file provided by the package instead of using my own
- patches in previous version are depreciated. Included in SRPM for
  reference only

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jun 28 2000 Tim Powers <timp@redhat.com>
- rebuilt package

* Thu Jun 8 2000 Tim Powers <timp@redhat.com>
- fixed man pages so that they are in an FHS compliant location
- use %%makeinstall
- use predefined RPM macros wherever possible

* Tue May 16 2000 Tim Powers <timp@redhat.com>
- updated to 2.53
- using applnk now
- use %configure, and %{_prefix} where possible
- removed redundant defines at top of spec file

* Mon Dec 13 1999 Tim Powers <timp@redhat.com>
- based on origional spec file from
	http://www.insecure.org/nmap/index.html#download
- general cleanups, removed lots of commenrts since it madethe spec hard to
	read
- changed group to Applications/System
- quiet setup
- no need to create dirs in the install section, "make
	prefix=$RPM_BUILD_ROOT&{prefix} install" does this.
- using defined %{prefix}, %{version} etc. for easier/quicker maint.
- added docs
- gzip man pages
- strip after files have been installed into buildroot
- created separate package for the frontend so that Gtk+ isn't needed for the
	CLI nmap
- not using -f in files section anymore, no need for it since there aren't that
	many files/dirs
- added desktop entry for gnome

* Sun Jan 10 1999 Fyodor <fyodor@dhp.com>
- Merged in spec file sent in by Ian Macdonald <ianmacd@xs4all.nl>

* Tue Dec 29 1998 Fyodor <fyodor@dhp.com>
- Made some changes, and merged in another .spec file sent in
  by Oren Tirosh <oren@hishome.net>

* Mon Dec 21 1998 Riku Meskanen <mesrik@cc.jyu.fi>
- initial build for RH 5.x
