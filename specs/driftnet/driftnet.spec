# $Id$
# Authority: dag
# Upstream: Chris Lightfoot <chris$ex-parrot,com>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}

%{?el5:%define _with_libpcapdevel 1}

%{?fc6:%define _with_libpcapdevel 1}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: Sniff the network for images and movies and displays them
Name: driftnet
Version: 0.1.6
Release: 1.2
License: GPL
Group: Applications/Internet
URL: http://www.ex-parrot.com/~chris/driftnet/

Source: http://www.ex-parrot.com/~chris/driftnet/driftnet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap, gtk+-devel, libungif-devel, libjpeg-devel
%{!?_without_modxorg:BuildRequires: imake}
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
Driftnet is a program which listens to network traffic and picks out images
from TCP streams it observes. Fun to run on a host which sees lots of web
traffic.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 driftnet %{buildroot}%{_sbindir}/driftnet
%{__install} -Dp -m0644 driftnet.1 %{buildroot}%{_mandir}/man1/driftnet.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING CREDITS README TODO
%doc %{_mandir}/man1/driftnet.1*
%{_sbindir}/driftnet

%changelog
* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 0.1.6-1
- Initial package. (using DAR)
