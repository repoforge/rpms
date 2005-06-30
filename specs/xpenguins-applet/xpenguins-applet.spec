# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

%define real_name xpenguins_applet

Summary: Cute little penguins that walk along the top of your windows
Name: xpenguins-applet
Version: 1.0
Release: 0
License: GPL
Group: Amusements/Graphics
URL: http://xpenguins.seul.org/

Source: http://xpenguins.seul.org/xpenguins_applet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: xpenguins >= 1.9
BuildRequires: gnome-libs-devel, automake, autoconf
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
This program is a GNOME panel applet that animates a friendly family
of penguins in your root window.  They drop in from the top of the
screen, walk along the top of your windows, up the side of your
windows, levitate, skateboard, and do other similarly exciting
things. XPenguins is now themeable so if you're bored of penguins, try
something else.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc %{_datadir}/gnome/help/xpenguins_applet/
%{_sysconfdir}/CORBA/servers/*.gnorba
%{_bindir}/xpenguins_applet
%{_datadir}/applets/Amusements/*.desktop
%{_datadir}/pixmaps/*

%changelog
* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
