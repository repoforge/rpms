# $Id$
# Authority: shuff
# Upstream: Max Kellermann <max$duempel,org>


Summary: Full-featured curses Music Player Daemon client
Name: ncmpc
Version: 0.19
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.musicpd.org/

Source: http://downloads.sourceforge.net/project/musicpd/ncmpc/%{version}/ncmpc-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: glib2-devel >= 2.4
# BuildRequires: liblircclient-devel
BuildRequires: libmpdclient2-devel >= 2.2
BuildRequires: ncurses-devel
BuildRequires: pkgconfig

%description
ncmpc is a fully featured MPD client, which runs in a terminal (using ncurses).
Its goal is to provide a keyboard oriented and consistent interface to MPD,
without wasting resources. 

%prep
%setup


%build
%configure \
    --disable-dependency-tracking \
    --enable-colors \
    --enable-lyrics-screen \
    --with-lyrics-plugin-dir="%{_libexecdir}/ncmpc/lyrics"
    # --enable-lirc
%{__make} %{?_smp_mflags}
%find_lang %{name}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__mkdir} ncmpc-doc
%{__mv} %{buildroot}%{_docdir}/ncmpc/* ncmpc-doc
%{__rm} -rf %{buildroot}%{_docdir}/ncmpc/*

%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc ncmpc-doc/* INSTALL
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libexecdir}/ncmpc


%changelog
* Wed Sep 21 2011 Steve Huff <shuff@vecna.org> - 0.19-1
- Initial package.
