# $Id$

# Authority: dag
# Upstream: Lennart Poettering <mz617469@poettering.de>

Summary: tool to use ATI TV-OUT
Name: atitvout
Version: 0.4
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://www.stud.uni-hamburg.de/users/lennart/projects/atitvout/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.stud.uni-hamburg.de/users/lennart/projects/atitvout/atitvout-0.4.tar.gz
Patch0: atitvout-rv200.patch
Patch1: http://ftp.debian.org/debian/pool/main/a/atitvout/atitvout_0.4-2.diff.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
This utility program may be used for executing several configuration
commands for the TV Out connector of ATI Rage Mobility P/M graphics
boards under GNU/Linux on x86. It is intended primarily to enable TV
Out support after bootup and for switching the used TV standard from
NTSC to PAL.

The utility makes use of x86-VESA-BIOS-calls and thus is not portable
to other architectures like PPC: No TV-Out on Macs with this tool.

%prep
%setup -n %{name}
%patch0 -p0
%patch1 -p1
%{__perl} -pi.orig -e 's|(-O2 )?-g|%{optflags}|' Makefile lrmi-0.6/Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_mandir}/man1
%{__install} -m0755 atitvout %{buildroot}%{_sbindir}
%{__install} -m0644 debian/atitvout.1 %{buildroot}%{_mandir}/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING HARDWARE README
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Mon Sep 08 2003 Dag Wieers <dag@wieers.com> - 0.4-0
- Initial package. (using DAR)
