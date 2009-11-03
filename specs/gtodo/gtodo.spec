# $Id$
# Authority: dag
# Upstream: <gtodo-list$lists,sf,net>

Summary: Graphical todo list tool
Name: gtodo
Version: 0.14
Release: 1.2%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://qball.no-ip.com/test/index.php?s=4

Source: http://download.qballcow.nl/programs/gtodo/gtodo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.0, libxml2-devel >= 2.5, GConf2-devel
BuildRequires: perl(XML::Parser), intltool, gtk2-devel, gettext
BuildRequires: gnome-vfs2-devel

%description
gToDo is as the name suggests a todo list application.
The goal of the program is to be simple and easy to use.

%prep
%setup

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1.2
- Rebuild for Fedora Core 5.

* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 0.14-1
- Initial package. (using DAR)
