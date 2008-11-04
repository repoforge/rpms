# $Id$
# Authority: dag
# Upstream: Mario Viara <mario@viara,cn>

%define real_version 1_11

Summary: Tool to synchronize directories
Name: dirsync
Version: 1.11
Release: 1
License: GPL
Group: Applications/System
URL: http://www.viara.cn/en/dirsync.htm

Source: http://www.viara.cn/download/dirsync-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
dirsync is a directory synchronizer that takes a source and destination
directory as arguments and recursively ensures that the two directories
are identical. It can be used to create incremental copies of large chunks
of data.

%prep
%setup -c

%build
%{__make} %{?_smp_mflags} linux

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 dirsync %{buildroot}%{_bindir}/dirsync
%{__install} -Dp -m0644 dirsync.1 %{buildroot}%{_mandir}/man1/dirsync.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc readme.txt
%doc %{_mandir}/man1/dirsync.1*
%{_bindir}/dirsync

%changelog
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 
- Initial package. (using DAR)
