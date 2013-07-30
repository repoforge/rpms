%global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%{?el4:%define _without_bzr 1}

Name:      etckeeper
Version:   1.6
Release:   1%{?dist}
Summary:   Store /etc in a SCM system (git, mercurial, bzr or darcs)
Group:     Applications/System
License:   GPLv2+
URL:       http://kitenet.net/~joey/code/etckeeper/
Source:    http://ftp.debian.org/debian/pool/main/e/%{name}/%{name}_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires:  git >= 1.5.4

%description
The etckeeper program is a tool to let /etc be stored in a git,
mercurial, bzr or darcs repository. It hooks into yum to automatically
commit changes made to /etc during package upgrades. It tracks file
metadata that version control systems do not normally support, but that
is important for /etc, such as the permissions of /etc/shadow. It's
quite modular and configurable, while also being simple to use if you
understand the basics of working with version control.

The default backend is git, if want to use a another backend please
install the appropriate tool (mercurial, darcs or bzr).
To use bzr as backend, please also install the %{name}-bzr package.

To start using the package please read %{_docdir}/%{name}-%{version}/README

%package bzr
Summary:  Support for bzr with etckeeper
Group:    Applications/System
Requires: %{name} = %{version}-%{release} bzr
%{!?_without_bzr:BuildRequires: bzr}
BuildRequires: python-devel

%description bzr
This package provides a bzr backend for etckeeper, if you want to use
etckeeper with bzr backend, install this package.

%prep
%setup -q -n %{name}
%{__perl} -pi -e '
    s|HIGHLEVEL_PACKAGE_MANAGER=apt|HIGHLEVEL_PACKAGE_MANAGER=yum|;
    s|LOWLEVEL_PACKAGE_MANAGER=dpkg|LOWLEVEL_PACKAGE_MANAGER=rpm|;
    s|#AVOID_DAILY_AUTOCOMMITS=1|AVOID_DAILY_AUTOCOMMITS=1|;
    ' etckeeper.conf
%{__sed} -i -e '1d' yum-etckeeper.py

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"
%{__install} -D -p debian/cron.daily %{buildroot}%{_sysconfdir}/cron.daily/%{name}
%{__install} -d  %{buildroot}%{_localstatedir}/cache/%{name}
%{!?_without_bzr: %{__sed} -i -e '1d' %{buildroot}%{python_sitelib}/bzrlib/plugins/%{name}/__init__.py }

%clean
rm -rf %{buildroot}

# Users must study the README anyway.
#post
#{_sbindir}/%{name} init -d /etc/

%post
if [ $1 -gt 1 ] ; then
   %{_bindir}/%{name} update-ignore
fi

%files
%defattr(-, root, root, -)
%doc GPL TODO README
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/*.d
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{_sysconfdir}/cron.daily/%{name}
%dir %{_sysconfdir}/bash_completion.d
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%dir %{_prefix}/lib/yum-plugins
%{_prefix}/lib/yum-plugins/%{name}.*
%dir %{_sysconfdir}/yum/pluginconf.d
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/%{name}.conf
%{_localstatedir}/cache/%{name}

%if 0%{!?_without_bzr:1}
%files bzr
%defattr(-, root, root, -)
%doc GPL
%{python_sitelib}/bzrlib/plugins/%{name}
%if 0%{?fedora} || 0%{?rhel} > 5
%{python_sitelib}/bzr_%{name}-*.egg-info
%endif
%endif

%changelog
* Tue Jul 30 2013 David Hrbáč <david@hrbac.cz> - 1.6-1
- new upstream release

* Wed May 15 2013 David Hrbáč <david@hrbac.cz> - 1.33-1
- new upstream release

* Tue May 07 2013 David Hrbáč <david@hrbac.cz> - 1.1-1
- new upstream release

* Wed Oct 31 2012 David Hrbáč <david@hrbac.cz> - 0.64-1
- enabled AVOID_DAILY_AUTOCOMMITS
- new upstream release

* Wed Jun 20 2012 David Hrbáč <david@hrbac.cz> - 0.63-1
- new upstream release

* Wed Apr 11 2012 David Hrbáč <david@hrbac.cz> - 0.62-1
- new upstream release

* Thu Jan 12 2012 David Hrbáč <david@hrbac.cz> - 0.60-1
- new upstream release

* Thu Jan 12 2012 David Hrbáč <david@hrbac.cz> - 0.59-1
- new upstream release
- removed missing README.fedora

* Wed Dec 07 2011 David Hrbáč <david@hrbac.cz> - 0.58-1
- new upstream release

* Wed Dec 07 2011 David Hrbáč <david@hrbac.cz> - 0.57-1
- new upstream release

* Mon Aug 29 2011 David Hrbáč <david@hrbac.cz> - 0.56-2
- Initial reruild
- Disable bzr on el4

* Wed Aug 17 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.56-2
- Rebuilt for trailing slash bug of rpm-4.9.1

* Thu Jul 21 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.56-1
- Update to 0.56.

* Fri Jun 24 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.55-1
- Update to 0.55.

* Wed Jun  1 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.54-1
- Update to 0.54.
- Add patch for bz 709487.

* Mon Mar 28 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.53-1
- Update to 0.53.
- Run update-ignore on package upgrade (bz 680632).

* Wed Feb  9 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.52-1
- Update to 0.52.
- Include a README.fedora (bz 670934).

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan  3 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.51-1
- Update to 0.51.
- etckeeper has been moved out of sbin.

* Sat Dec 11 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.50-2
- Don't package INSTALL.

* Wed Oct 27 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.50-1
- Update to 0.50.
- Change %%define -> %%global.

* Fri Sep 17 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.49-2
- Adjust minimum required version of GIT.
- egg-info files are not created automatically on RHEL5.

* Wed Sep 15 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.49-1
- Update to 0.49.
- Remove obsolete patch.

* Fri Sep  3 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.48-1
- Update to 0.48.
- Don't list /etc/etckeeper/*.d directories twice in %%files.
- Add patch from upstream that fixes bz 588086.

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.41-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Sep 12 2009 Bernie Innocenti <bernie@codewiz.org> - 0.41-1
- Update to 0.41
- Add missing directory ownerships

* Sat Sep 12 2009 Bernie Innocenti <bernie@codewiz.org> - 0.40-3
- Make the bzr subpackage builddepend on python-devel

* Wed Sep 09 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.40-2
- Package is noarch
- Rpmlint clean
- Random cleanup
- Ship cache dir in package
- bzr subpackage
- Add bzr to buildreq

* Sat Sep 05 2009 Bernie Innocenti <bernie@codewiz.org> - 0.40-1
- Update to 0.40

* Sun Jun 14 2009 Bernie Innocenti <bernie@codewiz.org> - 0.37-1
- Update to 0.37
- Change license tag to GPLv2+

* Fri Feb 27 2009 Jimmy Tang <jtang@tchpc.tcd.ie> - 0.33-4
- fix up initial install to make directory in /var/cache/etckeeper
- install the etckeeper daily cron job
- define some config files that shouldn't be replaced, should the hooks
in commit.d, init.d etc... saved and not blown away? if so they can
defined as config files. etckeeper should record the changes anyway.

* Wed Feb 25 2009 Jimmy Tang <jtang@tchpc.tcd.ie> - 0.32-1
- yum etckeeper plugin is now apart of this package

* Tue Feb 24 2009 Jimmy Tang <jtang@tchpc.tcd.ie> - 0.31-1
- initial package

