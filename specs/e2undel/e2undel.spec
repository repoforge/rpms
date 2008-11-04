# $Id$
# Authority: dag

Summary: Tool for recovering deleted files on an ext2 or ext3 filesystem
Name: e2undel
Version: 0.82
Release: 1
License: GPL
Group: Applications/File
URL: http://e2undel.sf.net/

Source: http://dl.sf.net/e2undel/e2undel-%{version}.tgz
Patch: e2undel-0.82-compile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Ext2/Ext3 filesystem file undeletion support.
e2undel is an interactive console tool that recovers the data of deletedfiles
on an ext2 or ext3 filesystem under Linux. Included is a library that allows
to recover deleted files by name. It does not require any knowledge about the
secrets of the ext2 file system and should be useable by everyone.

e2undel does not manipulate internal ext2 structures and requires only read
access to the file system where the files to recover are located. It accesses
the ext2 or ext3 filesystem by way of Ted Ts'o's ext2fs library.

The e2undel package contains a library that allows you to recover deleted
files by their names. Usually, when a file is deleted, its name is lost; after
installing this library, the names of deleted files are logged and accessible
via the e2undel program. 

%prep
%setup
%patch -p1 -b .compile

%build
%{__make} e2undel compactlog %{?_smp_mflags} CFLAGS="%{optflags}" LDFLAGS="-O"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 e2undel %{buildroot}%{_bindir}/e2undel
%{__install} -Dp -m0755 compactlog %{buildroot}%{_bindir}/compactlog

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS HISTORY INSTALL* README*
%{_bindir}/e2undel
%{_bindir}/compactlog

%changelog
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 0.82-1
- Initial package. (using DAR)
