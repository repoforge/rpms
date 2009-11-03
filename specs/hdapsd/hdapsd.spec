# $Id$
# Authority: dag

Summary: HDAPS (Hard Disk Active Protection System) daemon
Name: hdapsd
%define real_version 20070524
Version: 0.0
Release: 0.20070524%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://www.zen24593.zen.co.uk/hdaps/

Source0: http://www.zen24593.zen.co.uk/hdaps/hdapsd-20070524.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: kernel >= 2.6.18

%description
hdapsd is a daemon that reads from the HDAPS (Hard Disk Active Protection
System) driver and protects the hard disk from sudden movements that may
harm it.

%prep
%setup -T -c %{name}-%{version}

%build
%{__cc} %{optflags} -o hdapsd %{SOURCE0}

%install
%{__install} -Dp -m0755 hdapsd %{buildroot}%{_sbindir}/hdapsd

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_sbindir}/hdapsd

%changelog
* Mon Jun 11 2007 Dag Wieers <dag@wieers.com> - 0.0-0.20070524
- Initial package. (using DAR)
