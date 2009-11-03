# $Id$
# Authority: dag
# Upstream: Enrico Scholz <enrico,scholz$informatik,tu-chemnitz,de>

Summary: tool to prevent unauthorized usage of IPs
Name: ip-sentinel
Version: 0.12
Release: 1%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.nongnu.org/ip-sentinel/

Source: http://download.savannah.gnu.org/releases/ip-sentinel/ip-sentinel-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: dietlibc

Requires(pre): /usr/sbin/useradd /usr/sbin/groupadd
Requires(postun): /usr/sbin/userdel /usr/sbin/groupdel

%description
IP Sentinel is a tool that tries to prevent unauthorized usage of
IP addresses within an ethernet broadcast domain by answering ARP
requests. After receiving faked replies, requesting parties store
the MAC in their ARP tables and will send future packets to this
invalid MAC, rendering the IP unreachable.

%prep
%setup

%build
%configure \
	--enable-release \
	--with-username="ip-sentinel" \
	--disable-dietlibc
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m755 contrib/ip-sentinel.init %{buildroot}%{_initrddir}/ip-sentinel
%{__install} -Dp -m644 contrib/ip-sentinel.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/ip-sentinel

%{__install} -d -m0750 %{buildroot}%{_var}/lib/ip-sentinel/

%pre
/usr/sbin/groupadd -r ip-sentinel &>/dev/null || :
/usr/sbin/useradd -r -s /sbin/nologin -M -d %{_var}/lib/ip-sentinel
	 	  -c 'IP sentinel user' -g ip-sentinel ip-sentinel &>/dev/null || :

%post
/sbin/chkconfig --add ip-sentinel

%preun
if [ $1 -eq 0 ]; then
	service ip-sentinel stop &>/dev/null || :
	/sbin/chkconfig --del ip-sentinel
fi

%postun
if [ $1 -eq 0 ]; then
	/usr/sbin/userdel ip-sentinel &>/dev/null || :
	/usr/sbin/groupdel ip-sentinel &>/dev/null || :
if
service ip-sentinel condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS
%doc %{_mandir}/man8/ip-sentinel
%config(noreplace) %{_sysconfdir}/sysconfig/ip-sentinel
%config %{_initrddir}/ip-sentinel
%{_sbindir}/ip-sentinel
%defattr(-, root, ip-sentinel, 0750)
%{_var}/lib/ip-sentinel/

%changelog
* Wed Apr 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.11-1.2
- Rebuild for Fedora Core 5.

* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Sat Jun 19 2004 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Wed Dec 17 2003 Dag Wieers <dag@wieers.com> - 0.9-0
- Updated to release 0.9.

* Thu Sep 11 2003 Dag Wieers <dag@wieers.com> - 0.7-0
- Initial package. (using DAR)
