# $Id$

# Authority: dries
# Upstream:  Dennis Opacki <dopacki$adotout,com> 

Summary: Responds to or drops ICMP echo requests packets
Name: echoart
Version: 0.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://mirror1.internap.com/echoart/

Source: http://mirror1.internap.com/echoart/echoart.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libnet, libpcap

%description
Echoart responds to or drops ICMP echo request packets based on a
pre-defined sequence, and could be used to return crude ASCII art in
response to pings from a Cisco router. It works by intercepting ICMP echo
request packets and consulting a pattern template to determine whether or
not to respond to a specific echo request. It then uses libnet to inject
responses back into the network as necessary. 

%prep
%setup -n %{name}

%build
./configure.pl Linux
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D echoart %{buildroot}%{_bindir}/echoart

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/*

%changelog
* Sun Oct 31 2004 Dries Verachtert <dries@ulyssis.org> - 0.1-1
- Initial package.

