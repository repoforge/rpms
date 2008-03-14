# $Id$
# Authority: dag
# Upstream: Alexander V. Lukyanov <lav$yars,free,net>
# Upstream: <lftp-devel$uniyar,ac,ru>

# Rationale: lftp 3.0+ supports sftp, http redirects and lots of important improvements

Summary: Sophisticated file transfer program
Name: lftp
Version: 3.7.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://lftp.yar.ru/

Source: http://ftp.yars.free.net/pub/source/lftp/lftp-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, openssl-devel, pkgconfig, readline-devel, gcc-c++
BuildRequires: libtool

%description
LFTP is a sophisticated ftp/http file transfer program. Like bash, it has job
control and uses the readline library for input. It has bookmarks, built-in
mirroring, and can transfer several files in parallel. It is designed with
reliability in mind.

%prep
%setup

%build
### Workaround for broken openssl on RH9 and EL3
export CPPFLAGS="-I/usr/kerberos/include"
%configure \
	--with-modules \
	--disable-static \
	--with-openssl="/usr"
%{__make} clean
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc BUGS ChangeLog COPYING FAQ FEATURES INSTALL MIRRORS NEWS README* THANKS TODO
%doc %{_mandir}/man1/lftp.1*
%doc %{_mandir}/man1/lftpget.1*
%config(noreplace) %{_sysconfdir}/lftp.conf
%{_bindir}/lftp
%{_bindir}/lftpget
%{_datadir}/lftp/
%{_libdir}/lftp/
%exclude %{_libdir}/liblftp-jobs.la
%{_libdir}/liblftp-jobs.so*
%exclude %{_libdir}/liblftp-tasks.la
%{_libdir}/liblftp-tasks.so*

%changelog
* Thu Mar 13 2008 Dag Wieers <dag@wieers.com> - 3.7.0-1
- Updated to release 3.7.0.

* Mon Jan 28 2008 Dag Wieers <dag@wieers.com> - 3.6.3-1
- Updated to release 3.6.3.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 3.6.1-1
- Updated to release 3.6.1.

* Sat Sep 08 2007 Dag Wieers <dag@wieers.com> - 3.5.14-1
- Updated to release 3.5.14.

* Fri Aug 31 2007 Dag Wieers <dag@wieers.com> - 3.5.13-1
- Updated to release 3.5.13.

* Fri Jul 06 2007 Dag Wieers <dag@wieers.com> - 3.5.11-1
- Updated to release 3.5.11.

* Wed Mar 28 2007 Dag Wieers <dag@wieers.com> - 3.5.10-1
- Updated to release 3.5.10.

* Fri Jan 26 2007 Dag Wieers <dag@wieers.com> - 3.5.9-1
- Updated to release 3.5.9.

* Wed Nov 01 2006 Dag Wieers <dag@wieers.com> - 3.5.6-2
- Fixed a problem with compiled objects in upstream source. (Tim Rupp)

* Sat Oct 28 2006 Dag Wieers <dag@wieers.com> - 3.5.6-1
- Updated to release 3.5.6.

* Fri Aug 11 2006 Dag Wieers <dag@wieers.com> - 3.5.4-1
- Updated to release 3.5.4.

* Mon Aug 07 2006 Dag Wieers <dag@wieers.com> - 3.5.3-1
- Updated to release 3.5.3.

* Fri Aug 04 2006 Dag Wieers <dag@wieers.com> - 3.5.2-2
- Added patch to handle SSL errors gracefully.

* Mon Jul 31 2006 Dag Wieers <dag@wieers.com> - 3.5.2-1
- Updated to release 3.5.2.

* Fri Jul 07 2006 Dag Wieers <dag@wieers.com> - 3.5.1-1
- Updated to release 3.5.1.

* Mon May 29 2006 Dries Verachtert <dries@ulyssis.org> - 3.4.7-1
- Updated to release 3.4.7.

* Thu May 11 2006 Dries Verachtert <dries@ulyssis.org> - 3.4.6-1
- Updated to release 3.4.6.

* Fri Apr 07 2006 Dag Wieers <dag@wieers.com> - 3.4.4-1
- Updated to release 3.4.4.

* Wed Mar 01 2006 Dag Wieers <dag@wieers.com> - 3.4.2-1
- Updated to release 3.4.2.

* Wed Mar 01 2006 Dag Wieers <dag@wieers.com> - 3.4.2-1
- Updated to release 3.4.2.

* Wed Dec 07 2005 Dag Wieers <dag@wieers.com> - 3.3.5-1
- Updated to release 3.3.5.

* Sat Nov 26 2005 Dag Wieers <dag@wieers.com> - 3.3.4-1
- Updated to release 3.3.4.

* Thu Aug 11 2005 Dag Wieers <dag@wieers.com> - 3.2.1-3
- Fixed missing ssl support on rh9 and el3. (Michael McCallister)

* Thu Jul 14 2005 Dag Wieers <dag@wieers.com> - 3.2.1-2
- Fixed openssl build. (Tomá¨ Janou¨ek)

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 3.2.1-1
- Updated to release 3.2.1.

* Mon May 16 2005 Dag Wieers <dag@wieers.com> - 3.2.0-1
- Updated to release 3.2.0.

* Fri Apr 29 2005 Dag Wieers <dag@wieers.com> - 3.1.3-1
- Updated to release 3.1.3.

* Wed Mar 23 2005 Dag Wieers <dag@wieers.com> - 3.1.1-1
- Updated to release 3.1.1.

* Tue Dec 21 2004 Dag Wieers <dag@wieers.com> - 3.0.13-1
- Updated to release 3.0.13.

* Tue Dec 07 2004 Dag Wieers <dag@wieers.com> - 3.0.12-1
- Updated to release 3.0.12.

* Thu Nov 04 2004 Dag Wieers <dag@wieers.com> - 3.0.11-1
- Updated to release 3.0.11.

* Sun Oct 31 2004 Dag Wieers <dag@wieers.com> - 3.0.10-1
- Updated to release 3.0.10.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 3.0.9-1
- Updated to release 3.0.9.

* Wed Aug 11 2004 Dag Wieers <dag@wieers.com> - 3.0.7-1
- Updated to release 3.0.7.

* Sat Jun 12 2004 Dag Wieers <dag@wieers.com> - 3.0.6-1
- Updated to release 3.0.6.

* Mon May 31 2004 Dag Wieers <dag@wieers.com> - 3.0.5-1
- Updated to release 3.0.5.

* Wed May 26 2004 Dag Wieers <dag@wieers.com> - 3.0.4-1
- Updated to release 3.0.4.

* Mon Apr 26 2004 Dag Wieers <dag@wieers.com> - 3.0.3-1
- Updated to release 3.0.3.

* Fri Apr 16 2004 Dag Wieers <dag@wieers.com> - 3.0.2-2
- Fixed HTTP 301/302 redirects. (Alexander V. Lukyanov)

* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 3.0.2-1
- Updated to release 3.0.2.

* Wed Apr 07 2004 Dag Wieers <dag@wieers.com> - 3.0.1-1
- Updated to release 3.0.1.

* Fri Apr 02 2004 Dag Wieers <dag@wieers.com> - 3.0.0-1
- Updated to release 3.0.0.

* Sat Jan 24 2004 Dag Wieers <dag@wieers.com> - 2.6.12-0
- Updated to release 2.6.12.

* Mon Dec 15 2003 Dag Wieers <dag@wieers.com> - 2.6.10-0
- Updated to release 2.6.10.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 2.6.9-0
- Updated to release 2.6.9.

* Tue Oct 14 2003 Dag Wieers <dag@wieers.com> - 2.6.8-0
- Updated to release 2.6.8.

* Sun Oct 05 2003 Dag Wieers <dag@wieers.com> - 2.6.7-0
- Initial package. (using DAR)
