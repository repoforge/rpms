Summary: A general purpose sound file conversion tool
Name: sox
Version: 14.3.2
Release: 1.{?dist}
License: GPLv2+ and LGPLv2+
Group: Applications/Multimedia
Source: http://prdownloads.sourceforge.net/sox/sox-%{version}.tar.gz
URL: http://sox.sourceforge.net/
BuildRequires: libvorbis-devel
BuildRequires: alsa-lib-devel, libtool-ltdl-devel, libsamplerate-devel
BuildRequires: gsm-devel, wavpack-devel, ladspa-devel, libpng-devel
BuildRequires: flac-devel, libao-devel, libsndfile-devel, libid3tag-devel
BuildRequires: libtool
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
SoX (Sound eXchange) is a sound file format converter SoX can convert
between many different digitized sound formats and perform simple
sound manipulation functions, including sound effects.

%package -n  sox-devel
Summary: The SoX sound file format converter libraries
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description -n sox-devel
This package contains the library needed for compiling applications
which will use the SoX sound file format converter.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64 -fno-strict-aliasing" %configure --with-flac --with-gsm --with-sndfile --with-mp3 --disable-static --includedir=%{_includedir}/sox
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/libsox.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/sox/*.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/sox/*.a


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/play
%{_bindir}/rec
%{_bindir}/sox
%{_bindir}/soxi
%{_libdir}/libsox.so.*
%dir %{_libdir}/sox/
%{_mandir}/man1/*
%{_mandir}/man7/*
#%{_libdir}/sox/libsox_fmt_*.so

%files -n sox-devel
%defattr(-,root,root,-)
%{_includedir}/sox
%{_libdir}/libsox.so
%{_libdir}/pkgconfig/sox.pc
%{_mandir}/man3/*


%changelog
* Mon Nov  7 2011 Mark Janssen <mark@sig-io.nl> - 14.3.2-0
- Rebased to upstream version 14.3.2
- Enabled mp3 support

* Fri Jun 04 2010 Jiri Moskovcak <jmoskovc@redhat.com> - 14.2.0-6
- added -fno-strict-aliasing
- Resolves: #596213

* Fri Feb 26 2010 Jiri Moskovcak <jmoskovc@redhat.com> - 14.2.0-5
- fixed license tag to follow Fedora guidlines
- Related: rhbz#543948

* Fri Feb 26 2010 Jiri Moskovcak <jmoskovc@redhat.com> - 14.2.0-4
- fixed license tag
- Related: rhbz#543948

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 14.2.0-3.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 14.2.0-1
- 14.2.0

* Mon Nov 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 14.1.0-7.20081105cvs
- patch for newer libtool

* Mon Nov 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 14.1.0-6.20081105cvs
- rebuild for libtool

* Wed Nov  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 14.1.0-5.20081105cvs
- forgot to add libtool as a BR

* Wed Nov  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 14.1.0-4.20081105cvs
- update to 20081105 cvs checkout (fixes many bugs, no longer creates _fmt_*.so.*)
- move _fmt_*.so to main package so support for file formats no longer requires devel

* Thu Sep  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> 14.1.0-3
- missed a few BR, this should be all of them

* Thu Sep  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> 14.1.0-2
- enable the full set of functionality with missing BR

* Thu Sep  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> 14.1.0-1
- fix license tag
- update to 14.1.0
- disabled static libs (if something really needs them, re-enable them
  in a -static subpackage)

* Wed Apr 16 2008 Jiri Moskovcak <jmoskovc@redhat.com> - 14.0.1-2
- enabled flac support
- Resolves: #442703

* Mon Feb 25 2008 Jiri Moskovcak <jmoskovc@redhat.com> - 14.0.1-1
- New version 14.0.1

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 14.0.0-2
- Autorebuild for GCC 4.3

* Mon Oct 29 2007 Jiri Moskovcak <jmoskovc@redhat.com> - 14.0.0-1
- New version 14.0.0
- Thanks to Chris Bagwell <chris at cnpbagwell dot com> for initial changes to spec file

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 13.0.0-3
- Rebuild for selinux ppc32 issue.

* Mon Jul 16 2007 Jiri Moskovcak <jmoskovc@redhat.com> 13.0.0-2
- uses external libgsm instead of local copy
- spec file update: added BuildRequires: gsm-devel
- Resolves: #239955

* Mon Feb 26 2007 Thomas Woerner <twoerner@redhat.com> 13.0.0-1
- new version 13.0.0
- spec file cleanup (#227429)
- new ldconfig calls for post and postun

* Mon Jul 24 2006 Thomas Woerner <twoerner@redhat.com> 12.18.1-1
- new version 12.18.1
- fixed multilib devel conflict in libst-config (#192751)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 12.17.9-1.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 12.17.9-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 12.17.9-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Dec 13 2005 Thomas Woerner <twoerner@redhat.com> 12.17.9-1
- new version 12.17.9

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu May 12 2005 Thomas Woerner <twoerner@redhat.com> 12.17.7-3
- fixed bad link for man/man1/rec.1.gz (#154089)
- using /usr/include instead of kernel-devel includes

* Tue Apr 26 2005 Warren Togami <wtogami@redhat.com> 12.17.7-2
- overflow patch (#155224 upstream)

* Sun Apr 17 2005 Warren Togami <wtogami@redhat.com> 12.17.7-1
- 12.17.7
- BR alsa-lib-devel (#155224 thias)

* Sun Feb 27 2005 Florian La Roche <laroche@redhat.com>
- Copyright: -> License:

* Mon Nov 22 2004 Thomas Woerner <twoerner@redhat.com> 12.17.6-1
- new version 12.17.6

* Wed Sep 15 2004 Thomas Woerner <twoerner@redhat.com> 12.17.5-3
- moved libst-config to devel package (#132489)

* Thu Aug 26 2004 Thomas Woerner <twoerner@redhat.com> 12.17.5-2
- fixed initialization bug in wav file handler (#130968)

* Thu Aug 19 2004 Thomas Woerner <twoerner@redhat.com> 12.17.5-1
- new version 12.17.5

* Fri Jul 23 2004 Bill Nottingham <notting@redhat.com> 12.17.4-4.fc2
- add patch for buffer overflow in wav code (CAN-2004-0557, #128158)

* Fri Jul  9 2004 Bill Nottingham <notting@redhat.com> 12.17.4-4
- add patch for 64-bit problem (#127502)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Oct  7 2003 Bill Nottingham <notting@redhat.com> 12.17.4-1
- update to 12.17.4
- ship soxmix (#102499)
- fix soxplay to handle files with spaces (#91144)
- use LFS (#79151)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 21 2003 Elliot Lee <sopwith@redhat.com> 12.17.3-10
- Add sox-vorberr.patch to fix segfault in #81448
- _smp_mflags

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Nov 27 2002 Tim Powers <timp@redhat.com> 12.17.3-8
- remoive unpackaged files from the buildroot
- lib64'ize

* Fri Jul 18 2002 Bill Nottingham <notting@redhat.com>
- build against current libvorbis

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Feb 21 2002 Bill Nottingham <notting@redhat.com>
- rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jan 07 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- do not require gsm-devel as it has been excluded from rawhide

* Fri Jan  4 2002 Bill Nottingham <notting@redhat.com> 12.17.3-1
- update to 12.17.3

* Wed Dec  4 2001 Bill Nottingham <notting@redhat.com>
- update to 12.17.2

* Thu Aug  9 2001 Bill Nottingham <notting@redhat.com>
- add patch to fix recording (#41755)
- fix license (#50574)

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Tue Jan  9 2001 Bill Nottingham <notting@redhat.com>
- rebuild against new gsm-devel

* Tue Jan  2 2001 Bill Nottingham <notting@redhat.com>
- re-enable gsm stuff
- update to 12.17.1

* Fri Dec 01 2000 Bill Nottingham <notting@redhat.com>
- rebuild because of broken fileutils

* Mon Nov 13 2000 Bill Nottingham <notting@redhat.com>
- update to 12.17
- yank out gsm stuff

* Tue Aug  7 2000 Bill Nottingham <notting@redhat.com>
- fix playing of sounds on cards that don't support mono

* Sat Aug  5 2000 Bill Nottingham <notting@redhat.com>
- fix playing of sounds on cards that don't support 8-bit

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Feb 03 2000 Bill Nottingham <notting@redhat.com>
- fix manpage link the Right Way(tm)

* Thu Feb 03 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix rec manpage link - now that man pages are compressed, it should point to
  play.1.gz, not play.1

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description

* Tue Sep 28 1999 Bill Nottingham <notting@redhat.com>
- Grrr. Arrrrgh. Fix link.

* Fri Sep 24 1999 Bill Nottingham <notting@redhat.com>
- add some more files to devel

* Fri Sep 17 1999 Bill Nottingham <notting@redhat.com>
- fix link

* Fri Jul 30 1999 Bill Nottingham <notting@redhat.com>
- update to 12.16

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Wed Jan 20 1999 Bill Nottingham <notting@redhat.com>
- allow spaces in filenames for play/rec

* Wed Dec  9 1998 Bill Nottingham <notting@redhat.com>
- fix docs

* Mon Nov 23 1998 Bill Nottingham <notting@redhat.com>
- update to 12.15

* Sat Oct 10 1998 Michael Maher <mike@redhat.com>
- fixed broken spec file

* Mon Jul 13 1998 Michael Maher <mike@redhat.com>
- updated source from Chris Bagwell.

* Wed Jun 23 1998 Michael Maher <mike@redhat.com>
- made patch to fix the '-e' option. BUG 580
- added buildroot

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Nov 06 1997 Erik Troan <ewt@redhat.com>
- built against glibc
