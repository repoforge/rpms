# $Id$
# Authority: dag

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: Graphical Download manager using wget
Name: gwget
Version: 0.14
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://gwget.sourceforge.net/

Source: http://dl.sf.net/gwget/gwget-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Buildrequires: libgnomeui-devel, libglade-devel, gtk2-devel >= 2.4
Buildrequires: gnome-vfs2-devel, automake, autoconf
BuildRequires: perl-XML-Parser, intltool, gettext
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: wget

%description
Gwget is a Download Manager for Gnome 2. It uses wget as a backend.
Currently, very basic wget options are available, supporting multiple
downloads, drag&drop and display the errors from wget process.

%prep
%setup

%{__cat} <<EOF >gwget.desktop.in
[Desktop Entry]
Name=Download Manager
Comment=Download files from the Internet
Exec=gwget
Icon=gwget.png
Terminal=false
MultipleArgs=false
Type=Application
Categories=Application;Network;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -Dp -m0644 pixmaps/gwget.png %{buildroot}%{_datadir}/pixmaps/gwget.png

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 gwget.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/gwget.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome \
		--dir %{buildroot}%{_datadir}/applications  \
		--add-category X-Red-Hat-Base \
		gwget.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/gwget
%exclude %{_datadir}/applications/gwget.desktop
%{?_without_freedesktop:%{_datadir}/gnome/apps/Internet/gwget.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/gnome-gwget.desktop}
%{_datadir}/gwget/
%{_datadir}/pixmaps/gwget.png
%exclude %{_includedir}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1.2
- Rebuild for Fedora Core 5.

* Sat Aug 25 2004 Dag Wieers <dag@wieers.com> - 0.14-1
- Initial package. (using DAR)
