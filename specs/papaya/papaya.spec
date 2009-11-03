# $Id$
# Authority: dag

Summary: MUD client with plugins
Name: papaya
Version: 0.96
Release: 0.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://www.gtk-papaya.org/

Source: papaya-src-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
Papaya is a fully featured GTK/Gnome MUD client for UNIX, Windows and MacOS X.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-src-%{version}

%{__cat} <<EOF >gnome-%{name}.desktop
[Desktop Entry]
Name=MUD Client
Comment=Access Multi User Dungeon games online
Exec=papaya
Type=Application
MimeType=
Icon=gnome-squeak.png
Terminal=false
Categories=Application;Game
StartupNotify=true
EOF

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake} --add-missing
%configure \
	--enable-plugins="yes"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
%{__install} -Dp -m0644 gnome-papaya.desktop %{buildroot}%{_datadir}/applications/gnome-papaya.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc doc/Changelog doc/CREDITS doc/FEATURES doc/LICENSE doc/manual/manual.pdf
%doc doc/*-Plugins doc/Plugins/
%{_bindir}/*
%{_datadir}/papaya/
%{_datadir}/applications/*.desktop
%{_libdir}/papaya/

%files devel
%defattr(-, root, root, 0755)
%doc doc/Programmers/*.README doc/Programmers/README.*
%{_includedir}/papaya/
%{_libdir}/pkgconfig/*.pc

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.96-0.2
- Rebuild for Fedora Core 5.

* Sun Jul 27 2003 Dag Wieers <dag@wieers.com> - 0.96-0
- Initial package. (using DAR)
