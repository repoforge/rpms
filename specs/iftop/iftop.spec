# $Id$
# Authority: dag
# Upstream: Paul Warren <pdw$ex-parrot,com>
# Upstream: Chris Lightfoot <chris$ex-parrot,com>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Display bandwidth usage on an interface
Name: iftop
Version: 0.17
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.ex-parrot.com/~pdw/iftop/

Source: http://www.ex-parrot.com/~pdw/iftop/download/iftop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap, ncurses-devel
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
iftop does for network usage what top(1) does for CPU usage. It listens
to network traffic on a named interface and displays a table of current
bandwidth usage by pairs of hosts. Handy for answering the question
"why is our ADSL link so slow?".

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 iftop %{buildroot}%{_sbindir}/iftop
%{__install} -Dp -m0644 iftop.8 %{buildroot}%{_mandir}/man8/iftop.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man8/iftop.8*
%{_sbindir}/iftop

%changelog
* Mon Jun 26 2006 Dag Wieers <dag@wieers.com> - 0.17-1
- Updated to release 0.17.

* Sun Feb 29 2004 Dag Wieers <dag@wieers.com> - 0.16-0
- Initial package. (using DAR)
