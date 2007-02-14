# $Id$
# Authority: dag

%define real_name git-core

%{?dist: %{expand: %%define %dist 1}}
%{?fc1:%define _without_asciidoc 1}
%{?el3:%define _without_asciidoc 1}
%{?rh9:%define _without_asciidoc 1}
%{?rh8:%define _without_asciidoc 1}
%{?rh7:%define _without_asciidoc 1}
%{?el2:%define _without_asciidoc 1}
%{?rh6:%define _without_asciidoc 1}

Summary: Git core and tools
Name: git
Version: 0.99.4
Release: 3
License: GPL
Group: Development/Tools
URL: http://git.or.cz/

Source: http://kernel.org/pub/software/scm/git/git-core-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel, openssl-devel, curl-devel
%{!?_without_asciidoc:BuildRequires: xmlto, asciidoc > 6.0.3}
Requires: sh-utils, diffutils, rsync, rcs, mktemp >= 1.5

%description
GIT comes in two layers. The bottom layer is merely an extremely fast
and flexible filesystem-based database designed to store directory trees
with regard to their history. The top layer is a SCM-like tool which
enables human beings to work with the database in a manner to a degree
similar to other SCM tools (like CVS, BitKeeper or Monotone).

%prep
%setup -n %{real_name}-%{version}
# avoid warning about ../README:
%{__perl} -pi -e "s|asciidoc |asciidoc --unsafe |g;" Documentation/Makefile
# avoid asciidoc errors:
%{__perl} -pi -e "s|\^|\\\^|g;" Documentation/git-rev-list.txt

%build
%{__make} %{?_smp_mflags} all %{!?_without_asciidoc:doc} prefix="%{_prefix}"

%install
%{__rm} -rf %{buildroot}
%{__make} install %{!?_without_asciidoc:install-doc} dest="%{buildroot}" prefix="%{_prefix}" mandir="%{_mandir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Documentation/*.txt README
%{!?_without_asciidoc:%doc %{_mandir}/man1/*.1*}
%{!?_without_asciidoc:%doc %{_mandir}/man7/*.7*}
%{_bindir}/git*
%{_datadir}/git-core

%changelog
* Wed Feb 14 2007 Dries Verachtert <dries@ulyssis.org> - 0.99.4-3
- Fix location of templates (Dave Miller).
- Option '--unsafe' added to call to asciidoc.
- Fix asciidoc problem with '^'.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.99.4-1.2
- Rebuild for Fedora Core 5.

* Sun Aug 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.99.4-1
- Update to release 0.99.4.

* Wed Aug 10 2005 Dag Wieers <dag@wieers.com> - 0.99.1-1
- Small cleanup.
- Added documentation using asciidoc.

* Wed Jul 07 2005 Chris Wright <chris@osdl.org> - 0.99-1
- Initial git spec file.
