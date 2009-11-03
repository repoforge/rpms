# $Id$
# Authority: dag
# Upstream: John madden <john+svnfs@jmadden,eu>

%define real_name svnfs

Summary: FUSE-based user-space file system for accessing subversion repositories
Name: fuse-svnfs
Version: 0.3
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://www.jmadden.eu/index.php/svnfs/

Source: http://www.jmadden.eu/wp-content/uploads/svnfs/svnfs-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fuse-devel >= 2.2
Requires: fuse >= 2.2

Obsoletes: svnfs <= %{name}-%{version}
Provides: svnfs = %{name}-%{version}

%description
svnfs is a FUSE-based user-space file system for accessing subversion
repositories.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
	--disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
#%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO doc/clamfs.xml
#%doc %{_mandir}/man1/clamfs.1*
#%{_bindir}/clamfs

%changelog
* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
