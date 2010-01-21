# $Id$
# Authority: dries
# Upstream: EFF

# added so it also works with the upstream el4 tor package
%define toruser _tor
%define torgroup _tor

Summary: Send network traffic through virtual tunnels to improve your privacy
Name: tor
Version: 0.2.1.22
Release: 1%{?dist}
License: BSD
Group: Applications/Internet
URL: http://tor.eff.org/

Source: http://tor.eff.org/dist/tor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libevent-devel, zlib-devel, automake, autoconf, openssl-devel

%description
Tor is a network of virtual tunnels that allows people and groups to improve
their privacy and security on the Internet. It also enables software
developers to create new communication tools with built-in privacy features.
It provides the foundation for a range of applications that allow
organizations and individuals to share information over public networks
without compromising their privacy. Individuals can use it to keep remote
Websites from tracking them and their family members. They can also use it
to connect to resources such as news sites or instant messaging services
that are blocked by their local Internet service providers (ISPs).

%prep
%setup

%build
#export CPPFLAGS="-I/usr/include/kerberos"
export CPPFLAGS="-I/usr/kerberos/include"
%configure --with-tor-user="%{toruser}" --with-tor-group="%{torgroup}"
%{__make} %{?_smp_mflags}
%{__perl} -pi -e "s|# chkconfig: 2345|# chkconfig: -|g;" contrib/tor.sh

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m755 contrib/torctl %{buildroot}%{_bindir}/torctl
%{__install} -Dp -m755 contrib/tor.sh %{buildroot}%{_initrddir}/tor
%{__install} -Dp -m644 contrib/tor.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/tor
%{__mv} -f %{buildroot}%{_sysconfdir}/tor/torrc.sample %{buildroot}%{_sysconfdir}/tor/torrc
%{__install} -d %{buildroot}%{_localstatedir}/lib/tor/
%{__install} -d %{buildroot}%{_localstatedir}/log/tor/
%{__install} -d %{buildroot}%{_localstatedir}/run/tor/

%clean
%{__rm} -rf %{buildroot}

%pre
/usr/sbin/groupadd %{torgroup} 2> /dev/null || :
/usr/sbin/useradd -c "Tor user" -g %{torgroup} -s /bin/false -r -d %{_localstatedir}/lib/tor %{toruser} 2>/dev/null || :

%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add tor
fi
%{__chown} -R %{toruser}.%{torgroup} %{_localstatedir}/lib/tor %{_localstatedir}/run/tor %{_localstatedir}/log/tor || :

%preun
if [ $1 -eq 0 ]; then
   /sbin/service tor stop || :
   /sbin/chkconfig --del tor
fi

%postun
/sbin/service tor condrestart &>/dev/null || :

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog INSTALL LICENSE README
%doc %{_mandir}/man1/tor*
%config %{_initrddir}/tor
%config(noreplace) %{_sysconfdir}/logrotate.d/tor
%{_bindir}/tor-resolve
%{_bindir}/tor
%{_bindir}/torctl
%{_bindir}/torify
%{_bindir}/tor-gencert
%dir %{_datadir}/tor/
%{_datadir}/tor/geoip

%defattr(-, root, %{torgroup}, 0750)
%dir %{_sysconfdir}/tor/

%defattr(-, root, %{torgroup}, 0640)
%config(noreplace) %{_sysconfdir}/tor/tor-tsocks.conf
%config(noreplace) %{_sysconfdir}/tor/torrc

%defattr(-, %{toruser}, %{torgroup}, 0700)
%dir %{_localstatedir}/lib/tor

%defattr(-, %{toruser}, %{torgroup}, 0750)
%dir %{_localstatedir}/run/tor
%dir %{_localstatedir}/log/tor

%changelog
* Thu Jan 21 2010 Steve Huff <shuff@vecna.org> - 0.2.1.22-1
- Updated to release 0.2.1.22.

* Mon Jan 04 2010 Steve Huff <shuff@vecna.org> - 0.2.1.21-1
- Updated to release 0.2.1.21.

* Thu Nov 12 2009 Steve Huff <shuff@vecna.org> - 0.2.1.20-1
- Updated to release 0.2.1.20.

* Mon Aug 31 2009 Dries Verachtert <dries@ulyssis.org> - 0.2.1.19-1
- Updated to release 0.2.1.19.

* Sun Jul 12 2009 Dries Verachtert <dries@ulyssis.org> - 0.2.0.35-1
- Updated to release 0.2.0.35.

* Sat Feb 21 2009 Tom G. Christensen <swpkg@jupiterrise.com> - 0.2.0.34-1
- Updated to release 0.2.0.34.

* Tue Dec 11 2008 Dries Verachtert <dries@ulyssis.org> - 0.2.0.32-1
- Updated to release 0.2.0.32.

* Tue Sep  9 2008 Dries Verachtert <dries@ulyssis.org> - 0.2.0.31-1
- Updated to release 0.2.0.31.

* Mon Sep  1 2008 Dries Verachtert <dries@ulyssis.org> - 0.2.0.30-1
- Updated to release 0.2.0.30.

* Sun Jan 20 2008 Dries Verachtert <dries@ulyssis.org> - 0.1.2.19-1
- Updated to release 0.1.2.19.

* Sun Sep  2 2007 Dries Verachtert <dries@ulyssis.org> - 0.1.2.17-1
- Updated to release 0.1.2.17.

* Fri Aug 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.1.2.16-1
- Updated to release 0.1.2.16.

* Mon Jul 23 2007 Dries Verachtert <dries@ulyssis.org> - 0.1.2.15-1
- Updated to release 0.1.2.15.

* Sun May 27 2007 Dag Wieers <dag@wieers.com> - 0.1.2.14-1
- Updated to release 0.1.2.14.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 0.1.2.13-1
- Updated to release 0.1.2.13.

* Sun Mar 25 2007 Dag Wieers <dag@wieers.com> - 0.1.1.26-4
- Rebuild against libevent-1.1a on EL5.

* Wed Mar 07 2007 Dag Wieers <dag@wieers.com> - 0.1.1.26-3
- Rebuild against libevent-1.3b.

* Tue Feb 20 2007 Dag Wieers <dag@wieers.com> - 0.1.1.26-2
- Rebuild against libevent-1.3a.

* Mon Dec 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.1.26-1
- Updated to release 0.1.1.26.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.1.25-1
- Updated to release 0.1.1.25.

* Mon Aug 07 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.1.23-1
- Updated to release 0.1.1.23.

* Sun Jun 04 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.1.20-1
- Updated to release 0.1.1.20.
- Use a _tor user and _tor group.

* Wed Jan 04 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.0.16-1
- Update to release 0.1.0.16.

* Sun Aug 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.0.14-1
- Update to release 0.1.0.14.

* Sat Aug 06 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.0.13-1
- Update to release 0.1.0.13.

* Sat Jul 23 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.0.12-1
- Initial package.
