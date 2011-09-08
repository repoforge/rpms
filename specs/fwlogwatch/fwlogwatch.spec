# $Id$
# Authority: dag
# Upstream: Boris Wesslowski <boris$wesslowski,com>

%{?el6:%define _without_initlog 1}
%{?el6:%define _with_flex 1}

Summary: Firewall log analyzer, report generator and realtime response agent
Name: fwlogwatch
Version: 1.2
Release: 1%{?dist}
License: GPLv2+
Group: Applications/System
URL: http://fwlogwatch.inside-security.de/

Source0: http://fwlogwatch.inside-security.de/sw/%{name}-%{version}.tar.bz2
Patch0: fwlogwatch-1.2-initlog.patch
Patch1: fwlogwatch-1.2-flex.patch
Patch2: fwlogwatch-1.2-nostrip.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{?_with_flex:BuildRequires: flex}
BuildRequires: gettext
BuildRequires: zlib-devel

%description
fwlogwatch produces Linux ipchains, Linux netfilter/iptables,
Solaris/BSD/Irix/HP-UX ipfilter, Cisco IOS, Cisco PIX/ASA, NetScreen, Elsa
Lancom router and Snort IDS log summary reports in plain text and HTML form
and has a lot of options to analyze and display relevant patterns. It also
can run as daemon (with web interface) doing realtime log monitoring and
reporting anomalies or starting attack countermeasures.

%prep
%setup

%{?_without_initlog:%patch0 -p1}
%{!?_with_flex:%patch1 -p1}

%patch2 -p1

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e '
    s|/usr/local/sbin|\%{_sbindir}|g;
    s|/usr/local|%{_prefix}|g;
    ' fwlogwatch.config main.h contrib/*

%build
%{__make} %{?_smp_mflags} \
    CFLAGS=" %{optflags} -DHAVE_ZLIB -DHAVE_GETTEXT -DHAVE_IPV6 " \
    LDFLAGS=" -g "
    CONF_DIR="%{_sysconfdir}" \
    INSTALL_DIR="%{_prefix}" \
    LOCALE_DIR="%{_prefix}" \

%install
%{__rm} -rf %{buildroot}

### FIXME: Create directories as Makefile doesn't take care of this.
%{__install} -d -m0755 \
    %{buildroot}%{_sbindir} \
    %{buildroot}%{_initrddir} \
    %{buildroot}%{_mandir}/man8/ \
    %{buildroot}%{_datadir}/locale/{de,ja,pt,sv,zh_CN,zh_TW}/LC_MESSAGES

%makeinstall install-config install-i18n install-rhinit \
    CONF_DIR="%{buildroot}%{_sysconfdir}" \
    INSTALL_DIR="%{buildroot}%{_prefix}" \
    LOCALE_DIR="%{buildroot}%{_prefix}" \

%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS README
%doc contrib/fwlogsummary.cgi contrib/fwlogsummary_small.cgi
%doc contrib/fwlogwatch.php
%doc contrib/pix-names.sh
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/fwlogwatch.config
%{_initrddir}/fwlogwatch
%{_sbindir}/fwl*

%changelog
* Thu Sep 08 2011 Yury V. Zaytsev <yury@shurup.com> - 1.2-1
- Enabled zlib, gettext and ipv6 support for good.
- Disabled initlog on RHEL6 (Helmut Drodofsky).
- Updated to release 1.2.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.1-1
- Updated to release 1.1.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1.2
- Rebuild for Fedora Core 5.

* Mon Apr 26 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Added missing zlib-devel dependency. (Herbert Straub)
- Updated to release 1.0.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 0.9.3-2
- Cosmetic rebuild for Group-tag.

* Mon Mar 15 2004 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Initial package. (using DAR)
