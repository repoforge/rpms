# $Id$
# Authority: dag
# Upstream: <mtools@tux.org>

Summary: Read/write/list/format DOS disks
Name: mtools
Version: 3.9.9
Release: 2
License: GPL/Lilux
Group: System Environment/Base
URL: http://mtools.linux.lu/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://mtools.linux.lu/mtools-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Mtools is a collection of utilities to access MS-DOS disks
from Unix without mounting them. It supports Win'95 style
long file names, OS/2 Xdf disks, ZIP/JAZ disks and 2m
disks (store up to 1992k on a high density 3 1/2 disk).

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall install-info

%pre
groupadd floppy 2>/dev/null || :

%post
/sbin/install-info %{_infodir}/mtools.info.gz %{_infodir}/dir

%preun
/sbin/install-info --delete %{_infodir}/mtools.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING README* Release.notes scripts/
%doc %{_mandir}/man?/*
%doc %{_infodir}/*.info*
%{_bindir}/*

%changelog
* Thu Apr 29 2004 Dag Wieers <dag@wieers.com> - 3.9.9-2
- Cosmetic fixes, the sequel.

* Wed Apr 28 2004 Dag Wieers <dag@wieers.com> - 3.9.9-1
- Cosmetic fixes.

* Thu Apr 03 2003 Dag Wieers <dag@wieers.com> - 3.9.9-0
- Initial package. (using DAR)
