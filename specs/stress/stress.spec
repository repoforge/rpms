# $Id$

# Authority: dag

# Upstream: Amos Waterland <apw@us.ibm.com>

Summary: A tool to impose stress on a POSIX-compliant operating system.
Name: stress
Version: 0.18.1
Release: 0
Group: Applications/System
License: GPL
URL: http://weather.ou.edu/~apw/projects/stress/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://weather.ou.edu/~apw/projects/stress/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

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

### Clean up buildroot
%{__rm} -f %{buildroot}%{_infodir}/dir

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
%doc %{_infodir}/*
%{_bindir}/*

%changelog
* Tue Aug 05 2003 Dag Wieers <dag@wieers.com> - 0.18.1-0
- Updated to release 0.18.1.

* Sat Jun 28 2003 Dag Wieers <dag@wieers.com> - 0.17.2-0
- Updated to release 0.17.2.

* Mon May 26 2003 Dag Wieers <dag@wieers.com> - 0.17-1
- Updated to release 0.17.

* Sat May 17 2003 Dag Wieers <dag@wieers.com> - 0.17-0.pre20
- Initial package. (using DAR)
