# $Id$
# Authority: dag
# Upstream: Daniel Barron <author$dansguardian,org>

%define real_name DansGuardian

Summary: Content filtering web proxy
Name: dansguardian
Version: 2.10.1.1
Release: 1%{?dist}
License: GPLv2+
Group: System Environment/Daemons
URL: http://www.dansguardian.org/

Source0: http://dansguardian.org/downloads/2/Stable/%{name}-%{version}.tar.gz
Source1: dansguardian.init
Source2: dansguardian.httpd
Source3: dansguardian.logrotate

# Fixes some compilation errors with gcc 4.4
Patch1: dansguardian-gcc44.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: pcre-devel
BuildRequires: zlib-devel
BuildRequires: pkgconfig
BuildRequires: which

Requires(pre):   shadow-utils
Requires(post):  chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts

%description
DansGuardian is a web filtering engine that checks the content within
the page itself in addition to the more traditional URL filtering.

DansGuardian is a content filtering proxy. It filters using multiple methods,
including URL and domain filtering, content phrase filtering, PICS filtering,
MIME filtering, file extension filtering, POST filtering.

%prep
%setup
%patch1 -p1

%build

%configure \
   --disable-clamav \
   --disable-clamd \
   --enable-icap \
   --enable-kavd \
   --enable-commandline \
   --enable-trickledm \
   --enable-ntlm \
   --enable-email \
   --with-proxyuser=dansguardian \
   --with-proxygroup=dansguardian

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%{__make} install DESTDIR=%{buildroot}

install -Dpm 644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}

# delete the other scripts since they are of no use for Fedora users
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts
chmod 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.pl

# install init script and httpd config
install -Dpm 755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/%{name}
install -Dp -m0644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/%{name}.conf

# we'll install this later within %doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

# create the log dir
install -dm 755 $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}

%clean
%{__rm} -rf %{buildroot}

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
useradd -r -g %{name} -d %{_datadir}/%{name} -s /sbin/nologin \
   -c "DansGuardian web content filter" %{name}
exit 0

%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add %{name}
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service %{name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi

%postun
if [ $1 -ge 1 ] ; then
    /sbin/service %{name} condrestart >/dev/null 2>&1 || :
fi

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL README UPGRADING
%doc doc/AuthPlugins doc/ContentScanners doc/DownloadManagers doc/FAQ
%doc doc/FAQ.html doc/Plugins
%doc %{_mandir}/man8/%{name}.8.gz
%{_sbindir}/%{name}
%attr(-,%{name},%{name}) %{_datadir}/%{name}
%{_initrddir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}*.conf
%dir %{_sysconfdir}/%{name}/authplugins
%config(noreplace) %{_sysconfdir}/%{name}/authplugins/*
%dir %{_sysconfdir}/%{name}/contentscanners
%config(noreplace) %{_sysconfdir}/%{name}/contentscanners/*
%dir %{_sysconfdir}/%{name}/downloadmanagers
%config(noreplace) %{_sysconfdir}/%{name}/downloadmanagers/*
%dir %{_sysconfdir}/%{name}/lists
%config(noreplace) %{_sysconfdir}/%{name}/lists/*
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf

%defattr(644, %{name}, %{name}, 755)
%dir %{_localstatedir}/log/%{name}

%changelog
* Thu Jul 14 2011 Yury V. Zaytsev <yury@shurup.com> - 2.10.1.1-1
- Synced the SPEC with Fedora Rawhide where appropriate.
- Updated to release 2.10.1.1.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.8.0.6-1.2
- Rebuild for Fedora Core 5.

* Mon Aug 15 2005 Dries Verachtert <dries@ulyssis.org> - 2.8.0.6-1
- Updated to release 2.8.0.6.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 2.8.0.4-1
- Updated to release 2.8.0.4.

* Fri Jul 30 2004 Dag Wieers <dag@wieers.com> - 2.8.0.2-1
- Updated to release 2.8.0.2.

* Wed Jul 21 2004 Dag Wieers <dag@wieers.com> - 2.8.0-1
- Updated to release 2.8.0-0.

* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 2.6.1.13-1
- Updated to release 2.6.1-13.

* Fri Mar 26 2004 Dag Wieers <dag@wieers.com> - 2.6.1.12-1
- Initial package. (using DAR)
