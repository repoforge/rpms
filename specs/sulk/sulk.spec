# $Id$
# Authority: dries

# Screenshot: http://sulk.sourceforge.net/pics/sulk-screen-0.26.1.png
# ScreenshotURL: http://sulk.sourceforge.net/pics.html

%define real_version 0.29-snapshot-20030623

Summary: Sulk, the hackable Space Hulk
Name: sulk
Version: 0.29
Release: 2
License: LGPL
Group: Amusements/Games
URL: http://sulk.sf.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/sulk/sulk-%{realversion}.tar.gz
Patch: makefile-and-shellscript.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: python, python-game

%description
Sulk is a board game, based on Space Hulk published by Games Workshop. It's
made in Python with Pygame.

%prep
%setup
%patch -p1

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%files
%defattr(-, root, root, 0755)
%doc README AUTHORS COPYING HACKING WHATSNEW
%{_datadir}/games/sulk/
%{_prefix}/games/sulk/

%changelog
* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 0.29-2
- Cosmetic cleanup.

* Sun Feb 29 2004 Dries Verachtert <dries@ulyssis.org> 0.29-1
- update to 0.29
- cleanup of spec file

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 0.28-2
- finished the packaging
- used sulk 0.28, not the 0.29 snapshot

* Wed Dec 24 2003 Dries Verachtert <dries@ulyssis.org> 0.29snapshot20030623-1
- first packaging for Fedora Core 1
