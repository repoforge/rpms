# $Id: $

# Authority: dries
# Upstream: Tom Deblauwe <tom.deblauwe@pandora.be>

Summary: Program for editing subtitles in the SRT format
Name: ksubtile
Version: 1.0.1
%define real_version 1.0-1
Release: 2
License: GPL
Group: Applications/Multimedia
URL: http://ksubtile.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/ksubtile/ksubtile_%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel
Requires: kdelibs

# Screenshot: http://ksubtile.sourceforge.net/images/ksubtile.png
# ScreenshotURL: http://ksubtile.sourceforge.net/

%description
With this editor, you can edit, make and save subtitles
in the SRT subtitle format.

%prep
%setup -n ksubtile-1.0

%build
. /etc/profile.d/qt.sh
%configure
for i in $(find . -type f | egrep '\.ui'); do sed -i 's/version="3.2"/version="3.1"/g;' $i; done
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
%makeinstall
mkdir -p %{buildroot}/usr/share/applications
mv %{buildroot}/usr/share/applnk/Editors/ksubtile.desktop %{buildroot}/usr/share/applications/ksubtile.desktop
echo "Categories=Application;AudioVideo;X-Red-Hat-Extra;" >> %{buildroot}/usr/share/applications/ksubtile.desktop

%files
%defattr(-,root,root,0755)
%doc README AUTHORS COPYING TODO
%{_bindir}/ksubtile
%{_bindir}/ksubtile_client
%{_datadir}/applications/ksubtile.desktop
%{_datadir}/apps/ksubtile/ksubtileui.rc
%{_datadir}/doc/HTML/en/ksubtile
%{_datadir}/icons/*/*/apps/ksubtile.png
%{_datadir}/mimelnk/application/srt.desktop

%changelog
* Mon Mar 1 2004 Dries Verachtert <dries@ulyssis.org> 1.0.1-2
- cleanup of spec file
- little patch so it compiles with qt 3.1

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 1.0.1-4
- first packaging for Fedora Core 1
