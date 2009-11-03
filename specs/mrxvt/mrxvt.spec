# $Id$
# Authority: dag


%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

Summary: Lightweight multi-tabbed X terminal
Name: mrxvt
Version: 0.5.1
Release: 1%{?dist}
License: GPL
Group: User Interface/X
URL: http://materm.sourceforge.net/

Source: http://dl.sf.net/materm/mrxvt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: freetype-devel
#Requires:  qt >= 2.3.0
Obsoletes: materm
%{!?_without_modxorg:BuildRequires: libX11-devel, libXt-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
Mrxvt (previously named as materm) is a lightweight and powerful
multi-tabbed X terminal emulator based on the popular rxvt and aterm.
It implements many useful features seen in some modern X terminal
emulators, like gnome-terminal and konsole, but keep to be lightweight
and independent from the GNOME and KDE desktop environment.

%prep
%setup

%build
%configure --enable-everything --disable-debug
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS FAQ NEWS TODO
%doc %{_mandir}/man1/mrxvt.1*
%config %{_sysconfdir}/mrxvt/
%{_bindir}/mrxvt
%{_datadir}/pixmaps/mrxvt*.png
%{_datadir}/pixmaps/mrxvt*.xpm
%exclude %{_docdir}/mrxvt/

%changelog
* Sun Apr 23 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.1-1
- Updated to release 0.5.1.
- Disabled debugging output (Davide Cesari).

* Sun Apr 23 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.0-1
- Updated to release 0.5.0.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.1-1.2
- Rebuild for Fedora Core 5.

* Thu Aug 11 2005 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Initial package. (using DAR)
