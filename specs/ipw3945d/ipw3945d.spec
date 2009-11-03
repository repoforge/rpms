# $Id$
# Authority: matthias
# Dist: nodist

# We have only executables with no debugging symbols, so no need for an empty
# debuginfo package.
%define debug_package %{nil}

Summary: Regulatory Daemon for Intel® PRO/Wireless 3945 network adaptors
Name: ipw3945d
Version: 1.7.22
Release: 4%{?dist}
License: Distributable
Group: System Environment/Kernel
URL: http://bughost.org/ipw3945/
Source0: http://bughost.org/ipw3945/daemon/ipw3945d-%{version}.tgz
Source1: 11ipw3945
Source2: ipw3945d.init
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
ExclusiveArch: i386 x86_64

%description
The regulatory daemon is responsible for controlling and configuring aspects
of the hardware required to operate the device within compliance of various
regulatory agencies.  This includes controlling which channels are allowed to
do active/passive scanning, transmit power levels, which channels are allowed
to be transmitted on, and support for IEEE 802.11h (DFS and TPC).


%prep
%setup


%build


%install
%{__rm} -rf %{buildroot}
# Install binary daemon
%ifarch i386
%{__install} -D -p -m 0755 x86/ipw3945d %{buildroot}/sbin/ipw3945d
%endif
%ifarch x86_64
%{__install} -D -p -m 0755 x86_64/ipw3945d %{buildroot}/sbin/ipw3945d
%endif
# Install PM hook
%{__install} -D -p -m 0755 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/pm/hooks/11ipw3945
# Install init script
%{__install} -D -p -m 0755 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/rc.d/init.d/ipw3945d


%post
/sbin/chkconfig --add ipw3945d

%preun
if [ $1 -eq 0 ]; then
    /sbin/service ipw3945d stop &>/dev/null || :
    /sbin/chkconfig --del ipw3945d
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service ipw3945d condrestart &>/dev/null || :
fi


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc LICENSE.ipw3945d README.ipw3945d
%{_sysconfdir}/pm/hooks/11ipw3945
%{_sysconfdir}/rc.d/init.d/ipw3945d
/sbin/ipw3945d


%changelog
* Tue Jan  9 2007 Matthias Saou <http://freshrpms.net/> 1.7.22-4
- Include PM hook from Ralf Ertzinger for suspend and hibernate to work.

* Tue Oct 24 2006 Matthias Saou <http://freshrpms.net/> 1.7.22-3
- Fix preun scriplet (missing "fi", doh!).

* Mon Oct 23 2006 Matthias Saou <http://freshrpms.net/> 1.7.22-2
- Include init script, thanks to Stefan Becker.

* Mon Oct  9 2006 Matthias Saou <http://freshrpms.net/> 1.7.22-1
- Update to 1.7.22.

* Thu Mar 30 2006 Matthias Saou <http://freshrpms.net/> 1.7.18-1
- Initial RPM release.

