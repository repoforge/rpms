# $Id: $
# Authority: dries
# Upstream: <smbc-list@lists.sourceforge.net>

# Screenshot: http://www.air.rzeszow.pl/smbc/smbc/screenshots/mainpage.jpg
# ScreenshotURL: http://www.air.rzeszow.pl/smbc/smbc/screenshots/

Summary: Text mode SMB (Samba) commander
Name: smbc
Version: 0.8.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.rafim.prv.pl/smbc/smbc/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.air.rzeszow.pl/smbc/smbc/%{version}/smbc-%{version}.tgz
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

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING FAQ NEWS README doc/sample.smbcrc
%{_bindir}/*
%exclude %{_datadir}/doc

%changelog
* Fri Jun 25 2004 Dries Verachtert <dries@ulyssis.org> 0.8.1-1
- Update to version 0.8.1.

* Mon May 24 2004 Dries Verachtert <dries@ulyssis.org> 0.7.3-1
- Initial package.
