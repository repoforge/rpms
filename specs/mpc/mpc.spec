# $Id$
# Authority: shuff
# Upstream: Max Kellermann <max$duempel,org>


Summary: Music Player Daemon client
Name: mpc
Version: 0.19
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.musicpd.org/

Source: http://downloads.sourceforge.net/project/musicpd/mpc/%{version}/mpc-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc, make, autoconf, automake
BuildRequires: glibc-devel
BuildRequires: libmpdclient2-devel
BuildRequires: pkgconfig

%description
MPC is a minimalist command line interface to MPD.

%prep
%setup


%build
%configure --disable-dependency-tracking
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__mkdir} mpc-doc
%{__mv} %{buildroot}%{_docdir}/mpc/* mpc-doc
%{__rm} -rf %{buildroot}%{_docdir}/mpc/*

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc mpc-doc/* INSTALL
%doc %{_mandir}/man?/*
%{_bindir}/*


%changelog
* Thu Mar 25 2010 Steve Huff <shuff@vecna.org> - 0.19-1
- Initial package.
