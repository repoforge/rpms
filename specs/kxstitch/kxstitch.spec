# $Id: $

# Authority: dries
# Upstream: 
# Screenshot: http://kxstitch.sourceforge.net/image/mainview.png
# ScreenshotURL: http://kxstitch.sourceforge.net/screenshots.shtml

Summary: Cross stitch patterns editor
Name: kxstitch
Version: 0.5
Release: 1
License: GPL
Group: Amusements/Graphics
URL: http://kxstitch.sourceforge.net/index.shtml

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/kxstitch/kxstitch-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel, libart_lgpl-devel, arts-devel 
BuildRequires: gcc-c++, gettext, XFree86-devel, zlib-devel
BuildRequires: qt-devel, libjpeg-devel, kdelibs-devel
BuildRequires: ImageMagick-c++-devel

%description
KXStitch allows the creation and editing of cross stitch patterns. 

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_bindir}/*
%{_datadir}/apps/kxstitch
%{_datadir}/applnk/Graphics/kxstitch.desktop
%{_datadir}/icons/*/*/apps/kxstitch.png
%{_datadir}/locale/*/LC_MESSAGES/kxstitch.mo
%{_datadir}/doc/HTML/en/kxstitch

%changelog
* Fri Jun 11 2004 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Initial package.
