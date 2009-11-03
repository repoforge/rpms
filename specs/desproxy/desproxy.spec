# $Id$
# Authority: dag
# Upstream: Miguelanxo Otero Salgueiro <miguelanxotero$hotmail,com>

%define real_version 0.1.0-pre2

Summary: TCP tunnel for HTTP proxies
Name: desproxy
Version: 0.1.0
Release: 0.pre2.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://desproxy.sourceforge.net/

Source: http://dl.sf.net/desproxy/desproxy-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
desproxy allows you to establish TCP connections through HTTP proxies.

With desproxy you can use every application you got used to work with:
your favourite browser (MSIE, Mozilla...), your mailer (Outlook Express,
Pine, Mutt, Eudora), your news reader (Netscape News...)... without
having to worry whether they have HTTP support or not.

%prep
%setup -n %{name}-%{real_version}

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e 's|^localedir = \@prefix\@/share/locale$|datadir = \@datadir\@\nlocaledir = \$(datadir)/locale|' Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
### FIXME: Makefile doesn't create target directories (Please fix upstream)
#makeinstall
%{__install} -Dp -m0755 src/desproxy %{buildroot}%{_bindir}/desproxy
%{__install} -Dp -m0755 src/desproxy-dns %{buildroot}%{_bindir}/desproxy-dns
%{__install} -Dp -m0755 src/desproxy-inetd %{buildroot}%{_bindir}/desproxy-inetd
%{__install} -Dp -m0755 src/desproxy-socksserver %{buildroot}%{_bindir}/desproxy-socksserver
%{__install} -Dp -m0755 src/socket2socket %{buildroot}%{_bindir}/socket2socket


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Changes COPYING doc/*.html
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.0-0.pre2.2
- Rebuild for Fedora Core 5.

* Wed Sep 24 2003 Dag Wieers <dag@wieers.com> - 0.1.0-0.pre2
- Initial package. (using DAR)

