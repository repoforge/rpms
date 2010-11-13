# $Id$
# Authority: dag
# Upstream: <mtools$tux,org>

### EL6 ships with mtools-4.0.12-1.el6
### EL5 ships with mtools-3.9.10-2.fc6
### EL4 ships with mtools-3.9.9-9
%{?el4:# Tag: rfx}
### EL3 ships with mtools-3.9.8-8
%{?el3:# Tag: rfx}
### EL2 ships with mtools-3.9.8-2
%{?el2:# Tag: rfx}
# ExclusiveDist: el2 el3 el4

Summary: Read/write/list/format DOS disks
Name: mtools
Version: 3.9.10
Release: 1%{?dist}
License: GPL/Lilux
Group: System Environment/Base
URL: http://mtools.linux.lu/

Source: http://mtools.linux.lu/mtools-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: texinfo

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
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 3.9.10-1
- Updated to release 3.9.10.

* Thu Apr 29 2004 Dag Wieers <dag@wieers.com> - 3.9.9-2
- Cosmetic fixes, the sequel.

* Wed Apr 28 2004 Dag Wieers <dag@wieers.com> - 3.9.9-1
- Cosmetic fixes.

* Thu Apr 03 2003 Dag Wieers <dag@wieers.com> - 3.9.9-0
- Initial package. (using DAR)
