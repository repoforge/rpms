# $Id: $

# Authority: dries
# Upstream: 

Summary: Gui for lvemkdvd
Name: klvemkdvd
Version: 0.4
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://lvempeg.sourceforge.net/klvemkdvd.html

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/lvempeg/klvemkdvd-%{version}.src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel, libart_lgpl-devel, arts-devel, gcc-c++, gettext, XFree86-devel, zlib-devel, qt-devel, libjpeg-devel, kdelibs-devel
Requires: lve, dvd+rw-tools, dvdauthor

%description
klvemkdvd is able to build (and burn) DVD filesystems from 
various mpeg media files using lve tools and some other 
programs. 

the main intention of klvemkdvd is to build DVDs from 
project files (edit lists) created with lve editor. 
But it can use other kind of mpegs (VOB, TS, PS, PVA, ...)
as input also.

At all it's a GUI replacement for the command line tool
lvemkdvd (much easier to handle) and is a extension to the
lve package.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/*
%{_datadir}/applnk/Utilities/klvemkdvd.desktop
%{_datadir}/apps/klvemkdvd/klvemkdvdui.rc
%{_datadir}/doc/HTML/en/klvemkdvd
%{_datadir}/icons/*/*/apps/klvemkdvd.png

%changelog
* Tue Jun 1 2004 Dries Verachtert <dries@ulyssis.org> - 0.4-1
- Initial package.
