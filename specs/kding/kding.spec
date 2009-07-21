# $Id$
# Authority: dries
# Upstream: Michael Rex <me$rexi,org>

Summary: Frontend for ding, a dictionary lookup program
Name: kding
Version: 0.5
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.rexi.org/software/kding/

Source: http://www.rexi.org/downloads/kding/kding-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gcc-c++, gettext
Requires: ding

%description
KDing is a KDE frontend for Ding, a dictionary lookup program. It sits
in KDE's system tray and can translate the current clipboard content.
Users can also enter single words or phrases for translation. It is
intended to be used for translating between German and English, but
can be used with every language for which a word list is available for
Ding.

%prep
%setup

%build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DPREFIX=%{_prefix} .
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/kding
%{_datadir}/applications/kde4/kding.desktop
%{_datadir}/kde4/apps/kding/
%{_datadir}/config.kcfg/kding.kcfg
%{_datadir}/doc/HTML/*/kding/
%{_datadir}/icons/*/*/apps/kding.png
%{_datadir}/icons/*/*/actions/kding_search.png
%{_datadir}/icons/*/*/actions/kding_babelfish.png

%changelog
* Tue Jul 21 2009 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Updated to release 0.5.

* Tue May 20 2008 Dries Verachtert <dries@ulyssis.org> - 0.4.3-1
- Updated to release 0.4.3.

* Sun Feb 17 2008 Dries Verachtert <dries@ulyssis.org> - 0.4.2-1
- Updated to release 0.4.2.

* Mon Sep 10 2007 Dries Verachtert <dries@ulyssis.org> - 0.4.1-1
- Updated to release 0.4.1.

* Fri Aug 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.4-1
- Updated to release 0.4.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1.2
- Rebuild for Fedora Core 5.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
