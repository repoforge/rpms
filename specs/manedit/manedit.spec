# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Graphical editor for creating man pages.
Name: manedit
Version: 0.6.1
Release: 1.2%{?dist}
License: GPL
Group: Development/Tools
URL: http://wolfpack.twu.net/ManEdit/

Source: http://wolfpack.twu.net/users/wolfpack/manedit-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel, zlib-devel, gcc-c++, bzip2-devel
Requires: groff

%description
ManEdit is a UNIX Manual Page Integrated Development Environment.
It has full UNIX manual page editing capabilities using an XML
interface with instant preview. ManEdit uses the GTK+ widget set
and requires the X Window Systems.

%prep
%setup

%{__perl} -pi.orig -e 's|/usr/man|%{_mandir}|g' manedit/pref.c manedit/prefcb.c
%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' pconf/platforms.ini

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Manpage Editor
Comment=Create and edit UNIX manual pages
Exec=manedit
Icon=manedit.xpm
Terminal=false
Type=Application
Categories=GNOME;Application;Development;
EOF

%build
./configure Linux \
	--prefix="%{_prefix}" \
	--mandir="%{_mandir}" \
	--libdir="%{_libdir}" \
	--disable="arch-i486" \
	--disable="arch-i586" \
	--disable="arch-i686" \
	--disable="arch-pentiumpro"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	PREFIX="%{buildroot}%{_prefix}" \
	MAN_DIR="%{buildroot}%{_mandir}/man1"

%{__install} -Dp -m0644 manedit/manedit.xpm %{buildroot}%{_datadir}/pixmaps/manedit.xpm

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS LICENSE README
%doc %{_mandir}/man?/*
%{_bindir}/man*
%{_datadir}/manedit/
%{_datadir}/icons/*
%{_datadir}/pixmaps/*.xpm
%{_datadir}/applications/%{desktop_vendor}-manedit.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.1-1.2
- Rebuild for Fedora Core 5.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.1-1
- Updated to release 0.6.1.

* Sat Nov 20 2004 Dag Wieers <dag@wieers.com> - 0.5.12-1
- Updated to release 0.5.12.

* Sun Oct 05 2003 Dag Wieers <dag@wieers.com> - 0.5.10-0
- Initial package. (using DAR)
