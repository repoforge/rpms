# $Id$
# Authority: shuff
# Upstream: Pierre Martineau <pmartino$users,sourceforge,net>

%define major_version 1.4.3

Summary: Bibliography manager for OpenOffice.org
Name: bibus
Version: 1.4.3.2
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://bibus-biblio.sourceforge.net/

Source: http://downloads.sourceforge.net/project/bibus-biblio/bibus-biblio/bibus-%{major_version}/bibus-%{version}.tar.gz
Patch0: bibus-1.4.3.2_Makefile.patch
Patch1: bibus-1.4.3.2_config.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: MySQL-python >= 1.2.1
BuildRequires: openoffice.org-core
BuildRequires: openoffice.org-pyuno
BuildRequires: python-devel >= 2.3
BuildRequires: python-sqlite2
BuildRequires: wxPython-devel >= 2.6
Requires: MySQL-python >= 1.2.1
Requires: openoffice.org-core
Requires: openoffice.org-draw
Requires: openoffice.org-pyuno
Requires: python >= 2.3
Requires: python-sqlite2
Requires: setup
Requires: wxPython >= 2.6

%description
Bibus is a bibliographic and reference management software. As with other such
tools, Bibus allows one to search, edit, and sort bibliographic records. In
addition, Bibus contains features that makes it unique among open source and
even commercial bibliographic databases:

* Hierarchical organization of the references with user defined keys
* Designed for multiuser environments
o You can share the database between an "unlimited" number of users
o Each user will have its own classification
o You can define read-only and read-write users 
* Live queries; that is searches that update as the database changes
* On-line PubMed queries
* On-line eTBLAST queries
* Insertion of references and formatting of bibliographies into two widely used
  Word Processors (OpenOffice.org and Microsoft Word)
* Foreign language support through Unicode and gettext. As of version 1.4,
  Bibus is available in English, Chinese, Czech, French, German, Hungarian,
  Portuguese, Slovenian, Spanish. 

%prep
%setup -n %{name}-%{major_version}
%patch0 -p1
%patch1 -p1

%build
%define bibus_makeflags python=%{__python} oopath='%{_libdir}/openoffice.org/program' ooure='%{_libdir}/openoffice.org/basis-link/ure-link/%{_lib}' oobasis='%{_libdir}/openoffice.org/basis-link/program'

# create profile scripts
%{__mkdir} profile
%{__cat} > profile/bibus.sh <<'BOURNE'
if [[ -n ${PYTHONPATH} ]]; then
    export PYTHONPATH=${PYTHONPATH}:%{_libdir}/openoffice.org/program
else
    export PYTHONPATH=%{_libdir}/openoffice.org/program
fi
BOURNE

%{__cat} > profile/bibus.csh <<'CSH'
if ( ${?PYTHONPATH} == 1 ) then
  setenv PYTHONPATH "${PYTHONPATH}:%{_libdir}/openoffice.org/program"
else
  setenv PYTHONPATH "%{_libdir}/openoffice.org/program"
endif
CSH

%install
%{__rm} -rf %{buildroot}
%{__make} -f Setup/Makefile install DESTDIR=%{buildroot} %{bibus_makeflags}

# make the %{_bindir}/bibus symlink
pushd %{buildroot}
ln -sf %{_datadir}/bibus/bibusStart.py .%{_bindir}/bibus
%{__chmod} 0755 .%{_datadir}/bibus/bibusStart.py
popd

%{__install} -m0755 -d %{buildroot}%{_sysconfdir}/profile.d
%{__install} -m0755 profile/bibus.sh %{buildroot}%{_sysconfdir}/profile.d
%{__install} -m0755 profile/bibus.csh %{buildroot}%{_sysconfdir}/profile.d

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Docs/*
%doc %{_docdir}/bibus
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/bibus.config
%{_datadir}/locale/*/LC_MESSAGES/*
%{_datadir}/icons/*/*/apps/*
%{_datadir}/bibus
%{_desktopdir}/*
%{_bindir}/*
%{_sysconfdir}/profile.d/*

%changelog
* Mon Feb 22 2010 Steve Huff <shuff@vecna.org> - 1.4.3.2-1
- Initial package.
