# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Last.fm track scrobbler
Name: last.fm
Version: 1.4.0.56102
Release: 1%{?dist}
Group: Applications/Multimedia
License: GPL
URL: http://www.last.fm/download/

Source: http://cdn.last.fm/client/src/last.fm-%{version}.src.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt4-devel >= 4.3, alsa-lib-devel
BuildRequires: desktop-file-utils

%description
Last.fm is the flagship product from the team that designed the
Audioscrobbler music engine. More than ten million times a day,
Last.fm users "scrobble" their tracks to our servers, helping to
collectively build the world's largest social music platform.

Last.fm taps the wisdom of the crowds, leveraging each user's musical
profile to make personalised recommendations, connect users who share
similar tastes, provide custom radio streams, and much more.

%prep
%setup

%{__cat} <<EOF >last.fm.desktop
[Desktop Entry]
Version=1.0
Type=Application
Name=Last.fm client
Comment=Scrobbles played music tracks and tunes to Last.fm radio stations
TryExec=last.fm
Exec=last.fm
Icon=last.fm
Terminal=false
Categories=Qt;AudioVideo;Audio;
EOF

%{__cat} <<EOF >last.fm.sh
#!/bin/sh
cd %{_libdir}/last.fm/
exec ./last.fm
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -dp -m0755 %{buildroot}%{_libdir}/last.fm/
%{__cp} -av bin/* %{buildroot}%{_libdir}/last.fm/

#%{__install} -Dp -m0755 bin/last.fm %{buildroot}%{_bindir}/last.fm
%{__install} -Dp -m0755 last.fm.sh %{buildroot}%{_bindir}/last.fm

%{__install} -Dp -m0644 bin/data/icons/as.png %{buildroot}%{_datadir}/pixmaps/last.fm.png

%{__mkdir_p} %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications  \
    last.fm.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING ChangeLog README
%{_bindir}/last.fm
%{_datadir}/applications/last.fm.desktop
%{_datadir}/applications/%{desktop_vendor}-last.fm.desktop
%{_libdir}/last.fm/

%changelog
* Mon Jan 28 2008 Dag Wieers <dag@wieers.com> - 1.4.0.56102-1
- Initial package. (using DAR)
