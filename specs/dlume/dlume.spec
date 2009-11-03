# $Id$
# Authority: dag
# Upstream: Tomasz Maka <pasp$ll,pl>


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Graphical address book
Name: dlume
Version: 0.2.4
Release: 1.2%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://clay.ll.pl/dlume.html

Source: http://clay.ll.pl/download/dlume-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.2.0
BuildRequires: libxml2-devel >= 2.4.0, ImageMagick
%{?!_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Dlume is nice, graphical address book. You can easily add, edit,
and delete records from an XML database. A Quick-search makes it
easy to find entries. Exporting to CSV and HTML formats is also
possible.

%prep
%setup

%{__cat} <<EOF >dlume.desktop
[Desktop Entry]
Name=Dlume Address Manager
Comment=Manage contacts and addresses
Icon=dlume.png
Exec=dlume
Terminal=false
Type=Application
Categories=GNOME;Application;Office;
StartupNotify=true
EOF

%build
%configure \
	--enable-nls
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
#%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
        --add-category X-Red-Hat-Base              \
        --dir %{buildroot}%{_datadir}/applications \
        dlume.desktop

%clean
%{__rm} -rf %{buildroot}

#%files -f %{name}.lang
%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.4-1.2
- Rebuild for Fedora Core 5.

* Sun Jul 18 2004 Dag Wieers <dag@wieers.com> - 0.2.4-1
- Updated to release 0.2.4.

* Mon Mar 15 2004 Dag Wieers <dag@wieers.com> - 0.2.2-1.a
- Updated to release 0.2.2a.

* Fri Mar 12 2004 Dag Wieers <dag@wieers.com> - 0.2.0-1
- Initial package. (using DAR)
