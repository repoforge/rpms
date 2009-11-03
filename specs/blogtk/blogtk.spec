# $Id$
# Authority: dag
# Upstream: Jay Reding <blogtk$jayreding,com>

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

%define real_name BloGTK

Summary: Graphical weblogging client
Name: blogtk
Version: 1.1
Release: 1%{?dist}
License: BSD
Group: Applications/Internet
URL: http://blogtk.sourceforge.net/

Source: http://dl.sf.net/blogtk/blogtk_%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, pygtk2, pygtk2-libglade
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: python, pygtk2, pygtk2-libglade

%description
BloGTK is a weblogging client based on PyGTK that allows users to
connect with blogging systems like Blogger, Movable Type, as well
as any system that uses the MetaWeblog API. BloGTK supports
advanced editing of posts including custom HTML tags and offline
post saving and editing. BloGTK also includes support for basic
HTTP proxies.

%prep
%setup -n %{real_name}-%{version}

%{__perl} -pi.orig -e '
		s|\$\(BINDIR\)|\$(DESTDIR)\$(bindir)|;
		s|\$\(LIBDIR\)|\$(DESTDIR)\$(libdir)/blogtk|;
		s|\$\(DATADIR\)|\$(DESTDIR)\$(datadir)/blogtk|;
		s|\$\(APPLICATIONSDIR\)|\$(DESTDIR)\$(datadir)/applications|;
		s|\$\(ICONDIR\)|\$(DESTDIR)\$(datadir)/pixmaps|;
	' Makefile

%{__cat} <<EOF >blogtk.desktop
[Desktop Entry]
Name=BloGTK Weblog Editor
Comment=Post to your weblog
Icon=blogtk-icon.svgz
Exec=blogtk
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;Application;Network;
EOF

%build

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Fix symlinks
%{__ln_s} -f %{_libdir}/blogtk/BloGTK.py %{buildroot}%{_bindir}/blogtk
%{__ln_s} -f %{_libdir}/blogtk/BloGTK.py %{buildroot}%{_bindir}/BloGTK

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	blogtk.desktop

### Clean up buildroot
%{__rm} -f %{buildroot}%{_datadir}/applications/blogtk.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_libdir}/blogtk/
%{_datadir}/blogtk/
%{_datadir}/pixmaps/blogtk-icon.*
%{_datadir}/applications/*.desktop

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.1-1
- Updated to release 1.1.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1.2
- Rebuild for Fedora Core 5.

* Fri May 14 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
