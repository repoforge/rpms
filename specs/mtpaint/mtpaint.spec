# $Id$
# Authority: dries
# Upstream:  Mark Tyler <marktyler_5$hotmail,com>

Summary: Painting program for creating icons and pixel-based artwork
Name: mtpaint
Version: 2.20
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://mtpaint.sourceforge.net/

Source: http://dl.sf.net/mtpaint/mtpaint-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel, libpng-devel
BuildRequires: libungif-devel, libjpeg-devel, libtiff-devel
BuildRequires: desktop-file-utils, gettext

%description
mtPaint is a simple GTK+1/2 painting program designed for creating icons 
and pixel-based artwork. It can edit indexed palette or 24 bit RGB images 
and offers basic painting and palette manipulation tools. Its main file 
format is PNG, although it can also handle JPEG, GIF, TIFF, BMP, XPM, and 
XBM files.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Mtpaint
Comment=Painting program
Exec=mtpaint
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;Graphics;Viewer;
EOF

%build
%configure gtk2 tiff jpeg gif man
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall BIN_INSTALL=%{buildroot}%{_bindir} MT_MAN_DEST=%{buildroot}%{_mandir}/man1

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING NEWS README
%doc %{_mandir}/man1/mtpaint*
%{_bindir}/mtpaint
%{_datadir}/applications/*.desktop

%changelog
* Sun Jan 01 2006 Dries Verachtert <dries@ulyssis.org> - 2.20-1
- Updated to release 2.20.

* Mon Nov 21 2005 Dries Verachtert <dries@ulyssis.org> - 2.10-1
- Updated to release 2.10.

* Sat Sep 24 2005 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Updated to release 2.03.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Initial package.
