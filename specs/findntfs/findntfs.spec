# $Id$
# Authority: dag
# Upstream: Szabolcs Szakacsits <szaka$ntfs-3g,org>

Summary: Find NTFS partitions
Name: findntfs
Version: 1.3
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://mlf.linux.rulez.org/mlf/ezaz/ntfsresize.html#troubleshoot

Source: http://ntfs-3g.org/download/findntfs-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
findntfs is a tool to find NTFS filesystems.

%prep
%setup

%build
%{__cc} %{optflags} -o findntfs findntfs.c

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 findntfs %{buildroot}%{_bindir}/findntfs

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/findntfs

%changelog
* Tue Nov 11 2008 Dag Wieers <dag@wieers.com> - 1.3-1
- Initial package. (using DAR)
