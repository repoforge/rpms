# $Id: $

# Authority: dries
# Upstream: 

# Need to package kyra first

Summary: Group gems together
Name: gemhunters
Version: 
Release: 1
License: GPL
Group: Applications/
URL: http://gemhun.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: 

%description
Gemhun is all about grouping gems/stones of a chosen amount together which
will then dissappear. There will be plenty of different game-modes, theme-
and network-support. It is inspired by FrozenBubble/Tetris and some others.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Name Thingy Tool
Comment=Do things with things
Icon=name.png
Exec=name
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Network;X-Red-Hat-Extra;
EOF

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%post
/sbin/ldconfig 2>/dev/null
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL LICENSE NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%files devel
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Son May 19 2004 Dries Verachtert <dries@ulyssis.org> - 
- Initial package.

