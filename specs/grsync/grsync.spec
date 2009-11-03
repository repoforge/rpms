# $Id$
# Authority: dries

Summary: GUI for rsync
Name: grsync
Version: 0.6.3
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.opbyte.it/grsync/

Source: http://www.opbyte.it/release/grsync-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, glib2-devel >= 2.6, gtk2-devel, perl(XML::Parser)
Requires: rsync

%description
Grsync is a GUI for rsync, the command line directory synchronization tool.
It supports only a limited set of rsync features, but can be effectively
used to synchronize local directories.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/grsync.1*
%doc %{_mandir}/man1/grsync-batch.1*
%{_bindir}/grsync
%{_bindir}/grsync-batch
%{_datadir}/pixmaps/grsync.png
%{_datadir}/applications/grsync.desktop

%changelog
* Tue Apr 14 2009 Dries Verachtert <dries@ulyssis.org> - 0.6.3-1
- Updated to release 0.6.3.

* Thu Nov 30 2007 Dries Verachtert <dries@ulyssis.org> - 0.6.1-1
- Updated to release 0.6.1.

* Sun Jul 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Updated to release 0.6.

* Sun May 13 2007 Dag Wieers <dag@wieers.com> - 0.5.2-1
- Added perl(XML::Parser) dependency. (Lajos)

* Sun Jan 21 2007 Dag Wieers <dag@wieers.com> - 0.5.2-1
- Updated to release 0.5.2.

* Sun Aug 13 2006 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Updated to release 0.5.

* Thu Jun 29 2006 Dag Wieers <dag@wieers.com> 0.4.3-1
- Updated to release 0.4.3.

* Fri May 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.2-1
- Updated to release 0.4.2.

* Sat May 06 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.1-1
- Updated to release 0.4.1.

* Sun Apr 30 2006 Dag Wieers <dag@wieers.com> - 0.4-1
- Updated to release 0.4.

* Sun Apr 23 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.2-1
- Updated to release 0.3.2.

* Wed Mar 01 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Updated to release 0.3.

* Sun Jan 29 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.1-1
- Initial package.
