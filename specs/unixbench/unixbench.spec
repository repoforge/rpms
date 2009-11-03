# $Id$
# Authority: dag
# Upstream: Ian Smith <johantheghost$yahoo,com>

Summary: BYTE's UNIX Benchmarks
Name: unixbench
Version: 5.1.2
Release: 1%{?dist}
License: Distributable
Group: Applications/System
URL: http://www.hermit.org/Linux/Benchmarking/

Source: http://www.hermit.org/Linux/Benchmarking/unixbench-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This page presents some information on Linux benchmarking; and in particular,
UnixBench Version 5, a version of the venerable Byte benchmarks updated to
handle multi-CPU systems.

%prep
%setup

### Add old XFree86 library path, add -lm for EL2
%{__perl} -pi.orig -e 's|(GL_LIBS\s*=\s*)(.*)$|$1 -L%{_prefix}/X11R6/%{_lib} -lm $2|' Makefile

%build
%{__make} %{?_smp_mflags} OPTION="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 Run %{buildroot}%{_bindir}/unixbench

%{__install} -d -m0755 %{buildroot}%{_libdir}/unixbench/
%{__cp} -av pgms/ testdir/ %{buildroot}%{_libdir}/unixbench/

%clean
%{__rm} -rf %{buildroot}

%files
%doc README USAGE WRITING_TESTS
%{_bindir}/unixbench
%{_libdir}/unixbench/

%changelog
* Wed Dec 10 2008 Dag Wieers <dag@wieers.com> - 5.1.2-1
- Updated to release 5.1.2.

* Fri Feb 16 2007 Dag Wieers <dag@wieers.com> - 4.0.1-1
- Initial package. (using DAR)
