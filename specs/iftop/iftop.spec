# $Id$
# Authority: dag
# Upstream: Paul Warren <pdw$ex-parrot,com>
# Upstream: Chris Lightfoot <chris$ex-parrot,com>

Summary: Display bandwidth usage on an interface
Name: iftop
Version: 0.16
Release: 0
License: GPL
Group: Applications/System
URL: http://www.ex-parrot.com/~pdw/iftop/

Source: http://www.ex-parrot.com/~pdw/iftop/download/iftop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap, ncurses-devel

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
%{__install} -D -m0755 iftop %{buildroot}%{_sbindir}/iftop
%{__install} -D -m0644 iftop.8 %{buildroot}%{_mandir}/man8/iftop.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man8/iftop.8*
%{_sbindir}/iftop

%changelog
* Sun Feb 29 2004 Dag Wieers <dag@wieers.com> - 0.16-0
- Initial package. (using DAR)
