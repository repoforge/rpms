# $Id$
# Authority: dries
# Upstream: Hogan Robert <hoganrobert$klamav,sf,net>

Summary: Tor controller
Name: tork
Version: 0.26
Release: 1
License: GPL
Group: Applications/Utilities
URL: http://tork.sf.net

Source: http://dl.sf.net/tork/tork-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, kdelibs-devel, gettext

%description
TorK is a Tor Controller for KDE. It allows you to configure, run, and update 
Tor. It also allows you to view the Tor network and choose how you would like 
to interact with the it.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/tork*.1*
%doc %{_mandir}/man5/torksocks.conf.5*
%doc %{_mandir}/man8/torksocks.8*
%doc %{_docdir}/HTML/en/tork/
%{_sysconfdir}/tork-tsocks.conf
%{_bindir}/tork
%{_bindir}/torkify
%{_bindir}/torkarkollon
%{_bindir}/torksocks
%{_libdir}/kde3/khtml_tork.*
%{_libdir}/kde3/kickermenu_tork.*
%{_libdir}/kde3/kio_torioslave.*
%dir %{_libdir}/tork
%{_libdir}/tork/libtorksocks.*
%{_datadir}/apps/khtml/kpartplugins/tork_plug_in.*
%{_datadir}/apps/kicker/menuext/torkmenu.desktop
%{_datadir}/apps/konqueror/servicemenus/tork_downloadwith*.desktop
%{_datadir}/config.kcfg/torkconfig.kcfg
%{_datadir}/apps/tork/
%{_datadir}/pixmaps/tork.xpm
%{_datadir}/menu/tork
%{_datadir}/applications/kde/tork.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/services/torioslave.protocol

%changelog
* Tue Jan  1 2008 Dries Verachtert <dries@ulyssis.org> - 0.26-1
- Initial package.
