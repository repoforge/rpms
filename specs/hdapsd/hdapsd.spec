# $Id$
# Authority: dag

Summary: HDAPS (Hard Disk Active Protection System) daemon
Name: hdapsd
%define real_version 20090401
Version: 0.0
Release: 0.20090401%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://hdaps.sourceforge.net/
Source0: http://sourceforge.net/projects/hdaps/files/hdapsd/hdapsd-%{real_version}/hdapsd-%{real_version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: kernel >= 2.6.18

%description
hdapsd is a daemon that reads from the HDAPS (Hard Disk Active Protection
System) driver and protects the hard disk from sudden movements that may
harm it.

%prep
%setup -n %{name}-%{real_version}

%build
export CFLAGS="%{optflags}"

%configure
%{__make} %{?_smp_mflags}

%install
%{__make} install DESTDIR="%{buildroot}"

# remove duplicate docs
%{__rm} -rf %{buildroot}%{_defaultdocdir}/hdapsd

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_sbindir}/hdapsd
%doc ChangeLog
%doc README
%doc %{_mandir}/man8/hdapsd.8*

%changelog
* Fri Feb 18 2011 Denis Fateyev <denis@fateyev.com> - 0.0-0.20090401
- Update to build 20090401.

* Mon Jun 11 2007 Dag Wieers <dag@wieers.com> - 0.0-0.20070524
- Initial package. (using DAR)
