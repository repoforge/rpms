# Authority: dag

Summary: A GNOME Type1 font editor.
Name: gribouy
Version: 0.0.8
Release: 0
License: GPL
Group: Applications/System
URL: http://www.nongnu.org/gribouy/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://savannah.nongnu.org/download/gribouy/unstable.pkg/0.0/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
Gribouy is a GNOME Type1 font editor.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Gribouy Font Editor
Comment=A Type1 font editor
Icon=gribouy.png
Exec=%{name}
Terminal=false
Type=Application
Categories=Graphics;Application;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/ \
			%{buildroot}%{_datadir}/pixmaps/
desktop-file-install --vendor gnome                \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%{__install} -m0755 graphics/gribouy.png %{buildroot}%{_datadir}/pixmaps/

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/gribouy/
%{_datadir}/pixmaps/*

%changelog
* Sat Nov 22 2003 Dag Wieers <dag@wieers.com> - 0.0.8-0
- Updated to release 0.0.8.

* Sat Sep 27 2003 Dag Wieers <dag@wieers.com> - 0.0.7-0
- Updated to release 0.0.7.

* Fri Aug 01 2003 Dag Wieers <dag@wieers.com> - 0.0.6-0
- Updated to release 0.0.6.

* Wed Jul 30 2003 Dag Wieers <dag@wieers.com> - 0.0.5-0
- Updated to release 0.0.5.

* Wed Jul 02 2003 Dag Wieers <dag@wieers.com> - 0.0.4-0
- Updated to release 0.0.4.

* Sun Jun 14 2003 Dag Wieers <dag@wieers.com> - 0.0.3-0
- Initial package. (using DAR)
