# $Id$
# Authority: dag

### FIXME: This package needs a sysv script

Summary: UNFS3 user-space NFSv3 server
Name: unfs3
Version: 0.9.10
Release: 1
License: BSD
Group: Applications/System
URL: http://unfs3.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/unfs3/unfs3-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
UNFS3 is a user-space implementation of the NFS (Network File System)
version 3 server specification. It provides a daemon that supports both
the MOUNT and NFS protocol.

%prep
%setup

%build
%configure \
	--enable-cluster
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CREDITS LICENSE NEWS README contrib/ doc/
%doc %{_mandir}/man7/tags.7*
%doc %{_mandir}/man8/unfsd.8*
%{_sbindir}/unfsd
