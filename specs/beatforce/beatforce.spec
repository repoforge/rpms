# $Id$
# Authority: dag
# Upstream: Patrick Prasse <patrick,prasse$gmx,net>

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

Summary: Computer DJing system
Name: beatforce
Version: 0.2.0
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.beatforce.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.beatforce.org/files/beatforce-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext
BuildRequires: gnome-libs-devel, libxml-devel, vrb-devel
BuildRequires: libmad-devel, libid3tag-devel, fftw-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

Obsoletes: BeatForce

%description
Beatforce is a computer dj-ing system with 2 players, a XML-based song
database, a mixer with manual and auto-fade and some more features.

%prep
%setup -n %{name}

### FIXME: Make it build with vrb 0.4.0. (Fix upstream please)
%{__perl} -pi.orig -e 's|^(\s+vrb)(\s+vrb_buf;)|$1_p$2|;' src/ringbuffer.h

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Beat Force DJ System
Comment=Mix beats and sounds realtime
Exec=beatforce
Type=Application
Terminal=false
Categories=Application;AudioVideo;
Encoding=UTF-8
EOF

%build
%configure \
	--with-plugin-dir="%{_libdir}/beatforce" \
	--with-theme-dir="%{_datadir}/beatforce"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#makeinstall 
%{__make} DESTDIR="%{buildroot}" install \
	THEME_DIR="%{buildroot}%{_datadir}/beatforce"

%if %{?_without_freedesktop:1}0
        %{__install} -D -m0644 beatforce.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/beatforce.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		beatforce.desktop
%endif

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/beatforce/*.a

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS QuickStart README TODO
%{_bindir}/beatforce
%{_libdir}/beatforce/
%{_datadir}/beatforce/
%{!?_without_freedesktop:%{_datadir}/applications/gnome-beatforce.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/beatforce.desktop}

%changelog
* Mon Aug 02 2004 Dag Wieers <dag@wieers.com> - 0.2.0-1
- Updated to release 0.2.0.

* Tue Sep 02 2003 Dag Wieers <dag@wieers.com> - 0.1.5-0
- Initial package. (using DAR)
