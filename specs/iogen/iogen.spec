# $Id$
# Authority: dag

Summary: I/O generator
Name: iogen
Version: 3.1
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.peereboom.us/iogen/

Source: http://www.peereboom.us/iogen/iogen_%{version}p0.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: groff

%description
iogen is an I/O generator. It forks child processes that each run a mix
of reads and writes. The idea is to generate heavily fragmented files
to make the hardware suffer as much as possible. This tool has been
used to test filesystems, drivers, firmware, and hardware devices.

It is by no means meant as a performance measuring tool since it tries
to recreate the worst case scenario I/O.

%prep
%setup -n %{name}_%{version}p0

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 iogen %{buildroot}%{_bindir}/iogen
%{__install} -Dp -m0644 src/iogen.8 %{buildroot}%{_mandir}/man8/iogen.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man8/iogen.8*
%{_bindir}/iogen

%changelog
* Sat May 23 2007 Dag Wieers <dag@wieers.com> - 3.1-1
- Updated to release 3.1p0.

* Tue Apr 17 2007 Dag Wieers <dag@wieers.com> - 3.0-1
- Updated to release 3.0.

* Fri Mar 09 2007 Dag Wieers <dag@wieers.com> - 2.2-2
- Fixed group.

* Sun Feb 11 2007 Dag Wieers <dag@wieers.com> - 2.2-1
- Initial package. (using DAR)
