# $Id: _template.spec 130 2004-03-17 10:51:35Z dude $
# Authority: dag
# Upstream: Henrik Carlqvist <henca@users.sf.net>

Summary: Create DOS/MS-compatible boot records
Name: ms-sys
Version: 1.0.2
Release: 1
License: GPL
Group: Applications/System
URL: http://ms-sys.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/ms-sys/ms-sys-%{version}.tgz
BuildRequires: bash
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This program is used to create DOS/MS-compatible boot records. It is
able to do the same as Microsoft "fdisk /mbr" to a hard disk. It is
also able to do the same as DOS "sys" to a floppy or FAT32 partition
except that it does not copy any system files, only the boot record is
written.

%prep
%setup

%build
%{__make} debug \
	SHELL="/bin/bash" \
	PREFIX="%{_prefix}" \
	CC="${CC:-%{__cc}}" \
	EXTRA_CFLAGS="%{optflags} -fasm" \
	EXTRA_LDFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir} \
		%{buildroot}%{_mandir}/man1/
%makeinstall \
	PREFIX="%{buildroot}%{_prefix}" \
	MANDIR="%{buildroot}%{_mandir}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc CHANGELOG CONTRIBUTORS COPYING README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Initial package. (using DAR)
