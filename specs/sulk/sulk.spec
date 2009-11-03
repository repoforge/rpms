# $Id$
# Authority: dries
# Screenshot: http://sulk.sourceforge.net/pics/sulk-screen-0.26.1.png
# ScreenshotURL: http://sulk.sourceforge.net/pics.html

%define real_version 0.29-snapshot-20030623

Summary: Sulk, the hackable Space Hulk
Name: sulk
Version: 0.29
Release: 3.2%{?dist}
License: LGPL
Group: Amusements/Games
URL: http://sulk.sourceforge.net/

Source: http://dl.sf.net/sulk/sulk-%{real_version}.tar.gz
Patch: makefile-and-shellscript.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: python, python-game

%description
Sulk is a board game, based on Space Hulk published by Games Workshop. It's
made in Python with Pygame.

%prep
%setup -n sulk-%{real_version}
%patch -p1

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot}
%{__chmod} +x %{buildroot}%{_bindir}/sulk

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING HACKING README WHATSNEW
%{_datadir}/games/sulk/
%{_bindir}/sulk

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.29-3.2
- Rebuild for Fedora Core 5.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.29-3
- Moved the shell script to /usr/bin/
- Shell script executable (Thanks to C.Lee Taylor)

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
