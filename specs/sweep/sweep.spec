# $Id$
# Authority: dag
# Conrad Parker <conrad@vergenet.net>

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: Sound wave editor
Name: sweep
Version: 0.8.3
Release: 2
License: GPL
Group: Applications/Multimedia
URL: http://sweep.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/sweep/sweep-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libsndfile-devel >= 1.0.1, libmad-devel
BuildRequires: gtk+-devel >= 1.2.0, libvorbis-devel, speex-devel

%description
Sweep is an editor for sound samples. It operates on files of various
formats such as .wav, .aiff and .au, and has multiple undo/redo levels
and filters. It supports audio filter plugins from the LADSPA project.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

### FIXME: Include improved desktop-file. (Please fix upstream)
%{__cat} <<EOF >sweep.desktop
[Desktop Entry]
Name=Sweep Sound Editor
Comment=Edit audio files
Icon=sweep.png
Exec=sweep
Terminal=false
Type=Application
Encoding=UTF-8
MimeType=audio/x-wav
Categories=GNOME;Application;AudioVideo;
EOF

%build
%configure \
	--libdir="%{_libdir}/sweep"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall libdir="%{buildroot}%{_libdir}/sweep"
%find_lang %{name}

%if %{!?_without_freedesktop:1}0
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome --delete-original \
		--add-category X-Red-Hat-Base                 \
		--dir %{buildroot}%{_datadir}/applications    \
		%{buildroot}%{_datadir}/gnome/apps/Multimedia/sweep.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog NEWS README* doc/*.txt
%doc %{_mandir}/man1/*
%{_bindir}/*
%dir %{_libdir}/sweep/
%{_libdir}/sweep/*.so
%{_datadir}/pixmaps/*
%{_datadir}/sweep/
%{!?_without_freedesktop:%{_datadir}/applications/gnome-sweep.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/sweep.desktop}

%files devel
%defattr(-, root, root, 0755)
%doc doc/plugin_writers_guide.txt
%{_includedir}/sweep/
%dir %{_libdir}/sweep/
%{_libdir}/sweep/*.a
%{_libdir}/sweep/*.la

%changelog
* Sat Jun 06 2004 Dag Wieers <dag@wieers.com> - 0.8.3-2
- Add improved desktop file.

* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 0.8.3-1
- Updated to release 0.8.3.

* Fri May 02 2003 Dag Wieers <dag@wieers.com> - 0.8.2-0
- Initial package. (using DAR)
