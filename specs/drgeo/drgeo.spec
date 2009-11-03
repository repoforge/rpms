# $Id$
# Authority: dag
# Upstream: Hilaire Fernandes <hilaire$ext,cri74,org>

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Interactive educational geometry software
Name: drgeo
Version: 1.1.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://ofset.sourceforge.net/drgeo/

Source: http://dl.sf.net/ofset/drgeo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex, bison, gmp-devel >= 2.0.2, glib-devel, gtk+-devel
BuildRequires: guile-devel, gnome-libs-devel, gob >= 1.0.10
BuildRequires: perl-XML-Parser, intltool, gcc-c++, gtk2-devel, libglade2-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

Obsoletes: drgenius

%description
Dr. Geo is a interactive geometry GUI application. It allows one to create
geometric figure plus the interactive manipulation of such figure in
respect with their geometric constraints. It is useable in teaching
situation with students from primary or secondary level.

%prep
%setup

### FIXME: Include improved desktop-file. (Please fix upstream)
%{__cat} <<EOF >drgeo.desktop.in
[Desktop Entry]
Name=Dr.Geo Math Tool
Comment=Learn geometry interactively
Exec=drgeo
Icon=drgeo.png
Type=Application
Terminal=false
Encoding=UTF-8
StartupNotify=true
Categories=GNOME;Application;Game;Math;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -Dp -m0644 glade/drgeo.png %{buildroot}%{_datadir}/pixmaps/drgeo.png

%if %{?!_without_freedesktop:1}0
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --delete-original             \
		--vendor %{desktop_vendor}                 \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{buildroot}%{_datadir}/applications/drgeo.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
#%doc %{_datadir}/gnome/help/*
%{_bindir}/drgeo
%{_datadir}/drgeo/
%{_datadir}/pixmaps/*.png
%{_datadir}/texmacs/TeXmacs/plugins/drgeo/
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-drgeo.desktop}
%{?_without_freedesktop:%{_datadir}/applications/drgeo.desktop}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.0-1.2
- Rebuild for Fedora Core 5.

* Sun Mar 06 2005 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 0.9.14-1
- Updated to release 0.9.14.

* Tue Jun 08 2004 Dag Wieers <dag@wieers.com> - 0.9.13-1
- Updated to release 0.9.13.

* Sun Jun 06 2004 Dag Wieers <dag@wieers.com> - 0.9.12-1
- Add improved desktop file.

* Sun Jan 31 2004 Dag Wieers <dag@wieers.com> - 0.9.12-0
- Updated to release 0.9.12.

* Fri Oct 24 2003 Dag Wieers <dag@wieers.com> - 0.9.10-0
- Updated to release 0.9.10.

* Tue Sep 23 2003 Dag Wieers <dag@wieers.com> - 0.9.9-0
- Updated to release 0.9.9.

* Sun Sep 07 2003 Dag Wieers <dag@wieers.com> - 0.9.8-0
- Updated to release 0.9.8.

* Wed Aug 13 2003 Dag Wieers <dag@wieers.com> - 0.9.7-0
- Package renamed to drgeo.
- Updated to release 0.9.7.

* Sun Mar 16 2003 Dag Wieers <dag@wieers.com> - 0.8.4-0
- Updated to release 0.8.4.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 0.8.3-0
- Updated to release 0.8.3.

* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 0.7.2-0
- Initial package. (using DAR)
