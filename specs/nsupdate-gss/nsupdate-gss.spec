# $Id$
# Authority: dag
# Upstream: <jmruiz$animatika,net>

Summary: Dynamic DNS update using GSSAPI TSIG
Name: nsupdate-gss
%define real_version 20050330
Version: 0.0.20050330
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://rc.vintela.com/topics/ddns/

Source0: http://de.samba.org/samba/ftp/tsig-gss/nsupdate-gss
Source1: http://ftp.sayclub.com/pub/samba/tsig-gss/README
Patch: nsupdate-gss-ad-sites2.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: perl(Net::DNS) >= 0.44, perl-GSSAPI >= 0.21

%description
nsupdate-gss is a tool to update the DNS entry for the current host
on a Win2000 DNS server using gss-tsig.

%prep
%setup -c -T
%{__cp} -v %{SOURCE0} %{SOURCE1} .
%patch0

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 nsupdate-gss %{buildroot}%{_bindir}/nsupdate-gss

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/nsupdate-gss

%changelog
* Tue Jul 31 2007 Dag Wieers <dag@wieers.com> - 0.0.20050330-1
- Initial package. (using DAR)
