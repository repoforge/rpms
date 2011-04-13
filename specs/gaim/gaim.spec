# $Id$
# Authority: matthias

### EL5 ships with gaim-2.0.0-0.28.beta5.el5
# ExclusiveDist: el2 el3
### FC2, FC3 and EL4 come with the latest gaim
##ExcludeDist: fc2 fc3 el4

%{?el3:%define _without_krb4 1}
%{?el3:%define _without_perl 1}
%{?rh9:%define _without_krb4 1}
%{?rh9:%define _without_perl 1}
%{?rh7:%define _without_krb4 1}
%{?rh7:%define _without_perl 1}
%{?rh7:%define _without_startup_notification 1}

%define perl_vendorarch    %(eval "`perl -V:installvendorarch`";    echo $installvendorarch)
%define perl_vendorman3dir %(eval "`perl -V:installvendorman3dir`"; echo $installvendorman3dir)

Summary: Multiprotocol instant messaging client
Name: gaim
Version: 1.5.0
Release: 0.2%{?dist}
Epoch: 1
License: GPL
Group: Applications/Internet
URL: http://gaim.sourceforge.net/

Source: http://dl.sf.net/gaim/gaim-%{version}.tar.bz2
#Source1: gaim-rpmforge-prefs.xml
Patch4: gaim-0.76-xinput.patch
Patch6: gaim-1.0.1-naive-gnome-check.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: XFree86-devel, gcc-c++
BuildRequires: libtool, gtk2-devel, gtkspell-devel, libao-devel
BuildRequires: mozilla-nss, mozilla-nss-devel
BuildRequires: mozilla-nspr, mozilla-nspr-devel, libstdc++-devel
BuildRequires: audiofile-devel
%{!?_without_startup_notification:BuildRequires: startup-notification-devel}
%{?_with_tcltk:BuildRequires: tcl-devel, tk-devel}
%{?_with_arts:BuildRequires: arts-devel}
%{!?_without_perl:BuildRequires: perl}
%{!?_without_krb4:BuildRequires: krb5-devel >= 1.3}
Provides: gaim-devel = %{version}-%{release}
%{?_with_tcltk:Requires: tcl, tk}
%{!?_without_perl:Requires: perl}

%description
Gaim is a multi-protocol instant messaging client compatible with AIM (Oscar
and TOC protocols), ICQ, MSN Messenger, Yahoo, IRC, Jabber, Gadu-Gadu, and
Zephyr networks.

Gaim users can log in to multiple accounts on multiple IM networks
simultaneously. This means that you can be chatting with friends on AOL
Instant Messenger, talking to a friend on Yahoo Messenger, and sitting
in an IRC channel all at the same time.

Gaim supports many features of the various networks, such as file transfer
(coming soon), away messages, typing notification, and MSN window closing
notification. It also goes beyond that and provides many unique features.
A few popular features are Buddy Pounces, which give the ability to notify
you, send a message, play a sound, or run a program when a specific buddy
goes away, signs online, or returns from idle; and plugins, consisting of
text replacement, a buddy ticker, extended message notification, iconify on
away, and more.

Available rpmbuild rebuild options :
--with : tcltk arts
--without : perl


%prep
%setup
%patch4 -p1
%patch6 -p1

%build
%configure \
	--program-prefix="%{?_program_prefix}" \
	--enable-gnutls="no" \
	--enable-nss="yes" \
	%{!?_with_arts:--disable-artsc} \
	%{!?_without_krb4:--with-krb4} \
	--with-silc-includes="%{_includedir}/silc" --with-silc-libs="%{_libdir}" \
	%{!?_with_tcltk:--disable-tcl --disable-tk} \
	%{?_without_perl:--disable-perl}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}
%{__strip} %{buildroot}%{_libdir}/*.so* %{buildroot}%{_libdir}/gaim/*.so || :

#%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/gaim/prefs.xml

%post
/sbin/ldconfig -n %{_libdir}/gaim

%postun
/sbin/ldconfig -n %{_libdir}/gaim


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING doc/CREDITS doc/FAQ doc/the_penguin.txt NEWS README
%doc ChangeLog doc/gaims_funniest_home_convos.txt doc/PERL-HOWTO.dox HACKING
#%{_sysconfdir}/gaim/
%{_bindir}/gaim*
%{_includedir}/gaim/
%dir %{_libdir}/gaim/
%exclude %{_libdir}/libgaim-remote.la
%{_libdir}/libgaim-remote.so*
%exclude %{_libdir}/gaim/*.la
%{_libdir}/gaim/*.so
%{_datadir}/applications/gaim.desktop
%{_datadir}/pixmaps/gaim.png
%{_datadir}/pixmaps/gaim/
%{_datadir}/sounds/gaim/
%{_mandir}/man1/gaim*.1*
%{_libdir}/pkgconfig/gaim.pc

%if %{!?_without_perl:1}0
%{perl_vendorarch}/Gaim.pm
%{perl_vendorarch}/auto/Gaim/
%{perl_vendorman3dir}/*
%exclude %{perl_archlib}
%endif

%changelog
* Fri Mar 17 2006 Dag Wieers <dag@wieers.com> - 1.5.0-0.2
- Provide gaim-devel as well.

* Tue Sep 06 2005 Dag Wieers <dag@wieers.com> - 1.5.0-0.1
- Updated to release 1.5.0.

* Sat Jun 11 2005 Dag Wieers <dag@wieers.com> - 1.3.1-0.1
- Updated to release 1.3.1.

* Mon Apr 04 2005 Dag Wieers <dag@wieers.com> - 1.2.1-0
- Updated to release 1.2.1.

* Tue Mar 22 2005 Dag Wieers <dag@wieers.com> - 1.2.0-0
- Updated to release 1.2.0, keep release 0.

* Sun Mar 06 2005 Dag Wieers <dag@wieers.com> - 1.1.4-1
- Updated to release 1.1.4.

* Sat Feb 26 2005 Dag Wieers <dag@wieers.com> - 1.1.3-1
- Updated to release 1.1.3.

* Fri Jan 21 2005 Dag Wieers <dag@wieers.com> - 1.1.2-1
- Updated to release 1.1.2.

* Wed Jan 19 2005 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Re-enabled perl support. (Chris Weyl)
- Updated to release 1.1.1.

* Wed Nov 17 2004 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Updated to release 1.0.3.

* Sun Oct 31 2004 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Sun Oct 17 2004 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Sun Aug 29 2004 Dag Wieers <dag@wieers.com> - 0.82.1-1
- Updated to release 0.82.1.

* Fri Aug 27 2004 Dag Wieers <dag@wieers.com> - 0.82-1
- Updated to release 0.82.

* Sat Aug 07 2004 Dag Wieers <dag@wieers.com> - 0.81-1
- Updated to release 0.81.

* Sun Jul 24 2004 Dag Wieers <dag@wieers.com> - 0.80-2
- Removed .la files.

* Mon Jul 19 2004 Dag Wieers <dag@wieers.com> - 0.80-1
- Updated to release 0.80.

* Fri Apr 30 2004 Matthias Saou <http://freshrpms.net/> 0.77-1
- Update to 0.77.

* Fri Apr  2 2004 Matthias Saou <http://freshrpms.net/> 0.76-1
- Update to 0.76.

* Mon Feb  2 2004 Matthias Saou <http://freshrpms.net/> 0.75-2
- Include latest security patch to fix potential vulnerabilities.

* Sun Jan 11 2004 Matthias Saou <http://freshrpms.net/> 0.75-1
- Update to 0.75.
- Updated the desktop patch.

* Fri Dec 12 2003 Matthias Saou <http://freshrpms.net/> 0.74-3
- Rebuild now that mach seems to get proper configure paths for X stuff.

* Mon Dec  1 2003 Matthias Saou <http://freshrpms.net/> 0.74-2
- Included changes for the optional perl build from Gary Peck.

* Wed Nov 26 2003 Matthias Saou <http://freshrpms.net/> 0.74-1
- Update to 0.74.

* Mon Nov 24 2003 Matthias Saou <http://freshrpms.net/> 0.73-1
- Update to 0.73.

* Thu Nov  6 2003 Matthias Saou <http://freshrpms.net/> 0.72-1
- Added missing build deps : startup-notification, audiofile, XFree86-devel.

* Mon Nov  3 2003 Matthias Saou <http://freshrpms.net/> 0.72-1
- Update to 0.72.
- Updated the desktop patch.

* Tue Oct 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.71.

* Mon Sep 29 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.70.
- Updated description with a more current list of features.
- Disable tcl/tk bindings by default, "tcltk" conditional build.
- Added libstdc++-devel dependency, thanks to mach.

* Fri Sep 26 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.69.

* Wed Sep  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.68.
- Disable perl module by default.

* Sat Aug 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.67.

* Sat Jul 19 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.66.
- Added explicit library stripping for YDL.

* Thu Jul 17 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.65.
- Added new gaim-remote files.

* Mon Jul 14 2003 Matthias Saou <http://freshrpms.net/>
- Added MSN fix patch.

* Sun Jun  1 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.64.

* Tue May 20 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.63.

* Tue Apr 29 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.62.

* Wed Apr  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.61.

* Sat Apr  5 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.60 final!
- Now rebuild on Red Hat Linux 9.

* Thu Jan 29 2003 Matthias Saou <http://freshrpms.net/>
- Update to 20030131 CVS release.
- Removed the openssl dependencies as the encryption plugin isn't there.
- Put the Epoch tag back to 1 as Red Hat's package has it set.

* Thu Jan 29 2003 Matthias Saou <http://freshrpms.net/>
- Update to 20030129 CVS release.
- Spec file changes and merge of the encryption plugin sub-package.
- Added --with arts rebuild option.

* Mon Jan  20 2003 Warren Togami <warren@togami.com> 20030120.fedora.2
- Add BuildRequires: gtkspell-devel
- CVS update

* Mon Dec  26 2002 Warren Togami <warren@togami.com>
- Updated to latest CVS
- Package for Fedora

