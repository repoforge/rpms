# $Id$
# Authority: dag

Summary: Busybox version suited for Mindi
Name: mindi-busybox
Version: 1.7.2
Release: 1%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://www.mondorescue.org/

Source: ftp://ftp.mondorescue.org/src/mindi-busybox-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExcludeArch: ppc

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
%doc AUTHORS ChangeLog INSTALL LICENSE README svn.log TODO
%dir %{_libdir}/mindi/
%{_libdir}/mindi/rootfs/

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.7.2-1
- Initial package. (using DAR)
