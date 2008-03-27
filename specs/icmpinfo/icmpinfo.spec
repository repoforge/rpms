# $Id$
# Authority: dag
# Upstream: Laurent Demailly <dl@hplyot.obspm.fr>

Summary: Tool for looking at the ICMP messages
Name: icmpinfo
Version: 1.11
Release: 1.2
License: BSD
Group: Applications/Internet
URL: http://www.demailly.com/~dl/softs.html

Source: ftp://ftp.demailly.com/pub/icmpinfo-%{version}.tar.gz
Patch: icmpinfo-1.11-libc6.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A tool for looking at the icmp messages received on
the running host.

%prep
%setup
%patch -p1

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags} -pipe -D_BSD_SOURCE -Dlinux"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 icmpinfo %{buildroot}%{_sbindir}/icmpinfo
%{__install} -Dp -m0644 icmpinfo.man %{buildroot}%{_mandir}/man1/icmpinfo.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES DOC LICENSE NocTools.Infos README TODO
%doc %{_mandir}/man1/icmpinfo.1*
%{_sbindir}/icmpinfo

%changelog
* Sun May 08 2005 Dag Wieers <dag@wieers.com> - 1.11-1
- Initial package. (using DAR)
