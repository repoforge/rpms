# Authority: dag

# Upstream: 

Summary: Advanced TV program.
Name: fftv
Version: 0.6.4
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://fftv.sourceforge.net/fftv.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/fftv/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: a52dec-devel, faad2-devel, faac-devel, libvorbis-devel, tcron-devel

%description
fftv is an advanced TV iviewing and recording program.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=FFTV Television Viewer
Comment=Advanced television viewing program.
Icon=fftv.png
Exec=fftv
Terminal=false
Type=Application
Categories=Application;AudioVideo;
EOF

%build
%configure \
	--disable-mmx \
	--enable-mp3lame \
	--enable-vorbis \
	--enable-a52 \
	--enable-faad \
	--enable-faac \
	--enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
desktop-file-install --vendor gnome                \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop

%changelog
* Thu Jan 15 2004 Dag Wieers <dag@wieers.com> - 0.6.4-0
- Initial package. (using DAR)
