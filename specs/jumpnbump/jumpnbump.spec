# $Id$
# Authority: dag
# Upstream: <gurkan$linuks,mine,nu>

Summary: Cute multiplayer network game with bunnies
Name: jumpnbump
Version: 1.50
Release: 1
License: GPL
Group: Amusements/Games
URL: http://www.jumpbump.mine.nu/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.jumpbump.mine.nu/port/jumpnbump-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL_net-devel, SDL_mixer, SDL-devel

%description
You, as a bunny, have to jump on your opponents to make them
explode. It's a true multiplayer game, you can't play this
alone. It has network support.

%prep
%setup

%build
%{__make} %{?_smp_mflags} \
	PREFIX="%{_prefix}"

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 jumpnbump %{buildroot}%{_bindir}/jumpnbump
%{__install} -D -m0755 jumpnbump.fbcon %{buildroot}%{_bindir}/jumpnbump.fbcon
%{__install} -D -m0755 jumpnbump.svgalib %{buildroot}%{_bindir}/jumpnbump.svgalib
%{__install} -D -m0644 data/jumpbump.dat %{buildroot}%{_datadir}/jumpnbump/jumpbump.dat
%{__install} -D -m0644 jumpnbump.6 %{buildroot}%{_mandir}/man6/jumpnbump.6

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0775)
%doc AUTHORS ChangeLog COPYING jumpnbump.html LINKS README readme.txt source.txt TODO
%doc levelmaking/
%doc %{_mandir}/man6/*
%{_bindir}/*
%{_datadir}/jumpnbump/

%changelog 
* Wed Jun 16 2004 Dag Wieers <dag@wieers.com> - 1.50-1
- Updated to release 1.50.

* Sun Mar 30 2003 Dag Wieers <dag@wieers.com> - 1.41-0
- Updated to release 1.41.

* Mon Dec 16 2002 Dag Wieers <dag@wieers.com> - 1.40-1
- Updated to release 1.40.

* Mon Jun 10 2002 Dag Wieers <dag@wieers.com> - 1.3-0
- Updated to release 1.3.

* Sun Apr 21 2002 Dag Wieers <dag@wieers.com> - 1.2-0
- Initial package.
