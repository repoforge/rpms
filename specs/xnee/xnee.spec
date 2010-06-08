# $Id$
# Authority: dries
# Upstream: Henrik Sandklef

%define desktop_vendor rpmforge

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: Record, distribute and replay X protocol data
Name: xnee
Version: 3.06
Release: 1%{?dist}
License: GPL
Group: User Interface/X
URL: http://www.gnu.org/software/xnee/

Source: http://ftp.gnu.org/gnu/xnee/xnee-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ImageMagick
BuildRequires: desktop-file-utils
BuildRequires: ghostscript
BuildRequires: gtk2-devel
BuildRequires: tetex
BuildRequires: texinfo
%{!?_without_modxorg:BuildRequires: libXtst-devel}

%description
Xnee can record, distribute, and replay X (X11) protocol data. This is
useful for automated tests of applications or benchmarking of applications.
Think of it as a robot.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=xnee
Comment=Record, distribute and replay X protocol data
Exec=gnee
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;AudioVideo;
EOF

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
    --add-category X-Red-Hat-Base              \
    --dir %{buildroot}%{_datadir}/applications \
    xnee.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FAQ INSTALL NEWS README TODO
#%doc %{_infodir}/cnee.info*
%doc %{_mandir}/man1/cnee.1*
%doc %{_mandir}/man1/gnee.1*
%doc %{_mandir}/man1/pnee.1*
%doc %{_mandir}/man1/xnee.1*
%{_bindir}/cnee
%{_bindir}/gnee
%{_libdir}/bonobo/servers/pnee.server
%{_libdir}/gnome-panel/pnee
%{_libdir}/libtestcb.a
%{_libdir}/libtestcb.la
%{_datadir}/applications/%{desktop_vendor}-xnee.desktop
%{_datadir}/pixmaps/xnee.png
%{_datadir}/pixmaps/xnee.xpm
%{_datadir}/xnee/

%changelog
* Tue Jun 01 2010 Dag Wieers <dag@wieers.com> - 3.06-1
- Updated to release 3.06.

* Mon Jun 25 2007 Dag Wieers <dag@wieers.com> - 2.06-1
- Updated to release 2.06.

* Sun Aug 06 2006 Dag Wieers <dag@wieers.com> - 2.05-1
- Updated to release 2.05.

* Sun Mar 19 2006 Dries Verachtert <dries@ulyssis.org> - 2.04-2
- Some missing buildrequirements added.

* Tue Feb 28 2006 Dries Verachtert <dries@ulyssis.org> - 2.04-1
- Updated to release 2.04.

* Tue Jan 03 2006 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Initial package.
