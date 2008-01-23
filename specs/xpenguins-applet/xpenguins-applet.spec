# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

Summary: Cute little penguins that walk along the top of your windows
Name: xpenguins-applet
Version: 2.0.1
Release: 1
License: GPL
Group: Amusements/Graphics
URL: http://xpenguins.seul.org/

Source: http://xpenguins.seul.org/xpenguins-applet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: xpenguins >= 1.9
BuildRequires: gnome-libs-devel, automake, autoconf, gnome-panel-devel, gettext
# configure checks if the themes are available
BuildRequires: xpenguins
%{!?_without_modxorg:BuildRequires: libXpm-devel, libXt-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
This program is a GNOME panel applet that animates a friendly family
of penguins in your root window.  They drop in from the top of the
screen, walk along the top of your windows, up the side of your
windows, levitate, skateboard, and do other similarly exciting
things. XPenguins is now themeable so if you're bored of penguins, try
something else.

%prep
%setup

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
%doc %{_datadir}/gnome/help/xpenguins-applet/
%{_sysconfdir}/gconf/schemas/xpenguins-applet.schemas
%{_prefix}/libexec/xpenguins-applet
%{_datadir}/gnome-2.0/ui/xpenguins-applet.xml
%{_datadir}/omf/xpenguins-applet/
%{_datadir}/pixmaps/gnome-xpenguins.png
%{_libdir}/bonobo/servers/xpenguins-applet.server

%changelog
* Sat May 27 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.1-1
- Updated to release 2.0.1.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-0.2
- Rebuild for Fedora Core 5.

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
