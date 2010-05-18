# $Id$
# Authority: yury
# Upstream: <bazaar$lists,canonical,com>

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

# Oh the horrors of arch dependent noarch packages!
# (bzrlib is arch dependent.  Thus bzrlib plugins are also arch dependent.)
%define debug_package %{nil}

%define bzrver 2.1
%define bzrnextver 2.2

Name: bzrtools
Version: %{bzrver}.0
Release: 1%{?dist}
Summary: A collection of utilities and plugins for Bazaar-NG

Group:   Development/Tools
License: GPLv2+
URL:     http://bazaar-vcs.org/BzrTools
Source0: http://launchpad.net/bzrtools/trunk/%{version}/+download/bzrtools-%{version}.tar.gz
Source1: http://launchpad.net/bzrtools/trunk/%{version}/+download/bzrtools-%{version}.tar.gz.sig

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  python-devel
# Bzrtools is meant to work with a version of bzr that is the same major
# version.  In addition to being incompatible with older bzr versions, it is 
# also untested with bzrversion++ and may not work (depending on what has
# changed between releases.). But releases often lag behind slightly so
# we allow one revision difference, hoping that it will work..
Requires:   bzr >= %{bzrver}, bzr <= %{bzrnextver}

%description
BzrTools is a collection of plugins for Bazaar-NG (bzr).  Among the included
plugins are:
* rspush - uses rsync to push local changes to a remote server
* annotate - prints a file annotated with the revision next to each line
* baz-import - (Requres PyBaz) import an arch archive losslessly into bzr
* shelve/unshelve - allows you to undo some changes, commit, and restore
* clean-tree - remove unknown, ignored-junk, or unversioned files from the tree
* graph-ancestry - use dot to produce banch ancestry graphs
* shell - a bzr command interpreter with command completion
* patch - apply a patch to your tree from a file or URL

%prep
%setup -q -n %{name}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT
if test "%{python_sitelib}" != "%{python_sitearch}" ; then
    install -d $RPM_BUILD_ROOT/%{python_sitearch}
    mv $RPM_BUILD_ROOT/%{python_sitelib}/* $RPM_BUILD_ROOT/%{python_sitearch}/
fi

# remove shebangs from all files as none should be executable scripts
sed -e '/^#!\//,1 d' -i $RPM_BUILD_ROOT/%{python_sitearch}/bzrlib/plugins/bzrtools/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README NEWS COPYING
%{python_sitearch}/bzrlib/plugins/bzrtools

%changelog
* Tue May 18 2010 Steve Huff <shuff@vecna.org> - 2.1.0-1
- Update to 2.1.0 for bzr-2.1.5.

* Wed Nov 11 2009 Yury V. Zaytsev <yury@shurup.com> - 2.0.1-2
- Ported to RPMForge.

* Sat Sep 26 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 2.0.1-1
- Update to 2.0.1

* Thu Sep 10 2009 Henrik Nordstrom <henrik@henriknordstrom.net> 2.0.0-1
- Update to 2.0.0 for bzr 2.0

* Thu Aug 20 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.18.0-2
- Update to 1.18.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.17.0-1
- Update to 1.17.0

* Sat Jun 13 2009 Henrik Nordstrom <henrik@henriknordstrom.net> 1.16.0-1
- Update to 1.16.0

* Fri Jun 12 2009 Henrik Nordstorm <henrik@henriknordstrom.net> 1.15.0-3
- Relax dependencies slightly to accept bzr 1.16rc1

* Thu May 28 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.15.0-2
- Update to 1.15.0

* Sat May 23 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.14.0-2
- Relax dependencies slightly as 1.14.0 works with bzr-1.15

* Sat Apr 11 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.14.0-1
- Update to 1.14.0

* Wed Mar 11 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.13.0-1
- Update to 1.13.0

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.12.0-1
- Update to 1.12.0

* Mon Jan 19 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.11.0-1
- Update to 1.11.0

* Fri Dec 12 2008 Henrik Nordstrom <henrik@henriknordstrom.net> 1.10.0-3
- correct changelog

* Thu Dec 11 2008 Henrik Nordstrom <henrik@henriknordstrom.net> - 1.10.0-2
- Minor packaging bugfix

* Wed Dec 10 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 1.10.0-1
- Update to 1.10.0

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.9.1-2
- Rebuild for Python 2.6

* Thu Nov 13 2008 Toshio Kuratomi <toshio@fedoraproject.org> 1.9.1-1
- Update to 1.9.1

* Thu Sep 18 2008 Toshio Kuratomi <toshio@fedoraproject.org> 1.7.0-1
- Update to 1.7.0

* Wed Sep 3 2008 Toshio Kuratomi <toshio@fedoraproject.org> 1.6.0-1
- Update to 1.6.0

* Wed May 21 2008 Toshio Kuratomi <toshio@fedoraproject.org> 1.5.0-1
- Update to 1.5.0

* Mon May 5 2008 Toshio Kuratomi <toshio@fedoraproject.org> 1.4.0-1
- Update to 1.4.0

* Wed Mar 26 2008 Warren Togami <wtogami@redhat.com> 1.3.0-1
- 1.3.0

* Mon Feb 25 2008 Toshio Kuratomi <toshio@fedoraproject.org> 1.2.0-1
- Update to 1.2.0

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.0-2
- Autorebuild for GCC 4.3

* Mon Jan 21 2008 Toshio Kuratomi <toshio@fedoraproject.org> 1.1.0-1
- Update to 1.1.

* Fri Dec 7 2007 Toshio Kuratomi <a.badger@gmail.com> 1.0.0-2
- Move the egg-info into sitearch alongside the module

* Fri Dec 7 2007 Toshio Kuratomi <a.badger@gmail.com> 1.0.0-1
- Update to 1.0.

* Wed Sep 26 2007 Toshio Kuratomi <a.badger@gmail.com> 0.91.0-1
- Update to 0.91.0.

* Thu Aug 30 2007 Toshio Kuratomi <a.badger@gmail.com> 0.90.0-2
- Move plugin manually since setuptools has no way of knowing that bzr is
  arch specific.
- Disable debuginfo packages.

* Tue Aug 28 2007 Toshio Kuratomi <a.badger@gmail.com> 0.90.0-1
- Update to 0.90.0.
- Fix License tag to conform to the new Licensing Guidelines.
- Bzr is now arch specific so all its plugins have to be as well.

* Wed Jul 25 2007 Warren Togami <wtogami@redhat.com> 0.18.0-1
- Update to 0.18.0.

* Thu Jun 28 2007 Warren Togami <wtogami@redhat.com> 0.17.1-1
- Update to 0.17.1.

* Mon Apr 2 2007 Toshio Kuratomi <toshio@tiki-lounge.com> 0.15.4-2
- Bump for tagging problem.

* Thu Mar 22 2007 Toshio Kuratomi <toshio@tiki-lounge.com> 0.15.4-1
- Update to 0.15.4.

* Tue Jan 23 2007 Toshio Kuratomi <toshio@tiki-lounge.com> 0.14.0-1
- Update to 0.14.0.

* Sat Jan 13 2007 Toshio Kuratomi <toshio@tiki-lounge.com> 0.13.0-2
- Update the dependencies to reflect the fact that bzrtools is meant to work
  with bzr of the same major version. (Thanks to Aaron Bentley for pointing
  this out.)

* Wed Dec 06 2006 Toshio Kuratomi <toshio@tiki-lounge.com> 0.13.0-1
- Update to 0.13.0

* Mon Nov 06 2006 Toshio Kuratomi <toshio@tiki-lounge.com> 0.12.2-2
- Add the tests directory as bzr has an undocumented "selftest" subcommand
  that relies on them.

* Thu Oct 05 2006 Toshio Kuratomi <toshio@tiki-lounge.com> 0.12.2-1
- Update to 0.12.2
- The push command was renamed to rspush.  Update the %%description to match.

* Thu Oct 05 2006 Toshio Kuratomi <toshio@tiki-lounge.com> 0.11.0-1
- Update to 0.11.0

* Sun Sep 17 2006 Warren Togami <wtogami@redhat.com> 0.10.0-2
- 0.10.0

* Sat Sep 16 2006 Shahms E. King <shahms@shahms.com> 0.9.1-2
- Rebuild for FC6

* Thu Aug 17 2006 Shahms E. King <shahms@shahms.com> 0.9.1-1
- Update to new upstream version

* Fri Aug 11 2006 Shahms E. King <shahms@shahms.com> 0.9-1
- Update to new upstream version

* Fri Aug 11 2006 Shahms E. King <shahms@shahms.com> 0.8.1-5
- Include, don't ghost .pyo files per new guidelines

* Wed May 24 2006 Shahms E. King <shahms@shahms.com> 0.8.1-4
- Require bzr >= 0.8, rather than only 0.8

* Tue May 16 2006 Shahms E. King <shahms@shahms.com> 0.8.1-3
- BuildRequires python, rather than python-devel

* Mon May 15 2006 Shahms E. King <shahms@shahms.com> 0.8.1-2
- Fix rpmlint non-executable-script errors

* Fri May 12 2006 Shahms E. King <shahms@shahms.com> 0.8.1-1
- Add COPYING to %%doc
- Update to new upstream version
- Require bzr 0.8

* Wed May 10 2006 Shahms E. King <shahms@shahms.com> 0.8-1
- Update to new upstream version

* Fri Apr 14 2006 Shahms E. King <shahms@shahms.com> 0.7-1
- Initial package
