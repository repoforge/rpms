# $Id: $

# Authority: dries
# Upstream: 

Summary: File manager
Name: krusader
Version: 1.30
Release: 1
License: GPL
Group: User Interface/Desktops
URL: http://krusader.sourceforge.net/home.php

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/krusader/krusader-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel, libart_lgpl-devel, arts-devel, gcc-c++, gettext, XFree86-devel, zlib-devel, qt-devel, libjpeg-devel, kdelibs-devel
%{?fc2:BuildRequires: libselinux-devel}

# Screenshot: http://krusader.sourceforge.net/img/scr01.png
# ScreenshotURL: http://krusader.sourceforge.net/scr.php

%description
Krusader is an advanced twin-panel (commander-style) file-manager for KDE
3.x (similar to Midnight or Total Commander) but with many extras. It
provides all the file-management features you could possibly want.
 Plus: extensive archive handling, mounted filesystem support, FTP, advanced
search module, viewer/editor, directory synchronisation, file content
comparisons, powerful batch renaming and much much more.
 It supports the following archive formats: tar, zip, bzip2, gzip, rar, ace,
arj and rpm and can handle other KIOSlaves such as smb:// or fish://
 It is (almost) completely customizable, very user friendly, fast and looks
great on your desktop! :-) 

%prep
%setup

%build
export KDEDIR=/usr
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export KDEDIR=/usr
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/applnk/Applications/krusader.desktop
%{_datadir}/icons/*/*/apps/krusader*.png
%{_datadir}/apps/krusader
%{_datadir}/mimelnk/application/x-ace.desktop
%{_datadir}/locale/*/LC_MESSAGES/krusader.mo
%{_datadir}/doc/HTML/en/krusader
%{_datadir}/services/krarc.protocol
%{_libdir}/kde3/kio_krarc.*

%changelog
* Thu Jun 3 2004 Dries Verachtert <dries@ulyssis.org> - 1.30-1
- Initial package.
