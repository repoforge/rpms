# $Id$
# Authority:    hadams

Name:           gtk2-engines-nodoka
Version:        0.6
Packager:       Christopher Bratusek <nano-master@gmx.de>
Release:        14.2
License:        GPL-2
URL:            https://hosted.fedoraproject.org/projects/nodoka/wiki
Source:         %{name}_%{version}-1nano.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  make, bash, gtk2-devel, sed

Group:          NANO
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
/usr/lib/gtk-2.0/
/usr/share/themes/Nodoka/gtk-2.0/gtkrc

%changelog
* Sun Jul 22 2007 Heiko Adams <info@fedora-blog.de> - 0.6-14.2
- Rebuild for rpmforge

