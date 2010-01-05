# $Id$
# Authority: dag

Summary: Create static HTML pages of a yum repository
Name: repoview
Version: 0.6.2
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: https://fedorahosted.org/repoview/

Source: http://icon.fedorapeople.org/repoview/repoview-%{version}.tar.gz
Source: http://www.mricon.com/downloads/repoview/repoview-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.2
BuildRequires: yum >= 3.0
Requires: python >= 2.2
Requires: python-elementtree
Requires: python-kid >= 0.6.3
Requires: python-sqlite
Requires: yum >= 3.0

%description
repoview allows to easily create a set of static HTML pages in a YUM
repository, allowing simple browsing of available packages. It uses
kid templating engine to create the pages and is therefore easily
customizeable.

%prep
%setup

%{__perl} -pi.orig \
    -e 's|^(VERSION) = .*$|$1 = "%{version}"|g;' \
    -e 's|^(DEFAULT_TEMPLATEDIR) =.*$|$1 = "%{_datadir}/repoview/templates"|g;' \
    repoview.py

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 repoview.py %{buildroot}%{_bindir}/repoview
%{__install} -Dp -m0644 repoview.8 %{buildroot}%{_mandir}/man8/repoview.8

%{__install} -d -m0755 %{buildroot}%{_datadir}/repoview/
%{__cp} -apv templates/ %{buildroot}%{_datadir}/repoview/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%doc %{_mandir}/man8/repoview.8*
%{_bindir}/repoview
%{_datadir}/repoview/

%changelog
* Wed Dec 17 2008 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Updated to release 0.6.2.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Updated to release 0.6.1.

* Sun Aug 06 2006 Dag Wieers <dag@wieers.com> - 0.5.2-1
- Updated to release 0.5.2.

* Fri Feb 17 2006 Dag Wieers <dag@wieers.com> - 0.5-3
- Changed python-celementtree dependency to python-elementtree. (Douglas E. Warner)

* Tue Feb 14 2006 Dag Wieers <dag@wieers.com> - 0.5-2
- Added yum >= 2.3 dependency.

* Thu Feb 02 2006 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Updated to release 0.5, thanks to Douglas E. Warner!

* Mon May 09 2005 Dag Wieers <dag@wieers.com> - 0.3-2
- Changed python-elementtree dependency into python-celementtree.

* Sat Apr 30 2005 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
