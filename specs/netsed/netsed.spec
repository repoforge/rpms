# $Id$
# Authority: dag
# Upstream: Michal Zalewski <lcamtuf$ids,pl>

Summary: Realtime packet payload mangling
Name: netsed
Version: 0.0.1
Release: 0.b.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://freshmeat.net/projects/netsed/

Source: http://dione.ids.pl/~lcamtuf/netsed.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
netsed brings sed functionality to the network layer, allowing you to
change the contents of packets travelling through your gateway on the
fly, in a completely transparent manner. It features basic expressions
and dynamic filtering, and cooperates with ipfwadm/ipchains transparent
proxy rules to pick specific packets.

%prep
%setup -c -n %{name}

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 netsed %{buildroot}%{_bindir}/netsed

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/netsed

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.1-0.b.2
- Rebuild for Fedora Core 5.

* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 0.0.1-0.b
- Initial package. (using DAR)
