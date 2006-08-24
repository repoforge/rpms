# $Id$
# Authority: dries
# Upstream: Joris Guisson <joris,guisson$gmail,com>

Summary: BitTorrent client for KDE
Name: ktorrent
Version: 2.0.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://ktorrent.pwsp.net/

Source: http://ktorrent.org/downloads/%{version}/ktorrent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gettext, gcc-c++, gmp-devel

%description
KTorrent is a BitTorrent program for KDE.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/ktcachecheck
%{_bindir}/ktshell
%{_bindir}/ktupnptest
%{_bindir}/ktorrent
%{_bindir}/kttorinfo
%{_libdir}/kde3/kt*
%{_libdir}/libktorrent.*
%{_datadir}/apps/ktorrent/
%{_datadir}/config.kcfg/
%{_datadir}/icons/*/*/apps/ktorrent.*
%{_datadir}/icons/*/*/mimetypes/torrent.*
%{_datadir}/services/kt*.desktop
%{_datadir}/servicetypes/kt*.desktop
%{_datadir}/applications/kde/ktorrent.desktop
%{_datadir}/applnk/Internet/ktorrent.desktop
#%{_datadir}/mimelnk/application/x-bittorrent.desktop

%changelog
* Thu Aug 24 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.1-1
- Updated to release 2.0.1.

* Wed Aug 09 2006 Dries Verachtert <dries@ulyssis.org> - 2.0-1
- Updated to release 2.0.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-1.2
- Rebuild for Fedora Core 5.

* Wed Mar 01 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Updated to release 1.2.

* Thu Jan 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-0.rc2
- Initial package.
