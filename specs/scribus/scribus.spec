# $Id$

# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: A GUI desktop publishing (DTP) application.
Name: scribus
Version: 1.0.1
Release: 0
License: GPL
Group: Applications/Productivity
URL: http://web2.altmuehlnet.de/fschmid/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://web2.altmuehlnet.de/fschmid/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: qt-devel >= 3.0, XFree86-devel
BuildRequires: zlib-devel, libjpeg-devel, libpng-devel, libtiff-devel

%description
Scribus is a GUI desktop publishing (DTP) application for GNU/Linux.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Scribus Desktop Publishing
Comment=%{summary}
Exec=scribus
Icon=scribus.png
Type=Application
Terminal=false
Categories=Application;Office;
EOF

%build
%{?rhfc1:export QTDIR="/usr/lib/qt-3.1"}
%{?rhel3:export QTDIR="/usr/lib/qt-3.1"}
%{?rh90:export QTDIR="/usr/lib/qt3"}
%{?rh80:export QTDIR="/usr/lib/qt3"}
%{?rh73:export QTDIR="/usr/lib/qt2"}
%{?rhel21:export QTDIR="/usr/lib/qt2"}
%{?rh62:export QTDIR="/usr/lib/qt-2.1.0"}
%configure \
	--disable-dependency-tracking \
	--with-xinerama
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/pixmaps/
%{__install} -m0644 scribus/icons/scribusicon.png %{buildroot}%{_datadir}/pixmaps/scribus.png

%if %{dfi}
        %{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Applications/
        %{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Applications/
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor kde                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{name}.desktop
%endif

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/scribus/{libs,plugins}/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/*
%{_libdir}/scribus/
%{_includedir}/scribus/
%{_datadir}/pixmaps/*
%if %{dfi}
        %{_datadir}/gnome/apps/Applications/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Tue Aug 12 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Updated to release 1.0.1.

* Wed Jul 16 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
