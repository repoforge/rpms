# $Id$

# Authority: dag

Summary: Tool to magnify parts of your screen
Name: peeper
Version: 0.3
Release: 0
License: GPL
Group: Applications/System
URL: http://peeper.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/peeper/peeper-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: XFree86-devel, libgnomeui-devel

%description
Peeper is a program to view an area of the screen at a certain
magnification. It has the ability to magnify animations, and
view the screen at different levels of magnification. It is
designed to support many widget sets and graphics backends.

%prep
%setup

cat <<EOF >gnome-%{name}.desktop
[Desktop Entry]
Name=Gv4l
Comment=%{summary}
Icon=gv4l/gv4l.png
Exec=%{name}
Terminal=false
Type=Application
EOF

%build
#configure
%{__make} %{?_smp_mflags} gnome

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
desktop-file-install --vendor gnome                \
	--add-category X-Red-Hat-Base              \
	--add-category Application                 \
	--add-category AudioVideo                  \
	--dir %{buildroot}%{_datadir}/applications \
	gnome-%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop

%changelog
* Sun Aug 03 2003 Dag Wieers <dag@wieers.com> - 0.3-0
- Initial package. (using DAR)
