# $Id$
# Authority: dries

Summary: GUI for rsync
Name: grsync
Version: 0.3.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.opbyte.it/grsync/

Source: http://www.opbyte.it/release/grsync-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, gtk2-devel
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
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/grsync*
%{_bindir}/grsync
%{_datadir}/pixmaps/grsync.png
%{_datadir}/applications/grsync.desktop

%changelog
* Sun Apr 23 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.2-1
- Updated to release 0.3.2.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1.2
- Rebuild for Fedora Core 5.

* Wed Mar 01 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Updated to release 0.3.

* Sun Jan 29 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.1-1
- Initial package.
