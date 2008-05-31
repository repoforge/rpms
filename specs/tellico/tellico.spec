# $Id: $

# Authority: dries
# Upstream: Robby Stephenson <mailto:robby$periapsis,org>
# Screenshot: http://www.periapsis.org/tellico/sshots/main_screen-0.9.png
# ScreenshotURL: http://www.periapsis.org/tellico/sshots.php

%{?dtag: %{expand: %%define %dtag 1}}

Summary: collection manager
Name: tellico
Version: 1.3.2.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.periapsis.org/tellico/

Source: http://www.periapsis.org/tellico/download/tellico-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgcrypt-devel, gcc-c++, gettext, libxslt-devel
BuildRequires: kdelibs-devel, desktop-file-utils, libxml2-devel
#BuildRequires: kdemultimedia-devel
%{?fc3:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}

%description
Tellico is a collection manager for KDE. It includes default collections for
books, bibliographies, comic books, videos, music, coins, stamps, trading
cards, and wines, and also allows custom collections. Unlimited user-defined
fields are allowed. Filters are available to limit the visible entries by
definable criteria. Full customization for printing is possible through
editing the default XSLT file. It can import CSV, Bibtex, and Bibtexml and
export CSV, HTML, Bibtex, Bibtexml, and PilotDB. Entries may be imported
directly from Amazon.com.

%prep
%setup

%build
source /etc/profile.d/qt.sh
%configure CPPFLAGS=-I%{_includedir}/kde
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /etc/profile.d/qt.sh
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
%doc %{_docdir}/HTML/*/tellico/
%{_bindir}/*
%{_datadir}/applications/kde/tellico.desktop
%dir %{_datadir}/apps/kconf_update/
%{_datadir}/apps/kconf_update/tellico.upd
%{_datadir}/apps/kconf_update/tellico-rename.upd
%{_datadir}/apps/kconf_update/tellico-1-3-update.pl
%{_datadir}/apps/tellico/
%{_datadir}/icons/hicolor/*/apps/tellico.png
%{_datadir}/icons/hicolor/*/mimetypes/application-x-tellico.png
%{_datadir}/mime/packages/tellico.xml
%{_datadir}/mimelnk/application/x-tellico.desktop
%{_datadir}/config.kcfg/tellico_config.kcfg
%{_datadir}/config/tellicorc

%changelog
* Fri May 30 2008 Dries Verachtert <dries@ulyssis.org> - 1.3.2.1-1
- Updated to release 1.3.2.1.

* Thu Mar 13 2008 Dries Verachtert <dries@ulyssis.org> - 1.3.1-1
- Updated to release 1.3.1.

* Sun Feb  3 2008 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Updated to release 1.3.

* Mon Sep 24 2007 Dries Verachtert <dries@ulyssis.org> - 12.14-1
- Updated to release 1.2.14.

* Sun Jul 29 2007 Dries Verachtert <dries@ulyssis.org> - 12.13-1
- Updated to release 1.2.13.

* Sun Jul 08 2007 Dries Verachtert <dries@ulyssis.org> - 12.12-1
- Updated to release 1.2.12.

* Wed May 09 2007 Dries Verachtert <dries@ulyssis.org> - 1.2.11-1
- Updated to release 1.2.11.

* Mon Apr 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.2.10-1
- Updated to release 1.2.10.

* Mon Mar 12 2007 Dries Verachtert <dries@ulyssis.org> - 1.2.9-1
- Updated to release 1.2.9.

* Tue Feb 13 2007 Dries Verachtert <dries@ulyssis.sorg> - 1.2.8-1
- Updated to release 1.2.8.

* Fri Dec 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.7-1
- Updated to release 1.2.7.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.6-1
- Updated to release 1.2.6.

* Mon May 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.6-1
- Updated to release 1.1.6.

* Fri Apr 21 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.5-1
- Updated to release 1.1.5.

* Mon Apr 03 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.4-1
- Updated to release 1.1.4.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.3-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Tue Mar 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.3-1
- Updated to release 1.1.3.

* Sun Feb 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.1-1
- Updated to release 1.1.1.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.1-1
- Updated to release 1.1.

* Wed Oct 19 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.3-1
- Updated to release 1.0.3.

* Mon Oct 03 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.2-1
- Updated to release 1.0.2.

* Thu Sep 22 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1
- Updated to release 1.0.1.

* Sat Sep 10 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Updated to release 1.0.

* Sun Jul 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.13.8-1
- Updated to release 0.15.8.

* Mon Apr 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.13.6-1
- Updated to release 0.13.6.

* Wed Mar 09 2005 Dries Verachtert <dries@ulyssis.org> - 0.13.5-1
- Updated to release 0.13.5.

* Mon Feb 28 2005 Dries Verachtert <dries@ulyssis.org> - 0.13.4-1
- Updated to release 0.13.4.

* Sat Jan 29 2005 Dries Verachtert <dries@ulyssis.org> - 0.13.1-2
- kdemultimedia-devel added to the buildrequirements so it picks up
  kcddb support (Thanks to Vic Gedris)

* Sun Dec 12 2004 Dries Verachtert <dries@ulyssis.org> - 0.13.1-1
- Update to release 0.13.1.

* Sat Dec 04 2004 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Update to release 0.13.

* Sat Oct 02 2004 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.
