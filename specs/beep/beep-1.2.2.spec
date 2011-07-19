# $Id$
# Authority: dag

%{?el5:%define _without_modprobe_d 1}
%{?el4:%define _without_modprobe_d 1}
%{?el3:%define _without_modprobe_d 1}
%{?el2:%define _without_modprobe_d 1}

Summary: Beep the PC speaker any number of ways
Name: beep
Version: 1.2.2
Release: 1%{?dist}
License: GPLv2+
Group: Applications/System
URL: http://www.johnath.com/beep/

Source0: http://www.johnath.com/beep/beep-%{version}.tar.gz
Source1: beep-modprobe.conf
Patch0: beep-1.2.2-install-fixes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glibc-kernheaders

%description
Beep allows the user to control the PC speaker with precision,
allowing different sounds to indicate different events. While it
can be run quite happily on the commandline, it's intended place
of residence is within shell/perl scripts, notifying the user when
something interesting occurs. Of course, it has no notion of
what's interesting, but it's real good at that notifying part.

%prep
%setup
%patch0 -p1 -b .install-fixes

%build
%{__make} %{?_smp_mflags} CFLAGS="${optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%if %{!?_without_modprobe_d:1}0
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/modprobe.d/beep.conf
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING CREDITS README
%doc %{_mandir}/man1/beep.1*
%{!?_without_modprobe_d:%config %{_sysconfdir}/modprobe.d/beep.conf}
%{_bindir}/beep

%changelog
* Sat Jun 04 2011 Dag Wieers <dag@wieers.com> - 1.2.2-1
- Initial package. (using DAR)
