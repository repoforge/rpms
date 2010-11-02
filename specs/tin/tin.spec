# $Id$
# Authority: shuff
# Upstream: Urs Janssen <urs$tin,org>

%define minor_release 1.9

Summary: Threaded NNTP and spool based newsreader
Name: tin
Version: %{minor_release}.5
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.tin.org/

Source: ftp://ftp.tin.org/pub/news/clients/tin/v%{minor_release}/tin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: aspell-devel
BuildRequires: binutils
BuildRequires: bison
BuildRequires: coreutils
BuildRequires: cyrus-sasl-devel
BuildRequires: dante-devel
BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: glibc-devel >= 2.1
BuildRequires: gpg
BuildRequires: inews
BuildRequires: libXaw-devel
BuildRequires: mailx
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: pcre-devel >= 2.08
BuildRequires: rpm-macros-rpmforge
BuildRequires: Xaw3d
Requires: aspell
Requires: coreutils
Requires: dante
Requires: gpg
Requires: inews
Requires: mailx

%description
tin is a full-screen easy to use Usenet newsreader. It  can  read  news locally
(e.g., /var/spool/news) or remotely (rtin or tin -r option) via a NNTP (Network
News Transport Protocol) server.

%prep
%setup

%build
%configure \
    --disable-dependency-tracking \
    --sysconfdir=%{_sysconfdir}/tin \
    --enable-break-long-lines \
    --enable-broken-listgroup-fix \
    --enable-cancel-locks \
    --enable-ipv6 \
    --enable-nntp \
    --enable-prototypes \
    --with-coffee \
    --with-pcre \
    --with-screen=ncursesw \
    --with-socks \
    --with-socks5 \
    --with-x \
    --with-Xaw3d \
    --without-pgp \
    --without-pgpk

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__make} install_sysdefs DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README* doc/ABOUT-NLS doc/CHANGES* doc/CREDITS doc/DEBUG_REFS
%doc doc/INSTALL doc/TODO doc/WHATSNEW doc/*.txt doc/*.sample 
%doc doc/config-anomalies doc/mime.types doc/nov_tests tools/
%doc %{_mandir}/man?/*
%{_bindir}/*
%dir %attr(755,root,root) %{_sysconfdir}/tin/
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/tin/*

%changelog
* Tue Nov 02 2010 Steve Huff <shuff@vecna.org> - 1.9.5-1
- Initial package.
