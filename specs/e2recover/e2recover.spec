# $Id$
# Authority: dag

Summary: Tools to assist in recovering deleted files from ext2 filesystems.
Name: e2recover
Version: 1.0
Release: 1
Group: Applications/File
License: GPL
URL: http://pobox.com/~aaronc/tech/e2-undel/

Source: http://www.ibiblio.org/pub/Linux/utils/file/e2recover-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: e2fsprogs

%description
Tools to assist in recovering deleted files from ext2 file systems. Includes
fsgrab (which simply copies data from a specified position in a file or
device) and e2recover, a Perl script which calls both fsgrab and debugfs
(from the e2fsprogs) to automate file recovery.

fsgrab was originally part of the same author's fsgrab package, which is no
longer maintained.

See also the Linux Ext2fs-Undeletion mini-HOWTO which can be found on
http://pobox.com/~aaronc/tech/e2-undel/ any Linux Documentation Project mirror.

%prep
%setup

%build
%configure --with-libext2fs="yes"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 e2recover %{buildroot}%{_bindir}/e2recover
%{__install} -Dp -m0755 fsgrab %{buildroot}%{_bindir}/fsgrab
%{__install} -Dp -m0644 e2recover.1 %{buildroot}%{_mandir}/man1/e2recover.1
%{__install} -Dp -m0644 fsgrab.1 %{buildroot}%{_mandir}/man1/fsgrab.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README THANKS e2recover-1.0.lsm
%doc %{_mandir}/man1/e2recover.1*
%doc %{_mandir}/man1/fsgrab.1*
%{_bindir}/e2recover
%{_bindir}/fsgrab

%changelog
* Sun Nov 09 2008 Dag Wieers <dag@wieers.com> - 1.0-2
- Removed static binaries and package.

* Sat Mar 17 2001 Dag Wieers <dag@life.be> - 1.0-1
- Initial package.
