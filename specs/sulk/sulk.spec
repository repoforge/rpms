# $Id$

# Authority: dries

Summary: Sulk, the hackable Space Hulk.
Name: sulk
Version: 0.29
Release: 1
License: LGPL
Group: Amusements/Games
URL: http://sulk.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/sulk/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Patch: makefile-and-shellscript.patch.bz2
Requires: python, python-game

#(d) primscreenshot: http://sulk.sourceforge.net/pics/sulk-screen-0.26.1.png
#(d) screenshotsurl: http://sulk.sourceforge.net/pics.html

%description
Sulk is a board game, based on Space Hulk published by Games Workshop. It's
made in Python with Pygame.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup -n sulk-0.29
%patch -p1

%build
%{__make} %{?_smp_mflags}

%install
export DESTDIR=$RPM_BUILD_ROOT
%{__make} install
chmod +x ${DESTDIR}/usr/games/sulk

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING HACKING WHATSNEW
/usr/share/games/sulk
/usr/games/sulk

%changelog
* Sun Feb 29 2004 Dries Verachtert <dries@ulyssis.org> 0.29-1
- update to 0.29
- cleanup of spec file

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 0.28-2
- finished the packaging
- used sulk 0.28, not the 0.29 snapshot

* Wed Dec 24 2003 Dries Verachtert <dries@ulyssis.org> 0.29snapshot20030623-1
- first packaging for Fedora Core 1
