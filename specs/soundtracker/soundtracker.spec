# $Id$

# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Sound module player and composer.
Name: soundtracker
Version: 0.6.7
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://www.soundtracker.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.soundtracker.org/dl/v0.6/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gtk+-devel, gdk-pixbuf-devel, audiofile-devel, esound-devel
BuildRequires: libsndfile-devel, gettext

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

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=SoundTracker Module Tracker
Comment=Sound module player and composer
Exec=soundtracker
Icon=gv4l/gv4l.png
Terminal=false
Type=Application
Categories=GNOME;Application;AudioVideo;
EOF

%build
%configure \
	--disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%makeinstall
%find_lang %{name}

### Clean up buildroot (before dfi)
%{__rm} -f %{buildroot}%{_datadir}/gnome/apps/Multimedia/*.desktop

%if %{dfi}
        %{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Multimedia/
        %{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog* COPYING FAQ NEWS README TODO
%{_bindir}/*
%{_datadir}/soundtracker/
%if %{dfi}
        %{_datadir}/gnome/apps/Multimedia/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Wed Jan 14 2004 Dag Wieers <dag@wieers.coM> - 0.6.7-0
- Initial package. (using DAR)
