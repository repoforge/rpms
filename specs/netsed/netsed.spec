# $Id$
# Authority: dag
# Upstream: Michal Zalewski <lcamtuf$ids,pl>

Summary: Realtime packet payload mangling
Name: netsed
Version: 0.0.1
Release: 0.b
License: GPL
Group: Applications/Internet
URL: http://freshmeat.net/projects/netsed/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dione.ids.pl/~lcamtuf/netsed.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
netsed brings sed functionality to the network layer, allowing you to
change the contents of packets travelling through your gateway on the
fly, in a completely transparent manner. It features basic expressions
and dynamic filtering, and cooperates with ipfwadm/ipchains transparent
proxy rules to pick specific packets.

%prep
%setup -n %{name}

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 netsed %{buildroot}%{_bindir}/netsed

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%{_bindir}/*

%changelog
* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 0.0.1-0.b
- Initial package. (using DAR)
