# $Id$
# Authority: dag
# Upstream: 

Summary: Live syncing (mirroring) daemon
Name: lsyncd
Version: 1.0
Release: 1
License: GPL
Group: Applications/File
URL: http://www.pri.univie.ac.at/lsyncd/

Source: http://www.pri.univie.ac.at/lsyncd/lsyncd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: rsync

%description
Lsyncd uses rsync to synchronize local directories with a remote machine
running rsyncd. Lsyncd watches multiple directories trees through inotify.

The first step after adding the watches is to, rsync all directories with
the remote host, and then sync single file buy collecting the inotify events.
So lsyncd is a light-weight live mirror solution that should be easy to
install and use while blending well with your system.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS TODO
%{_bindir}/lsyncd

%changelog
* Thu Mar 27 2008 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
