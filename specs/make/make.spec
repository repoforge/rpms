# $Id$
# Authority: dag

### This package replaces base packages
# Tag: rfb

### This package has been imported from RHEL6 beta2 (but same version is in RHEL5)
# ExclusiveDist: el2 el3 el4

# -*- coding: utf-8 -*-
Summary: A GNU tool which simplifies the build process for users
Name: make
Epoch: 1
Version: 3.81
Release: 0.18.1%{?dist}
License: GPLv2+
Group: Development/Tools
URL: http://www.gnu.org/software/make/

Source: ftp://ftp.gnu.org/gnu/make/make-%{version}.tar.bz2
Patch0: make-3.79.1-noclock_gettime.patch
Patch4: make-3.80-j8k.patch
Patch5: make-3.80-getcwd.patch
Patch6: make-3.81-err-reporting.patch
Patch7: make-3.81-memory.patch
Patch8: make-3.81-rlimit.patch
Patch9: make-3.81-newlines.patch
Patch10: make-3.81-jobserver.patch
Patch11: make-3.81-fdleak.patch
Patch12: make-3.81-strcpy-overlap.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description
A GNU tool for controlling the generation of executables and other
non-source files of a program from the program's source files. Make
allows users to build and install packages without any significant
knowledge about the details of the build process. The details about
how the program should be built are provided for make in the program's
makefile.

%prep
%setup -q
%patch0 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p0

%build
%configure
make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=$RPM_BUILD_ROOT install
ln -sf make ${RPM_BUILD_ROOT}/%{_bindir}/gmake
ln -sf make.1 ${RPM_BUILD_ROOT}/%{_mandir}/man1/gmake.1
rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir

%find_lang %name

%check
echo ============TESTING===============
/usr/bin/env LANG=C make check
echo ============END TESTING===========

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
if [ -f %{_infodir}/make.info.gz ]; then # for --excludedocs
   /sbin/install-info %{_infodir}/make.info.gz %{_infodir}/dir --entry="* Make: (make).                 The GNU make utility." || :
fi

%preun
if [ $1 = 0 ]; then
   if [ -f %{_infodir}/make.info.gz ]; then # for --excludedocs
      /sbin/install-info --delete %{_infodir}/make.info.gz %{_infodir}/dir --entry="* Make: (make).                 The GNU make utility." || :
   fi
fi

%files  -f %{name}.lang
%defattr(-,root,root)
%doc NEWS README COPYING AUTHORS
%{_bindir}/*
%{_mandir}/man*/*
%{_infodir}/*.info*

%changelog
* Thu Aug 12 2010 Dag Wieers <dag@wieers.com> - 1:3.81-0.18.1
- Imported from RHEL6 beta2.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1:3.81-18.1
- Rebuilt for RHEL 6

* Tue Aug 11 2009 Petr Machata <pmachata@redhat.com> - 1:3.81-18
- Fix installation with --excludedocs
- Resolves: #515917

* Fri Jul 31 2009 Petr Machata <pmachata@redhat.com> - 1:3.81-17
- Replace the use of strcpy on overlapping areas with memmove
- Resolves: #514721

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.81-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.81-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 22 2008 Petr Machata <pmachata@redhat.com> - 1:3.81-14
- Fix patches to apply cleanly with fuzz=0

* Tue Sep 16 2008 Petr Machata <pmachata@redhat.com> - 1:3.81-13
- Mark opened files as cloexec to prevent their leaking through fork
- Resolves: #462090

* Tue Mar 25 2008 Petr Machata <pmachata@redhat.com> - 1:3.81-12
- Fix the rlimit patch.  The success flag is kept in memory shared
  with parent process after vfork, and so cannot be reset.
- Related: #214033

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:3.81-11
- Autorebuild for GCC 4.3

* Thu Oct  4 2007 Petr Machata <pmachata@redhat.com> - 1:3.81-10
- Fix parallel builds with reexec.
- Related: #212111, #211290

* Thu Oct  4 2007 Petr Machata <pmachata@redhat.com> - 1:3.81-8
- Cleaned up per merge review.
- Related: #226120

* Thu Aug 16 2007 Petr Machata <pmachata@redhat.com> - 1:3.81-7
- Fix licensing tag.

* Fri Mar 16 2007 Petr Machata <pmachata@redhat.com> - 1:3.81-6
- Always run testsuite with C locale.
- Resolves: #232607

* Thu Feb 22 2007 Petr Machata <pmachata@redhat.com> - 1:3.81-5
- Fix newline handling for quoted SHELL.
- Resolves: #219409

* Fri Feb  2 2007 Petr Machata <pmachata@redhat.com> - 1:3.81-4
- Tidy up the specfile per rpmlint comments
- Use utf-8 and fix national characters in contributor's names

* Thu Jan 25 2007 Petr Machata <pmachata@redhat.com> - 1:3.81-3
- Ville Skyttä: patch for non-failing %%post, %%preun
- Resolves: #223709

* Thu Jan 25 2007 Petr Machata <pmachata@redhat.com> - 1:3.81-2
- make now restores rlimit to its original values before launching
  subprocess (#214033)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:3.81-1.1
- rebuild

* Tue May 23 2006 Petr Machata <pmachata@redhat.com> - 1:3.81-1
- Upstream 3.81:
  - Contains several backwards incompatible changes.  See NEWS inside
    the source package to find out more.
- memory patch and error reporting patch were ported to this version.

* Wed Mar 15 2006 Petr Machata <pmachata@redhat.com> 1:3.80-11
- Applied (five years old) patch from Jonathan Kamens to allow make to
  handle several pattern-specific variables (#52962).

  The patch was changed so that it forces make to process pattern
  specific variables in the same order as they appear in file.
  (Upstream make behaves this way, too.)  This is change from old make
  behavior, which processed the variables in reverse order.  In case
  you used only x=a assignments, this had the effect of using the
  first pattern specific variable that matched.  For x+=a this just
  doesn't work, and it produces absolutely nonintuitive results.

- (It would be great if make's target-specific variables were handled
  the same way as pattern-specific ones, just without the pattern
  component.  However current handling is documented and considered a
  feature.)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:3.80-10.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:3.80-10.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Feb 02 2006 Petr Machata <pmachata@redhat.com> 3.80-10
- H.J. Lu caught a typo in the patch and provided a new one. (#175376)

* Mon Jan 09 2006 Petr Machata <pmachata@redhat.com> 3.80-9
- Applied patch from H.J. Lu.  Somehow reduces make's enormous memory
  consumption. (#175376)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Aug 22 2005 Jakub Jelinek <jakub@redhat.com> 3.80-8
- make sure errno for error reporting is not lost accross _() calls
- report EOF on read pipe differently from read returning < 0 reporting

* Mon Mar  7 2005 Jakub Jelinek <jakub@redhat.com> 3.80-7
- rebuilt with GCC 4

* Mon Dec 13 2004 Jakub Jelinek <jakub@redhat.com> 3.80-6
- refuse -jN where N is bigger than PIPE_BUF (#142691, #17374)

* Thu Oct  7 2004 Jakub Jelinek <jakub@redhat.com> 3.80-5
- add URL rpm tag (#134799)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Dec 02 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add important bug-fixes from make home-page

* Sun Nov 30 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 3.80

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Sun Dec 29 2002 Tim Powers <timp@redhat.com>
- fix references to %%install in the changelog so that the package will build

* Tue Dec 03 2002 Elliot Lee <sopwith@redhat.com> 3.79.1-15
- _smp_mflags
- Fix ppc build (sys_siglist issues in patch2)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Jakub Jelinek <jakub@redhat.com>
- Run make check during build

* Thu May 23 2002 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix build with current auto* tools

* Fri Jan 25 2002 Jakub Jelinek <jakub@redhat.com>
- rebuilt with gcc 3.1

* Fri Jul  6 2001 Trond Eivind Glomsrød <teg@redhat.com>
- s/Copyright/License/
- langify
- Make sure it isn't setgid if built as root

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Mon Aug  7 2000 Tim Waugh <twaugh@redhat.com>
- change info-dir entry so that 'info make' works (#15029).

* Tue Aug  1 2000 Jakub Jelinek <jakub@redhat.com>
- assume we don't have clock_gettime in configure, so that
  make is not linked against -lpthread (and thus does not
  limit stack to 2MB).

* Sat Jul 22 2000 Jeff Johnson <jbj@redhat.com>
- add locale files (#14362).

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sat Jun 24 2000 Preston Brown <pbrown@redhat.com>
- 3.79.1 bugfix release

* Mon Jun  5 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Sun May  7 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix build for some odd situations, such as
  - previously installed make != GNU make
  - /bin/sh != bash

* Mon Apr 17 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- update to 3.79

* Thu Feb 24 2000 Cristian Gafton <gafton@redhat.com>
- add patch from Andreas Jaeger to fix dtype lookups (for glibc 2.1.3
  builds)

* Mon Feb  7 2000 Jeff Johnson <jbj@redhat.com>
- compress man page.

* Fri Jan 21 2000 Cristian Gafton <gafton@redhat.com>
- apply patch to fix a /tmp race condition from Thomas Biege
- simplify %%install

* Sat Nov 27 1999 Jeff Johnson <jbj@redhat.com>
- update to 3.78.1.

* Thu Apr 15 1999 Bill Nottingham <notting@redhat.com>
- added a serial tag so it upgrades right

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Wed Sep 16 1998 Cristian Gafton <gafton@redhat.com>
- added a patch for large file support in glob
 
* Tue Aug 18 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.77

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 16 1997 Donnie Barnes <djb@redhat.com>
- udpated from 3.75 to 3.76
- various spec file cleanups
- added install-info support

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
