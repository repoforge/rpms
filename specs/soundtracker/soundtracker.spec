# $Id$
# Authority: dag
# Upstream: Michael Krause <rawstyle$soundtracker,org>
# Upstream: <soundtracker-discuss$lists,sourceforge,net>


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: Sound module player and composer
Name: soundtracker
Version: 0.6.8
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.soundtracker.org/

Source: http://www.soundtracker.org/dl/v0.6/soundtracker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel, gdk-pixbuf-devel, audiofile-devel, esound-devel
BuildRequires: libsndfile-devel, gettext, SDL-devel, gnome-libs-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Soundtracker is a module tracker similar to the DOS program `FastTracker'.
Soundtracker is based on the XM file format.

%prep
%setup

### FIXME: Disable chown and suid for local packaging. (Please fix upstream)
%{__perl} -pi.orig -e '
		s|(chown)|echo $1|g;
		s|(chmod \+s)|echo $1|g;
	' app/Makefile.in

%{__cat} <<EOF >soundtracker.desktop
[Desktop Entry]
Name=SoundTracker Module Tracker
Comment=Play and compose XM sound module files
Exec=soundtracker
Icon=gnome-multimedia.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=GNOME;Application;AudioVideo;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

### FIXME: Makefile doesn't create target directories (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_bindir}

%makeinstall
%find_lang %{name}


%if %{!?_without_freedesktop:1}0
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome --delete-original \
		--add-category X-Red-Hat-Base                 \
		--dir %{buildroot}%{_datadir}/applications    \
		%{buildroot}%{_datadir}/gnome/apps/Multimedia/soundtracker.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog* COPYING FAQ NEWS README TODO
%{_bindir}/*
%{_datadir}/soundtracker/
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/soundtracker.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/gnome-soundtracker.desktop}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.8-1.2
- Rebuild for Fedora Core 5.

* Tue Feb 28 2006 Dag Wieers <dag@wieers.com> - 0.6.8-1
- Updated to release 0.6.8.

* Wed Jan 14 2004 Dag Wieers <dag@wieers.com> - 0.6.7-1
- Initial package. (using DAR)
