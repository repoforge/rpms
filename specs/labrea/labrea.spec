# $Id$
# Authority: dag
# Upstream: lorgor <lorgor$users,sourceforge,net>

%define real_version 2.5-stable-1

Summary: "Sticky" Honeypot and IDS
Name: labrea
Version: 2.5
Release: 1
License: GPL
Group: Applications/Internet
URL: http://labrea.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/labrea/labrea-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
LaBrea takes over unused IP addresses, and creates virtual servers that
are attractive to worms, hackers, and other denizens of the Internet.
The program answers connection attempts in such a way that the machine
at the other end gets "stuck", sometimes for a very long time.

%prep
%setup -n %{name}-%{real_version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/labrea.conf
%{_sbindir}/labrea

%changelog
* Fri Jul 02 2004 Dag Wieers <dag@wieers.com> - 2.5-1
- Initial package. (using DAR)
