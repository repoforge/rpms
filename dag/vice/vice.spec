# Authority: newrpms

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: VICE, the Versatile Commodore Emulator.
Name: vice
Version: 1.11
Release: 1
License: GPL
Group: Applications/Emulators
URL: http://viceteam.bei.t-online.de/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.funet.fi/pub/cbm/crossplatform/emulators/VICE/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
VICE is a set of accurate emulators for the Commodore 64, 128, VIC20,
PET and CBM-II 8-bit computers, all of which run under the X Window
System.

%prep
%setup

%build
#CFLAGS="%{optflags} -DNO_REGPARM" %configure
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

cat <<EOF >gnome-%{name}.desktop
[Desktop Entry]
Name=Vice (c64)
Type=Application
Comment=%{summary}
Exec=x64
#Icon=%{name}.xpm
Terminal=false
EOF

%if %{dfi}
	%{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Utilities/
	%{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--add-category Application                 \
		--add-category Utility                     \
		--dir %{buildroot}%{_datadir}/applications \
		gnome-%{name}.desktop
%endif

### Clean up buildroot
%{__rm} -f %{buildroot}%{_infodir}/dir

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

%preun
/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS FEEDBACK INSTALL README
%doc %{_mandir}/man1/*
%doc %{_infodir}/*
%{_bindir}/*
%{_libdir}/vice/
%if %{dfi}
	%{_datadir}/gnome/apps/Utilities/*.desktop
%else
	%{_datadir}/applications/*.desktop
%endif

%Changelog
* Fri Apr 18 2003 Dag Wieers <dag@wieers.com> - 1.11-0
- Initial package. (using DAR)
