# $Id$
# Authority: dag
# Upstream: Janet Casey <jcasey$gnu,org>
# Upstream: <sercd$lists,lysator,liu,se>

Summary: Serial Port Interface for Cyclades Terminal Servers
Name: cyclades-serial-client
Version: 0.93
Release: 1.2%{?dist}
License: GPL
Group: Applications/Communications
URL: http://www.lysator.liu.se/~astrand/projects/cyclades-serial-client/

Source: http://www.lysator.liu.se/~astrand/projects/cyclades-serial-client/cyclades-serial-client-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++

%description
cyclades-serial-client is a RFC 2217 compliant client. It works with
servers such as sercd.

%prep
%setup

%{__perl} -pi.orig -e -s 's|tsrsock|cyclades-ser-cli|g' cyclades-serial-client

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 cyclades-devices %{buildroot}%{_sysconfdir}/cyclades-devices
%{__install} -Dp -m0755 cyclades-ser-cli %{buildroot}%{_sbindir}/cyclades-ser-cli
%{__install} -Dp -m0755 cyclades-serial-client %{buildroot}%{_sbindir}/cyclades-serial-client
%{__install} -Dp -m0644 man/cyclades-ser-cli.8 %{buildroot}%{_mandir}/man8/cyclades-ser-cli.8
%{__install} -Dp -m0644 man/cyclades-serial-client.8 %{buildroot}%{_mandir}/man8/cyclades-serial-client.8
%{__install} -Dp -m0644 man/cyclades-devices.5 %{buildroot}%{_mandir}/man5/cyclades-devices.5

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man5/cyclades-devices.5*
%doc %{_mandir}/man8/cyclades-ser-cli.8*
%doc %{_mandir}/man8/cyclades-serial-client.8*
%config(noreplace) %{_sysconfdir}/cyclades-devices
%{_sbindir}/cyclades-ser-cli
%{_sbindir}/cyclades-serial-client

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.93-1.2
- Rebuild for Fedora Core 5.

* Fri Mar 18 2005 Dag Wieers <dag@wieers.com> - 0.93-1
- Initial package. (using DAR)
