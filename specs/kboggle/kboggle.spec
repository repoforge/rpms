# $Id$
# Authority: dries

Summary: Boggle game
Name: kboggle
Version: 0.4.1
Release: 1
License: GPL
Group: Amusements/Games
URL: http://www.kde-apps.org/content/show.php?content=26195

Source: http://home.hccnet.nl/bram_s/kboggle/kboggle-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gettext, gcc-c++

%description
KBoggle is a Boggle game for KDE. Boggle is a game in which the players must
make words out of the letters found in a randomly generated grid of letters.
The goal is to find as many words as possible in the given time.

%prep
%setup

%build
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/kboggle
%{_datadir}/applications/kde/kboggle.desktop
%{_datadir}/apps/kboggle/
%{_datadir}/icons/*/*/apps/kboggle.png

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.1-1
- Updated to release 0.4.1.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.1-1.2
- Rebuild for Fedora Core 5.

* Mon Dec 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.3.1-1
- Initial package.
