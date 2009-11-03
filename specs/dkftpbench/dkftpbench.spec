# $Id$
# Authority: dag

Summary: FTP server benchmarking tool
Name: dkftpbench
Version: 0.45
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.kegel.com/dkftpbench/

Source: http://www.kegel.com/dkftpbench/dkftpbench-%{version}.tar.gz
Patch: 64bit-fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: autoconf, automake, gcc-c++

%description
dkftpbench is an FTP benchmark program inspired by SPECweb99. The result
of the benchmark is a number-of-simultaneous-users rating; after running
the benchmark properly, you have a good idea how many simultaneous dialup
clients a server can support. The target bandwidth per client is set at
28.8 kilobits/second to model dialup users; this is important for servers
on the real Internet, which often serve thousands of clients on only
10 MBits/sec of bandwidth.

The final result of the benchmark is "the number of simultaneous
28.8 kilobits/second dialup users". To estimate this number, the
benchmark starts up a new simulated user as soon as the last one has
finished connecting. It stops increasing the number of users when one
fails to connect, fails to maintain the desired bandwidth, or the limit
specified by the -n option is reached. It runs the simulated users until
the amount of time specified by the -t option has elapsed since the last
simulated user birth or death; the final score is the number of users
still alive at the end.

%prep
%setup
%patch -p1

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags} all dklimits

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0755 dklimits %{buildroot}%{_bindir}/dklimits

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.html AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/dkftpbench
%{_bindir}/dklimits
%exclude %{_includedir}/dkftpbench
%exclude %{_libdir}/libPoller.a

%changelog
* Mon Oct 09 2006 Dag Wieers <dag@wieers.com> - 0.45-2
- Fixed group name.

* Sun May 08 2005 Dag Wieers <dag@wieers.com> - 0.45-1
- Initial package. (using DAR)
