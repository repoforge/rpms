# $Id: 
# Authority: 	h.adams

Summary: 	Ristretto
Name: 		ristretto
Version: 	0.0.19
Release: 	1%{?dist}
License: 	GPL
Group: 		Applications/Graphics
URL: 		http://goodies.xfce.org/projects/applications/ristretto

Source: 	http://goodies.xfce.org/releases/ristretto/%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: 	gtk2-devel >= 2.10
BuildRequires: 	libexif-devel >= 0.6
BuildRequires: 	Thunar-devel >= 0.9
BuildRequires: 	libxfce4util-devel >= 4.4.0
BuildRequires: 	libxfcegui4-devel >= 4.4.0
BuildRequires: 	dbus-glib-devel >= 0.34

Requires: 	gtk2 >= 2.10
Requires: 	Thunar >= 0.9
Requires: 	libxfce4util >= 4.4.0
Requires: 	libxfcegui4 >= 4.4.0
Requires: 	libexif >= 0.6.0
Requires: 	dbus-glib >= 0.34

%description
Ristretto is a fast and lightweight picture-viewer for the Xfce desktop environment.

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
%{_bindir}/ristretto
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*
%{_datadir}/locale/*

%changelog
* Sat Apr 10 2008 Heiko Adams <info-2007@fedora-blog.de> - 0.0.19-1
- Initial package.
