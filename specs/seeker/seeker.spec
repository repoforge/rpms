# $Id$
# Authority: dag
# Upstream: 

Summary: Tool to measure disk performance (random access time)
Name: seeker
Version: 2.0
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.linuxinsight.com/how_fast_is_your_disk.html

Source: http://www.linuxinsight.com/files/seeker.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
seeker is a tool to measure disk performance by measuring the random access
time. seeker reads small pieces of data from a raw disk device in a random
access pattern.

It is important to run it on the whole disk (and not on a single partition)
if you want to compare the results of one disk to another disk.

%prep
%setup -Tc
%{__cp} -av %{SOURCE0} .

%build
%{__cc} %{optflags} -o seeker seeker.c

%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m0755 seeker %{buildroot}%{_bindir}/seeker

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/seeker

%changelog
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 2.0-1
- Initial package. (using DAR)
