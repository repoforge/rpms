# $Id$
# Authority: dag
# Upstream: Amos Waterland <apw$us,ibm,com>


Summary: Tool to impose stress on a POSIX-compliant operating system
Name: stress
Version: 1.0.0
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://weather.ou.edu/~apw/projects/stress/

Source: http://weather.ou.edu/~apw/projects/stress/stress-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?dtag:BuildRequires: glibc-headers}
%{?fc3:BuildRequires: glibc-headers}
%{?fc2:BuildRequires: glibc-headers}
%{?fc1:BuildRequires: glibc-headers}
%{?el3:BuildRequires: glibc-headers}
%{?rh9:BuildRequires: glibc-devel}
%{?rh8:BuildRequires: glibc-devel}
%{?rh7:BuildRequires: glibc-devel}
%{?el2:BuildRequires: glibc-devel}
%{?rh6:BuildRequires: glibc-devel}

%description
Stress is a tool which imposes a configurable amount of CPU, memory, I/O,
or disk stress on a POSIX-compliant operating system. Stress is written
in highly-portable ANSI C, and uses the GNU Autotools to compile on a
great number of UNIX-like operating systems.

Stress is not a benchmark, it is rather a tool which puts the system under
a repeatable, defined amount of load so that a systems programmer or system
administrator can analyze the performance characteristics of the system or
specific components thereof.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

%preun
/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README doc/*.html
%doc %{_mandir}/man1/stress.1*
%doc %{_infodir}/stress.info*
%{_bindir}/stress
#exclude %{_infodir}/dir

%changelog
* Tue Dec 18 2007 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Fri Dec 09 2005 Dag Wieers <dag@wieers.com> - 0.18.8-1
- Updated to release 0.18.8.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 0.18.6-1
- Updated to release 0.18.6.

* Fri Apr 08 2005 Dag Wieers <dag@wieers.com> - 0.18.4-1
- Updated to release 0.18.4.

* Fri Nov 19 2004 Dag Wieers <dag@wieers.com> - 0.18.2-1
- Updated to release 0.18.2.

* Wed Jul 14 2004 Dag Wieers <dag@wieers.com> - 0.18.1-1
- Cosmetic changes.

* Tue Aug 05 2003 Dag Wieers <dag@wieers.com> - 0.18.1-0
- Updated to release 0.18.1.

* Sat Jun 28 2003 Dag Wieers <dag@wieers.com> - 0.17.2-0
- Updated to release 0.17.2.

* Mon May 26 2003 Dag Wieers <dag@wieers.com> - 0.17-1
- Updated to release 0.17.

* Sat May 17 2003 Dag Wieers <dag@wieers.com> - 0.17-0.pre20
- Initial package. (using DAR)
