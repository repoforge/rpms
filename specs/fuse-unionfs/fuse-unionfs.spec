# $Id$
# Authority: dag

%define real_name unionfs-fuse

Summary: FUSE-base user-space union filesystem
Name: fuse-unionfs
Version: 0.20
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://podgorny.cz/moin/UnionFsFuse

Source: http://podgorny.cz/unionfs-fuse/releases/unionfs-fuse-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fuse-devel >= 2.2
Requires: fuse >= 2.2

Obsoletes: unionfs-fuse <= %{name}-%{version}
Provides: unionfs-fuse = %{name}-%{version}
Obsoletes: unionfs <= %{name}-%{version}
Provides: unionfs = %{name}-%{version}

%description
unionfs is a FUSE-base user-space union filesystem.

%prep
%setup -n %{real_name}-%{version}

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 unionfs %{buildroot}%{_bindir}/unionfs

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CREDITS
%{_bindir}/unionfs

%changelog
* Tue Jun 03 2008 Dag Wieers <dag@wieers.com> - 0.20-1
- Updated to release 0.20.

* Tue Jun 03 2008 Dag Wieers <dag@wieers.com> - 0.19-1
- Updated to release 0.19.

* Sat Aug 11 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Updated to release 0.18.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.17-1
- Initial package. (using DAR)
