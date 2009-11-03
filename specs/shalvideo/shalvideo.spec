# $Id$
# Authority: dries
# Upstream: Raul Portales Fernandez <raulpor$olidformacion,com>

# Screenshot: http://shalvideo.sourceforge.net/screenshot1.png
# ScreenshotURL: http://shalvideo.sourceforge.net/

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define real_version 1.4-1
%define dir_name shalVideo-1.4-pre1

Summary: TV record sheduling program
Name: shalvideo
Version: 1.4.1
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://shalvideo.sourceforge.net/

Source: http://dl.sf.net/shalvideo/shalvideo-%{real_version}.tar.bz2
# Patch: no-default-vals-in-cpp-files.patch.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel, kdelibs-devel, gcc-c++
BuildRequires: qt-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
BuildRequires: automake15
Requires: mplayer, at

%description
shalvideo allows you to program the TV recording feature of your computer
just like a video recorder. Just set the channel, quality, and start and end
times, and it uses mplayer and atd for the encoding and timing processes.

%prep
%setup -n %{dir_name}
# %patch -p1

%{__cat} <<EOF >shalvideo.desktop
[Desktop Entry]
Name=Shalvideo
Comment=A video record programing application
Encoding=UTF-8
Type=Application
Exec=shalvideo -caption "%c" %i %m
Icon=shalvideo.png
DocPath=kvideo/index.html
Terminal=false
Categories=Application;AudioVideo;
EOF


%build
source /etc/profile.d/qt.sh
%{__mv} autom4te.cache junk.autom4te.cache
%{__aclocal}
%{__automake} -a
%{__autoconf}
%configure \
	--x-libraries="%{_prefix}/X11R6/%{_lib}" \
	CPPFLAGS=-I/usr/lib/qt-3.3/include
moc shalvideo/mixerdlg.h > shalvideo/mixerdlg.moc
moc shalvideo/shalvideobasic.h > shalvideo/shalvideobasic.moc
moc shalvideo/kprogramrecords.h > shalvideo/kprogramrecords.moc
moc shalvideo/kvideoapp.h > shalvideo/kvideoapp.moc
uic shalvideo/advanced.ui > shalvideo/advanced.h
moc shalvideo/kvideodlg2.h > shalvideo/kvideodlg2.moc
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 shalvideo.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/shalvideo.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor kde --delete-original \
		--dir %{buildroot}%{_datadir}/applications  \
		--add-category X-Red-Hat-Base               \
		shalvideo.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING FAQ INSTALL README TODO
%{_bindir}/shalvideo
%{_datadir}/icons/locolor/32x32/apps/shalvideo.png
%{_datadir}/pixmaps/shalvideo.png
%{_datadir}/shalvideo/
%{!?_without_freedesktop:%{_datadir}/applications/kde-shalvideo.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/shalvideo.desktop}


%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.4.1-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Wed Jul 28 2004 Dries Verachtert <dries@ulyssis.org> - 1.4.1-1
- Update to version 1.4.1.

* Fri Jun 25 2004 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Cosmetic cleanup.

* Sun Feb 1 2004 Dries Verachtert <dries@ulyssis.org> 1.1.1-1
- first packaging for Fedora Core 1
