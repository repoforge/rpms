# $Id$
# Authority: dries
# Upstream: Federico Poloni <fph$ngi,it>

Summary: Very nasty tetris game
Name: bastet
Version: 0.43
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://fph.altervista.org/prog/bastet.shtml

Source: http://fph.altervista.org/prog/files/bastet-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
Bastet (stands for "bastard tetris") is a free (GPL'd) clone of Tetris(r)
(built on the top of petris by Peter Seidler) which is designed to be "as
bastard as possible": it tries to compute how useful blocks are and gives
you the worst, the most bastard it can find. Playing bastet can be a painful
experience, especially if you usually make "canyons" and wait for the long
I-shaped block.

Users can save their highscores if you add them to the 'games' group.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 bastet %{buildroot}%{_bindir}/bastet
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/games/
touch %{buildroot}%{_localstatedir}/games/bastet.scores

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS COPYING NEWS README* TODO
%{_bindir}/bastet

%defattr(0775, root, games, 0755)
%{_localstatedir}/games/bastet.scores

%changelog
* Tue Apr  7 2009 Dries Verachtert <dries@ulyssis.org> - 0.43-1
- Updated to release 0.43.

* Fri Apr 28 2006 Dries Verachtert <dries@ulyssis.org> - 0.41-2
- Changed the ownership of bastet.scores to root.games so users just 
  need to add themselves to the games group, thanks to Edward Rudd.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.41-1.2
- Rebuild for Fedora Core 5.

* Fri Oct 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.41-1
- Update to release 0.41.

* Sat May 15 2004 Dag Wieers <dag@wieers.com> - 0.37-1
- Cosmetic cleanup.

* Sun May 2 2004 Dries Verachtert <dries@ulyssis.org> - 0.37-1
- Initial package.
