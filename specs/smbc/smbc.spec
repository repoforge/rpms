# $Id$
# Authority: dries
# Upstream: <smbc-list$lists,sourceforge,net>

# Screenshot: http://smbc.airm.net/screenshots/mainpage.jpg
# ScreenshotURL: http://smbc.airm.net/screenshots/

Summary: Text mode SMB (Samba) commander
Name: smbc
Version: 1.0.0
Release: 2
License: GPL
Group: Applications/Internet
URL: http://smbc.airm.net/en/index.php

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://smbc.airm.net/1.0.0/smbc-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, ncurses-devel, samba-common

%description
Smbc is a program for browsing a local SMB (Samba) network. With smbc, you
can download and upload files or directories and create remote and local
directories. Smbc has a resume function and supports UTF-8 characters.

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
%doc COPYING FAQ NEWS README doc/sample.smbcrc
%{_mandir}/man?/smbc*
%doc %{_infodir}/*.info*
%{_bindir}/*
%exclude %{_datadir}/smbc/FAQ
%exclude %{_datadir}/smbc/README
%exclude %{_datadir}/smbc/sample.smbrc


%changelog
* Sun Oct 03 2004 Dries Verachtert <dries@ulyssis.org> 1.0.0-2
- Fix the urls.

* Sat Oct 02 2004 Dries Verachtert <dries@ulyssis.org> 1.0.0-1
- Updated to version 1.0.0.

* Wed Sep 01 2004 Dries Verachtert <dries@ulyssis.org> 0.9.0-1
- Updated to version 0.9.0.

* Wed Jul 28 2004 Dries Verachtert <dries@ulyssis.org> 0.8.2-1
- Updated to version 0.8.2.

* Fri Jun 25 2004 Dries Verachtert <dries@ulyssis.org> 0.8.1-1
- Update to version 0.8.1.

* Mon May 24 2004 Dries Verachtert <dries@ulyssis.org> 0.7.3-1
- Initial package.
