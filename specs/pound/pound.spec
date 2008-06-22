# $Id$
# Authority: dries
# Upstream: <roseg$apsis,ch>

Summary: Reverse HTTP proxy, load balancer and SSL wrapper
Name: pound
Version: 2.4.3
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.apsis.ch/pound/index.html

Source: http://www.apsis.ch/pound/Pound-%{version}.tgz
Source1: pound.init
Source2: pound.cfg
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel, pkgconfig

%description
Pound is a reverse HTTP proxy, load balancer, and SSL wrapper. It proxies 
client HTTPS requests to HTTP backend servers, distributes the requests 
among several servers while keeping sessions, supports HTTP/1.1 requests 
even if the backend server(s) are HTTP/1.0, and sanitizes requests.

%prep
%setup -n Pound-%{version}
%{__perl} -pi -e '
        s|-o \@I_OWNER\@ -g \@I_GRP\@||g;
        s| -s | |g;
    ' Makefile*

%build
### Add correct CFLAGS for EL3 and RH9
%{expand: %%define optflags %{optflags} %(pkg-config --cflags openssl)}
%configure \
    --disable-super
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_sbindir} %{buildroot}%{_mandir}  %{buildroot}%{_sysconfdir}/init.d
%{__make} install DESTDIR=%{buildroot}
%{__install} %{_sourcedir}/pound.init %{buildroot}%{_sysconfdir}/init.d/pound
%{__install} %{_sourcedir}/pound.cfg %{buildroot}%{_sysconfdir}/pound.cfg

%post
/sbin/chkconfig --add pound

%preun
if [ $1 -eq 0 ]; then
	/sbin/service pound stop >/dev/null 2>&1
	/sbin/chkconfig --del pound
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG FAQ GPL.txt README
%doc %{_mandir}/man8/pound.8*
%doc %{_mandir}/man8/poundctl.8*
%{_sbindir}/pound
%{_sbindir}/poundctl
%{_sysconfdir}/init.d/pound
%config %{_sysconfdir}/pound.cfg

%changelog
* Fri Jun 20 2008 Thomas M Steenholdt <tmus@tmus.dk> - 2.4.3-1
- Updated to release 2.4.3
- Added initscript and default pound.cfg (intentionally non-working as provided)

* Thu Apr 17 2008 Dag Wieers <dag@wieers.com> - 2.4.1-1
- Updated to release 2.4.1.

* Mon Feb 11 2008 Dag Wieers <dag@wieers.com> - 2.4-1
- Updated to release 2.4.

* Mon Apr 16 2007 Dries Verachtert <dries@ulyssis.org> - 2.3-1
- Updated to release 2.3.

* Mon Dec 18 2006 Dries Verachtert <dries@ulyssis.org> - 2.2-1
- Updated to release 2.2.

* Mon Aug 07 2006 Dries Verachtert <dries@ulyssis.org> - 2.1-1
- Updated to release 2.1.

* Wed Apr 19 2006 Dries Verachtert <dries@ulyssis.org> - 2.0-1
- Initial package.
