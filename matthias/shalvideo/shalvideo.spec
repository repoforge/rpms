# $Id$
# Authority: dries

%define real_version 1.3-pre1
%define dir_version  1.3-1

Summary: A TV record sheduling program
Name: shalvideo
Version: 1.3
Release: 0.1.pre1
License: GPL
Group: Applications/Multimedia
URL: http://shalvideo.sourceforge.net/
Source: http://dl.sf.net/shalvideo/shalvideo-%{real_version}.tar.bz2
Patch: shalvideo-1.2.1-no-default-values-in-cpp-files.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: mplayer, at
BuildRequires: XFree86-devel, qt-devel, kdelibs-devel, arts-devel, gcc-c++
BuildRequires: libjpeg-devel, libpng-devel, zlib-devel
BuildRequires: gettext, libart_lgpl-devel

#(d) primscreenshot: http://shalvideo.sourceforge.net/screenshot1.png
#(d) screenshotsurl: http://shalvideo.sourceforge.net/

%description
shalvideo allows you to program the TV recording feature of your computer
just like a video recorder. Just set the channel, quality, and start and end
times, and it uses mplayer and atd for the encoding and timing processes.


%prep
%setup -n %{name}-%{dir_version}


%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf ${RPM_BUILD_ROOT}
%makeinstall
%find_lang %{name}


%clean
%{__rm} -rf ${RPM_BUILD_ROOT}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING FAQ README INSTALL TODO
%{_bindir}/shalvideo
%{_datadir}/applications/shalvideo.desktop
%{_datadir}/icons/locolor/32x32/apps/kvideo.png
%{_datadir}/shalvideo


%changelog
* Wed Mar 17 2004 Matthias Saou <http://freshrpms.net/> 1.3-0.1.pre1
- Update to 1.3-pre1.

* Thu Mar  4 2004 Matthias Saou <http://freshrpms.net/> 1.2-0.1.pre1
- Update to 1.2-pre1.
- Removed obsolete patch.
- Updated patch with Dries' new one.

* Sun Feb  1 2004 Dries Verachtert <dries@ulyssis.org> 1.1.1-1
- first packaging for Fedora Core 1

