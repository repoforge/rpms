# $Id$
# Authority: dag
# Upstream: Duane Wessels

Summary: Captures and displays DNS messages on your network
Name: dnsdump
Version: 1.4
Release: 1
License: BSD
Group: Applications/Internet
URL: http://dns.measurement-factory.com/tools/dnsdump/

Source0: http://dns.measurement-factory.com/tools/dnsdump/src/dnsdump-%{version}
Source1: http://dns.measurement-factory.com/tools/dnsdump/index.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
Requires: perl

%description
dnsdump is a tool that captures and displays DNS messages on your network.
Think of dnsdump as an alternative to running tcpdump port domain. You can
control dnsdump's output using a printf-like format string.

%prep
%{__cp} -av %{SOURCE1} README.html

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 %{SOURCE0} %{buildroot}%{_sbindir}/dnsdump

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.html
%{_sbindir}/dnsdump

%changelog
* Sun Mar 16 2008 Dag Wieers <dag@wieers.com> - 1.4-1
- Initial package. (using DAR)
