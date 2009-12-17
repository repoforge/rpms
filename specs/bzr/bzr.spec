# $Id$
# Authority: yury
# Upstream: <bazaar$lists,canonical,com>

%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

# All package versioning is found here:
# the actual version is composed from these below, including leading 0 for release candidates
#   bzrmajor:  main bzr version
#   Version: bzr version, add subrelease version here
#   bzrrc: release candidate version, if any, line starts with % for rc, # for stable releas (no %).
#   release: rpm subrelease (0.N for rc candidates, N for stable releases)
%define bzrmajor 2.0
%define bzrminor .3
#define bzrrc rc2
%define release 1

# Magics to get the dots in Release string correct per the above
%define subrelease %{?bzrrc:.}%{?bzrrc}

Name:           bzr
Version:        %{bzrmajor}%{?bzrminor}
Release:        %{release}%{?subrelease}%{?dist}
Summary:        Friendly distributed version control system

Group:          Development/Tools
License:        GPLv2+
URL:            http://www.bazaar-vcs.org/
Source0:        https://launchpad.net/%{name}/%{bzrmajor}/%{version}%{?bzrrc}/+download/%{name}-%{version}%{?bzrrc}.tar.gz
Source1:        https://launchpad.net/%{name}/%{bzrmajor}/%{version}%{?bzrrc}/+download/%{name}-%{version}%{?bzrrc}.tar.gz.sig

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  python-devel zlib-devel
# We're using an old version of Pyrex, use the pregenerated C files instead
# of rebuilding
#BuildRequires: Pyrex
Requires:   python-paramiko
# Workaround Bug #230223 otherwise this would be a soft dependency
Requires:   python-curl

# ElementTree is part of python2.5 on FC7+
# This is also needed for EL-5
BuildRequires:   python-elementtree
Requires:   python-elementtree

%description
Bazaar is a distributed revision control system that is powerful, friendly,
and scalable.  It is the successor of Baz-1.x which, in turn, was
a user-friendly reimplementation of GNU Arch.

%prep
%setup -q -n %{name}-%{version}%{?bzrrc}

sed -i '1{/#![[:space:]]*\/usr\/bin\/\(python\|env\)/d}' bzrlib/_patiencediff_py.py
sed -i '1{/#![[:space:]]*\/usr\/bin\/\(python\|env\)/d}' bzrlib/weave.py

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

chmod a-x contrib/bash/bzrbashprompt.sh

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --install-data %{_datadir} --root $RPM_BUILD_ROOT
chmod 0644 contrib/bzr_access
chmod 0644 contrib/bzr_ssh_path_limiter
chmod 0755 $RPM_BUILD_ROOT%{python_sitearch}/bzrlib/*.so

install -d $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/
install -m 0644 contrib/bash/bzr $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/
rm contrib/bash/bzr

# This is included in %doc, remove redundancy here
#rm -rf $RPM_BUILD_ROOT%{python_sitearch}/bzrlib/doc/

# Use independently packaged python-elementtree instead
rm -rf $RPM_BUILD_ROOT%{python_sitearch}/bzrlib/util/elementtree/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc NEWS README TODO COPYING.txt doc/  contrib/
%{_bindir}/bzr
%{_mandir}/man1/*
%{python_sitearch}/bzrlib/
%{_sysconfdir}/bash_completion.d/

%changelog
* Thu Dec 17 2009 Steve Huff <shuff@vecna.org> - 2.0.3-1
- Updated to 2.0.3 release.
- RPMforge provides python-curl, not python-pycurl.

* Wed Nov 11 2009 Yury V. Zaytsev <yury@shurup.com> - 2.0.1-2
- Ported to RPMForge.

* Thu Oct 29 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 2.0.1-1
- Update to 2.0.1 bugfix release

* Fri Sep 25 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 2.0.0-1
- Update to 2.0.0

* Thu Sep 10 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 2.0.0-0.1rc2
- Update to 2.0rc2 with new default repository format 2a

* Wed Aug 26 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.18-1
- Update to 1.18

* Thu Aug 20 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.18-0.1.rc1
- Update to 1.18rc1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.17-1
- Update to 1.17

* Mon Jul 13 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.17-0.1.rc1
- Update to 1.17rc1

* Fri Jun 26 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.16.1-1
- Update to 1.16.1

* Thu Jun 18 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.16-1
- Update to 1.16

* Wed Jun 10 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.15.1-1
- Update to 1.15.1

* Sat May 23 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.15-2
- Update to 1.15final

* Sat May 16 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.15-0.1.rc1
- Update to 1.15rc1

* Sat May 02 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.14.1-1
- Update to 1.14.1

* Wed Apr 29 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.14-1
- Update to 1.14

* Mon Apr 20 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.14-0.3.rc2
- Update to 1.14rc2

* Sat Apr 11 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.14-0.2.rc1
- Correct build dependencies

* Thu Apr 09 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.14-0.1.rc1
- Update to 1.14rc1

* Tue Mar 24 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.13.1-1
- Update to 1.13.1

* Mon Mar 16 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.13-1
- Update to 1.13

* Tue Mar 10 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.13-0.1.rc1
- Update to 1.13rc1

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.12-1
- Update to 1.12

* Tue Feb 10 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.12-0.1.rc1
- Update to 1.12rc1

* Mon Jan 19 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.11-1
- Update to 1.11

* Wed Dec 10 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 1.10-1
- Update to 1.10

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.9-2
- Rebuild for Python 2.6

* Thu Nov 13 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 1.9-1
- Update to 1.9

* Thu Sep 25 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 1.7-1
- 1.7 Final

* Wed Sep 3 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 1.7-0.1.rc2
- 1.7rc2
- Remove executable permission from a %%doc file

* Wed Sep 3 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 1.6.1-0.1.rc2
- New upstream bugfix release.

* Thu May 21 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 1.5-2
- Upload tarball.

* Wed May 21 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 1.5-1
- Update to 1.5.

* Thu May 15 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 1.4-2
- Workaround upstream Bug# 230223 by Requiring python-pycurl.

* Mon May 5 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 1.4-1
- Update to 1.4.

* Sun Apr 27 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.1-1
- Paramiko/sftp backport from 1.4.0. bz#444325
- Update to 1.3.1 final.

* Sat Apr 4 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.1-0.1.rc1
- Update to 1.3.1rc1 to fix a bug when you have a pack based remote repo and
  knit based local branch.

* Wed Mar 26 2008 Warren Togami <wtogami@redhat.com> - 1.3-1
- Update to 1.3.

* Mon Feb 25 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2-1
- Update to 1.2.

* Fri Feb 8 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1-2
- Rebuild for new gcc.

* Mon Jan 21 2008 Toshio Kuratomi <a.badger@gmail.com> - 1.1-1
- Upstream 1.1 bugfix and performance enhancement release.
- Enable bash completion script from the contrib directory.

* Thu Dec 13 2007 Toshio Kuratomi <a.badger@gmail.com> - 1.0-1
- Update to 1.0 final.

* Tue Dec 11 2007 Toshio Kuratomi <a.badger@gmail.com> - 1.0-0.1.rc3
- Update to 1.0rc3
- The new rawhide python package generates egg-info files.

* Fri Nov 30 2007 Toshio Kuratomi <a.badger@gmail.com> - 1.0-0.1.rc2
- Update to 1.0rc2

* Tue Aug 28 2007 Toshio Kuratomi <a.badger@gmail.com> - 0.91-1
- Update to 0.91.
  + Fixes some issues with using tag-enabled branches.

* Tue Aug 28 2007 Toshio Kuratomi <a.badger@gmail.com> - 0.90-1
- Update to 0.90

* Mon Aug 27 2007 Toshio Kuratomi <a.badger@gmail.com> - 0.90-0.1.rc1
- Update to 0.90rc1.
- 0.90 contains some pyrex code to speed things up.  bzr is now arch specific.
- Update license tag.

* Wed Jul 25 2007 Warren Togami <wtogami@redhat.com> - 0.18-1
- Update to 0.18.

* Tue Jun 26 2007 Warren Togami <wtogami@redhat.com>  - 0.17-2
- Update to 0.17.

* Tue May 08 2007 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.16-1
- Update to 0.16.

* Thu Mar 22 2007 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.15-1
- Update to 0.15.
- Simplify the %%files list.

* Tue Jan 23 2007 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.14-1
- Update to 0.14

* Sun Dec 10 2006 Toshio Kuratomi <toshio@tiki-lounge.com> 0.13-2
- Conditionalize the python-elementtree requires as python2.5 in FC7 includes
  elementtree

* Wed Dec 6 2006 Toshio Kuratomi <toshio@tiki-lounge.com> 0.13-1
- Update to 0.13

* Thu Oct 30 2006 Toshio Kuratomi <toshio@tiki-lounge.com> 0.12-1
- Update to 0.12

* Thu Oct 08 2006 Toshio Kuratomi <toshio@tiki-lounge.com> 0.11-1
- Update to 0.11
- New download location.

* Sun Sep 17 2006 Warren Togami <wtogami@redhat.com> 0.10-1
- 0.10

* Fri Aug 11 2006 Shahms E. King <shahms@shahms.com> 0.9-1
- Update to new upstream

* Fri Aug 11 2006 Shahms E. King <shahms@shahms.com> 0.8.2-3
- Include, don't ghost .pyo files per new guidelines

* Mon Jun 26 2006 Shahms E. King <shahms@shahms.com> 0.8.2-2
- Require python-paramiko for sftp support

* Tue May 23 2006 Shahms E. King <shahms@shahms.com> 0.8.2-1
- Update to new upstream version
- Fix dist tag

* Wed May 10 2006 Shahms E. King <shahms@shahms.com> 0.8-1
- Update to new upstream version
- Update bzr-sys-etree.patch for changes

* Mon Feb 13 2006 Shahms E. King <shahms@shahms.com> 0.7-3
- Add python-elementtree to BuildRequires

* Mon Feb 13 2006 Shahms E. King <shahms@shahms.com> 0.7-2
- Add dist tag

* Fri Feb 10 2006 Shahms E. King <shahms@shahms.com> 0.7-1
- Update to 0.7

* Thu Jan 26 2006 Shahms E. King <shahms@shahms.com> 0.6.2-2
- Fix system library patch

* Wed Dec 07 2005 Shahms E. King <shahms@shahms.com> 0.6.2-1
- Initial package
