# $Id$
# Authority: yury
# Upstream: Junio C. Hamano <gitster$pobox,com>
#
# Tag: rft

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define desktop_vendor rpmforge

%{?el2:%define _with_old_makemaker 1}
%{?el2:%define _without_curl 1}
%{?el2:%define _without_gitweb 1}
%{?el2:%define _without_gui 1}
%{?el2:%define _without_module_compat 1}
%{?el2:%define _without_nsec 1}
%{?el2:%define _without_svn 1}
%{?el2:%define _without_external_grep 1}

%{?el3:%define _with_old_makemaker 1}
%{?el3:%define _without_gitweb 1}
%{?el3:%define _without_gui 1}

#%%define snap	.rc2

Name: 		git
Version: 	1.6.5.6
Release: 	1%{?snap}%{?dist}
Summary:	Fast Version Control System
License: 	GPLv2
Group: 		Development/Tools
URL: 		http://git-scm.com/
Source0: 	http://kernel.org/pub/software/scm/git/%{name}-%{version}%{?snap}.tar.bz2
Source2:	git.xinetd
Source3:	git.conf.httpd
Source100:	http://kernel.org/pub/software/scm/git/git-manpages-%{version}%{?snap}.tar.bz2
Patch0:		git-1.5-gitweb-home-link.patch
# https://bugzilla.redhat.com/490602
Patch1:		git-cvsimport-Ignore-cvsps-2.2b1-Branches-output.patch
# https://bugzilla.redhat.com/500137
Patch2:		git-1.6-update-contrib-hooks-path.patch
Patch10:	git-1.6.5-nomakemaker.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	zlib-devel, openssl-devel, expat-devel
BuildRequires:	gnupg
%{!?_without_curl:BuildRequires:	curl-devel >= 7.9.8}
Requires:	perl-Git = %{version}-%{release}
Requires:	rsync, less
Provides:	git-core = %{version}-%{release}

%description
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

The git rpm installs the core tools with minimal dependencies.  To
install all git packages, including tools for integrating with other
SCMs, install the git-all meta-package.

%package all
Summary:	Meta-package to pull in all git tools
Group:		Development/Tools
Requires:	git = %{version}-%{release}
Requires:	git-email = %{version}-%{release}
%{!?_without_svn:Requires:	git-svn = %{version}-%{release}}
%{!?_without_cvs:Requires:	git-cvs = %{version}-%{release}}
%{!?_without_gui:Requires:	gitk = %{version}-%{release}}
%{!?_without_gui:Requires:	git-gui = %{version}-%{release}}
%{?_with_arch:Requires:	git-arch = %{version}-%{release}}

%description all
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This is a dummy package which brings in all subpackages.

%package daemon
Summary:	Git protocol dæmon
Group:		Development/Tools
Requires:	git = %{version}-%{release}, xinetd
%description daemon
The git dæmon for supporting git:// access to git repositories

%if %{!?_without_gitweb:1}0
%package -n gitweb
Summary:    Simple web interface to git repositories
Group:	    Development/Tools
Requires:   git = %{version}-%{release}

%description -n gitweb
Simple web interface to track changes in git repositories
%endif

%if %{!?_without_svn:1}0
%package svn
Summary:        Git tools for importing Subversion repositories
Group:          Development/Tools
BuildRequires:	perl(SVN::Core) >= 1.1.0
Requires:       git = %{version}-%{release}, perl(SVN::Core) >= 1.1.0
%description svn
Git tools for importing Subversion repositories.
%endif

%if %{!?_without_cvs:1}0
%package cvs
Summary:        Git tools for importing CVS repositories
Group:          Development/Tools
BuildRequires:	cvs
Requires:       git = %{version}-%{release}, cvs, cvsps
%description cvs
Git tools for importing CVS repositories.
%endif

%if %{?_with_arch:1}0
%package arch
Summary:        Git tools for importing Arch repositories
Group:          Development/Tools
Requires:       git = %{version}-%{release}, tla
%description arch
Git tools for importing Arch repositories.
%endif

%package email
Summary:        Git tools for sending email
Group:          Development/Tools
Requires:	git = %{version}-%{release}, perl-Git = %{version}-%{release}
%description email
Git tools for sending email.

%if %{!?_without_gui:1}0
%package gui
Summary:        Git GUI tool
Group:          Development/Tools
BuildRequires:	gettext, desktop-file-utils
Requires:       git = %{version}-%{release}, tk >= 8.4
Requires:	gitk = %{version}-%{release}
%description gui
Git GUI tool.

%package -n gitk
Summary:        Git revision tree visualiser
Group:          Development/Tools
BuildRequires:	gettext
Requires:       git = %{version}-%{release}, tk >= 8.4
%description -n gitk
Git revision tree visualiser.
%endif

%package -n perl-Git
Summary:        Perl interface to Git
Group:          Development/Libraries
Requires:       git = %{version}-%{release}, perl(Error)
%{!?_without_module_compat:Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))}
BuildRequires:	perl(Error), perl(ExtUtils::MakeMaker)

%description -n perl-Git
Perl interface to Git.

%prep
%setup -n %{name}-%{version}%{?snap}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch10 -p1

# Consolidate build options in one place
# All on one line please, older rpms don't grok multiline macros.
%define make_git make %{?_smp_mflags} V=1 CFLAGS="%{optflags}%{?el3: -I/usr/kerberos/include}" ETC_GITCONFIG=%{_sysconfdir}/gitconfig DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p" PREFIX="%{_prefix}" INSTALLDIRS="vendor" %{?_without_curl:NO_CURL=YES} %{?_without_gui:NO_TCLTK=YES} %{?_without_nsec:NO_NSEC=YES} %{?_without_external_grep:NO_EXTERNAL_GREP=YES} %{?_with_old_makemaker:NO_PERL_MAKEMAKER=YES} prefix=%{_prefix} mandir=%{_mandir}

# Filter bogus perl requires
# packed-refs comes from a comment in contrib/hooks/update-paranoid
cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
sed -e '/perl(packed-refs)/d'
EOF

%global __perl_requires %{_builddir}/%{name}-%{version}%{?snap}/%{name}-req
chmod +x %{__perl_requires}

%{__cat} <<EOF >git-gui.desktop
[Desktop Entry]
Encoding=UTF-8
Name=Git GUI
GenericName=Git GUI
Comment=A graphical interface to Git
Exec=git gui
Icon=/usr/share/git-gui/lib/git-gui.ico
Terminal=false
Type=Application
Categories=Development;
EOF

%build
%{make_git} all

# Remove shebang from bash-completion script
sed -e '/^#!bash/,+1 d' contrib/completion/git-completion.bash \
    > contrib/completion/git-completion.bash.tmp && \
    mv contrib/completion/git-completion.bash.tmp \
       contrib/completion/git-completion.bash

%install
rm -rf $RPM_BUILD_ROOT
%{make_git} install

%{__mkdir} -p %{buildroot}%{_mandir}
cd %{buildroot}%{_mandir}
tar xvjf %{SOURCE100}
cd -

# We must own system global configfile
%{__mkdir} -p %{buildroot}/%{_sysconfdir}
touch %{buildroot}/%{_sysconfdir}/gitconfig

%{__install} -Dp -m0644 %SOURCE2 $RPM_BUILD_ROOT/%{_sysconfdir}/xinetd.d/git

%if %{!?_without_gitweb:1}0
%{__install} -Dp -m0755 gitweb/gitweb.cgi $RPM_BUILD_ROOT%{_var}/www/git/gitweb.cgi
%{__install} -p -m0644 gitweb/*.png gitweb/*.css $RPM_BUILD_ROOT%{_var}/www/git
%{__install} -Dp -m0644 %SOURCE3 $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/git.conf
%endif

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name perllocal.pod -exec rm -f {} ';'

# Nuke any traces of a private copy of perl(Error)
find $RPM_BUILD_ROOT -type f -name Error.pm -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name private-Error.3pm* -exec rm -f {} ';'

(find $RPM_BUILD_ROOT%{_bindir} -type f | grep -vE "archimport|svn|cvs|email|gitk|git-gui|git-citool|git-daemon" | sed -e s@^$RPM_BUILD_ROOT@@) > bin-man-doc-files
(find $RPM_BUILD_ROOT%{_libexecdir}/git-core -type f | grep -vE "archimport|svn|cvs|email|gitk|git-gui|git-citool|git-daemon" | sed -e s@^$RPM_BUILD_ROOT@@) >> bin-man-doc-files
(find $RPM_BUILD_ROOT%{_mandir} -type f | grep -vE "archimport|svn|git-cvs|email|gitk|git-gui|git-citool|git-daemon" | sed -e s@^$RPM_BUILD_ROOT@@ -e 's/$/*/' ) >> bin-man-doc-files
(find $RPM_BUILD_ROOT%{perl_vendorlib} -type f | sed -e s@^$RPM_BUILD_ROOT@@) >> perl-files

# Find files for git-arch
(find $RPM_BUILD_ROOT%{_libexecdir}/git-core -type f | grep -E "archimport" | sed -e s@^$RPM_BUILD_ROOT@@) > archimport-files
(find $RPM_BUILD_ROOT%{_mandir} -type f | grep -E "archimport" | sed -e s@^$RPM_BUILD_ROOT@@ -e 's/$/*/' ) >> archimport-files
%if %{!?_with_arch:1}0
# Make the main filelist exclude these if we're not building this subpackage
sed -e 's/^/%exclude /g' archimport-files >> bin-man-doc-files
%endif

# Find files for git-svn
(find $RPM_BUILD_ROOT%{_libexecdir}/git-core -type f | grep -E "svn" | sed -e s@^$RPM_BUILD_ROOT@@) > svn-files
(find $RPM_BUILD_ROOT%{_mandir} -type f | grep -E "svn" | sed -e s@^$RPM_BUILD_ROOT@@ -e 's/$/*/' ) >> svn-files
%if %{?_without_svn:1}0
# Make the main filelist exclude these if we're not building this subpackage
sed -e 's/^/%exclude /g' svn-files >> bin-man-doc-files
%endif

# Find files for git-cvs
(find $RPM_BUILD_ROOT%{_bindir} -type f | grep -E "cvs" | sed -e s@^$RPM_BUILD_ROOT@@) > cvs-files
(find $RPM_BUILD_ROOT%{_libexecdir}/git-core -type f | grep -E "cvs" | sed -e s@^$RPM_BUILD_ROOT@@) >> cvs-files
(find $RPM_BUILD_ROOT%{_mandir} -type f | grep -E "cvs" | sed -e s@^$RPM_BUILD_ROOT@@ -e 's/$/*/' ) >> cvs-files
%if %{?_without_cvs:1}0
# Make the main filelist exclude these if we're not building this subpackage
sed -e 's/^/%exclude /g' cvs-files >> bin-man-doc-files
%endif

# If we're not building the gui/gitk packages then exclude their manpages
%if %{?_without_gui:1}0
echo %exclude %{_mandir}/man1/git-citool.1* >> bin-man-doc-files
echo %exclude %{_mandir}/man1/git-gui.1* >> bin-man-doc-files
echo %exclude %{_mandir}/man1/gitk.1* >> bin-man-doc-files
%endif

mkdir -p $RPM_BUILD_ROOT%{_var}/lib/git

%{__install} -Dp -m0644 contrib/completion/git-completion.bash $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/git

# Move contrib/hooks out of %%docdir and make them executable
mkdir -p $RPM_BUILD_ROOT%{_datadir}/git-core/contrib
mv contrib/hooks $RPM_BUILD_ROOT%{_datadir}/git-core/contrib
chmod +x $RPM_BUILD_ROOT%{_datadir}/git-core/contrib/hooks/*
pushd contrib > /dev/null
ln -s ../../../git-core/contrib/hooks
popd > /dev/null

%if %{!?_without_gui:1}0
%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}	    \
	--dir %{buildroot}%{_datadir}/applications \
	git-gui.desktop
%endif

# quiet some rpmlint complaints
chmod g-w $RPM_BUILD_ROOT%{_libexecdir}/git-core/*
chmod a-x $RPM_BUILD_ROOT%{_libexecdir}/git-core/git-mergetool--lib
rm -f {Documentation/technical,contrib/emacs}/.gitignore
chmod a-x Documentation/technical/api-index.sh
find contrib -type f -perm +a+x | xargs chmod -x

%check || :
# A few tests fail on el2 because perl is too old
%{?el2:export GIT_SKIP_TESTS="t2016 t3701 t3904 t7105 t7501.20"} 
# This test fails with subversion 1.1.4
%{?el4:export GIT_SKIP_TESTS="t9140.4"}
%{make_git} -k test

%clean
rm -rf $RPM_BUILD_ROOT

%files -f bin-man-doc-files
%defattr(-,root,root)
%{_datadir}/git-core/
%dir %{_libexecdir}/git-core
%doc README COPYING Documentation/*.txt contrib
%config(noreplace) %ghost %{_sysconfdir}/gitconfig
%{_sysconfdir}/bash_completion.d

%if %{!?_without_svn:1}0
%files svn -f svn-files
%defattr(-,root,root)
%endif

%if %{!?_without_cvs:1}0
%files cvs -f cvs-files
%defattr(-,root,root)
%endif

%if %{?_with_arch:1}0
%files arch -f archimport-files
%defattr(-,root,root)
%endif

%files email
%defattr(-,root,root)
%{_libexecdir}/git-core/*email*
%{_mandir}/man1/*email*.1*

%if %{!?_without_gui:1}0
%files gui
%defattr(-,root,root)
%{_libexecdir}/git-core/git-gui
%{_libexecdir}/git-core/git-gui--askpass
%{_libexecdir}/git-core/git-citool
%{_mandir}/man1/git-gui.1*
%{_mandir}/man1/git-citool.1*
%{_datadir}/applications/*git-gui.desktop
%{_datadir}/git-gui/

%files -n gitk
%defattr(-,root,root)
%{_bindir}/*gitk*
%{_mandir}/man1/gitk.1*
%{_datadir}/gitk/
%endif

%files -n perl-Git -f perl-files
%defattr(-,root,root)

%files daemon
%defattr(-,root,root)
%{_libexecdir}/git-core/git-daemon
%{_mandir}/man1/git-daemon.1*
%config(noreplace)%{_sysconfdir}/xinetd.d/git
%{_var}/lib/git

%if %{!?_without_gitweb:1}0
%files -n gitweb
%defattr(-,root,root)
%doc gitweb/README
%{_var}/www/git/
%config(noreplace)%{_sysconfdir}/httpd/conf.d/git.conf
%endif

%files all
# No files for you!

%changelog
* Tue Dec 15 2009 Yury V. Zaytsev <yury@shurup.com> - 1.6.5.6-1
- More minor updates (thanks to Tom G. Christensen).

* Tue Dec 8 2009 Yury V. Zaytsev <yury@shurup.com> - 1.6.5.3-2
- Minor updates for RPMForge.

* Mon Nov 23 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.5.3-1
- Update to 1.6.5.3

* Tue Oct 26 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.5.2-1
- Update to 1.6.5.2

* Tue Oct 20 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.5.1-1
- Update to 1.6.5.1

* Mon Oct 12 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.5-1
- Update to 1.6.5
- Use NO_PERL_MAKEMAKER for < el4
- Fix NO_PERL_MAKEMAKER to install into perl libdir and not %%{_libdir}
- Skip new tests that depend on git-add--interactive on el2

* Thu Oct  8 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.4.4-2
- Sync with Fedora
  - Move contributed hooks to %%{_datadir}/git-core/contrib/hooks (bug 500137)
  - Fix rpmlint warnings about Summary and git-mergetool--lib missing shebang
  - Add a .desktop file for git-gui (bug 498801)
  - Escape newline in git-daemon xinetd description (bug 502393)
  - Add xinetd to git-daemon Requires (bug 504105)
  - Include contrib/ dir in %%doc (bug 492490)
  - Ignore Branches output from cvsps-2.2b1 (bug 490602)
  - Remove shebang from bash-completion script
  - Include README in gitweb subpackage
  - Update URL field

* Thu Sep 17 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.4.4-1
- Update to 1.6.4.4

* Fri Sep  4 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.4.2-1
- Update to 1.6.4.2

* Tue Aug 25 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.4.1-1
- Update to 1.6.4.1
- Build with NO_EXTERNAL_GREP on el2 to avoid t7002.26 failure

* Tue Jun  9 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.3.2-1
- Update to 1.6.3.2

* Tue May 14 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.3.1-1
- Update to 1.6.3.1
- Disable recording of sub-second timestamps on el2

* Tue May  5 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.2.5-1
- Update to 1.6.2.5

* Mon May  4 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.2.4-2
- Explicitly require perl(Error) for perl-Git

* Tue Apr 28 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.2.4-1
- Update to 1.6.2.4

* Wed Apr  1 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.2.1-2
- Fix typo in macro

* Mon Mar 16 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.2.1-1
- Update to 1.6.2.1

* Thu Mar  5 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.2-1
- Update to 1.6.2
- Remove emacs-git subpackage. The files are going away from upstream
  and support for emacs < 22 is poor

* Wed Feb 11 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.1.3-1
- Update to 1.6.1.3

* Fri Jan 30 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.1.2-1
- Update to 1.6.1.2

* Mon Jan 26 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.1.1-1
- Update to 1.6.1.1

* Mon Jan 19 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.1-3
- Fix testsuite with SVN::Core 1.1.4

* Fri Jan  9 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.1-2
- Add emacs-git subpackage (fc10)

* Wed Jan  7 2009 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.1-1
- Update to 1.6.1
- Add bash completion from contrib (fc10)
- Add gitweb and git-daemon subpackages (fc10)

* Mon Dec 22 2008 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.0.6-1
- Update to 1.6.0.6
- Enable verbose build output
- Don't remove files from buildroot %%exclude them instead
- Bump minimum required version of perl(SVN::Core) from 1.1.0 to 1.3.0

* Mon Dec  8 2008 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.0.5-1
- Update to 1.6.0.5

* Mon Nov 10 2008 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.0.4-2
- Update to 1.6.0.4
- git-cvsserver moved to %%_bindir
- Don't remove files from buildroot %%exclude them instead

* Wed Oct 22 2008 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.0.3-1
- Drop patch for t9700 issue that was fixed upstream
- Use GIT_SKIP_TESTS instead of patching the testsuite for el2
- Update to 1.6.0.3

* Mon Sep 15 2008 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.0.2-1
- Update to 1.6.0.2
- Reenable git-svn for el3.

* Mon Sep  1 2008 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.0.1-2
- Disable git-svn for el3 (File::Temp too old)
- Add patch from Brandon Casey to fix t9700 on el3 (File::Temp too old)

* Fri Aug 29 2008 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.0.1-1
- Update to 1.6.0.1

* Wed Aug  6 2008 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.5.6.4-1
- Update to 1.5.6.4

* Fri Jul  4 2008 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.5.6.1-3
- Update to 1.5.6.1

* Fri Jun 13 2008 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.5.5.4-1
- Update to 1.5.5.4

* Fri Jun  6 2008 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.5.5.3-3
- Make the git package own the default global gitconfig
- git-clone.sh requires curl for http fetch
- Add cvs and gnupg BRs to run more of the testsuite

* Mon Jun  2 2008 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.5.5.3-2
- Update to 1.5.5.3
- Don't build git-svn packages for el2
- Don't build git-arch packages unless --with arch was given

* Fri May 23 2008 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.5.5.1-2
- Update to 1.5.5.1
- Don't build gitk and gui packages for el2, el3 since tcl is too old anyway
- Add %%check
- remove mktemp, sh-utils and diffutils Requires
- git-svn requires atleast subversion-perl 1.1.0
- Sync with upstream spec
  - rename git to git-all and git-core to git

* Thu Jan 10 2008 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.5.3.8-5
- Update to 1.5.3.8
- Removed p4import
- Bump curl BR to 7.9.8 as Makefile suggests
- Workaround old MakeMaker (no DESTDIR support)

* Thu Aug 23 2007 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.5.2.5-4
- Remove dead sections of the specfile
- Remove all explicit requires picked up by autodeps
- Allow clean building on RHEL 3,4,5
- Add upstream pre-compiled manpages
- Remove all doc lines depending on asciidoc
- Add missing perl directory macros

* Tue May 13 2007 Quy Tonthat <qtonthat@gmail.com>
- Added lib files for git-gui
- Added Documentation/technical (As needed by Git Users Manual)

* Tue May 8 2007 Quy Tonthat <qtonthat@gmail.com>
- Added howto files

* Tue Mar 27 2007 Eygene Ryabinkin <rea-git@codelabs.ru>
- Added the git-p4 package: Perforce import stuff.

* Mon Feb 13 2007 Nicolas Pitre <nico@cam.org>
- Update core package description (Git isn't as stupid as it used to be)

* Mon Feb 12 2007 Junio C Hamano <junkio@cox.net>
- Add git-gui and git-citool.

* Mon Nov 14 2005 H. Peter Anvin <hpa@zytor.com> 0.99.9j-1
- Change subpackage names to git-<name> instead of git-core-<name>
- Create empty root package which brings in all subpackages
- Rename git-tk -> gitk

* Thu Nov 10 2005 Chris Wright <chrisw@osdl.org> 0.99.9g-1
- zlib dependency fix
- Minor cleanups from split
- Move arch import to separate package as well

* Tue Sep 27 2005 Jim Radford <radford@blackbean.org>
- Move programs with non-standard dependencies (svn, cvs, email)
  into separate packages

* Tue Sep 27 2005 H. Peter Anvin <hpa@zytor.com>
- parallelize build
- COPTS -> CFLAGS

* Fri Sep 16 2005 Chris Wright <chrisw@osdl.org> 0.99.6-1
- update to 0.99.6

* Fri Sep 16 2005 Horst H. von Brand <vonbrand@inf.utfsm.cl>
- Linus noticed that less is required, added to the dependencies

* Sun Sep 11 2005 Horst H. von Brand <vonbrand@inf.utfsm.cl>
- Updated dependencies
- Don't assume manpages are gzipped

* Thu Aug 18 2005 Chris Wright <chrisw@osdl.org> 0.99.4-4
- drop sh_utils, sh-utils, diffutils, mktemp, and openssl Requires
- use RPM_OPT_FLAGS in spec file, drop patch0

* Wed Aug 17 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.99.4-3
- use dist tag to differentiate between branches
- use rpm optflags by default (patch0)
- own %{_datadir}/git-core/

* Mon Aug 15 2005 Chris Wright <chrisw@osdl.org>
- update spec file to fix Buildroot, Requires, and drop Vendor

* Sun Aug 07 2005 Horst H. von Brand <vonbrand@inf.utfsm.cl>
- Redid the description
- Cut overlong make line, loosened changelog a bit
- I think Junio (or perhaps OSDL?) should be vendor...

* Thu Jul 14 2005 Eric Biederman <ebiederm@xmission.com>
- Add the man pages, and the --without docs build option

* Wed Jul 7 2005 Chris Wright <chris@osdl.org>
- initial git spec file
