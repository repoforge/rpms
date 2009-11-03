# $Id$
# Authority: dries
# Screenshot: http://cssed.sourceforge.net/images/screens/screenshor_doc_menu.png
# ScreenshotURL: http://cssed.sourceforge.net/screenshots.html

Summary: CSS stylesheets editor
Name: cssed
Version: 0.4.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://cssed.sourceforge.net/

Source: http://dl.sf.net/cssed/cssed-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: autoconf, make, gcc-c++, expat-devel
BuildRequires: gtk2-devel, gettext, vte-devel, pkgconfig
Requires: gtk2, vte


%description
Cssed is a GTK2 application for creating and maintaining CSS style sheets.

%prep
%setup

%build
autoconf
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%{__mkdir_p} %{buildroot}%{_datadir}/applications/
%{__cat} > %{buildroot}%{_datadir}/applications/cssed.desktop << EOF
[Desktop Entry]
Name=Cssed
Comment=A CSS editor
Exec=cssed
Terminal=0
Type=Application
Encoding=UTF-8
Categories=Application;Network;X-Red-Hat-Base;
EOF
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/cssed
%{_datadir}/applications/cssed.desktop
%{_datadir}/cssed
%{_libdir}/pkgconfig/cssed.pc
%{_mandir}/man1/cssed*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.0-1.2
- Rebuild for Fedora Core 5.

* Sun Nov 27 2005 Dries Verachtert <dries@ulyssis.org> - 0.4.0-1
- Updated to release 0.4.0.

* Wed Nov 17 2004 Dries Verachtert <dries@ulyssis.org> 0.3.0-2
- Fix of the source url (Thanks to Marek Matulka!)

* Mon Oct 25 2004 Dries Verachtert <dries@ulyssis.org> 0.3.0-1
- Update to release 0.3.0.

* Sun May 16 2004 Dries Verachtert <dries@ulyssis.org> 0.2.1-1
- update to 0.2.1

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 0.1.1pre-1
- first packaging for Fedora Core 1

