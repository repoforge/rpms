# $Id$

# Authority: dag

# Upstream: Fredrik Hubinette <hubbe@hubbe.net>

Summary: Bond an X display and a VNC session together
Name: x2vnc
Version: 1.6
Release: 0
License: GPL
Group: User Interface/Desktops
URL: http://fredrik.hubbe.net/x2vnc.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://fredrik.hubbe.net/x2vnc/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
x2vnc is an implementation of the VNC RFB protocol designed to control
a machine running a VNC server in a dual-monitor situation. Its effect
is to make the controlled machine's display function as if attached to
the controlling machine, allowing the use of just one set of input
devices on two or more machines.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1
%makeinstall \
	BINDIR="%{buildroot}%{_bindir}" \
	MANDIR="%{buildroot}%{_mandir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Thu Nov 27 2003 Dag Wieers <dag@wieers.com> - 1.6-0
- Updated to release 1.6.

* Wed Apr 09 2003 Dag Wieers <dag@wieers.com> - 1.5.1-0
- Initial package. (using DAR)
