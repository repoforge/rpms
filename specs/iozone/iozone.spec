# $Id$
# Authority: dag
# Upstream: <capps$iozone,org>
# Upstream: William Norcott <William,Norcott$oracle,com>

%define real_version 3_221

Summary: IOzone Filesystem Benchmark
Name: iozone
Version: 3.221
Release: 1
License: Freeware
Group: Applications/Engineering
URL: http://www.iozone.org/ 

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.iozone.org/src/current/iozone%{real_version}.tar
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
IOzone is a filesystem benchmark tool. The benchmark generates and
measures a variety of file operations. Iozone has been ported to
many machines and runs under many operating systems.

Iozone is useful for performing a broad filesystem analysis of a vendors
computer platform. The benchmark tests file I/O performance for the following
operations: Read, write, re-read, re-write, read backwards, read strided,
fread, fwrite, random read, pread ,mmap, aio_read, aio_write.

%prep
%setup -c

%build
%{__make} %{?_smp_mflags} -C src/current linux

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 src/current/iozone %{buildroot}%{_bindir}/iozone
%{__install} -D -m0755 src/current/Generate_Graphs %{buildroot}%{_datadir}/iozone/Generate_Graphs
%{__install} -D -m0755 src/current/gengnuplot.sh %{buildroot}%{_datadir}/iozone/gengnuplot.sh
%{__install} -D -m0755 src/current/gnu3d.dem %{buildroot}%{_datadir}/iozone/gnu3d.dem

%{__install} -D -m0644 docs/iozone.1 %{buildroot}%{_mandir}/man1/iozone.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc docs/IOzone_msword_98.pdf docs/Iozone_ps.gz src/current/Gnuplot.txt
%doc %{_mandir}/man?/*
%{_bindir}/iozone
%{_datadir}/iozone/

%changelog
* Tue Jul 20 2004 Dag Wieers <dag@wieers.com> - 3.221-1
- Updated to release 3.221.

* Sat Jun 19 2004 Dag Wieers <dag@wieers.com> - 3.218-1
- Initial package. (using DAR)
