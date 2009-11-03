# $Id$
# Authority: dries
# Upstream: Tom Deblauwe <tom,deblauwe$pandora,be>

# Screenshot: http://ksubtile.sourceforge.net/images/ksubtile.png
# ScreenshotURL: http://ksubtile.sourceforge.net/

%define real_version 1.0-1

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Program for editing subtitles in the SRT format
Name: ksubtile
Version: 1.0.1
Release: 3%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://ksubtile.sourceforge.net/

Source: http://dl.sf.net/ksubtile/ksubtile_%{real_version}.tar.bz2
Patch: gcc4-fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++
BuildRequires: qt-devel, fam-devel
%{?el4:BuildRequires:libselinux-devel}
%{?fc3:BuildRequires:libselinux-devel}
%{?fc2:BuildRequires:libselinux-devel}
Requires: kdelibs


%description
With this editor, you can edit, make and save subtitles
in the SRT subtitle format.

%prep
%setup -n ksubtile-1.0
%patch -p1

%build
source /etc/profile.d/qt.sh
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
for i in $(find . -type f | egrep '\.ui'); do sed -i 's/version="3.2"/version="3.1"/g;' $i; done
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /etc/profile.d/qt.sh
%makeinstall
mkdir -p %{buildroot}/usr/share/applications
mv %{buildroot}/usr/share/applnk/Editors/ksubtile.desktop %{buildroot}/usr/share/applications/ksubtile.desktop
echo "Categories=Application;AudioVideo;X-Red-Hat-Extra;" >> %{buildroot}/usr/share/applications/ksubtile.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README TODO
%{_bindir}/ksubtile
%{_bindir}/ksubtile_client
%{_datadir}/applications/ksubtile.desktop
%{_datadir}/apps/ksubtile/ksubtileui.rc
%{_datadir}/doc/HTML/en/ksubtile
%{_datadir}/icons/*/*/apps/ksubtile.png
%{_datadir}/mimelnk/application/srt.desktop

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.1-3
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Mon Mar 1 2004 Dries Verachtert <dries@ulyssis.org> 1.0.1-2
- cleanup of spec file
- little patch so it compiles with qt 3.1

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 1.0.1-4
- first packaging for Fedora Core 1
