# $Id$

# Authority: dag

Summary: Cute little penguins that walk along the tops of your windows
Name: xpenguins
Version: 2.2
Release: 0
License: GPL
Group: Amusements/Graphics
URL: http://xpenguins.seul.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://xpenguins.seul.org/%{name}-%{version}.tar.gz
Source1: http://xpenguins.seul.org/%{name}_themes-1.0.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

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
%makeinstall
%{__tar} -xvzf %{SOURCE1} -C %{buildroot}%{_datadir}/xpenguins/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README lay-out-frames.scm resize-frames.scm
%doc %{_mandir}/man1/*
%dir %{_datadir}/xpenguins/
%{_bindir}/*
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
