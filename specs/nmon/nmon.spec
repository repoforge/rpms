# $Id$
# Authority: dag
# Upstream: Nigel Griffiths <nag$uk,ibm,com>

Summary: Performance analysis tool
Name: nmon
Version: 11d
Release: 1
License: Proprietary
Group: Applications/System
URL: http://www-128.ibm.com/developerworks/aix/library/au-analyze_aix/
#URL: http://www-941.haw.ibm.com/collaboration/wiki/display/WikiPtype/nmon

Source0: http://www-941.haw.ibm.com/collaboration/wiki/download/attachments/437/nmon4linux_x86_%{version}.zip?version=1
Source1: http://www-941.haw.ibm.com/collaboration/wiki/download/attachments/437/nmon4linux_power_%{version}.zip?version=2
Source2: http://www-941.haw.ibm.com/collaboration/wiki/download/attachments/437/nmon4linux_x86_64_b.zip?version=1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386 x86_64 ppc ppc64

%description
nmon is designed for performance specialists to use for monitoring and
analyzing performance data.

%prep
%setup -c -a1 -a2

%build

%install
%{__rm} -rf %{buildroot}
%ifarch i386
%{?fc6:%{__install} -Dp -m0755 nmon_x86_fedora5 %{buildroot}%{_bindir}/nmon}
%{?fc5:%{__install} -Dp -m0755 nmon_x86_fedora5 %{buildroot}%{_bindir}/nmon}
%{?el4:%{__install} -Dp -m0755 nmon_x86_rhel4 %{buildroot}%{_bindir}/nmon}
%{?el3:%{__install} -Dp -m0755 nmon_x86_rhel3 %{buildroot}%{_bindir}/nmon}
%{?el2:%{__install} -Dp -m0755 nmon_x86_rhel2 %{buildroot}%{_bindir}/nmon}
%{?rh9:%{__install} -Dp -m0755 nmon_x86_redhat9 %{buildroot}%{_bindir}/nmon}
%endif
%ifarch x86_64
%{?fc6:%{__install} -Dp -m0755 nmon_x86_64_fedora6 %{buildroot}%{_bindir}/nmon}
%{?el4:%{__install} -Dp -m0755 nmon_x86_64_rhel4u4 %{buildroot}%{_bindir}/nmon}
%endif
%ifarch ppc ppc64
%{?el4:%{__install} -Dp -m0755 nmon_power_rhel4 %{buildroot}%{_bindir}/nmon}
%{?el3:%{__install} -Dp -m0755 nmon_power_rhel3 %{buildroot}%{_bindir}/nmon}
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/nmon

%changelog
* Wed Jan 31 2007 Dag Wieers <dag@wieers.com> - 11d-1
- Initial package. (using DAR)
