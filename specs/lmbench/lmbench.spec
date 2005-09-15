# $Id$
# Authority: dag

Summary: Suite of simple, portable benchmarks 
Name: lmbench
Version: 3.0
Release: 0.a5
License: GPL
Group: Utilities
URL: http://www.bitmover.com/lmbench

Source: http://dl.sf.net/lmbench/lmbench-%{version}-a5.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Bandwidth benchmarks: cached file read, memory copy (bcopy), memory read,
memory write, pipe, TCP; Latency benchmarks: context switching, connection
establishment, pipe, TCP, UDP, RPC hot potato, file system creates and
deletes, process creation, signal handling, system call overhead,  memory
read latency; Miscellanious Processor clock rate calculation.

%prep
%setup -n %{name}-%{version}-a5

%build
%{__make} %{?_smp_mflags}

%install
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_mandir}/{man1,man3,man8}/ \

cd bin/*-linux-gnu
%{__install} -p -m0755 bw_* %{buildroot}%{_bindir}
%{__install} -p -m0755 cache %{buildroot}%{_bindir}
%{__install} -p -m0755 disk %{buildroot}%{_bindir}
%{__install} -p -m0755 enough %{buildroot}%{_bindir}
%{__install} -p -m0755 flushdisk %{buildroot}%{_bindir}
%{__install} -p -m0755 hello %{buildroot}%{_bindir}
%{__install} -p -m0755 lat_* %{buildroot}%{_bindir}
%{__install} -p -m0755 line %{buildroot}%{_bindir}
%{__install} -p -m0755 lmdd %{buildroot}%{_bindir}
%{__install} -p -m0755 lmhttp %{buildroot}%{_bindir}
%{__install} -p -m0755 loop_o %{buildroot}%{_bindir}
%{__install} -p -m0755 memsize %{buildroot}%{_bindir}
%{__install} -p -m0755 mhz %{buildroot}%{_bindir}
%{__install} -p -m0755 msleep %{buildroot}%{_bindir}
%{__install} -p -m0755 par_* %{buildroot}%{_bindir}
%{__install} -p -m0755 stream %{buildroot}%{_bindir}
%{__install} -p -m0755 timing_o %{buildroot}%{_bindir}
%{__install} -p -m0755 tlb %{buildroot}%{_bindir}
cd -

%{__install} -p -m0644 doc/*.1 %{buildroot}%{_mandir}/man1/
%{__install} -p -m0644 doc/*.3 %{buildroot}%{_mandir}/man3/
%{__install} -p -m0644 doc/*.8 %{buildroot}%{_mandir}/man8/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ACKNOWLEDGEMENTS CHANGES COPYING COPYING-2 README hbench-REBUTTAL doc/*.ms
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Tue Sep 13 2005 Dag Wieers <dag@wieers.com> - 3.0-0.a5
Initial package. (using DAR)
