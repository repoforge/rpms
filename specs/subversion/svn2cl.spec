# $Id$
# Authority: dag
# Upstream: CollabNet <dev$subversion,apache,org>

Name: svn2cl
Version: 0.13
Release: 0.1%{?dist}
Summary: Create a ChangeLog from a Subversion log

Group: Development/Tools
License: ASL 2.0
URL: http://arthurdejong.org/svn2cl
Source0: http://arthurdejong.org/svn2cl/svn2cl-%{version}.tar.gz
Source1: http://arthurdejong.org/svn2cl/svn2cl-%{version}.tar.gz.sig
Source2: http://arthurdejong.org/svn2cl/svn2cl-%{version}.tar.gz.md5

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: subversion
Requires: libxslt
# svn2cl has been removed from Subversion tarballs, and the
# version there was out of date, anyway
Obsoletes: subversion-svn2cl


%description
svn2cl is a simple XSL transformation and shell script wrapper for
generating a classic GNU-style ChangeLog from a subversion repository
log.  It is made from several changelog-like scripts using common XSLT
constructs found in different places.

%prep
%setup
%{__sed} -i.path -e 's|^XSL="$dir/|XSL="%{_datadir}/svn2cl/|' \
        svn2cl.sh
# Sanity check svn2cl_version
v=$(./svn2cl.sh -V | sed -n '1{s/.* //;p;}')
if [ "$v" != "%{version}" ]; then
        echo -n "ERROR: svn2cl version not up to date in specfile: "
        echo "'$v' <> '%{version}'"
        exit 1
fi


%build
# Nothing to build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -Dp -m0755 svn2cl.sh ${RPM_BUILD_ROOT}%{_bindir}/svn2cl
%{__install} -d -m0755 ${RPM_BUILD_ROOT}%{_datadir}/svn2cl
%{__install} -p -m0644 *.xsl ${RPM_BUILD_ROOT}%{_datadir}/svn2cl
%{__install} -Dp -m0644 svn2cl.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/svn2cl.1

%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc NEWS README TODO *.css
%{_bindir}/*
%{_datadir}/*
%{_mandir}/man1/*

%changelog

* Tue Apr 24 2012 Nico Kadel-Garcia <ncadel@gmail.com> - 0.13-01
- First build
