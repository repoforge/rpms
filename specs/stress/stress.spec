# $Id$
# Authority: dag
# Upstream: Amos Waterland <apw$us,ibm,com>

%{?dist: %{expand: %%define %dist 1}}

Summary: tool to impose stress on a POSIX-compliant operating system
Name: stress
Version: 0.18.1
Release: 1
License: GPL
Group: Applications/System
URL: http://weather.ou.edu/~apw/projects/stress/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://weather.ou.edu/~apw/projects/stress/stress-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?dist:BuildRequires: glibc-headers}
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
%makeinstall

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

%preun
/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc doc/*.html
%doc %{_mandir}/man?/*
%doc %{_infodir}/*.info*
%{_bindir}/*
#exclude %{_infodir}/dir

%changelog
* Wed Jul 14 2004 Dag Wieers <dag@wieers.com> - 0.18.1-1
- Cosmetic changes

* Tue Aug 05 2003 Dag Wieers <dag@wieers.com> - 0.18.1-0
- Updated to release 0.18.1.

* Sat Jun 28 2003 Dag Wieers <dag@wieers.com> - 0.17.2-0
- Updated to release 0.17.2.

* Mon May 26 2003 Dag Wieers <dag@wieers.com> - 0.17-1
- Updated to release 0.17.

* Sat May 17 2003 Dag Wieers <dag@wieers.com> - 0.17-0.pre20
- Initial package. (using DAR)
