# $Id$
# Authority: dag

### This package replaces base packages
# Tag: rfb

### This package has been imported from RHEL6 beta2
# ExclusiveDist: el2 el3 el4 el5

Summary: A tool for creating scanners (text pattern recognizers)
Name: flex
Version: 2.5.35
Release: 0.8%{?dist}
License: BSD
Group: Development/Tools
URL: http://flex.sourceforge.net/

Source: http://dl.sf.net/flex/flex-%{version}.tar.bz2
Patch0: flex-2.5.35-sign.patch
Patch1: flex-2.5.35-hardening.patch
Patch2: flex-2.5.35-gcc44.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison
BuildRequires: gettext
BuildRequires: m4
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
Requires: m4

%description
The flex program generates scanners.  Scanners are programs which can
recognize lexical patterns in text.  Flex takes pairs of regular
expressions and C code as input and generates a C source file as
output.  The output file is compiled and linked with a library to
produce an executable.  The executable searches through its input for
occurrences of the regular expressions.  When a match is found, it
executes the corresponding C code.  Flex was designed to work with
both Yacc and Bison, and is used by many programs as part of their
build process.

You should install flex if you are going to use your system for
application development.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure --disable-dependency-tracking CFLAGS="-fPIC $RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

( cd ${RPM_BUILD_ROOT}
  ln -sf flex .%{_bindir}/lex
  ln -sf flex .%{_bindir}/flex++
  ln -s flex.1 .%{_mandir}/man1/lex.1
  ln -s flex.1 .%{_mandir}/man1/flex++.1
  ln -s libfl.a .%{_libdir}/libl.a
)

%find_lang flex

%post
if [ -f %{_infodir}/flex.info.gz ]; then # for --excludedocs
   /sbin/install-info %{_infodir}/flex.info.gz --dir-file=%{_infodir}/dir ||:
fi

%preun
if [ $1 = 0 ]; then
    if [ -f %{_infodir}/flex.info.gz ]; then # for --excludedocs
	/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir ||:
    fi
fi

%check
echo ============TESTING===============
make check
echo ============END TESTING===========

%clean
rm -rf ${RPM_BUILD_ROOT}

%files -f flex.lang
%defattr(-,root,root)
%doc COPYING NEWS README
%{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/*.a
%{_includedir}/FlexLexer.h
%{_infodir}/flex.info*

%changelog
* Thu Aug 12 2010 Dag Wieers <dag@wieers.com> - 2.5.35-0.8
- Imported from RHEL6 beta2.

* Tue Jan 12 2010 Petr Machata <pmachata@redhat.com> - 2.5.35-8
- Add source URL
- Related: #543948

* Mon Aug 24 2009 Petr Machata <pmachata@redhat.com> - 2.5.35-7
- Fix installation with --excludedocs
- Resolves: #515928

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.35-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 20 2009 Debarshi Ray <rishi@fedoraproject.org> - 2.5.35-5
- Resolves: #496548.

* Mon Apr 20 2009 Petr Machata <pmachata@redhat.com> - 2.5.35-4
- Get rid of warning caused by ignoring return value of fwrite() in
  ECHO macro.  Debian patch.
- Resolves: #484961

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon May 12 2008 Petr Machata <pmachata@redhat.com> - 2.5.35-2
- Resolves: #445950

* Wed Feb 27 2008 Petr Machata <pmachata@redhat.com> - 2.5.35-1
- Rebase to 2.5.35. Drop two patches.
- Resolves: #434961
- Resolves: #435047

* Mon Feb 25 2008 Petr Machata <pmachata@redhat.com> - 2.5.34-1
- Rebase to 2.5.34. Drop five patches.
- Resolves: #434676

* Mon Feb 11 2008 Petr Machata <pmachata@redhat.com> - 2.5.33-17
- Generate prototypes for accessor functions.  Upstream patch.
- Related: #432203

* Mon Feb  4 2008 Petr Machata <pmachata@redhat.com> - 2.5.33-16
- Fix comparison between signed and unsigned in generated scanner.
  Patch by Roland McGrath.
- Resolves: #431151

* Tue Jan 15 2008 Stepan Kasal <skasal@redhat.com> - 2.5.33-15
- Do not run autogen.sh, it undoes the effect of includedir patch.
- Adapt test-linedir-r.patch so that it fixes Makefile.in and works
  even though autogen.sh is not run.

* Thu Jan 10 2008 Stepan Kasal <skasal@redhat.com> - 2.5.33-14
- Insert the "-fPIC" on configure command-line.
- Drop the -fPIC patch.

* Tue Jan  8 2008 Petr Machata <pmachata@redhat.com> - 2.5.33-13
- Patch with -fPIC only after the autogen.sh is run.

* Thu Jan  3 2008 Petr Machata <pmachata@redhat.com> - 2.5.33-12
- Run autogen.sh before the rest of the build.
- Add BR autoconf automake gettext-devel.

* Thu Aug 30 2007 Petr Machata <pmachata@redhat.com> - 2.5.33-11
- Add BR gawk
- Fix use of awk in one of the tests

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 2.5.33-10
- Rebuild for selinux ppc32 issue.

* Fri Jun 22 2007 Petr Machata <pmachata@redhat.com> - 2.5.33-9
- Remove wrong use of @includedir@ in Makefile.in.
- Spec cleanups.
- Related: #225758

* Fri Jun 22 2007 Petr Machata <pmachata@redhat.com> - 2.5.33-8
- Don't emit yy-prefixed variables in C++ mode.  Thanks Srinivas Aji.
- Related: #242742
- Related: #244259

* Fri May 11 2007 Petr Machata <pmachata@redhat.com> - 2.5.33-7
- Allow joining short options into one commandline argument.
- Resolves: #239695

* Fri Mar 30 2007 Petr Machata <pmachata@redhat.com> - 2.5.33-5
- Make yy-prefixed variables available to scanner even with -P.

* Fri Feb  2 2007 Petr Machata <pmachata@redhat.com> - 2.5.33-4
- Use %%find_lang to package locale files.

* Wed Jan 31 2007 Petr Machata <pmachata@redhat.com> - 2.5.33-3
- Compile with -fPIC.

* Tue Jan 30 2007 Petr Machata <pmachata@redaht.com> - 2.5.33-2
- Add Requires:m4.

* Fri Jan 19 2007 Petr Machata <pmachata@redhat.com> - 2.5.33-1
- Rebase to 2.5.33

* Tue Jul 18 2006 Petr Machata <pmachata@redhat.com> - 2.5.4a-41
- Reverting posix patch.  Imposing posix because of warning is too
  much of a restriction.

* Sun Jul 16 2006 Petr Machata <pmachata@redhat.com> - 2.5.4a-40
- using dist tag

* Fri Jul 14 2006 Petr Machata <pmachata@redhat.com> - 2.5.4a-39
- fileno is defined in posix standard, so adding #define _POSIX_SOURCE
  to compile without warnings (#195687)
- dropping 183098 test, since the original bug was already resolved

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.5.4a-38.1
- rebuild

* Fri Mar 10 2006 Petr Machata <pmachata@redhat.com> - 2.5.4a-38
- Caught the real cause of #183098.  It failed because the parser
  built with `flex -f' *sometimes* made it into the final package, and
  -f assumes seven-bit tables.  Solution has two steps.  Move `make
  bigcheck' to `%%check' part, where it belongs anyway, so that flexes
  built during `make bigcheck' don't overwrite original build.  And
  change makefile so that `make bigcheck' will *always* execute *all*
  check commands.

* Wed Mar  8 2006 Petr Machata <pmachata@redhat.com> - 2.5.4a-37.4
- adding test for #183098 into build process

* Fri Mar  2 2006 Petr Machata <pmachata@redhat.com> - 2.5.4a-37.3
- rebuilt, no changes inside. In hunt for #183098

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.5.4a-37.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.5.4a-37.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Feb 02 2006 Petr Machata <pmachata@redhat.com> 2.5.4a-37
- adding `make bigcheck' into build process.  Refreshing initscan.c to
  make this possible.

* Wed Jan 18 2006 Petr Machata <pmachata@redhat.com> 2.5.4a-36
- Applying Jonathan S. Shapiro's bugfix-fixing patch. More std:: fixes
  and better way to silent warnings under gcc.

* Fri Jan 13 2006 Petr Machata <pmachata@redhat.com> 2.5.4a-35
- Adding `std::' prefixes, got rid of `using namespace std'. (#115354)
- Dummy use of `yy_flex_realloc' to silent warnings. (#30943)
- Adding URL of flex home page to spec (#142675)

* Sun Dec 18 2005 Jason Vas Dias<jvdias@redhat.com>
- rebuild with 'flex-pic.patch' to enable -pie links
  on x86_64 (patch from Jesse Keating) .

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sun Apr 10 2005 Jakub Jelinek <jakub@redhat.com> 2.5.4a-34
- rebuilt with GCC 4
- add %%check script

* Tue Aug 24 2004 Warren Togami <wtogami@redhat.com> 2.5.4a-33
- #116407 BR byacc

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan  7 2003 Jeff Johnson <jbj@redhat.com> 2.5.4a-28
- don't include -debuginfo files in package.

* Mon Nov  4 2002 Than Ngo <than@redhat.com> 2.5.4a-27
- YY_NO_INPUT patch from Jean Marie

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 18 2002 Than Ngo <than@redhat.com> 2.5.4a-25
- don't forcibly strip binaries

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Apr  2 2002 Than Ngo <than@redhat.com> 2.5.4a-23
- More ISO C++ 98 fixes (#59670)

* Tue Feb 26 2002 Than Ngo <than@redhat.com> 2.5.4a-22
- rebuild in new enviroment

* Wed Feb 20 2002 Bernhard Rosenkraenzer <bero@redhat.com> 2.5.4a-21
- More ISO C++ 98 fixes (#59670)

* Tue Feb 19 2002 Bernhard Rosenkraenzer <bero@redhat.com> 2.5.4a-20
- Fix ISO C++ 98 compliance (#59670)

* Wed Jan 23 2002 Than Ngo <than@redhat.com> 2.5.4a-19
- fixed #58643

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Nov  6 2001 Than Ngo <than@redhat.com> 2.5.4a-17
- fixed for working with gcc 3 (bug #55778)

* Sat Oct 13 2001 Than Ngo <than@redhat.com> 2.5.4a-16
- fix wrong License (bug #54574)

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Sat Sep 30 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix generation of broken code (conflicting isatty() prototype w/ glibc 2.2)
  This broke, among other things, the kdelibs 2.0 build
- Fix source URL

* Thu Sep  7 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging (64bit systems need to use libdir).

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun  6 2000 Bill Nottingham <notting@redhat.com>
- rebuild, FHS stuff.

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages

* Fri Jan 28 2000 Bill Nottingham <notting@redhat.com>
- add a libl.a link to libfl.a

* Wed Aug 25 1999 Jeff Johnson <jbj@redhat.com>
- avoid uninitialized variable warning (Erez Zadok).

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 6)

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- build for 6.0 tree

* Mon Aug 10 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from 2.5.4 to 2.5.4a

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Mar 20 1997 Michael Fulbright <msf@redhat.com>
- Updated to v. 2.5.4
