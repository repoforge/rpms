# $Id$
# Authority: dries
# Upstream: Federico Poloni <fph$ngi,it>

Summary: Very nasty tetris game
Name: bastet
Version: 0.41
Release: 1
License: GPL
Group: Amusements/Games
URL: http://fph.altervista.org/prog/bastet.shtml

Source: http://fph.altervista.org/prog/bastet-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
Bastet (stands for "bastard tetris") is a free (GPL'd) clone of Tetris(r)
(built on the top of petris by Peter Seidler) which is designed to be "as
bastard as possible": it tries to compute how useful blocks are and gives
you the worst, the most bastard it can find. Playing bastet can be a painful
experience, especially if you usually make "canyons" and wait for the long
I-shaped block.

With the following command, you can make the binary setuid games, so normal
users can save their highscores. This can be security hole!
chmod u+s /usr/bin/bastet

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
%doc AUTHORS COPYING README* TODO BUGS NEWS
%{_bindir}/bastet

%defattr(-, games, root, 0755)
%{_localstatedir}/games/bastet.scores

%changelog
* Fri Oct 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.41-1
- Update to release 0.41.

* Sat May 15 2004 Dag Wieers <dag@wieers.com> - 0.37-1
- Cosmetic cleanup.

* Sun May 2 2004 Dries Verachtert <dries@ulyssis.org> - 0.37-1
- Initial package.
