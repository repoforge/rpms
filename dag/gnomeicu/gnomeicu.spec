# Authority: newrpms
Summary: GnomeICU is a clone of Mirabilis' popular ICQ written with GTK.
Name: gnomeicu
Version: 0.99
Release: 2
Epoch: 1
License: GPL
Group: Applications/Communications
URL: http://gnomeicu.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libgnomeui-devel >= 2.0.0, gnet-devel >= 1.1.3
BuildRequires: libxml2-devel >= 2.4.7, scrollkeeper >= 0.3.5

Requires(post): scrollkeeper

%description
GnomeICU is a clone of Mirabilis' popular ICQ written with GTK.
The original source was taken from Matt Smith's mICQ. If you would
like to contribute, please contact Jeremy Wise <jwise@pathwaynet.com>.

%package applet
Summary: GNOME applet for GnomeICU
Group: Applications/Communications
Requires: %{name} = %{epoch}:%{version}-%{release}

%description applet
The is the gnome2 applet for GnomeICU. It is now deprecated.
GnomeICU is a clone of Mirabilis' popular ICQ written with GTK.
The original source was taken from Matt Smith's mICQ.

%prep
%setup

%build
%configure \
	--enable-applet
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%doc %{_datadir}/gnome/help/gnomeicu/
%config %{_sysconfdir}/gconf/schemas/*
%config %{_sysconfdir}/sound/events/*
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/gnomeicu/
%{_datadir}/omf/gnomeicu/
%{_datadir}/pixmaps/*
%{_datadir}/sounds/gnomeicu/

%files applet
%defattr(-,root,root)
%{_libexecdir}/*
%{_datadir}/gnome-2.0/ui/*
%{_libdir}/bonobo/servers/*

%changelog
* Wed Nov 19 2003 Dag Wieers <dag@wieers.com> - 0.99-2
- Fix incredibly stupid epoch problem with Fedora. (Axel Thimm)

* Mon Mar 10 2003 Dag Wieers <dag@wieers.com> - 0.99-1
- Added the deprecated applet sub-package.

* Sun Mar 09 2003 Dag Wieers <dag@wieers.com> - 0.99-0
- Initial package. (using DAR)
