# $Id$
# Authority: dag
# Upstream: Ward van Wanrooij <ward$ward,nu>

Summary: Shows process information and statistics
Name: psinfo
Version: 0.1
Release: 1
License: GPL
Group: Applications/
URL: http://www.ward.nu/computer/psinfo/

Source: http://www.ward.nu/computer/psinfo/psinfo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
psinfo shows process information and statistics using the kernel /proc
interface. It includes:

    Process state, environment, arguments and flags
    CPU usage
    Scheduling
    I/O usage
    Virtual memory status
    Pagefaults
    Capabilities
    Signals

psinfo is useful for providing a detailed view of the current state of an
application when diagnosing issues or performance problems.

%prep
%setup

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 psinfo %{buildroot}%{_bindir}/psinfo

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/psinfo

%changelog
* Fri Oct 10 2008 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
