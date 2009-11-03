# $Id$
# Authority: dag
# Upstream: Marc Lehmann <pether$plan9,de>

### FIXME: TODO: Add sysv script based on own template.

Summary: Create a virtual ethernet using host-to-host tunnels
Name: gvpe
Version: 2.22
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: https://savannah.gnu.org/projects/gvpe/

Source: http://ftp.gnu.org/gnu/gvpe/gvpe-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel, gcc-c++
Obsoletes: vpe <= %{version}

%description
VPE creates a virtual ethernet (broadcasts supported, any protocol that works
with a normal ethernet should work with VPE) by creating host-to-host tunnels
between multiple endpoints.

Unlike other virtual private "network" solutions which merely create a single
tunnel, VPE creates a real network with multiple endpoints.

It is designed to be very simple (cipher selection done at compiletime etc.),
and easy to setup (only a single config file shared unmodified between all
hosts).

Vpn hosts can neither sniff nor fake packets, that is, you can use MAC-based
filtering to ensure authenticity of packets even from member nodes.

VPE can also be used to tunnel into some vpn network using a variety of
protocols (https-proxy, tcp, udp, rawip, icmp-tunneling). It is, however,
primarily designed to sit on the gateway machines of company branches to
connect them together.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post
/sbin/install-info --entry="* gvpe: (gvpe).       %{summary}" %{_infodir}/%{name}.info.gz %{_infodir}/dir

%preun
/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc doc/complex-example/
%doc %{_mandir}/man5/gvpe.5*
%doc %{_mandir}/man5/gvpe.conf.5*
%doc %{_mandir}/man5/gvpe.osdep.5*
%doc %{_mandir}/man7/gvpe.protocol.7*
%doc %{_mandir}/man8/gvpe.8*
%doc %{_mandir}/man8/gvpectrl.8*
%doc %{_infodir}/gvpe.info*
%{_bindir}/gvpectrl
%{_sbindir}/gvpe

%changelog
* Sun Feb 22 2009 Dag Wieers <dag@wieers.com> - 2.22-1
- Updated to release 2.22.

* Thu Sep 04 2008 Dag Wieers <dag@wieers.com> - 2.2-1
- Updated to release 2.2.

* Fri Mar 30 2007 Dag Wieers <dag@wieers.com> - 2.01-1
- Updated to release 2.01.

* Fri Dec 23 2005 Dries Verachtert <dries@ulyssis.org> - 2.0-2
- Avoid install-info warning at install, thanks to xyzzy at mail333 dot com.

* Thu Dec 08 2005 Dag Wieers <dag@wieers.com> - 2.0-1
- Updated to release 2.0.

* Sat Apr 30 2005 Dag Wieers <dag@wieers.com> - 1.9-1
- Updated to release 1.9.

* Sat Mar 19 2005 Dag Wieers <dag@wieers.com> - 1.8-1
- Updated to release 1.8.

* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 1.6-1
- Updated to release 1.6.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 1.5-0
- Initial package. (using DAR)
