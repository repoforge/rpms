# $Id$
# Authority: dag
# Upstream: jose nazario <jose$monkey,org>

Summary: Basic IDS/IPS tool to help you investigate and manage your network
Name: flowgrep
Version: 0.8
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.monkey.org/~jose/software/flowgrep/

Source: http://www.monkey.org/~jose/software/flowgrep/flowgrep-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.2, python-nids
Requires: python >= 2.2, python-nids

%description
flowgrep is a basic IDS/IPS tool written in python as a way to help you
investigate and manage your network. It works by sniffing traffic,
reassembling TCP streams, and IP and UDP fragments into single packets,
and allowing you to "grep" through their payloads using regular expressions.
The quality of the regular expression engine is similar to Perl's. Think of
it as a marriage of tcpflow, tcpkill, and ngrep.

%prep
%setup

%build
python setup.py build

%install
%{__rm} -rf %{buildroot}
#python setup.py install \
#	--prefix="%{_prefix}" \
#	--root="%{buildroot}"
%{__install} -Dp -m0755 flowgrep.py %{buildroot}%{_sbindir}/flowgrep
%{__install} -Dp -m0644 flowgrep.8 %{buildroot}%{_mandir}/man8/flowgrep.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man8/flowgrep.8*
%{_sbindir}/flowgrep

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8-1.2
- Rebuild for Fedora Core 5.

* Fri Feb 11 2005 Dag Wieers <dag@wieers.com> - 0.8-1
- Initial package. (using DAR)
