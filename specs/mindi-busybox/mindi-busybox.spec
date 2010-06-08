# $Id$
# Authority: dag

Summary: Busybox version suited for Mindi
Name: mindi-busybox
Version: 1.7.3
Release: 1%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://www.mondorescue.org/

Source: ftp://ftp.mondorescue.org/src/mindi-busybox-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExcludeArch: ppc
BuildRequires: gcc

%description
This package provides a busybox version suited for Mindi.

%prep
%setup

%build
%{__make} oldconfig
%{__make} busybox

%install
%{__rm} -rf %{buildroot}
%{__make} install CONFIG_PREFIX="%{buildroot}%{_libdir}/mindi/rootfs"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog INSTALL LICENSE NEWS README TODO
%dir %{_libdir}/mindi/
%{_libdir}/mindi/rootfs/

%changelog
* Tue Jun 08 2010 Dag Wieers <dag@wieers.com> - 1.7.3-1
- Updated to release 1.7.3.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.7.2-1
- Initial package. (using DAR)
