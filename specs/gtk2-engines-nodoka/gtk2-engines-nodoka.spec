# $Id$
# Authority:    hadams

Name:           gtk2-engines-nodoka
Version:        0.6.2
Packager:       Heiko Adams <info@fedora-blog.de>
Release:        14.4
License:        GPL-2
URL:            https://hosted.fedoraproject.org/projects/nodoka/wiki
Source:         %{name}_%{version}-1nano.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  gtk2-devel
BuildRequires:  sed

Group:          System Environment/Libraries
Summary:        GTK+2 Theme Engine

%description
Nodoka is the Fedora 8 GTK+2 Theme Engine
It supports mac style menus, animation
and animations from left to right

%prep
%setup -q

%build
cp new_config_sub config.sub
cp new_config_guess config.guess
./configure --prefix=/usr --enable-macmenu --enable-animation --enable-animationtoleft

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(0755,root,root)
%doc AUTHORS ChangeLog NEWS COPYING
%{_libdir}/gtk-2.0/*/engines/*
%{_datadir}/*

%changelog
* Sun Feb 17 2008 Heiko Adams <info-2007@fedora-blog.de> - 0.6.2-14.4
- Update to 0.6.2

* Sat Sep 15 2007 Heiko Adams <info@fedora-blog.de> - 0.6-14.3
- Some small updates to the specfile

* Fri Sep 14 2007 Heiko Adams <info@fedora-blog.de> - 0.6-14.2
- Rebuild for rpmforge

