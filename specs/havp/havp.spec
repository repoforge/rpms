# $Id$
# Authority: dag

# Tag: rft

Summary: HTTP anti-virus proxy filter
Name: havp
Version: 0.90
Release: 1%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.server-side.de/

Source: http://www.server-side.de/download/havp-%{version}.tar.gz
Patch0: havp-init.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: httpd-devel, bzip2-devel, gmp-devel, curl-devel, clamav-devel, openssl-devel
BuildRequires: bzip2-devel, gmp-devel, curl-devel, clamav-devel, openssl-devel

%description
HAVP (HTTP AntiVirus proxy) is a proxy with an anti-virus filter.
It does not cache or filter content. At the moment the complete
traffic is scanned. The reason for this is the chance of malicious
code in nearly every filetype e.g. HTML (JavaScript) or Jpeg.

I aim to stop especially dialer or browser exploits. But writing
a http Anti Virus Proxy is a real dilemma! Huge downloads are
a problem for virus scanning proxies. A Client should not receive
data which is unchecked by the virus scanner, but big downloads
should not timeout.

%prep
%setup
%patch0 -p0 -b .init

%{__perl} -pi.orig \
	-e 's|^# (TEMPLATEPATH) .+$|$1 /etc/havp/templates/en|;' \
	-e 's|^# (WHITELIST) .+$|$1 /etc/havp/whitelist|;' \
	-e 's|^# (BLACKLIST) .+$|$1 /etc/havp/blacklist|;' \
	etc/havp/havp.config

%build
%configure \
	--enable-ssl-tunnel

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 havp/havp %{buildroot}%{_sbindir}/havp
%{__install} -Dp -m0755 etc/init.d/havp %{buildroot}%{_initrddir}/havp

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/havp/
%{__cp} -r etc/havp/*  %{buildroot}%{_sysconfdir}/havp/

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/havp/
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/run/havp/

%clean
%{__rm} -rf %{buildroot}

%pre
if ! /usr/bin/id havp &>/dev/null; then
	/usr/sbin/useradd -r -d %{_localstatedir}/log/havp -s /bin/sh -c "havp" havp || \
		%logmsg "Unexpected error adding user \"havp\". Aborting installation."
fi

%post
/sbin/chkconfig --add havp

%preun
if [ $1 -eq 0 ]; then
	/sbin/service havp stop &>/dev/null || :
	/sbin/chkconfig --del havp
fi

%postun
if [ $1 -eq 0 ]; then
	/usr/sbin/userdel havp || %logmsg "User \"havp\" could not be deleted."
fi

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL update-conf 
%config(noreplace) %{_sysconfdir}/havp/
%config %{_initrddir}/havp
%{_sbindir}/havp

%defattr(-, havp, havp, 0755)
%{_localstatedir}/log/havp/
%{_localstatedir}/run/havp/

%changelog
* Tue Apr  7 2009 Dries Verachtert <dries@ulyssis.org> - 0.90-1
- Updated to release 0.90.

* Wed Aug 13 2008 Dries Verachtert <dries@ulyssis.org> - 0.89-1
- Updated to release 0.89.

* Sun Apr 20 2008 Dries Verachtert <dries@ulyssis.org> - 0.88-1
- Updated to release 0.88.

* Mon Jul 23 2007 Dries Verachtert <dries@ulyssis.org> - 0.86-1
- Updated to release 0.86.

* Tue Aug 22 2006 Dag Wieers <dag@wieers.com> - 0.7.9-1
- Cosmetic changes.

* Wed May 31 2006 Bernard 'Tux' Lheureux <tux at portalinux dot org> 0.7.9-2
- Corrected the specfile to make it installable on CentOS 4.x
- Created and applied some patches to make it chkconfig compatible
- Created and applied a patch to make config reflect the correct location of the files

* Tue May 30 2006 Jim Perrin <jperrin at gmail dot com> 0.7.9-1
- Initial build for CentOS, 
- Specfile generation... still some work to do...
