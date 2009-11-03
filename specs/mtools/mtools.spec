# $Id$
# Authority: dag
# Upstream: <mtools$tux,org>

# ExclusiveDist: el2 el3

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

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.9.9-2.2
- Rebuild for Fedora Core 5.

* Thu Apr 29 2004 Dag Wieers <dag@wieers.com> - 3.9.9-2
- Cosmetic fixes, the sequel.

* Wed Apr 28 2004 Dag Wieers <dag@wieers.com> - 3.9.9-1
- Cosmetic fixes.

* Thu Apr 03 2003 Dag Wieers <dag@wieers.com> - 3.9.9-0
- Initial package. (using DAR)
