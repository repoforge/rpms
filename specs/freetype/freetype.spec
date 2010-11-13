# $Id$
# Authority: avi

### EL6 ships with freetype-2.3.11-6.el6_0.1
### EL5 ships with freetype-2.2.1-28.el5_5
### EL4 ships with freetype-2.1.9-17.el4.8
### EL3 ships with freetype-2.1.4-18.el3
### EL2 ships with freetype-2.0.3-15.el21
# Tag: rfx
# VerbatimSource: redhat

# Disables freetype 1 and 2 bytecode interpreter.  Setting to 0 enables
# the bytecode interpreter in both freetype 1 and 2.
%define without_bytecode_interpreter    1

%define with_freetype1	1

%define ft1 freetype-pre1.4

%{!?with_xfree86:%define with_xfree86 1}

Summary: Free and portable TrueType font rendering engine.
Name: freetype
Version: 2.1.9
Release: 1.2%{?dist}
License: BSD/GPL dual license
Group: System Environment/Libraries
URL: http://www.freetype.org
Source:  http://dl.sf.net/freetype/freetype-%{version}.tar.bz2
Source1: http://dl.sf.net/freetype/ftdocs-%{version}.tar.bz2
Source2: http://dl.sf.net/freetype/ft2demos-%{version}.tar.bz2
Source3: %{ft1}.tar.bz2

# Fix build of freetype-1.4 with gcc 3.3
Patch3: freetype-1.4-ac25.patch
Patch4: freetype-1.4-gcc33.patch
# Add -lm when linking X demos
Patch5: ft2demos-2.1.9-mathlib.patch
Patch20:  freetype-2.1.3-enable-ft2-bci.patch
Patch21:  freetype-1.4-disable-ft1-bci.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: automake autoconf >= 2.59 libtool symlinks zlib-devel

%description
The FreeType engine is a free and portable TrueType font rendering
engine, developed to provide TrueType support for a variety of
platforms and environments. FreeType is a library which can open and
manages font files as well as efficiently load, hint and render
individual glyphs. FreeType is not a font server or a complete
text-rendering library.


%if %{with_freetype1}
%package utils
Summary: Collection of FreeType utilities.
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description utils
The FreeType engine is a free and portable TrueType font rendering
engine, developed to provide TrueType support for a variety of
platforms and environments. FreeType is a library which can open and
manages font files as well as efficiently load, hint and render
individual glyphs. FreeType is not a font server or a complete
text-rendering library.
%endif

%package demos
Summary: Collection of FreeType demos.
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description demos
The FreeType engine is a free and portable TrueType font rendering
engine, developed to provide TrueType support for a variety of
platforms and environments. FreeType is a library which can open and
manages font files as well as efficiently load, hint and render
individual glyphs. FreeType is not a font server or a complete
text-rendering library.


%package devel
Summary: FreeType development libraries and header files
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: zlib-devel

%description devel
The FreeType engine is a free and portable TrueType font rendering
engine, developed to provide TrueType support for a variety of
platforms and environments. FreeType is a library which can open and
manages font files as well as efficiently load, hint and render
individual glyphs. FreeType is not a font server or a complete
text-rendering library.


%prep
%setup -q -b 1 -a 2 -a 3

%if %{with_freetype1}
pushd %{ft1}
%patch3   -p1 -b .ac25
%patch4   -p1 -b .gcc33

%if %{without_bytecode_interpreter}
%patch21  -p1 -b .disable-ft1-bci
%endif
popd
%endif

pushd ft2demos-%{version}
%patch5 -p1 -b .mathlib
popd

%if ! %{without_bytecode_interpreter}
%patch20  -p0 -b .enable-ft2-bci
%endif

# Need to update libtool to get deplibs right for x86_64
pushd builds/unix
libtoolize --force
aclocal
autoconf
popd

pushd %{ft1}
libtoolize --force
aclocal
autoconf
popd

%build
# Work around code generation problem with strict-aliasing
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=118021
#
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"

# Build Freetype 2
{
  %configure
  make %{?_smp_mflags}
}

%if %{with_freetype1}
# Build Freetype 1.4
{
  pushd %{ft1}
  %configure --disable-debug --enable-static --enable-shared \
             --with-locale-dir=%{_datadir}/locale
  make X11_LIB=/usr/X11R6/%{_lib}

  # Absolute symlinks in the debug output break debuginfo,
  # so use 'symlinks' to relativize and shorten; takes
  # two passes because 'symlinks' is stupid.
  symlinks -r -c . > /dev/null
  symlinks -r -s -c . > /dev/null

  popd
}
%endif

%if %{with_xfree86}
# Build freetype 2 demos
{
  pushd ft2demos-%{version}
  make X11_LIB=/usr/X11R6/%{_lib} X11_PATH="/usr/X11R6" TOP_DIR=".."
  popd
}
%endif

%install
%{__rm} -rf %{buildroot}


# Install Freetype 2
%makeinstall gnulocaledir=$RPM_BUILD_ROOT%{_datadir}/locale

%if %{with_freetype1}
# Install Freetype 1
{
  pushd %{ft1}
  %makeinstall gnulocaledir=$RPM_BUILD_ROOT%{_datadir}/locale
  libtool --finish $RPM_BUILD_ROOT%{_libdir}
  popd
}
%endif
%if %{with_freetype1}
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/freetype1
mv $RPM_BUILD_ROOT/%{_includedir}/freetype $RPM_BUILD_ROOT/%{_includedir}/freetype1
%endif

%if %{with_xfree86}
# Install freetype 2 demos
{
  for ftdemo in ftdump ftlint ftmemchk ftmulti ftstring fttimer ftview ;do
      libtool install -m 755 ft2demos-%{version}/bin/$ftdemo $RPM_BUILD_ROOT/%{_bindir}
  done
}
%endif
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%triggerpostun -- freetype < 2.0.5-3
{
  # ttmkfdir updated - as of 2.0.5-3, on upgrades we need xfs to regenerate
  # things to get the iso10646-1 encoding listed.
  for I in %{_datadir}/fonts/*/TrueType /usr/X11R6/lib/X11/fonts/TrueType; do
      [ -d $I ] && [ -f $I/fonts.scale ] && [ -f $I/fonts.dir ] && touch $I/fonts.scale
  done
  exit 0
}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%{_libdir}/libfreetype.so.*
%doc ChangeLog README
%if %{with_freetype1}
%{_libdir}/libttf.so.*
%doc %{ft1}/README %{ft1}/announce docs
%endif

%if %{with_freetype1}
%files utils
%defattr(-, root, root, 0755)
# 2.0.4 version included in demos package now
#%{_bindir}/ftdump
# 2.0.4 version included in demos package now
#%{_bindir}/ftlint
%{_bindir}/fterror
%{_bindir}/ftmetric
%{_bindir}/ftsbit
%{_bindir}/ftstrpnm
%endif

%files demos
%defattr(-, root, root, 0755)
%{_bindir}/ftdump
%{_bindir}/ftlint
%if %{with_xfree86}
%{_bindir}/ftmemchk
%{_bindir}/ftmulti
%{_bindir}/ftstring
%{_bindir}/fttimer
%{_bindir}/ftview
%endif

%files devel
%defattr(-, root, root, 0755)
%if %{with_freetype1}
%dir %{_includedir}/freetype1
%{_includedir}/freetype1/*
%endif
%dir %{_includedir}/freetype2
%{_datadir}/aclocal/freetype2.m4
%{_includedir}/freetype2/*
%{_includedir}/*.h
%if %{with_freetype1}
%{_libdir}/libttf.a
%{_libdir}/libttf.la
%{_libdir}/libttf.so
%endif
%{_libdir}/libfreetype.a
%{_libdir}/libfreetype.la
%{_libdir}/libfreetype.so
%{_bindir}/freetype-config
%{_libdir}/pkgconfig/

%changelog
* Sat Jun 04 2005 Avi Alkalay <avibrazil@gmail.com> - 2.1.9-1.2
- Undo bytecode interpreter.

* Tue May 31 2005 Avi Alkalay <avibrazil@gmail.com> - 2.1.9-1
- Enabled bytecode interpreter for better screen font rendering.

* Wed Aug  4 2004 Owen Taylor <otaylor@redhat.com> - 2.1.9-1
- Upgrade to 2.1.9
- Since we are just using automake for aclocal, use it unversioned,
  instead of specifying 1.4.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Apr 19 2004 Owen Taylor <otaylor@redhat.com> 2.1.7-4
- Add patch from freetype CVS to fix problem with eexec (#117743)
- Add freetype-devel to buildrequires and -devel requires
  (Maxim Dzumanenko, #111108)

* Wed Mar 10 2004 Mike A. Harris <mharris@redhat.com> 2.1.7-3
- Added -fno-strict-aliasing to CFLAGS and CXXFLAGS to try to fix SEGV and
  SIGILL crashes in mkfontscale which have been traced into freetype and seem
  to be caused by aliasing issues in freetype macros (#118021)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com> 2.1.7-2.1
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com> 2.1.7-2
- rebuilt

* Fri Jan 23 2004 Owen Taylor <otaylor@redhat.com> 2.1.7-1
- Upgrade to 2.1.7

* Tue Sep 23 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- allow compiling without the demos as that requires XFree86
  (this allows bootstrapping XFree86 on new archs)

* Fri Aug  8 2003 Elliot Lee <sopwith@redhat.com> 2.1.4-4.1
- Rebuilt

* Tue Jul  8 2003 Owen Taylor <otaylor@redhat.com> 2.1.4-4.0
- Bump for rebuild

* Wed Jun 25 2003 Owen Taylor <otaylor@redhat.com> 2.1.4-3
- Fix crash with non-format-0 hdmx tables (found by David Woodhouse)

* Mon Jun  9 2003 Owen Taylor <otaylor@redhat.com> 2.1.4-1
- Version 2.1.4
- Relibtoolize to get deplibs right for x86_64
- Use autoconf-2.5x for freetype-1.4 to fix libtool-1.5 compat problem (#91781)
- Relativize absolute symlinks to fix the -debuginfo package
  (#83521, Mike Harris)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 22 2003 Jeremy Katz <katzj@redhat.com> 2.1.3-9
- fix build with gcc 3.3

* Tue Feb 25 2003 Owen Taylor <otaylor@redhat.com>
- Add a memleak fix for the gzip backend from Federic Crozat

* Thu Feb 13 2003 Elliot Lee <sopwith@redhat.com> 2.1.3-7
- Run libtoolize/aclocal/autoconf so that libtool knows to generate shared libraries
  on ppc64.
- Use _smp_mflags (for freetype 2.x only)

* Tue Feb  4 2003 Owen Taylor <otaylor@redhat.com>
- Switch to using %%configure (should fix #82330)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jan  6 2003 Owen Taylor <otaylor@redhat.com> 2.1.3-4
- Make FreeType robust against corrupt fonts with recursive composite
  glyphs (#74782, James Antill)

* Thu Jan  2 2003 Owen Taylor <otaylor@redhat.com> 2.1.3-3
- Add a patch to implement FT_LOAD_TARGET_LIGHT
- Fix up freetype-1.4-libtool.patch

* Sat Dec 12 2002 Mike A. Harris <mharris@redhat.com> 2.1.3-2
- Update to freetype 2.1.3
- Removed ttmkfdir sources and patches, as they have been moved from the
  freetype packaging to XFree86 packaging, and now to the ttmkfdir package
- Removed patches that are now included in 2.1.3:
  freetype-2.1.1-primaryhints.patch, freetype-2.1.2-slighthint.patch,
  freetype-2.1.2-bluefuzz.patch, freetype-2.1.2-stdw.patch,
  freetype-2.1.2-transform.patch, freetype-2.1.2-autohint.patch,
  freetype-2.1.2-leftright.patch
- Conditionalized inclusion of freetype 1.4 library.

* Wed Dec 04 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- disable perl, it is not used at all

* Tue Dec 03 2002 Elliot Lee <sopwith@redhat.com> 2.1.2-11
- Instead of removing unpackaged file, include it in the package.

* Sat Nov 30 2002 Mike A. Harris <mharris@redhat.com> 2.1.2-10
- Attempted to fix lib64 issue in freetype-demos build with X11_LINKLIBS
- Cleaned up various _foodir macros throughtout specfile
- Removed with_ttmkfdir build option as it is way obsolete

* Fri Nov 29 2002 Tim Powers <timp@redhat.com> 2.1.2-8
- remove unpackaged files from the buildroot

* Wed Aug 28 2002 Owen Taylor <otaylor@redhat.com>
- Fix a bug with PCF metrics

* Fri Aug  9 2002 Owen Taylor <otaylor@redhat.com>
- Backport autohinter improvements from CVS

* Tue Jul 23 2002 Owen Taylor <otaylor@redhat.com>
- Fix from CVS for transformations (#68964)

* Tue Jul  9 2002 Owen Taylor <otaylor@redhat.com>
- Add another bugfix for the postscript hinter

* Mon Jul  8 2002 Owen Taylor <otaylor@redhat.com>
- Add support for BlueFuzz private dict value, fixing rendering
  glitch for Luxi Mono.

* Wed Jul  3 2002 Owen Taylor <otaylor@redhat.com>
- Add an experimental FT_Set_Hint_Flags() call

* Mon Jul  1 2002 Owen Taylor <otaylor@redhat.com>
- Update to 2.1.2
- Add a patch fixing freetype PS hinter bug

* Fri Jun 21 2002 Mike A. Harris <mharris@redhat.com> 2.1.1-2
- Added ft rpm build time conditionalizations upon user requests

* Tue Jun 11 2002 Owen Taylor <otaylor@redhat.com> 2.1.1-1
- Version 2.1.1

* Mon Jun 10 2002 Owen Taylor <otaylor@redhat.com>
- Add a fix for PCF character maps

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri May 17 2002 Mike A. Harris <mharris@redhat.com> 2.1.0-2
- Updated freetype to version 2.1.0
- Added libtool fix for freetype 1.4 (#64631)

* Wed Mar 27 2002 Nalin Dahyabhai <nalin@redhat.com> 2.0.9-2
- use "libtool install" instead of "install" to install some binaries (#62005)

* Mon Mar 11 2002 Mike A. Harris <mharris@redhat.com> 2.0.9-1
- Updated to freetype 2.0.9

* Sun Feb 24 2002 Mike A. Harris <mharris@redhat.com> 2.0.8-4
- Added proper docs+demos source for 2.0.8.

* Sat Feb 23 2002 Mike A. Harris <mharris@redhat.com> 2.0.8-3
- Added compat patch so 2.x works more like 1.x
- Rebuilt with new build toolchain

* Fri Feb 22 2002 Mike A. Harris <mharris@redhat.com> 2.0.8-2
- Updated to freetype 2.0.8, however docs and demos are stuck at 2.0.7
  on the freetype website.  Munged specfile to deal with the problem by using
  {oldversion} instead of version where appropriate.  <sigh>

* Sat Feb  2 2002 Tim Powers <timp@redhat.com> 2.0.6-3
- bumping release so that we don't collide with another build of
  freetype, make sure to change the release requirement in the XFree86
  package

* Fri Feb  1 2002 Mike A. Harris <mharris@redhat.com> 2.0.6-2
- Made ttmkfdir inclusion conditional, and set up a define to include
  ttmkfdir in RHL 7.x builds, since ttmkfdir is now moving to the new
  XFree86-font-utils package.

* Wed Jan 16 2002 Mike A. Harris <mharris@redhat.com> 2.0.6-1
- Updated freetype to version 2.0.6

* Wed Jan 09 2002 Tim Powers <timp@redhat.com> 2.0.5-4
- automated rebuild

* Fri Nov 30 2001 Elliot Lee <sopwith@redhat.com> 2.0.5-3
- Fix bug #56901 (ttmkfdir needed to list Unicode encoding when generating
  font list). (ttmkfdir-iso10646.patch)
- Use _smp_mflags macro everywhere relevant. (freetype-pre1.4-make.patch)
- Undo fix for #24253, assume compiler was fixed.

* Mon Nov 12 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.0.5-2
- Fix build with gcc 3.1 (#56079)

* Sun Nov 11 2001 Mike A. Harris <mharris@redhat.com> 2.0.5-1
- Updated freetype to version 2.0.5

* Sat Sep 22 2001 Mike A. Harris <mharris@redhat.com> 2.0.4-2
- Added new subpackage freetype-demos, added demos to build
- Disabled ftdump, ftlint in utils package favoring the newer utils in
  demos package.

* Tue Sep 11 2001 Mike A. Harris <mharris@redhat.com> 2.0.4-1
- Updated source to 2.0.4
- Added freetype demo's back into src.rpm, but not building yet.

* Wed Aug 15 2001 Mike A. Harris <mharris@redhat.com> 2.0.3-7
- Changed package to use {findlang} macro to fix bug (#50676)

* Sun Jul 15 2001 Mike A. Harris <mharris@redhat.com> 2.0.3-6
- Changed freetype-devel to group Development/Libraries (#47625)

* Mon Jul  9 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.0.3-5
- Fix up FT1 headers to please Qt 3.0.0 beta 2

* Sun Jun 24 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.0.3-4
- Add ft2build.h to -devel package, since it's included by all other
  freetype headers, the package is useless without it

* Thu Jun 21 2001 Nalin Dahyabhai <nalin@redhat.com> 2.0.3-3
- Change "Requires: freetype = name/ver" to "freetype = version/release",
  and move the requirements to the subpackages.

* Mon Jun 18 2001 Mike A. Harris <mharris@redhat.com> 2.0.3-2
- Added "Requires: freetype = name/ver"

* Tue Jun 12 2001 Mike A. Harris <mharris@redhat.com> 2.0.3-1
- Updated to Freetype 2.0.3, minor specfile tweaks.
- Freetype2 docs are is in a separate tarball now. Integrated it.
- Built in new environment.

* Fri Apr 27 2001 Bill Nottingham <notting@redhat.com>
- rebuild for C++ exception handling on ia64

* Sat Jan 20 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Build ttmkfdir with -O0, workaround for Bug #24253

* Fri Jan 19 2001 Nalin Dahyabhai <nalin@redhat.com>
- libtool is used to build libttf, so use libtool to link ttmkfdir with it
- fixup a paths for a couple of missing docs

* Thu Jan 11 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update ttmkfdir

* Wed Dec 27 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to 2.0.1 and 1.4
- Mark locale files as such

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 12 2000 Preston Brown <pbrown@redhat.com>
- move .la file to devel pkg
- FHS paths

* Thu Feb 17 2000 Preston Brown <pbrown@redhat.com>
- revert spaces patch, fix up some foundry names to match X ones

* Mon Feb 07 2000 Nalin Dahyabhai <nalin@redhat.com>
- add defattr, ftmetric, ftsbit, ftstrtto per bug #9174

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description and summary

* Wed Jan 12 2000 Preston Brown <pbrown@redhat.com>
- make ttmkfdir replace spaces in family names with underscores (#7613)

* Tue Jan 11 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.3.1
- handle RPM_OPT_FLAGS

* Wed Nov 10 1999 Preston Brown <pbrown@redhat.com>
- fix a path for ttmkfdir Makefile

* Thu Aug 19 1999 Preston Brown <pbrown@redhat.com>
- newer ttmkfdir that works better, moved ttmkfdir to /usr/bin from /usr/sbin
- freetype utilities moved to subpkg, X dependency removed from main pkg
- libttf.so symlink moved to devel pkg

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- strip binaries

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 5)

* Thu Mar 18 1999 Cristian Gafton <gafton@redhat.com>
- fixed the %doc file list

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Mon Feb 15 1999 Preston Brown <pbrown@redhat.com>
- added ttmkfdir

* Tue Feb 02 1999 Preston Brown <pbrown@redhat.com>
- update to 1.2

* Thu Jan 07 1999 Cristian Gafton <gafton@redhat.com>
- call libtoolize to sanitize config.sub and get ARM support
- dispoze of the patch (not necessary anymore)

* Wed Oct 21 1998 Preston Brown <pbrown@redhat.com>
- post/postun sections for ldconfig action.

* Tue Oct 20 1998 Preston Brown <pbrown@redhat.com>
- initial RPM, includes normal and development packages.
