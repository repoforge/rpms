# $Id$
# Authority: matthias
# Upstream: <mp3encoder$minnie,tuhs,org>

Summary: LAME Ain't an MP3 Encoder... but it's the best of all
Name: lame
Version: 3.96
Release: 1
License: LGPL
Group: Applications/Multimedia
URL: http://lame.sourceforge.net/
Source: http://dl.sf.net/lame/lame-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: ncurses-devel
%ifarch %{ix86}
BuildRequires: nasm
%endif
Provides: mp3encoder

%description
LAME is an educational tool to be used for learning about MP3 encoding.
The goal of the LAME project is to use the open source model to improve
the psycho acoustics, noise shaping and speed of MP3. Another goal of
the LAME project is to use these improvements for the basis of a patent
free audio compression codec for the GNU project.


%package devel
Summary: Shared and static libraries for LAME
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
LAME is an educational tool to be used for learning about MP3 encoding.
This package contains both the shared and the static libraries from the
LAME project.

You will also need to install the main lame package in order to install
these libraries.


%prep
%setup


%build
### We want to be optimized to the bone!
### You know what? This i386 stuff is as good as if it was only i686 and
### the MMX code is enabled at runtime if found! So this is gooooood :-)
%ifarch i386
    export CC_OPTS="-O3 -march=i386 -mcpu=i686 -fomit-frame-pointer -fno-strength-reduce -malign-functions=4 -funroll-loops -ffast-math"
%else
    # Vague and ix86 inspired (but working) ppc optimizations
    %ifarch ppc
        export CC_OPTS="-O3 -fsigned-char -fomit-frame-pointer -fno-strength-reduce -funroll-loops -ffast-math"
    %else
        export CC_OPTS="-O3 -fomit-frame-pointer -fno-strength-reduce -funroll-loops -ffast-math"
    %endif
%endif

%configure \
    --program-prefix=%{?_program_prefix} \
%ifarch %{ix86}
    --enable-nasm \
%endif
    --enable-decoder \
    --with-vorbis \
    --enable-analyser="no" \
    --enable-brhist

%{__make} %{?_smp_mflags} test CFLAGS="${CC_OPTS}"


%install
%{__rm} -rf %{buildroot}
%makeinstall

### Some apps still expect to find <lame.h>
%{__ln_s} -f lame/lame.h %{buildroot}%{_includedir}/lame.h

find doc/html -name "Makefile*" | xargs rm -f
%{__rm} -rf %{buildroot}%{_docdir}/lame/


%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null


%clean
%{__rm} -rf %{buildroot}


%files
%defattr (-, root, root, 0755)
%doc ChangeLog COPYING README TODO USAGE doc/html
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr (-, root, root, 0755)
%doc API HACKING STYLEGUIDE
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la


%changelog
* Wed Apr 21 2004 Matthias Saou <http://freshrpms.net/> 3.96-1
- Update to 3.96 w/ spec changes from Dag.

* Tue Jan 13 2004 Matthias Saou <http://freshrpms.net/> 3.95.1-1
- Update to 3.95.1.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 3.93.1-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Mon Jan 13 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.93.1.
- Removed Epoch: tag, upgrade by hand! :-/

* Sat Oct  5 2002 Matthias Saou <http://freshrpms.net/>
- Fix unpackaged doc problem.

* Fri Sep 27 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- Simplified deps as it now builds VBR code fine with default nasm and gcc 3.2.

* Tue Jul 16 2002 Matthias Saou <http://freshrpms.net/>
- Fix to the lamecc stuff.

* Wed Jul 10 2002 Matthias Saou <http://freshrpms.net/>
- Changes to now support ppc with no ugly workarounds.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Wed Apr 24 2002 Matthias Saou <http://freshrpms.net/>
- Update to 3.92.

* Mon Apr  8 2002 Matthias Saou <http://freshrpms.net/>
- Added a symlink from lame.h to lame/lame.h to fix some include file
  detection for most recent programs that use lame.

* Wed Jan  2 2002 Matthias Saou <http://freshrpms.net/>
- Update to 3.91.
- Simplified the compilation optimizations after heavy home-made tests.
- Now build only i386 version but optimized for i686. Don't worry i686
  owners, you loose only 1% in speed but gain about 45% compared to if
  you had no optimizations at all!

* Mon Dec 24 2001 Matthias Saou <http://freshrpms.net/>
- Update to 3.90.1.
- Enabled the GTK+ frame analyzer.
- Spec file cleanup (CVS, man page, bindir are now fixed).

* Fri Nov 16 2001 Matthias Saou <http://freshrpms.net/>
- Rebuilt with mpg123 decoding support.

* Tue Oct 23 2001 Matthias Saou <http://freshrpms.net/>
- Fixed the %pre and %post that should have been %post and %postun, silly me!
- Removed -malign-double (it's evil, Yosi told me and I tested, brrr ;-)).
- Now build with gcc3, VBR encoding gets a hell of a boost, impressive!
  I recommend you now use "lame --r3mix", it's the best.
- Tried to re-enable vorbis, but it's a no-go.

* Thu Jul 26 2001 Matthias Saou <http://freshrpms.net/>
- Build with kgcc to have VBR working.

* Wed Jul 25 2001 Matthias Saou <http://freshrpms.net/>
- Update to 3.89beta : Must be built with a non-patched version of nasm
  to work!

* Mon May  7 2001 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat 7.1.
- Disabled the vorbis support since it fails to build with it.
- Added a big optimisation section, thanks to Yosi Markovich
  <senna@camelot.com> for this and other pointers.

* Sun Feb 11 2001 Matthias Saou <http://freshrpms.net/>
- Split the package, there is now a -devel

* Thu Oct 26 2000 Matthias Saou <http://freshrpms.net/>
- Initial RPM release for RedHat 7.0 from scratch

