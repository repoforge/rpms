# $Id$

# Authority: dag
# Upstream: Dag Lem <rpcmgr$nimrod,no>

Summary: DVD RPC (Region Playback Control) tool
Name: rpcmgr
Version: 1.2
Release: 0.2%{?dist}
License: GPL
Group: Applications/System
URL: http://perso.club-internet.fr/farzeno/dvds/rpcmgr11.c

Source: http://perso.club-internet.fr/farzeno/dvds/rpcmgr11.c
Patch0: http://perso.club-internet.fr/farzeno/dvds/rpcmgr12.patch
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
%{__cp} -fp %{SOURCE0} .
%patch0 -p0 -b .rpcmgr12
%{__mv} -f rpcmgr11.c rpcmgr.c

%build
${CC:-%{__cc}} %{optflags} -o rpcmgr rpcmgr.c

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 rpcmgr %{buildroot}%{_sbindir}/rpcmgr

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc rpcmgr.c
%{_sbindir}/rpcmgr

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-0.2
- Rebuild for Fedora Core 5.

* Sun Dec 01 2003 Dag Wieers <dag@wieers.com> - 1.2-0
- Initial package. (using DAR)
