# Authority: dag

Summary: mtools, read/write/list/format DOS disks under Unix
Name: mtools
Version: 3.9.9
Release: 0
License: GPL/Lilux
Group: System Environment/Base
URL: http://mtools.linux.lu/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://mtools.linux.lu/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
Mtools is a collection of utilities to access MS-DOS disks
from Unix without mounting them. It supports Win'95 style
long file names, OS/2 Xdf disks, ZIP/JAZ disks and 2m
disks (store up to 1992k on a high density 3 1/2 disk).

%prep
%setup
%configure

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__make} install-info infodir="%{buildroot}%{_infodir}"
#/usr/bin/strip /usr/bin/mtools /usr/bin/mkmanifest /usr/bin/floppyd

%files
%doc Changelog COPYING README* Release.notes scripts/
%doc %{_mandir}/man1/*
%doc %{_mandir}/man5/*
%{_infodir}/*
%{_bindir}/*

%pre
groupadd floppy 2>/dev/null || echo -n ""

%post
if [ -f /usr/bin/install-info ] ; then
	if [ -f /usr/info/dir ] ; then
		/usr/bin/install-info /usr/info/mtools.info /usr/info/dir
	fi
	if [ -f /usr/info/dir.info ] ; then
		/usr/bin/install-info /usr/info/mtools.info /usr/info/dir.info
	fi
fi


%preun
install-info --delete /usr/info/mtools.info /usr/info/dir.info
if [ -f /usr/bin/install-info ] ; then
	if [ -f /usr/info/dir ] ; then
		/usr/bin/install-info --delete /usr/info/mtools.info /usr/info/dir
	fi
	if [ -f /usr/info/dir.info ] ; then
		/usr/bin/install-info --delete /usr/info/mtools.info /usr/info/dir.info
	fi
fi

%clean
%{__rm} -rf %{buildroot}

%changelog
* Thu Apr 03 2003 Dag Wieers <dag@wieers.com> - 3.9.9-0
- Initial package. (using DAR)
