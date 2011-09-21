# $Id$
# Authority: shuff
# Upstream: Max Kellermann <max$duempel,org>

Summary: MPD client which submits tracks to Last.fm
Name: mpdscribble
Version: 0.22
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://mpd.wikia.com/wiki/Client:Mpdscribble

Source: https://downloads.sourceforge.net/project/musicpd/mpdscribble/%{version}/mpdscribble-%{version}.tar.bz2
Patch0: mpdscribble-0.20_conf.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: glib2-devel >= 2.6
BuildRequires: libgcrypt-devel
BuildRequires: libmpdclient2-devel
BuildRequires: libsoup-devel
BuildRequires: make
BuildRequires: pkgconfig >= 0.9.0
BuildRequires: rpm-macros-rpmforge

%description
mpdscribble is a music player daemon client which submits information about tracks being played to Last.fm.

Features

* written in C, consumes very little memory and CPU
* full support for MPD's "idle" mode
* last.fm protocol 1.2 (including "now playing")
* supports seeking, crossfading, repeated songs 

%prep
%setup
%patch0 -p1

%build
%configure \
    --disable-dependency-tracking \
    --with-http-client=soup

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# make the cache directory
%{__mkdir_p} %{buildroot}%{_localstatedir}/cache/mpdscribble/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/*
%attr(0750, daemon, daemon) %dir %{_localstatedir}/cache/mpdscribble/
%config(noreplace) %{_sysconfdir}/mpdscribble.conf
%exclude %{_docdir}/mpdscribble/

%changelog
* Wed Sep 21 2011 Steve Huff <shuff@vecna.org> - 0.22-1
- Updated to 0.22.

* Tue Nov 09 2010 Steve Huff <shuff@vecna.org> - 0.20-1
- Initial package.
