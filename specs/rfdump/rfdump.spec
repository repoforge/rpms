# $Id$
# Authority: dries

Summary: Edit RFID tags
Name: rfdump
Version: 1.6
Release: 1%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://www.rfdump.org

Source: http://www.rfdump.org/dl/rfdump-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.6, gettext, gtk2-devel >= 2.4.0

%description
RFDUMP is a GUI to edit the "User Data Fields" on RFID tags and to test if 
a tag is protected against reading or writing. It implements a real life 
cookie on RFID tags.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/rfdump
%{_datadir}/applications/rfdump.desktop
%{_datadir}/pixmaps/rfdump.png
%{_datadir}/rfdump/

%changelog
* Fri Jun 20 2008 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Updated to release 1.6.

* Fri Nov 02 2007 Dag Wieers <dag@wieers.com> - 1.5-1
- Updated to release 1.5.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Updated to release 1.4.

* Sun Dec 18 2005 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Initial package.
