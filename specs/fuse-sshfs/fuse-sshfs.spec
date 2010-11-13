# $Id$
# Authority: dag

%{?el5:%define _without_openssh44 1}
%{?el4:%define _without_openssh44 1}
%{?el3:%define _without_openssh44 1}
%{?el2:%define _without_openssh44 1}

%define real_name sshfs-fuse

Summary: FUSE-Filesystem to access remote filesystems via SSH
Name: fuse-sshfs
Version: 2.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://fuse.sourceforge.net/sshfs.html

Source: http://dl.sf.net/sourceforge/fuse/sshfs-fuse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fuse-devel >= 2.2
BuildRequires: glib2-devel >= 2.0
BuildRequires: openssh-clients
Requires: fuse >= 2.2

Obsoletes: sshfs <= %{version}-%{release}
Provides: sshfs = %{version}-%{release}

%description
This is a FUSE-filesystem client based on the SSH File Transfer Protocol.
Since most SSH servers already support this protocol it is very easy to set
up: i.e. on the server side there's nothing to do. On the client side 
mounting the filesystem is as easy as logging into the server with ssh.

%prep
%setup -n %{real_name}-%{version}

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
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/sshfs.1*
%{_bindir}/sshfs
%{?_without_openssh44:%{_libdir}/sshnodelay.so}

%changelog
* Sat Oct 25 2008 Dag Wieers <dag@wieers.com> - 2.2-1
- Updated to release 2.2.

* Sat Jul 12 2008 Dag Wieers <dag@wieers.com> - 2.1-1
- Updated to release 2.1.

* Sat Apr 26 2008 Dag Wieers <dag@wieers.com> - 2.0-1
- Updated to release 2.0.

* Tue Dec 18 2007 Dag Wieers <dag@wieers.com> - 1.9-1
- Updated to release 1.9.

* Wed May 16 2007 Dag Wieers <dag@wieers.com> - 1.8-1
- Updated to release 1.8.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 1.7-1
- Initial package. (using DAR)
