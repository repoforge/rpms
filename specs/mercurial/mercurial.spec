# $Id$
# Authority: yury
# Upstream: Matt Mackall <mpm$selenic,com>

### EL6 ships with mercurial-1.4-3.el6
%{?el6:# Tag: rfx}

%define pythonver %(python -c 'import sys;print ".".join(map(str, sys.version_info[:2]))')
%define emacs_lispdir %{_datadir}/emacs/site-lisp

Summary: Fast, lightweight Source Control Management system
Name: mercurial
Version: 2.2
Release: 1%{?dist}
License: GPLv2+
Group: Development/Tools
URL: http://mercurial.selenic.com/

Source0: http://mercurial.selenic.com/release/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python >= 2.4
BuildRequires: python-devel >= 2.4
BuildRequires: python-docutils >= 0.5
BuildRequires: make
BuildRequires: gcc
BuildRequires: gettext

Provides: hg = %{version}-%{release}

%description
Mercurial is a fast, lightweight source control management system designed
for efficient handling of very large distributed projects.

%package hgk
Summary: hgk GUI for mercurial
Group: Development/Tools
Requires: %{name} = %{version}-%{release}
Requires: tk

%description hgk
With hgk you can browse a repository graphically.

%package ssh
Summary: SSH wrapper for mercurial
Group: Development/Tools
Requires: %{name} = %{version}-%{release}

%description ssh
A wrapper for ssh access to a limited set of mercurial repos.

%prep
%setup

%build
CFLAGS="%{optflags}" %{__make} %{?_smp_mflags} all

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" PREFIX="%{_prefix}" MANDIR="%{_mandir}"

%{__install} -Dp -m0755 contrib/hgk %{buildroot}%{_bindir}/hgk
%{__install} -Dp -m0755 contrib/hg-ssh %{buildroot}%{_bindir}/hg-ssh
%{__install} -Dp -m0644 contrib/bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/mercurial.sh
%{__install} -Dp -m0644 contrib/zsh_completion %{buildroot}%{_datadir}/zsh/site-functions/_mercurial
%{__install} -Dp -m0644 contrib/mercurial.el %{buildroot}%{emacs_lispdir}/mercurial.el
%{__install} -Dp -m0644 contrib/mq.el %{buildroot}%{emacs_lispdir}/mq.el
%{__install} -Dp -m0644 contrib/mergetools.hgrc %{buildroot}%{_sysconfdir}/mercurial/hgrc.d/mergetools.rc

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CONTRIBUTORS COPYING doc/README doc/hg*.txt doc/hg*.html *.cgi contrib/*.fcgi
%doc %attr(644, root, root) %{_mandir}/man?/hg*
%doc %attr(644, root, root) contrib/*.svg contrib/sample.hgrc
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_mercurial
%dir %{_datadir}/emacs/site-lisp/
%{_datadir}/emacs/site-lisp/mercurial.el
%{_datadir}/emacs/site-lisp/mq.el
%{_bindir}/hg
%dir %{_sysconfdir}/bash_completion.d/
%config(noreplace) %{_sysconfdir}/bash_completion.d/mercurial.sh
%dir %{_sysconfdir}/mercurial
%dir %{_sysconfdir}/mercurial/hgrc.d
%config(noreplace) %{_sysconfdir}/mercurial/hgrc.d/mergetools.rc
%if "%{?pythonver}" != "2.4"
%{_libdir}/python%{pythonver}/site-packages/%{name}-*-py%{pythonver}.egg-info
%endif
%{_libdir}/python%{pythonver}/site-packages/%{name}
%{_libdir}/python%{pythonver}/site-packages/hgext

%files hgk
%defattr(-, root, root, 0755)
%{_bindir}/hgk

%files ssh
%defattr(-, root, root, 0755)
%{_bindir}/hg-ssh

%changelog
* Wed May 02 2012 David Hrbáč <david@hrbac.cz> - 2.2-1
- new upstream release

* Thu Apr 05 2012 David Hrbáč <david@hrbac.cz> - 2.1.2-1
- new upstream release

* Mon Mar 05 2012 David Hrbáč <david@hrbac.cz> - 2.1.1-1
- new upstream release

* Thu Feb 16 2012 David Hrbáč <david@hrbac.cz> - 2.1-1
- new upstream release

* Mon Jan 30 2012 David Hrbáč <david@hrbac.cz> - 2.0.2-1
- new upstream release

* Fri Sep 23 2011 Yury V. Zaytsev <yury@shurup.com> - 1.9.2-1
- Updated to release 1.9.2 (GH-61).

* Tue Jul 19 2011 Dag Wieers <dag@wieers.com> - 1.9-1
- Updated to release 1.9.

* Fri Jun 03 2011 David Hrbáč <david@hrbac.cz> - 1.8.4-1
- new upstream release

* Tue May 03 2011 David Hrbáč <david@hrbac.cz> - 1.8.3-1
- new upstream release

* Mon Apr 04 2011 David Hrbáč <david@hrbac.cz> - 1.8.2-1
- new upstream release

* Fri Mar 11 2011 David Hrbáč <david@hrbac.cz> - 1.8.1-1
- new upstream release

* Wed Mar 02 2011 David Hrbáč <david@hrbac.cz> - 1.8-1
- new upstream release

* Wed Jan 05 2011 David Hrbáč <david@hrbac.cz> - 1.7.3-1
- new upstream release

* Mon Dec 06 2010 David Hrbáč <david@hrbac.cz> - 1.7.2-1
- new upstream release

* Tue Nov 30 2010 Yury V. Zaytsev <yury@shurup.com> - 1.7.1-1
- Updated to release 1.7.1 (Tim Dettrick).

* Tue Oct 05 2010 Yury V. Zaytsev <yury@shurup.com> - 1.6.4-1
- Updated to release 1.6.4 (Tim Dettrick).

* Sun Mar 21 2010 Dag Wieers <dag@wieers.com> - 1.5-1
- Updated to release 1.5.

* Mon Jul 27 2009 Dag Wieers <dag@wieers.com> - 1.3.1-1
- Updated to release 1.3.1.

* Sat Jul 11 2009 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Updated to release 1.3.

* Wed Mar 25 2009 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Updated to release 1.2.1.

* Thu Mar 12 2009 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Updated to release 1.2.

* Thu Jan  1 2009 Dries Verachtert <dries@ulyssis.org> - 1.1.2-1
- Updated to release 1.1.2.

* Thu Dec 11 2008 Dries Verachtert <dries@ulyssis.org> - 1.1-1
- Updated to release 1.1.

* Mon Aug 18 2008 Dries Verachtert <dries@ulyssis.org> - 1.0.2-1
- Updated to release 1.0.2.

* Sun Jun 29 2008 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1
- Updated to release 1.0.1.

* Mon Mar 24 2008 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Updated to release 1.0.

* Sun Oct 21 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.5-1
- Updated to release 0.9.5.

* Wed Oct  3 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.4-2
- Added hgk as a subpackage, based on the PLD spec file started by arekm.

* Fri Jun 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.4-1
- Updated to release 0.9.4.

* Fri Jun 15 2007 Dag Wieers <dag@wieers.com> - 0.9.3-2
- Use %%{python_sitearch} to build for x86_64. (Tong Ho)
- Added contrib/.

* Tue Jun 05 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.3-1
- Initial package.
