# $Id$

# Authority: dag

### FIXME: Add sysv script using sysconfig file.

Summary: Keylogger
Name: uberkey
Version: 1.2
Release: 0
License: GPL
Group: Applications/System
URL: http://www.linuks.mine.nu/uberkey/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.linuks.mine.nu/uberkey/uberkey-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A keylogger.

%prep
%setup

### FIXME: Fix to use autotools directories. (Please fix upstream)
%{__perl} -pi.orig -e '
		s|/usr/sbin/|\$(sbindir)/|;
		s|/usr/share/man/|\$(mandir)/|;
	' makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
### FIXME: Create directories. (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_mandir}/man8/
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 1.2-0
- Initial package. (using DAR)
