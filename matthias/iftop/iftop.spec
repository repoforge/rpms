# Authority: dag
# Upstream: Paul Warren <pdw@ex-parrot.com>, Chris Lightfoot <chris@ex-parrot.com>

Summary: Display bandwidth usage on an interface.
Name: iftop
Version: 0.16
Release: 0
License: GPL
Group: Applications/System
URL: http://www.ex-parrot.com/~pdw/iftop/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.ex-parrot.com/~pdw/iftop/download/iftop-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}%{version}
Prefix: %{_prefix}

BuildRequires: libpcap

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
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_mandir}/man8
%{__install} -m0755 iftop %{buildroot}%{_sbindir}
%{__install} -m0644 iftop.8 %{buildroot}%{_mandir}/man8/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Sun Feb 29 2004 Dag Wieers <dag@wieers.com> - 0.16-0
- Initial package. (using DAR)
