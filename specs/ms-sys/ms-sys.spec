# $Id$
# Authority: dag
# Upstream: Henrik Carlqvist <henca$users,sf,net>

Summary: Create DOS/MS-compatible boot records
Name: ms-sys
Version: 2.1.2
Release: 1
License: GPL
Group: Applications/System
URL: http://ms-sys.sourceforge.net/

Source: http://dl.sf.net/ms-sys/ms-sys-%{version}.tgz
BuildRequires: bash, gettext
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
%{__install} -d -m0755 %{buildroot}%{_bindir} \
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
%doc %{_mandir}/man1/ms-sys.1*
%{_bindir}/ms-sys

%changelog
* Sat Nov 26 2005 Dag Wieers <dag@wieers.com> - 2.1.2-1
- Updated to release 2.1.2.

* Thu Aug 04 2005 Dag Wieers <dag@wieers.com> - 2.1.1-1
- Updated to release 2.1.1.

* Sun Jun 06 2004 Dag Wieers <dag@wieers.com> - 2.0.0-1
- Updated to release 2.0.0.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Initial package. (using DAR)
