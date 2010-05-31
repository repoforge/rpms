# $Id$
# Authority: dag

# ExcludeDist: el2 el3 el4

Summary: A smaller version of the Bourne shell (sh).
Name: ash
Version: 0.3.8
Release: 20%{?dist}
License: BSD
Group: System Environment/Shells

Source: http://archive.debian.org/debian-archive/debian/dists/woody/main/source/shells/ash_%{version}.orig.tar.gz
Patch0: http://archive.debian.org/debian-archive/debian/dists/woody/main/source/shells/ash_%{version}-38.diff.gz
Patch2: ash-0.3.8-tempfile.patch
#Patch1: ash-0.3.8-build.patch # <-- no longer needed.
Patch3: ash-0.3.8-mannewline.patch
Patch4: ash-0.3.8-segv.patch
Patch5: ash-0.3.8-history-man.patch
Patch6: ash-0.3.8-gnu.patch
Patch7: ash-0.3.8-for.patch
Patch8: ash-0.3.8-pid.patch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

Conflicts: mkinitrd <= 1.7
BuildRequires: bison
BuildRequires: flex
Requires: fileutils
Requires: grep

%description
A shell is a basic system program that interprets keyboard and mouse
commands. The ash shell is a clone of Berkeley's Bourne shell
(sh). Ash supports all of the standard sh shell commands, but is
considerably smaller than sh. The ash shell lacks some Bourne shell
features (for example, command-line histories), but it uses a lot less
memory.

You should install ash if you need a lightweight shell with many of
the same capabilities as the sh shell.

%prep
%setup -n %{name}-%{version}.orig
%patch0 -p1 -b .linux
%patch2 -p1 -b .tempfile
#%ifarch alpha
#%patch1 -p1 -b .alpha
#%endif
%patch3 -p1

%patch4 -p0 -b .segv
%patch5 -p0 -b .man
%patch6 -p1 -b .gnu
%patch7 -p1 -b .for
%patch8 -p1 -b .pid

chmod -R a+rX .

%build
CFLAGS="%{optflags}" %{__make}
%{__mv} sh sh.dynamic

CFLAGS="%{optflags}" LDFLAGS="-static" %{__make}
%{__mv} sh sh.static

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 sh.dynamic %{buildroot}/bin/ash
%{__install} -Dp -m0755 sh.static %{buildroot}/bin/ash.static
%{__install} -Dp -m0644 sh.1 %{buildroot}%{_mandir}/man1/ash.1
%{__ln_s} -f ash.1 %{buildroot}%{_mandir}/man1/bsh.1
%{__ln_s} -f ash %{buildroot}/bin/bsh

%post
if [ ! -f /etc/shells ]; then
    echo "/bin/ash" >/etc/shells
    echo "/bin/bsh" >>/etc/shells
else
    if ! grep -q '^/bin/ash$' /etc/shells; then
        echo "/bin/ash" >>/etc/shells
    fi
    if ! grep -q '^/bin/bsh$' /etc/shells; then
        echo "/bin/bsh" >>/etc/shells
    fi
fi

%postun
if [ $1 -eq 0 ]; then
    grep -v -E '^/bin/[ab]sh' /etc/shells >/etc/shells.new
    %{__mv} -f /etc/shells.new /etc/shells
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/ash.1*
%doc %{_mandir}/man1/bsh.1*
/bin/ash
/bin/ash.static
/bin/bsh

%changelog
* Mon May 31 2010 Dag Wieers <dag@wieers.com> - 0.3.8-20
- Rebuild for RHEL5.

* Tue Nov 18 2008 Daniel Novotny <dnovotny@redhat.com> 0.3.8-20
- Resolves: #470443

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jun 07 2004 Lon Hohberger <lhh@redhat.com> 0.3.8-19
- Remove alpha-specific hacks; no longer necessary + cause 
builds to break.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Dec 04 2003 Lon Hohberger <lhh@redhat.com> 0.3.8-17
- Rebuild

* Thu Aug 14 2003 Lon Hohberger <lhh@redhat.com> 0.3.8-16
- Fix for #102334

* Wed Aug 06 2003 Lon Hohberger <lhh@redhat.com> 0.3.8-15
- Rebuild for Severn

* Wed Aug 06 2003 Lon Hohberger <lhh@redhat.com> 0.3.8-14
- Fix ash-0.3.8-gnu.patch to fix parsing on ia64

* Wed Aug 06 2003 Lon Hohberger <lhh@redhat.com> 0.3.8-13
- Change build to use GNU tools (flex/bison/gnu-make/gcc), fixes
#101755

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Apr 15 2003 Lon Hohberger <lhh@redhat.com> 0.3.8-11
- Bumped & Rebuilt

* Tue Apr 15 2003 Lon Hohberger <lhh@redhat.com> 0.3.8-9
- Fix for #81903: Man page documents commands which do not exist. (fc, jobid)

* Thu Feb 6 2003 Lon Hohberger <lhh@redhat.com> 0.3.8-8
- Fix for #83605

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 19 2002 Tim Powers <timp@redhat.com>
- bump and rebuild

* Wed Jul 17 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.3.8-5
- Update to -38 diff
- man page fixes (#63528)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Dec 11 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.3.8-1
- 0.3.8
- Patch to make it build
- workaround for oddities in the alpha compiler

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Mon Jan 08 2001 Preston Brown <pbrown@redhat.com>
- ported much newer version from Debian
- alpha is miscompiling mkinit helper utility; work around w/o optimization

* Thu Dec  7 2000 Crutcher Dunnavant <crutcher@redhat.com>
- intial rebuild for 7.1

* Wed Aug 30 2000 Matt Wilson <msw@redhat.com>
- rebuild to cope with glibc locale binary incompatibility, again

* Wed Jul 19 2000 Jakub Jelinek <jakub@redhat.com>
- rebuild to cope with glibc locale binary incompatibility

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Wed Jun 21 2000 Jakub Jelinek <jakub@redhat.com>
- mksyntax had undefined behaviour, make it conforming.

* Mon Jun 12 2000 Preston Brown <pbrown@redhat.com>
- FHS fixes
- had to disable optimization for sparc, was producing a mksyntax binary that
  infinitely looped!  FIX ME.

* Wed Mar 29 2000 Bill Nottingham <notting@redhat.com>
- fix bug in 'ash -e' handling

* Thu Feb 03 2000 Preston Brown <pbrown@redhat.com>
- gzipped man pages

* Mon Oct 04 1999 Cristian Gafton <gafton@redhat.com>
- rebuild against the lastest glibc in the sparc tree

* Sat Sep 11 1999 Bill Nottingham <notting@redhat.com>
- fix bogosity with fd's > 0
- fix builtin echo to understand -n & -e at the same time

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 17)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Jan 12 1999 Cristian Gafton <gafton@redhat.com>
- build on glibc 2.1

* Fri Nov 06 1998 Preston Brown <pbrown@redhat.com>
- updated to correct path on SunSITE.

* Fri Aug 28 1998 Jeff Johnson <jbj@redhat.com>
- recompile statically linked binary for 5.2/sparc

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- made /bin/ash built shared
- added ash.static
- uses a buildroot and %attr

* Sun Aug 24 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- statically linked

* Wed Apr 16 1997 Erik Troan <ewt@redhat.com>
- fixed preinstall script to >> /etc/shells for bsh.
