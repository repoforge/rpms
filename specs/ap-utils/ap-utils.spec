# $Id$
# Authority: dag
# Upstream: <ap-utils@lists.polesye.net>

Summary: Configure and monitor Wireless Access Points
Name: ap-utils
Version: 1.4.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://ap-utils.polesye.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/ap-utils/ap-utils-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildrequires: ncurses-devel

%description
Wireless Access Point Utilities for Unix is a set of utilities 
to configure and monitor Wireless Access Points using SNMP.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr (-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc Documentation/FAQ Documentation/*.html 
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_sbindir}/*

%changelog
* Sun May 30 2004 Dag Wieers <dag@wieers.com> - 1.4.1-1
- Updated to release 1.4.1.

* Mon Feb 23 2004 Dag Wieers <dag@wieers.com> - 1.4-0
- Initial package. (using DAR)
