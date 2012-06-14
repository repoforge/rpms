# $Id$
# Authority: dries
# Upstream: http://groups.yahoo.com/group/milter-greylist/

%define user smmsp

Summary: Stand-alone milter written in C that implements greylist filtering
Name: milter-greylist
Version: 4.2.7
Release: 2%{?dist}
License: BSD
Group: System Environment/Daemons
URL: http://hcpnet.free.fr/milter-greylist/

Source: ftp://ftp.espci.fr/pub/milter-greylist/milter-greylist-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: sendmail-devel >= 8.11
BuildRequires: bison

%description
milter-greylist is a stand-alone milter written in C that implements the 
greylist filtering method, as proposed by Evan Harris. 

Grey listing works by assuming that, unlike legitimate MTA, spam engines 
will not retry sending their junk mail on a temporary error. The filter 
will always reject mail temporarily on a first attempt, then accept it 
after some time has elapsed.

If spammers ever try to resend rejected messages, we can assume they will 
not stay idle between the two sends (if they do, the spam problem would 
just be solved). Odds are good that the spammer will send a mail to a honey 
pot address and get blacklisted in several real-time distributed black lists 
before the second attempt.

%prep
%setup

%build
%configure \
  --with-user=%{user} \
  --enable-dnsrbl
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install USER=$USER DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 milter-greylist.m4 %{buildroot}%{_datadir}/sendmail-cf/feature/milter-greylist.m4
%{__install} -Dp -m0755 rc-redhat.sh %{buildroot}%{_initrddir}/milter-greylist

%post
/sbin/chkconfig --add milter-greylist

%preun
if [ $1 -eq 0 ]; then
	/sbin/service milter-greylist stop &>/dev/null || :
	/sbin/chkconfig --del milter-greylist
fi

%postun
/sbin/service milter-greylist condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man5/greylist.conf.5*
%doc %{_mandir}/man8/milter-greylist.8*
%config(noreplace) %{_sysconfdir}/mail/greylist.conf
%config %{_initrddir}/milter-greylist
%{_bindir}/milter-greylist
%dir %{_datadir}/sendmail-cf/
%dir %{_datadir}/sendmail-cf/feature/
%{_datadir}/sendmail-cf/feature/milter-greylist.m4

%defattr(-, %{user}, %{user}, 0755)
%dir %{_localstatedir}/milter-greylist/

%changelog
* Thu Jun 14 2012 David Hrbáč <david@hrbac.cz> - 4.2.7-2
- enable dnsrbl

* Sat May 5 2012 2012 Kouhei Sutou <kou@clear-code.com> - 4.2.7-1
- Upgrade to 4.2.7.

* Tue Sep 25 2007 Dag Wieers <dag@wieers.com> - 3.0-2
- Change ownership of /var/milter-greylist/ to smmsp:smmsp. (Michael Mansour)

* Mon Sep 24 2007 Dries Verachtert <dries@ulyssis.org> - 3.0-1
- Initial package, based on the spec file made by Ivan F. Martinez.
