# $Id$
# Authority: dag

### EL6 ships with git-1.7.1-2.el6
%{?el6:# Tag: rfx}

%define _default_patch_fuzz 2

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define desktop_vendor rpmforge

Summary: Git core and tools
Name: git
Version: 1.7.11
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://git-scm.com/

Source0: https://git-core.googlecode.com/files/git-%{version}.tar.gz
Source1: git-init.el
Source5: gitweb.conf.in
Patch0: git-1.5-gitweb-home-link.patch
### https://bugzilla.redhat.com/490602
Patch1: git-cvsimport-Ignore-cvsps-2.2b1-Branches-output.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: asciidoc > 6.0.3
BuildRequires: curl-devel >= 7.9
BuildRequires: desktop-file-utils
BuildRequires: expat-devel
BuildRequires: gettext
BuildRequires: emacs
BuildRequires: openssl-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: xmlto
BuildRequires: zlib-devel >= 1.2
Requires: less
Requires: openssh-clients
Requires: perl-Git = %{version}-%{release}
Requires: rsync
Requires: zlib >= 1.2

Obsoletes: git-core <= %{version}-%{release}
Provides: git-core = %{version}-%{release}

%filter_from_requires /^perl(packed-refs)*/d
%filter_setup

%description
GIT comes in two layers. The bottom layer is merely an extremely fast
and flexible filesystem-based database designed to store directory trees
with regard to their history. The top layer is a SCM-like tool which
enables human beings to work with the database in a manner to a degree
similar to other SCM tools (like CVS, BitKeeper or Monotone).

%package all
Summary: Meta-package to pull in all git tools
Group: Development/Tools
Requires: emacs-git = %{version}-%{release}
Requires: git = %{version}-%{release}
Requires: git-arch = %{version}-%{release}
Requires: git-cvs = %{version}-%{release}
Requires: git-email = %{version}-%{release}
Requires: git-gui = %{version}-%{release}
Requires: git-svn = %{version}-%{release}
Requires: gitk = %{version}-%{release}
Requires: perl-Git = %{version}-%{release}
Obsoletes: git <= 1.5.4.3

%description all
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This is a dummy package which brings in all subpackages.

%package arch
Summary: Git tools for importing Arch repositories
Group: Development/Tools
Requires: %{name} = %{version}-%{release}
#Requires: tla

%description arch
Git tools for importing Arch repositories.

%package cvs
Summary: Git tools for importing CVS repositories
Group: Development/Tools
Requires: cvs
Requires: cvsps
Requires: %{name} = %{version}-%{release}

%description cvs
Git tools for importing CVS repositories.

%package daemon
Summary: Git protocol daemon
Group: Development/Tools
Requires: %{name} = %{version}-%{release}
Requires: xinetd

%description daemon
The git daemon for supporting git:// access to git repositories

%package email
Summary: Git tools for sending email
Group: Development/Tools
Requires: %{name} = %{version}-%{release}
Requires: perl-Git = %{version}-%{release}
Requires: perl(Authen::SASL::Perl)
Requires: perl(Email::Valid)
Requires: perl(Mail::Address)
Requires: perl(Net::Domain)
Requires: perl(Net::SMTP::SSL)
Requires: perl(Sys::Hostname)

%description email
Git tools for sending email.

%package gui
Summary: Graphical frontend to git
Group: Development/Tools
Requires: %{name} = %{version}-%{release}
Requires: tk >= 8.4
Requires: gitk = %{version}-%{release}

%description gui
Graphical frontend to git.

%package svn
Summary: Git tools for importing Subversion repositories
Group: Development/Tools
Requires: %{name} = %{version}-%{release}
Requires: perl(Error)
Requires: perl(Term::ReadKey)
Requires: subversion

%description svn
Git tools for importing Subversion repositories.

%package -n emacs-git
Summary: Git version control system support for Emacs
Group: Applications/Editors
Requires: %{name} = %{version}-%{release}
Requires: emacs-common

%description -n emacs-git
%{summary}.

%package -n gitk
Summary: Git revision tree visualiser
Group: Development/Tools
Requires: %{name} = %{version}-%{release}
Requires: tk >= 8.4

%description -n gitk
Git revision tree visualiser.

%package -n gitweb
Summary: Simple web interface to git repositories
Group: Development/Tools
Requires: %{name} = %{version}-%{release}

%description -n gitweb
Simple web interface to track changes in git repositories

%package -n perl-Git
Summary: Perl module that implements Git bindings
Group: Applications/CPAN
Requires: %{name} = %{version}-%{release}

%description -n perl-Git
Git is a Perl module that implements Git bindings.

%prep
%setup
%patch0 -p1
%patch1 -p1

%{__cat} <<EOF >config.mak
V = 1
CFLAGS = %{optflags}
BLK_SHA1 = 1
NEEDS_CRYPTO_WITH_SSL = 1
NO_PYTHON = 1
ETC_GITCONFIG = %{_sysconfdir}/gitconfig
DESTDIR = %{buildroot}
INSTALL = install -p
GITWEB_PROJECTROOT = %{_localstatedir}/lib/git
htmldir = %{_docdir}/%{name}-%{version}
prefix = %{_prefix}
INSTALLDIRS = vendor
mandir = %{_mandir}
WITH_OWN_SUBPROCESS_PY = YesPlease
ASCIIDOC_EXTRA = --unsafe
EOF

%{__cat} <<EOF >git.xinetd
# default: off
# description: The git daemon allows git repositories to be exported using \
#       the git:// protocol.

service git
{
        disable         = yes

        # git is in /etc/services only on RHEL5+
        #type            = UNLISTED
        #port            = 9418

        socket_type     = stream
        wait            = no
        user            = nobody
        server          = %{_libexecdir}/git-core/git-daemon
        server_args     = --base-path=%{_localstatedir}/lib/git --export-all --user-path=public_git --syslog --inetd --verbose
        log_on_failure  += USERID
        # xinetd does not enable IPv6 by default
        # flags           = IPv6
}
EOF

%{__cat} <<EOF >git-gui.desktop
[Desktop Entry]
Name=Git GUI
GenericName=Git GUI
Comment=A graphical interface to Git
Exec=git gui
Icon=%{_datadir}/git-gui/lib/git-gui.ico
Terminal=false
Type=Application
Categories=Development;
EOF

%{__cat} <<EOF >gitweb/gitweb.httpd
Alias /git %{_datadir}/gitweb

<Directory %{_datadir}/gitweb>
    Options +ExecCGI
    AddHandler cgi-script .cgi
    DirectoryIndex gitweb.cgi
</Directory>
EOF

%{__sed} -e "s|@PROJECTROOT@|%{_localstatedir}/lib/git|g" %{SOURCE5} >gitweb.conf

%build
%{__make} %{?_smp_mflags} all

# bah, DocBook validation errors
%{__perl} -pi -e 's|^XMLTO_EXTRA =\s*$|XMLTO_EXTRA = --skip-validation \n|;' Documentation/Makefile

%{__make} %{?_smp_mflags} doc

## Perl preparation
cd perl
%{__perl} Makefile.PL DESTDIR="%{buildroot}" PREFIX="%{_prefix}" INSTALLDIRS="vendor"
#%{__make} %{?_smp_mflags}
cd -

# Remove shebang from bash-completion script
sed -i '/^#!bash/,+1 d' contrib/completion/git-completion.bash

%install
%{__rm} -rf %{buildroot}
%{__make} install install-doc DESTDIR="%{buildroot}"

%{__make} -C contrib/emacs install emacsdir="%{buildroot}%{_datadir}/emacs/site-lisp"
for elc in %{buildroot}%{_datadir}/emacs/site-lisp/*.elc; do
    %{__install} -p -m0644 contrib/emacs/$(basename $elc .elc).el %{buildroot}%{_datadir}/emacs/site-lisp/
done
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_datadir}/emacs/site-lisp/site-start.d/git-init.el

### Perl installation
#%makeinstall -C perl INSTALLDIRS="vendor"

#%{__install} -d -m0755 %{buildroot}%{_localstatedir}/www/git/static/
#%{__install} -p -m0644 gitweb/*.{css,js,png} %{buildroot}%{_localstatedir}/www/git/
#%{__install} -p -m0755 gitweb/gitweb.cgi %{buildroot}%{_localstatedir}/www/git/
#%{__cp} -av gitweb/static/* %{buildroot}%{_localstatedir}/www/git/static/
%{__install} -Dp -m0644 gitweb/gitweb.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/git.conf
%{__install} -Dp -m0644 gitweb.conf %{buildroot}%{_sysconfdir}/gitweb.conf

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/git/
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/xinetd.d/
%{__install} -Dp -m0644 git.xinetd %{buildroot}%{_sysconfdir}/xinetd.d/git

%{__install} -Dp -m0644 contrib/completion/git-completion.bash %{buildroot}%{_sysconfdir}/bash_completion.d/git

# Move contrib/hooks out of %%docdir and make them executable
%{__install} -d -m0755 %{buildroot}%{_datadir}/git-core/contrib/
%{__mv} -v contrib/hooks %{buildroot}%{_datadir}/git-core/contrib
chmod +x %{buildroot}%{_datadir}/git-core/contrib/hooks/*
pushd contrib > /dev/null
ln -s ../../../git-core/contrib/hooks
popd > /dev/null

desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir=%{buildroot}%{_datadir}/applications \
    git-gui.desktop

### Quiet some rpmlint complaints
chmod -R g-w %{buildroot}
find %{buildroot} -name git-mergetool--lib | xargs chmod a-x
rm -f {Documentation/technical,contrib/emacs}/.gitignore
chmod a-x Documentation/technical/api-index.sh
find contrib -type f | xargs chmod -x

### Clean up buildroot
find %{buildroot}%{_bindir} -type f -exec %{__perl} -pi -e 's|^%{buildroot}||' {} \;
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch} %{buildroot}%{_datadir}/locale/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Documentation/*.txt README
%doc %{_mandir}/man1/*.1*
%doc %{_mandir}/man5/*.5*
%doc %{_mandir}/man7/*.7*
%config %{_sysconfdir}/bash_completion.d/
%{_bindir}/git
%{_bindir}/git-*
%{_datadir}/git-core/
%{_libexecdir}/git-core/
%exclude %{_libexecdir}/git-core/git-citool
%exclude %{_libexecdir}/git-core/git-cvsexportcommit
%exclude %{_libexecdir}/git-core/git-cvsimport
%exclude %{_libexecdir}/git-core/git-cvsserver
%exclude %{_libexecdir}/git-core/git-daemon
%exclude %{_libexecdir}/git-core/git-gui
%exclude %{_libexecdir}/git-core/git-gui--askpass
%exclude %{_libexecdir}/git-core/git-send-email
%exclude %{_libexecdir}/git-core/git-svn

%files all
%defattr(-, root, root, 0755)

%files arch
%defattr(-, root, root, 0755)
%{_libexecdir}/git-core/git-archimport

%files cvs
%defattr(-, root, root, 0755)
%{_bindir}/git-cvsserver
%{_libexecdir}/git-core/git-cvsexportcommit
%{_libexecdir}/git-core/git-cvsimport
%{_libexecdir}/git-core/git-cvsserver

%files daemon
%defattr(-, root, root, 0755)
%doc Documentation/*daemon*.txt
#%doc %{_mandir}/man1/*daemon*.1*
%config(noreplace)%{_sysconfdir}/xinetd.d/git
%{_libexecdir}/git-core/git-daemon
%{_localstatedir}/lib/git/

%files email
%defattr(-, root, root, 0755)
%{_libexecdir}/git-core/git-send-email

%files gui
%defattr(-, root, root, 0755)
%{_datadir}/applications/%{desktop_vendor}-git-gui.desktop
%{_datadir}/git-gui/
%{_libexecdir}/git-core/git-citool
%{_libexecdir}/git-core/git-gui
%{_libexecdir}/git-core/git-gui--askpass

%files svn
%defattr(-, root, root, 0755)
%{_libexecdir}/git-core/git-svn

%files -n emacs-git
%defattr(-,root,root)
%{_datadir}/emacs/site-lisp/*git*.el*
%{_datadir}/emacs/site-lisp/site-start.d/git-init.el

%files -n gitk
%defattr(-,root,root)
%doc Documentation/*gitk*.txt
%{_bindir}/gitk
%{_datadir}/gitk/

%files -n gitweb
%defattr(-, root, root, 0755)
%doc gitweb/GITWEB-BUILD-OPTIONS gitweb/INSTALL gitweb/README
%config(noreplace) %{_sysconfdir}/gitweb.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/git.conf
%{_datadir}/gitweb/

%files -n perl-Git
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/Git.3pm*
%doc %{_mandir}/man3/Git::I18N.3pm*
%doc %{_mandir}/man3/Git::SVN::Editor.3pm.gz
%doc %{_mandir}/man3/Git::SVN::Fetcher.3pm.gz
%doc %{_mandir}/man3/Git::SVN::Memoize::YAML.3pm.gz
%doc %{_mandir}/man3/Git::SVN::Prompt.3pm.gz
%doc %{_mandir}/man3/Git::SVN::Ra.3pm.gz
%{perl_vendorlib}/Git.pm
%{perl_vendorlib}/Git/I18N.pm
%{perl_vendorlib}/Git/SVN/Editor.pm
%{perl_vendorlib}/Git/SVN/Fetcher.pm
%{perl_vendorlib}/Git/SVN/Memoize/YAML.pm
%{perl_vendorlib}/Git/SVN/Prompt.pm
%{perl_vendorlib}/Git/SVN/Ra.pm

%changelog
* Tue Jun 19 2012 David Hrbáč <david@hrbac.cz> - 1.7.11-1
- new upstream release

* Mon Jun 04 2012 David Hrbáč <david@hrbac.cz> - 1.7.10.4-1
- new upstream release

* Mon May 28 2012 David Hrbáč <david@hrbac.cz> - 1.7.10.3-1
- new upstream release

* Tue May 22 2012 David Hrbáč <david@hrbac.cz> - 1.7.10.2-1
- new upstream release

* Wed May 02 2012 David Hrbáč <david@hrbac.cz> - 1.7.10.1-1
- new upstream release

* Sat Apr 07 2012 David Hrbáč <david@hrbac.cz> - 1.7.10-1
- new upstream release

* Thu Apr  5 2012 Steve Huff <shuff@vecna.org> - 1.7.9.6-1
- new upstream release

* Fri Mar 30 2012 David Hrbáč <david@hrbac.cz> - 1.7.9.5-1
- new upstream release

* Sat Mar 17 2012 David Hrbáč <david@hrbac.cz> - 1.7.9.4-1
- new upstream release

* Tue Mar 06 2012 David Hrbáč <david@hrbac.cz> - 1.7.9.3-1
- new upstream release

* Mon Feb 27 2012 David Hrbáč <david@hrbac.cz> - 1.7.9.2-1
- new upstream release

* Mon Feb 27 2012 David Hrbáč <david@hrbac.cz> - 1.7.9.1-1
- new upstream release

* Wed Jan  4 2012 Steve Huff <shuff@vecna.org> - 1.7.8.2-1
- Updated to release 1.7.8.2.

* Mon Dec 12 2011 Steve Huff <shuff@vecna.org> - 1.7.8-1
- Updated to release 1.7.8.
- Captured additional Perl dependencies in git-email.

* Sun Nov 20 2011 Steve Huff <shuff@vecna.org> - 1.7.7.4-1
- Updated to release 1.7.7.4.
- No more custom Error perl module.

* Tue Nov 15 2011 David Hrbáč <david@hrbac.cz> - 1.7.7.2-2
- emacs to build requirements

* Mon Nov 14 2011 David Hrbáč <david@hrbac.cz> - 1.7.7.2-1
- new upstream release

* Wed Oct 26 2011 Steve Huff <shuff@vecna.org> - 1.7.7.1-1
- Updated to release 1.7.7.1.
- post-receive-email hook patch no longer applicable.

* Tue Sep 27 2011 Steve Huff <shuff@vecna.org> - 1.7.6.4-1
- Updated to release 1.7.6.4.
- Source comes from Google Code now.

* Wed Aug 31 2011 Steve Huff <shuff@vecna.org> - 1.7.6.1-1
- Updated to release 1.7.6.1.

* Sun Jul 03 2011 Steve Huff <shuff@vecna.org> - 1.7.6-1
- Updated to release 1.7.6.

* Thu Jun 02 2011 Steve Huff <shuff@vecna.org> - 1.7.5.4-1
- Updated to release 1.7.5.4.

* Tue May 31 2011 Steve Huff <shuff@vecna.org> - 1.7.5.3-1
- Updated to release 1.7.5.3.

* Mon May 23 2011 Steve Huff <shuff@vecna.org> - 1.7.5.2-1
- Updated to release 1.7.5.2.

* Tue May 10 2011 Steve Huff <shuff@vecna.org> - 1.7.5.1-1
- Updated to release 1.7.5.1.

* Wed Apr 27 2011 Steve Huff <shuff@vecna.org> - 1.7.5-1
- Updated to release 1.7.5.

* Wed Jan 05 2011 Steve Huff <shuff@vecna.org> - 1.7.3.4-1
- Updated to release 1.7.3.4.
- Captured missing perl(Error) dependency in git-svn (thanks Seán O'Sullivan!)
- Some man pages were persistently failing DocBook validation :(

* Fri Sep 24 2010 Steve Huff <shuff@vecna.org> - 1.7.3-1
- Updated to release 1.7.3.

* Sat Aug 21 2010 Dag Wieers <dag@wieers.com> - 1.7.2.2-1
- Updated to release 1.7.2.2.

* Fri Jul 09 2010 Dag Wieers <dag@wieers.com> - 1.7.1.1-2
- Added missing documentation.

* Sun Jul 04 2010 Dag Wieers <dag@wieers.com> - 1.7.1.1-1
- Updated to release 1.7.1.1.

* Mon Jun 28 2010 Dag Wieers <dag@wieers.com> - 1.7.1-3
- Split out arch/cvs/email/svn as Fedora does. (Tom G. Christensen)

* Wed Jun 23 2010 Dag Wieers <dag@wieers.com> - 1.7.1-2
- Fix for perl(packed-refs), sigh.

* Sat Jun 19 2010 Dag Wieers <dag@wieers.com> - 1.7.1-1
- Updated to release 1.7.1. (based on Fedora)

* Sun Nov 25 2007 Dag Wieers <dag@wieers.com> - 1.5.2.1-2
- Fix group tag.

* Mon Jun 11 2007 Dag Wieers <dag@wieers.com> - 1.5.2.1-1
- Update to release 1.5.2.1.

* Sat Jun 09 2007 Dag Wieers <dag@wieers.com> - 1.5.0.6-1
- Update to release 1.5.0.6.

* Wed Feb 14 2007 Dries Verachtert <dries@ulyssis.org> - 0.99.4-3
- Fix location of templates (Dave Miller).
- Option '--unsafe' added to call to asciidoc.
- Fix asciidoc problem with '^'.

* Sun Aug 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.99.4-1
- Update to release 0.99.4.

* Wed Aug 10 2005 Dag Wieers <dag@wieers.com> - 0.99.1-1
- Small cleanup.
- Added documentation using asciidoc.

* Wed Jul 07 2005 Chris Wright <chris@osdl.org> - 0.99-1
- Initial git spec file.
