# $Id$
# Authority: dag

%{?el4:%define _without_libpcapdevel 1}
%{?el3:%define _without_libpcapdevel 1}
%{?el3:%define _without_pcapbpf_h 1}

%define desktop_vendor rpmforge

Summary: Graphical network viewer modeled after etherman
Name: etherape
Version: 0.9.9
Release: 2%{?dist}
License: GPL
Group: Applications/System
URL: http://etherape.sourceforge.net/

Source: http://dl.sf.net/etherape/etherape-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: libglade2-devel
BuildRequires: libgnomeui-devel
BuildRequires: libpcap
BuildRequires: pkgconfig
BuildRequires: scrollkeeper
%{!?_without_libpcapdevel:BuildRequires: libpcap-devel}

%description
Etherape is a graphical network monitor for Unix modeled after
etherman. Featuring ether, ip and tcp modes, it displays network
activity graphically. Hosts and links change in size with traffic.
Color coded protocols display. It supports ethernet, ppp and slip
devices. It can filter traffic to be shown, and can read traffic
from a file as well as live from the network.

%prep
%setup

%{__perl} -pi.orig -e 's|res_mkquery|__res_mkquery|g' configure

%{!?_without_pcapbpf_h:%{__perl} -pi.orig -e 's|net/bpf.h|pcap-bpf.h|' src/*.c src/*.h}

%{__cat} <<EOF >etherape.console
USER=root
PROGRAM=%{_sbindir}/etherape
SESSION=true
EOF

%{__cat} <<EOF >etherape.pam
#%PAM-1.0
auth       sufficient   pam_rootok.so
auth       sufficient   pam_timestamp.so
auth       required     pam_stack.so service=system-auth
session    required     pam_permit.so
session    optional     pam_timestamp.so
session    optional     pam_xauth.so
account    required     pam_permit.so
EOF

%build
export LDFLAGS="-L%{_libdir} -L/%{_lib}"
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__mv} -f %{buildroot}%{_bindir}/etherape %{buildroot}%{_sbindir}/etherape
%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/etherape

%{__install} -Dp -m0644 etherape.console %{buildroot}%{_sysconfdir}/security/console.apps/etherape
%{__install} -Dp -m0644 etherape.pam %{buildroot}%{_sysconfdir}/pam.d/etherape

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
    --delete-original                           \
    --add-category X-Red-Hat-Base               \
    --add-category Application                  \
    --remove-category Network                   \
    --dir %{buildroot}%{_datadir}/applications  \
    %{buildroot}%{_datadir}/applications/etherape.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FAQ NEWS OVERVIEW README* TODO
#doc html/*.html
%doc %{_mandir}/man1/etherape.1*
%doc %{_datadir}/gnome/help/etherape/
%doc %{_datadir}/omf/etherape/
%config %{_sysconfdir}/etherape/
%config %{_sysconfdir}/security/console.apps/etherape
%config %{_sysconfdir}/pam.d/etherape
%{_bindir}/etherape
%{_datadir}/applications/%{desktop_vendor}-etherape.desktop
%{_datadir}/etherape/
%{_datadir}/pixmaps/etherape.png
%{_sbindir}/etherape

%changelog
* Thu Aug 19 2010 Dag Wieers <dag@wieers.com> - 0.9.9-2
- Fix desktop categories.

* Mon Jan 11 2010 Dag Wieers <dag@wieers.com> - 0.9.9-1
- Updated to release 0.9.9.

* Mon Sep 28 2009 Dag Wieers <dag@wieers.com> - 0.9.8-1
- Updated to release 0.9.8.

* Mon Sep 28 2009 Dag Wieers <dag@wieers.com> - 0.9.7-1
- Updated to release 0.9.7.

* Wed May 17 2006 Dag Wieers <dag@wieers.com> - 0.9.6-1
- Updated to release 0.9.6.

* Sat May 06 2006 Dag Wieers <dag@wieers.com> - 0.9.5-1
- Updated to release 0.9.5.

* Mon Jan 16 2006 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Fri Aug 19 2005 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Wed Dec 22 2004 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Tue Apr 29 2003 Dag Wieers <dag@wieers.com> - 0.9.0-0
- Initial package. (using DAR)
