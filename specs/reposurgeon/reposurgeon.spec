# $Id$
# Authority: dfateyev

Name:               reposurgeon
Version:            2.20
Release:            0.1%{?dist}
Summary:            SCM Repository Manipulation Tool
Source:             http://www.catb.org/~esr/reposurgeon/reposurgeon-%{version}.tar.gz
URL:                http://www.catb.org/~esr/reposurgeon/
Group:              Development/Tools
License:            BSD License
BuildRoot:          %{_tmppath}/build-%{name}-%{version}
BuildRequires:      make
BuildRequires:      xmlto
BuildArch:          noarch
Requires:           python
# not actually required, but to make the build fail if it isn't
# available on the target dist:
BuildRequires:      python

%description
Reposurgeon enables risky operations that version-control systems don't want to
let you do, such as editing past comments and metadata and removing commits. It
works with any version control system that can export and import git
fast-import streams, including git, hg, and bzr.

%prep
%setup

%build
%{__make}

%install
%{__install} -D -m0755 reposurgeon "%{buildroot}%{_bindir}/reposurgeon"
%{__install} -D -m0644 reposurgeon.1 "%{buildroot}%{_mandir}/man1/reposurgeon.1"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING NEWS README
%{_bindir}/reposurgeon
%doc %{_mandir}/man1/reposurgeon.1*

%changelog
* Sat Feb  9 2013 Nico KAdel-Garcia <nkadel@gmail.com> - 2.20-0.1
- Update to 2.20
- Change Python dependency to just "python", not "python-base > 2.7" for
  OpenSuSE.

* Thu Nov  3 2011 pascal.bleser@opensuse.org
- update to 1.6:
  * fix Python 3.2 compatibility problem
  * gitsvnparse moves remote branches/tags to local ones (like svn2git)
- changes from 1.5:
  * suppress writing out properties if the importer won't handle them
  * 'references' lists events with possible SVN or CVS rev IDs in comments
  * 'references lift' turns CVS & SVN reference cookies into action stamps
  * cvslift -> cvspurge (it no longer does ID lifting)
  * gitsvnlift -> gitsvnparse (it no longer does ID lifting)
  * 'checkout' command allows filling a specified directory with a revision
  * 'diff' commant allows examining diffs between commits
  * new [ ] syntax for selecting commits containing a specified path

* Sat Oct 29 2011 pascal.bleser@opensuse.org
- initial version (1.4)
