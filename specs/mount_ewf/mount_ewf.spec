# $Id$
# Authority: dag

Summary: Tool to mount files in Expert Witness Format using loopback file system
Name: mount_ewf
Version: 20090113
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://sourceforge.net/projects/libewf/

Source: http://dl.sf.net/project/libewf/mount_ewf/mount_ewf-%{version}/mount_ewf-%{version}.py
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: libewf-devel
Requires: fuse-python
Requires: libewf

%description
Tool to mount files in Expert Witness Format using loopback file system.

%prep

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp %{SOURCE0} %{buildroot}%{_bindir}/mount-ewf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/mount-ewf

%changelog
* Wed Feb 16 2011 Dag Wieers <dag@wieers.com> - 20090113-1
- Initial package. (using DAR)
