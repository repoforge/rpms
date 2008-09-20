# $Id$
# Authority: dag

Summary: Utilities for performing block layer IO tracing in the linux kernel
Name: blktrace
Version: 0.99.3
Release: 1
License: GPL
Group: Development/System
URL: http://brick.kernel.dk/snaps/

Source: http://brick.kernel.dk/snaps/blktrace-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libaio-devel

%description
blktrace is a block layer IO tracing mechanism which provides detailed
information about request queue operations to user space. This package
includes both blktrace, a utility which gathers event traces from the kernel;
and blkparse, a utility which formats trace data collected by blktrace.

%prep
%setup -n %{name}

%build
%{__make} all CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install dest="%{buildroot}" \
    prefix="%{buildroot}%{_prefix}" \
    mandir="%{buildroot}%{_mandir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README doc/blktrace.tex
%doc %{_mandir}/man1/blkparse.1*
%doc %{_mandir}/man1/blkrawverify.1*
%doc %{_mandir}/man1/btt.1*
%doc %{_mandir}/man1/verify_blkparse.1*
%doc %{_mandir}/man8/blktrace.8*
%doc %{_mandir}/man8/btrace.8*
%{_bindir}/blkparse
%{_bindir}/blkrawverify
%{_bindir}/blktrace
%{_bindir}/btrace
%{_bindir}/btt
%{_bindir}/verify_blkparse

%changelog
* Thu Sep 18 2008 Dag Wieers <dag@wieers.com> - 0.0.20080103162505git-1
- Initial package. (using DAR)
