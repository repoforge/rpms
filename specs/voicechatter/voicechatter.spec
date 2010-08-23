# $Id$
# Authority: shuff
# Upstream: Chris Weiland <cweiland$voicechatter,org>

%define real_name VoiceChatter

Summary: VoiceChatter (cross-platform voice communication) client
Name: voicechatter
Version: 1.4.2
Release: 3%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.voicechatter.org/

Source: http://voicechatter.net/files/source/VoiceChatter-src-%{version}.tar.gz
Patch0: voicechatter-1.4.2_libsndfile-flac.patch
Patch1: voicechatter-1.4.2_init-script.patch
Patch2: voicechatter-1.4.2_VCServerManager.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: atk-devel
BuildRequires: arts-devel
BuildRequires: binutils 
BuildRequires: cairo-devel
BuildRequires: freetype-devel
BuildRequires: gcc 
BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: glibc-devel >= 2.0.0
BuildRequires: gtk2-devel
BuildRequires: libgnomecanvas-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libstdc++-devel
BuildRequires: libxml2-devel
BuildRequires: make
BuildRequires: pango-devel
BuildRequires: pkgconfig >= 0.9.0
BuildRequires: sqlite-devel >= 3
BuildRequires: zlib-devel >= 1.1.4

%description
VoiceChatter is a free, cross-platform voice communication (chat) application.
It was designed with gaming in mind, but can be used for many other purposes.

This package includes the VoiceChatter client.

%package server
Summary: VoiceChatter (cross-platform voice communication) server
Group: System Environment/Daemons

Requires: initscripts

%description server
This package includes the VoiceChatter server.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CFLAGS="%{optflags}" %configure
%{__make} %{?_smp_mflags} all

# build the server manager
cd VCServerManager
%{__make} %{?_smp_mflags}
cd ..

%install
%{__rm} -rf %{buildroot}
# install the client
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 VChat/voicechatter %{buildroot}/%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_datadir}/voicechatter/
%{__cp} -r VChat/data %{buildroot}%{_datadir}/voicechatter/
%{__chmod} -R 0755 %{buildroot}%{_datadir}/voicechatter/
# install the server
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__install} -m0755 VChatServer/voicechatterserver %{buildroot}/%{_sbindir}
%{__install} -m0755 VCServerManager/VCServerManager %{buildroot}/%{_sbindir}
%{__install} -d -m0755 %{buildroot}%{_initrddir}
%{__install} -m0755 VCServerManager/vcsm %{buildroot}/%{_initrddir}
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/voicechatterserver

%clean
%{__rm} -rf %{buildroot}

%post server
/sbin/chkconfig --add vcsm

%preun server
/sbin/chkconfig --del vcsm

%files
%defattr(-, root, root, 0755)
%doc ChangeLog.txt 
%{_bindir}/voicechatter
%{_datadir}/voicechatter/

%files server
%defattr(-, root, root, 0755)
%doc WebInterface/
%{_sbindir}/voicechatterserver
%{_sbindir}/VCServerManager
%{_initrddir}/vcsm
%{_sysconfdir}/voicechatterserver

%changelog
* Mon Aug 23 2010 Steve Huff <shuff@vecna.org> - 1.4.2-3
- D'oh, the chkconfig scripts were for the server package, not the client.

* Thu Aug 19 2010 Steve Huff <shuff@vecna.org> - 1.4.2-2
- Init script and VCServerManager patches from Steven Haigh.

* Fri Jul 9 2010 Steve Huff <shuff@vecna.org> - 1.4.2-1
- Initial package.
