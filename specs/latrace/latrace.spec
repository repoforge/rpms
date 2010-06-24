# $Id$
# Authority: dag

Summary: LD_AUDIT feature frontend for glibc 2.4+
Name: latrace
Version: 0.5.9
Release: 1%{?dist}
License: GPLv3+
Group: Development/Debuggers
URL: http://people.redhat.com/jolsa/latrace/

Source: http://people.redhat.com/jolsa/latrace/dl/latrace-%{version}.tar.bz2
Patch0: latrace-0.5.9-autoconf.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: %{ix86} x86_64 arm
BuildRequires: asciidoc
BuildRequires: autoconf
BuildRequires: binutils-devel
BuildRequires: bison
BuildRequires: xmlto

%description
latrace allows you to trace library calls and get their statistics in a
manner similar to the strace utility (syscall tracing).

%prep
%setup
%patch0 -p1

%build
autoconf
%configure
%{__make} V="1"

%install
%{__rm} -rf %{buildroot}
%{__make} install ROOTDIR="%{buildroot}" V="1"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README ReleaseNotes TODO
%doc %{_mandir}/man1/latrace.1*
%config(noreplace) %{_sysconfdir}/latrace.conf
%config(noreplace) %{_sysconfdir}/latrace.d/
%{_bindir}/latrace
%{_bindir}/latrace-ctl
%{_libdir}/libltaudit.so.%{version}

%changelog
* Thu Jun 24 2010 Dag Wieers <dag@wieers.com> - 0.5.9-1
- Initial package. (using DAR)
