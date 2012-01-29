# $Id$
# Authority: dag

Summary: Program to snoop on a TTY through another
Name: ttysnoop
Version: 0.12d
Release: 1%{?dist}
License: distributable
Group: System Environment/Base
URL: http://www.mirrors.wiretapped.net/security/host-security/

Source0: http://dl.packetstormsecurity.net/UNIX/IDS/ttysnoop-%{version}.tar.gz
#Source0: http://www.mirrors.wiretapped.net/security/host-security/ttysnoop-%{version}.tar.gz
Patch0: ttysnoop-0.12c-glibc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The package allows you to snoop on login tty's through another tty-device
or pseudo-tty. The snoop-tty becomes a 'clone' of the original tty,
redirecting both input and output from/to it.

%prep
%setup
#patch0 -p1

%build
%{__make} %{?_smp_mflags} RPM_OPTS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
#%{__make} install
%{__install} -Dp -m0755 ttysnoop %{buildroot}%{_sbindir}/ttysnoop
%{__install} -Dp -m0755 ttysnoops %{buildroot}%{_sbindir}/ttysnoops
%{__install} -Dp -m0644 ttysnoop.8 %{buildroot}%{_mandir}/man8/ttysnoop.8
%{__install} -Dp -m0644 snooptab.dist %{buildroot}%{_sysconfdir}/snooptab

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man8/ttysnoop.8*
%config %{_sysconfdir}/snooptab
%{_sbindir}/ttysnoop
%{_sbindir}/ttysnoops

%changelog
* Fri Dec 24 2010 Dag Wieers <dag@wieers.com> - 0.12d-1
- Updated to release 0.12d.

* Mon Aug 22 2005 Dag Wieers <dag@wieers.com> - 0.12c-1
- Initial package. (using DAR)
