# $Id$
# Authority: dag
# Upstream: Satoru Takabayashi <satoru$namazu,org>

Summary: Daily backup system similar to Plan9's dumpfs
Name: pdumpfs
Version: 1.2
Release: 1
License: GPL
Group: Applications/Archiving
URL: http://namazu.org/~satoru/pdumpfs/

Source: http://namazu.org/~satoru/pdumpfs/pdumpfs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ruby
Requires: ruby

%description
pdumpfs is a simple daily backup system similar to Plan9's dumpfs which
preserves every daily snapshot. pdumpfs is written in Ruby. You can
access the past snapshots at any time for retrieving a certain day's
file. Let's backup your home directory with pdumpfs!

pdumpfs constructs the snapshot YYYY/MM/DD in the destination directory.
All source files are copied to the snapshot directory for the first time.
On and after the second time, pdumpfs copies only updated or newly created
files and stores unchanged files as hard links to the files of the previous
day's snapshot for saving a disk space. 

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 pdumpfs %{buildroot}%{_bindir}/pdumpfs
%{__install} -D -m0644 man/man8/pdumpfs.8 %{buildroot}%{_mandir}/man8/pdumpfs.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README doc/
%doc %{_mandir}/man8/pdumpfs.8*
%{_bindir}/pdumpfs

%changelog
* Wed Aug 11 2004 Dag Wieers <dag@wieers.com> - 1.2-1
- Updated to release 1.2.

* Mon Jul 12 2004 Dag Wieers <dag@wieers.com> - 1.1-1
- Initial package. (using DAR)
