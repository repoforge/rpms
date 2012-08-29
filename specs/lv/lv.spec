# $Id$
# Authority: dfateyev
# Upstream: NARITA Tomio <nrt$ff,iij4u,or,jp>

### Already presented in repo
# ExcludeDist: el4 el5

Summary: Powerful Multilingual File Viewer
Name: lv
%define real_version 451
Version: 4.51
Release: 1%{?dist}
License: distributable
Group: Applications/Text
URL: http://www.ff.iij4u.or.jp/~nrt/lv/

Source: http://www.ff.iij4u.or.jp/~nrt/freeware/lv%{real_version}.tar.gz
Patch1: lv-4.49.4-nonstrip.patch
Patch2: lv-4.51-162372.patch
Patch3: lv-+num-option.patch
Patch4: lv-fastio.patch
Patch5: lv-lfs.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: libtermcap-devel

%description
lv is a powerful file viewer like less.
lv can decode and encode multilingual streams through
many coding systems: ISO-8859, ISO-2022, EUC, SJIS, Big5,
HZ, Unicode.
It recognizes multi-bytes patterns as regular
expressions, lv also provides multilingual grep.
In addition, lv can recognize ANSI escape sequences
for text devoration.

%prep
%setup -n %{name}%{real_version}
%patch1 -p1 -b .nonstrip
%patch2 -p1 -b .162372
%patch3 -p1 -b .num
%patch4 -p1 -b .fastio
%patch5 -p1 -b .lfs

%build
cd src/
autoconf
%configure --enable-fastio
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__make} -C src install bindir="%{buildroot}%{_bindir}" libdir="%{buildroot}%{_libdir}" mandir="%{buildroot}%{_mandir}"

%files
%defattr(-, root, root, 0755)
%doc GPL.txt README build/ hello.sample hello.sample.gif index.html
%doc relnote.html
%doc %{_mandir}/man1/lv.1*
%{_bindir}/lv
%{_bindir}/lgrep
%{_libdir}/lv/

%clean
%{__rm} -rf %{buildroot}

%changelog
* Fri Apr 20 2012 IWAI, Masaharu <iwaim.sub@gmail.com> - 4.51-9
- first build for Repoforge el6

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 4.51-8.1
- rebuild

* Mon Jun 12 2006 Akira TAGOH <tagoh@redhat.com> - 4.51-8
- clean up the spec file.
- add autoconf to BuildReq. (#194753)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 4.51-7.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 4.51-7.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Oct 31 2005 Akira TAGOH <tagoh@redhat.com> - 4.51-7
- lv-+num-option.patch: applied a patch to allow +num option to jump to the specific line.
- lv-fastio.patch: applied a patch to improve the performance to read the files.
- lv-lfs.patch: applied a patch for Lerge File Summit support.

* Mon Jul 11 2005 Akira TAGOH <tagoh@redhat.com> - 4.51-6
- lv-4.51-162372.patch: silence gcc warning. (#162372)

* Thu Mar 17 2005 Akira TAGOH <tagoh@redhat.com> - 4.51-5
- rebuilt

* Thu Feb 10 2005 Akira TAGOH <tagoh@redhat.com> - 4.51-4
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jan 16 2004 Akira TAGOH <tagoh@redhat.com> 4.51-1
- New upstream release.
- lv-fix-install-opts.patch: removed because it's unnecessary anymore.

* Tue Nov 25 2003 Akira TAGOH <tagoh@redhat.com> 4.50-1
- New upstream release.
  here is this release of note.
  - [4.49.5.a]
  - Added ISO-8859-10,11,13,14,15,16.
  - Changed coding system names for '=' key.
  - [4.49.5.b]
  - Updated KSX1001 <-> Unicode mapping table.
  - [4.49.5.c]
  - Input coding detection improved.
  - -D option now specifies default (fall-back) coding system, not default EUC coding system.
  - Output coding detection based on LC_CTYPE locale.
  - [4.49.5.d]
  - Checks $EDITOR and $VISUAL variables when invoking an editor.
  - [4.49.5.f]
  - Initialize file->used[] in FileAttach() in file.c to avoid segfault in lgrep.
  - [4.5.0]
  - added polling function for regular files with slightly modified patch from Pawel S. Veselov <vps@manticore.2y.net>.
  - enabled itable cache.
  - Big5 to Unicode mapping didn't work at all (fixed offset of coding system table)
    (See http://lists.debian.or.jp/debian-devel/200311/msg00006.html)
  - fixed editor call not to return by SIGINT unexpectedly.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 12 2003 Akira TAGOH <tagoh@redhat.com> 4.49.5-1
- New upstream release.
- lv-4.49.4-dont-read-dotlv-on-cwd.patch: removed.
- lv-4.49.4-fix-manpage.patch: removed.

* Mon Apr 28 2003 Akira TAGOH <tagoh@redhat.com> 4.49.4-11
- lv-4.49.4-fix-manpage.patch: fix the man pages to reflect previous changes.

* Mon Apr 28 2003 Akira TAGOH <tagoh@redhat.com> 4.49.4-10
- lv-4.49.4-dont-read-dotlv-on-cwd.patch: don't read .lv file from current
  directory to prevent the possibility of local root exploit.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Nov 20 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 19 2002 Akira TAGOH <tagoh@redhat.com> 4.49.4-6
- lv-4.49.4-nonstrip.patch: applied to fix the stripped binary.
- s/Copyright/License/

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jul 24 2001 SATO Satoru <ssato@redhat.com>
- BuildPrereq: libtermcap-devel (close #49517)

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Wed Dec 20 2000 SATO Satoru <ssato@redhat.com>
- clean up spec

* Tue Dec 19 2000 SATO Satoru <ssato@redhat.com>
- new upstream
- use system-defined macros

* Thu Aug 24 2000 SATO Satoru <ssato@redhat.com>
- fix spec (remove japanese description)

* Mon Aug 07 2000 SATO Satoru <ssato@redhat.com>
- fix spec (make prefix... replaced with %makeinstall)

* Tue Jul 04 2000 SATO Satoru <ssato@redhat.com>
- initial release.

