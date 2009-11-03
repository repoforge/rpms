# $Id$
# Authority: dag
# Upstream: Amos Waterland <apw$rossby,metr,ou,edu>

Summary: Tool that performs system call replay of strace logs
Name: sreplay
Version: 0.2.8
Release: 1%{?dist}
License: LGPL
Group: Development/Debuggers
URL: http://weather.ou.edu/~apw/projects/sreplay/

Source: http://weather.ou.edu/~apw/projects/sreplay/sreplay-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
sreplay is a tool that performs system call replay of strace logs. It supports
playback of about 27 system calls, which is enough to replay the interesting
paths of some server applications and to replay simple dynamically-linked
applications in their entirety.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 sreplay %{buildroot}%{_bindir}/sreplay

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING NEWS README
%{_bindir}/sreplay

%changelog
* Tue Jun 05 2007 Dag Wieers <dag@wieers.com> - 0.2.8-1
- Updated to release 0.2.8.

* Tue May 29 2007 Dag Wieers <dag@wieers.com> - 0.2.7-1
- Updated to release 0.2.7.

* Tue May 15 2007 Dag Wieers <dag@wieers.com> - 0.2.6-1
- Initial package. (using DAR)
