# --- TSRPM HINT: /here/prefetch/tsrpm/etc/cygwin.tshint
# Copyright (C) 2004, 2005, 2006 TimeSys, Inc.
#
# This file is part of tsrpm.
#
# This software is a copyrighted work licensed under the terms of the
# GNU General Public License.  See http://www.gnu.org/copyleft/gpl.html
# for details.
#
Summary: A RPM front-end for building cross packages from standard source rpms.
Name: tsrpm
Version: 1.31
Release: 1
License: GPL
Group: System
Source: %{name}-%{version}.tar.bz2
Source50: cygwin.tshint
Buildroot: %{_tmppath}/%{name}-root
Prefix: %{_prefix}
Requires: rpm >= 4.1

%description
tsrpm is used to manipulate source and binary RPMs for a cross-build
environment.  It controls the extraction of source rpms for manipulation,
the building of packages from source rpms or spec files, the installation of
packages in a separate target root filesystem, and the extraction of library
and header files to a cross compiler environment.

%prep

%setup -q

%build
%{__make} files= rpm_files=

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall files= rpm_files= man1dir=$RPM_BUILD_ROOT/usr/share/man/man1 man5dir=$RPM_BUILD_ROOT/usr/share/man/man5

%files
%defattr(-,root,root, 0755)
%dir %{_prefix}/lib
%{_prefix}/lib/tsrpm
%{_prefix}/bin
%dir /usr/share/man/man1
%dir /usr/share/man/man5
/usr/share/man/man*/*
