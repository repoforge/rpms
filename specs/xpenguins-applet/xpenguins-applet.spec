# $Id$
# Authority: dag

%define real_name xpenguins_applet

Summary: Cute little penguins that walk along the top of your windows
Name: xpenguins-applet
Version: 1.0
Release: 0
License: GPL
Group: Amusements/Graphics
URL: http://xpenguins.seul.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://xpenguins.seul.org/xpenguins_applet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: xpenguins >= 1.9

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
