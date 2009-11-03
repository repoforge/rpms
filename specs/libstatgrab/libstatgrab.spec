# $Id$
# Authority: dag

Summary: Make system statistics
Name: libstatgrab
Version: 0.15
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.i-scream.org/libstatgrab/

Source: http://ftp.i-scream.org/pub/i-scream/libstatgrab/libstatgrab-%{version}.tar.gz
Patch: libstatgrab-0.14-nochmod.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libtool, ncurses-devel

%description
Libstatgrab is a library that provides cross platform access to statistics
about the system on which it's run. It's written in C and presents a selection
of useful interfaces which can be used to access key system statistics. The
current list of statistics includes CPU usage, memory utilisation, disk usage,
process counts, network traffic, disk I/O, and more. 

The current list of platforms is Solaris 2.x, Linux, and FreeBSD 4.x/5.x.
The aim is to extend this to include as many operating systems as possible. 

The package also includes a couple of useful tools. The first, saidar,
provides a curses-based interface to viewing the current state of the 
system. The second, statgrab, gives a sysctl-style interface to the
statistics gathered by libstatgrab. This extends the use of libstatgrab
to people writing scripts or anything else that can't easily make C 
function calls. Included with statgrab is a script to generate an MRTG
configuration file to use statgrab. 

%package -n statgrab-tools
Summary: Tools from libstatgrab to monitoring the system
Group: Applications/System

%description -n statgrab-tools
This package contains a few tools shiped with libstatgrab.
Eg. A tool called saidar, which shows various system
information like top, but - of course - OTHER informations.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package examples
Summary: The example files from %{name}
Group: Development/Tools
Requires: %{name} = %{version}-%{release}

%description examples
This package contains various examples used to show how
to develop libstatgrab based applications.

%prep
%setup
%patch0 -p0

%build
%configure --with-ncurses
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

cd examples/.libs
%{__install} -Dp -m0755 cpu_usage %{buildroot}%{_bindir}/cpu_usage
%{__install} -Dp -m0755 disk_traffic %{buildroot}%{_bindir}/disk_traffic
%{__install} -Dp -m0755 load_stats %{buildroot}%{_bindir}/load_stats
%{__install} -Dp -m0755 network_iface_stats %{buildroot}%{_bindir}/network_iface_stats
%{__install} -Dp -m0755 network_traffic %{buildroot}%{_bindir}/network_traffic
%{__install} -Dp -m0755 os_info %{buildroot}%{_bindir}/os_info
%{__install} -Dp -m0755 page_stats %{buildroot}%{_bindir}/page_stats
%{__install} -Dp -m0755 process_snapshot %{buildroot}%{_bindir}/process_snapshot
%{__install} -Dp -m0755 process_stats %{buildroot}%{_bindir}/process_stats
%{__install} -Dp -m0755 user_list %{buildroot}%{_bindir}/user_list
%{__install} -Dp -m0755 vm_stats %{buildroot}%{_bindir}/vm_stats
cd -

### Clean up buildroot
%{__chmod} 0755 %{buildroot}%{_bindir}/*

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n statgrab-tools
%defattr(-, root, root, 0755)
%doc COPYING
%doc %{_mandir}/man1/saidar.1*
%doc %{_mandir}/man1/statgrab.1*
%doc %{_mandir}/man1/statgrab-make-mrtg-config.1*
%doc %{_mandir}/man1/statgrab-make-mrtg-index.1*
%doc %{_mandir}/man3/statgrab.3*
%{_bindir}/saidar
%{_bindir}/statgrab
%{_bindir}/statgrab-make-mrtg-config
%{_bindir}/statgrab-make-mrtg-index

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README examples/*.c
%{_libdir}/libstatgrab.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/sg_get_*.3*
%{_includedir}/statgrab.h
%{_includedir}/statgrab_deprecated.h
%{_libdir}/libstatgrab.so
%{_libdir}/pkgconfig/libstatgrab.pc
%exclude %{_libdir}/libstatgrab.a
%exclude %{_libdir}/libstatgrab.la

%files examples
%defattr(-, root, root, 0755)
%{_bindir}/cpu_usage
%{_bindir}/disk_traffic
%{_bindir}/load_stats
%{_bindir}/network_iface_stats
%{_bindir}/network_traffic
%{_bindir}/os_info
%{_bindir}/page_stats
%{_bindir}/process_snapshot
%{_bindir}/process_stats
%{_bindir}/user_list
%{_bindir}/vm_stats

%changelog
* Mon Aug 06 2007 Dag Wieers <dag@wieers.com> - 0.15-1
- Initial package. (based on Fedora Extras)
