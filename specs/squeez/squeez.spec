# $Id: 
# Authority: 	h.adams

Summary: 	Squeeze
Name: 		squeeze
Version: 	0.2.3
Release: 	1
License: 	GPL
Group: 		Applications/Utilities
URL: 		http://squeeze.xfce.org

Source: 	http://squeeze.xfce.org/downloads/%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: 	gtk2-devel >= 2.10
BuildRequires: 	libxfce4util-devel >= 4.4.0
BuildRequires: 	libxfcegui4-devel >= 4.4.0
BuildRequires: 	dbus-glib-devel >= 0.34
BuildRequires: 	Thunar-devel >= 0.8

Requires: 	gtk2 >= 2.10
Requires: 	libxfce4util >= 4.4.0
Requires: 	libxfcegui4 >= 4.4.0
Requires: 	dbus-glib >= 0.34
Requires: 	Thunar >= 0.8

%description
Squeeze is a modern and advanced archive manager for the Xfce Desktop Environment.
Its design adheres to the Xfce philosophy, which basically means Squeeze is designed to be both fast and easy to use. 

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} %{buildroot}/usr/share/icons/hicolor/icon-theme.cache
%find_lang %{name}

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/%{name}
%{_includedir}/libsqueeze-0.2
%{_libdir}/*
%{_libexecdir}/thunar-archive-plugin/%{name}.tap
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*
%{_datadir}/locale/*
%{_datadir}/pixmaps/*
%{_datadir}/gtk-doc/html/libsqueeze/*

%changelog
* Sat Apr 10 2008 Heiko Adams <info-2007@fedora-blog.de> - 0.2.3-1
- Initial package.
