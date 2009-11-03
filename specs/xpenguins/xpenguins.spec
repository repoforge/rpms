# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

Summary: Cute little penguins that walk along the tops of your windows
Name: xpenguins
Version: 2.2
Release: 0.2%{?dist}
License: GPL
Group: Amusements/Graphics
URL: http://xpenguins.seul.org/

Source: http://xpenguins.seul.org/xpenguins-%{version}.tar.gz
Source1: http://xpenguins.seul.org/xpenguins_themes-1.0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libXpm-devel, libXext-devel, libXt-devel}

%description
XPenguins animates a friendly family of penguins in your root window.
They drop in from the top of the screen, walk along the tops of your
windows, up the side of your windows, levitate, skateboard, and do
other similarly exciting things. XPenguins is now themeable so if
you're bored of penguins, try something else.

%package themes
Summary: Themes for xpenguins
Group: Amusements/Graphics
Requires: %{name} = %{version}-%{release}

%description themes
Themes for xpenguins, includes:

  + Big Penguins
  + Bill
  + Classic Penguins
  + Lemmings
  + Sonic the Hedgehog
  + The Simpsons
  + Turtles
  + Winnie the Pooh
  + Worms

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__tar} -xvzf %{SOURCE1} -C %{buildroot}%{_datadir}/xpenguins/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING lay-out-frames.scm README resize-frames.scm
%doc %{_mandir}/man1/*
%dir %{_datadir}/xpenguins/
%{_bindir}/*
%dir %{_datadir}/xpenguins/themes/
%{_datadir}/xpenguins/themes/Penguins/

%files themes
%defattr(-, root, root, 0755)
%{_datadir}/xpenguins/themes/Big_Penguins/
%{_datadir}/xpenguins/themes/Bill/
%{_datadir}/xpenguins/themes/Classic_Penguins/
%{_datadir}/xpenguins/themes/Lemmings/
%{_datadir}/xpenguins/themes/Sonic_the_Hedgehog/
%{_datadir}/xpenguins/themes/The_Simpsons/
%{_datadir}/xpenguins/themes/Turtles/
%{_datadir}/xpenguins/themes/Winnie_the_Pooh/
%{_datadir}/xpenguins/themes/Worms/

%changelog
* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 2.2-0
- Initial package. (using DAR)
