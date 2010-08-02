# $Id$
# Authority: dag

Summary: Graphical interface to the CVS and Subversion

Name: tkcvs
%define real_version 8_2_2
Version: 8.2.2
Release: 1%{?dist}
License: GPL+
Group: Development/Tools
URL: http://www.twobarleycorns.net/tkcvs.html

Source: http://www.twobarleycorns.net/tkcvs_%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Provides: tksvn = %{version}
Requires: tcl
Requires: tk

%description
TkCVS is a Tcl/Tk-based graphical interface to the CVS and Subversion
configuration management systems. It will also help with RCS. The user
interface is consistent across Unix/Linux, Windows, and MacOS X. TkDiff
is included for browsing and merging your changes.

TkCVS shows the status of the files in the current working directory,
and has tools for tagging, merging, importing, exporting, checking
in/out, and other user operations.

TkCVS also aids in browsing the repository. For Subversion, the
repository tree is browsed like an ordinary file tree. For CVS, the
CVSROOT/modules file is read. TkCVS extends CVS with a method to
produce a "user friendly" listing of modules by using special
comments in the CVSROOT/modules file.

%prep
%setup -n %{name}_%{real_version}

perl -pi -e '
        s|set TCDIR \[file join \$TclRoot tkcvs\]|set TCDIR "%{_datadir}/tkcvs"|;
        s|\[file join \$TclRoot tkcvs bitmaps\]|\[file join \$TCDIR bitmaps\]|;
    ' tkcvs/tkcvs.tcl

%{__rm} -f tkcvs/tkcvs.blank tkcvs/mklocal tkcvs/mkmanpage.pl

%build

%install
%{__install} -Dp -m0755 tkcvs/tkcvs.tcl %{buildroot}%{_bindir}/tkcvs
%{__install} -Dp -m0644 tkcvs/tkcvs.1 %{buildroot}%{_mandir}/man1/tkcvs.1
%{__install} -Dp -m0755 tkdiff/tkdiff %{buildroot}%{_bindir}/tkdiff

%{__install} -d -m0755 %{buildroot}%{_datadir}
%{__cp} -av tkcvs %{buildroot}%{_datadir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING FAQ vendor5readme.pdf
%doc %{_mandir}/man1/*.1*
%{_bindir}/tkcvs
%{_bindir}/tkdiff
%{_datadir}/tkcvs/

%changelog
* Thu Jul 29 2010 Dag Wieers <dag@wieers.com> - 8.2.2-1
- Initial package (based on fedora)
