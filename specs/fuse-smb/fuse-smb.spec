# $Id$
# Authority: dag

%define real_name fusesmb

Summary: FUSE-Filesystem to fast and easy access remote resources via SMB
Name: fuse-smb
Version: 0.8.7
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://www.ricardis.tudelft.nl/~vincent/fusesmb/

Source: http://www.ricardis.tudelft.nl/~vincent/fusesmb/download/fusesmb-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fuse-devel >= 2.3, samba-client >= 3.0

%description 
With SMB for Fuse you can seamlessly browse your network neighbourhood as were
it on your own filesystem. It's basically smbmount with a twist. Instead of
mounting one Samba share at a time, you mount all workgroups, hosts and shares
at once. Only when you're accessing a share a connection is made to the remote
computer. 

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
%doc AUTHORS ChangeLog COPYING INSTALL README TODO fusesmb.conf.ex
%doc %{_mandir}/man1/fusesmb.1*
%doc %{_mandir}/man5/fusesmb.conf.5*
%{_bindir}/fusesmb
%{_bindir}/fusesmb.cache

%changelog 
* Wed Oct 24 2007 Dag Wieers <dag@wieers.com> - 0.8.7-1
- Updated to release 0.8.7.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.8.5-1
- Initial package. (using DAR)
