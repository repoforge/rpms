# $Id$
# Authority: dag
# Upstream: Josh Buhl <jbuhl$users,sourseforge,net>

%define real_version 0.32

Summary: Display the current phase of the Moon as an applet for the gnome panel. 
Name: glunarclock
Version: 0.32.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://glunarclock.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/glunarclock/glunarclock-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gail-devel
BuildRequires: scrollkeeper

Requires(post): scrollkeeper

%description
GNOME Lunar Clock displays the current phase of the Moon as an applet
for the gnome panel. 

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
%find_lang %{name}-%{real_version}

%post
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}-%{real_version}.lang
%defattr (-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README 
#%doc %{_mandir}/man1/*
%doc %{_datadir}/gnome/help/glunarclock-applet-2/
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_libexecdir}/*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/glunarclock/
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/glunarclock/
%{_datadir}/omf/glunarclock/*.omf
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.30.3-0
- Updated to release 0.30.3.

* Thu Apr 03 2003 Dag Wieers <dag@wieers.com> - 0.30.2-0
- Updated to release 0.30.2.

* Wed Mar 12 2003 Dag Wieers <dag@wieers.com> - 0.30.1-0
- Initial package. (using DAR)
