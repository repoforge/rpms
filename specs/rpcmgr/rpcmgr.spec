# $Id$

# Authority: dag
# Upstream: Dag Lem <rpcmgr@nimrod.no>

Summary: DVD RPC (Region Playback Control) tool
Name: rpcmgr
Version: 1.2
Release: 0
License: GPL
Group: Applications/System
URL: http://perso.club-internet.fr/farzeno/dvds/rpcmgr11.c

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://perso.club-internet.fr/farzeno/dvds/rpcmgr11.c
Patch: http://perso.club-internet.fr/farzeno/dvds/rpcmgr12.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A DVD RPC (Region Playback Control) tool.

What is RPC? RPC stands for Region Playback Control. RPC divides the
world into eight regions and potentially denies you the right to play
back DVD discs from all but one of these regions. RPC comes in two
flavors; software control (RPC Phase I / RPC1) and hardware control
(RPC Phase II / RPC2). RPC1 is enforced by the DVD player software,
while RPC2 is enforced by both the software and by the DVD drive
itself.

%prep
%setup -c %{name}-%{version} -T -D
%{__cp} -f %{SOURCE0} .
%patch -p0 -b .rpcmgr12
%{__mv} -f rpcmgr11.c rpcmgr.c

%build
${CC:-%{__cc}} %{optflags} -o rpcmgr rpcmgr.c

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__install} rpcmgr %{buildroot}%{_sbindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc rpcmgr.c
%{_sbindir}/*

%changelog
* Sun Dec 01 2003 Dag Wieers <dag@wieers.com> - 1.2-0
- Initial package. (using DAR)
