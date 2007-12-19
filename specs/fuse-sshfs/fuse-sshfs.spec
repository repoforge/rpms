# $Id$
# Authority: dag

%define real_name sshfs-fuse

Summary: FUSE-Filesystem to access remote filesystems via SSH
Name: fuse-sshfs
Version: 1.9
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://fuse.sourceforge.net/sshfs.html

Source: http://dl.sf.net/sourceforge/fuse/sshfs-fuse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.0, fuse-devel >= 2.2
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
%{_bindir}/sshfs
%{_libdir}/sshnodelay.so

%changelog
* Tue Dec 18 2007 Dag Wieers <dag@wieers.com> - 1.9-1
- Updated to release 1.9.

* Wed May 16 2007 Dag Wieers <dag@wieers.com> - 1.8-1
- Updated to release 1.8.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 1.7-1
- Initial package. (using DAR)
