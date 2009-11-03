# $Id$
# Authority: dag
# Upstream: Jeffrey Stedfast <fejj$ximian,com>

%define desktop_vendor rpmforge

Summary: Graphical front-end to the Valgrind memory checker for x86
Name: alleyoop
Version: 0.8.2
Release: 1.2%{?dist}
License: GPL
Group: Development/Tools
URL: http://alleyoop.sourceforge.net/

Source: http://dl.sf.net/alleyoop/alleyoop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: valgrind >= 1.9.0, glib2 >= 2.2, pango-devel >= 1.2, gtk2-devel >= 2.2
BuildRequires: GConf2-devel >= 2.2, libgnome-devel >= 2.2, libgnomeui-devel >= 2.2, gettext
Requires: valgrind >= 1.9.0

%description
Alleyoop is a graphical front-end to the increasingly popular Valgrind
memory checker for x86 GNU/ Linux using the Gtk+ widget set and other
GNOME libraries for the X-Windows environment.

Features include a right-click context menu to intelligently suppress
errors or launch an editor on the source file/jumping to the exact
line of the error condition. A searchbar at the top of the viewer can
be used to limit the viewable errors to those that match the regex
criteria entered. Also included is a fully functional Suppressions
editor.

%prep
%setup

%{__cat} <<EOF >alleyoop.desktop
[Desktop Entry]
Name=Memory Checker
Comment=Validate the memory usage of any program
Icon=gnome-devel.png
Exec=alleyoop
Terminal=false
Type=Application
Categories=GNOME;Application;Development;
StartupNotify=true
EOF

%build
%configure \
	--disable-install-schemas
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	alleyoop.desktop

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q

%postun
scrollkeeper-update -q

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%config %{_sysconfdir}/gconf/schemas/alleyoop.schemas
%{_bindir}/alleyoop
%{_datadir}/applications/%{desktop_vendor}-alleyoop.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.2-1.2
- Rebuild for Fedora Core 5.

* Sun Apr 04 2004 Dag Wieers <dag@wieers.com> - 0.8.2-1
- Updated to release 0.8.2.

* Wed Oct 22 2003 Dag Wieers <dag@wieers.com> - 0.8.0-0
- Updated to release 0.8.0.

* Mon Jun 02 2003 Dag Wieers <dag@wieers.com> - 0.7.3-0
- Updated to release 0.7.3.

* Thu May 22 2003 Dag Wieers <dag@wieers.com> - 0.7.2-0
- Updated to release 0.7.2.

* Mon Apr 28 2003 Dag Wieers <dag@wieers.com> - 0.7.1-0
- Updated to release 0.7.1.

* Wed Apr 23 2003 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Build against new valgrind 1.9.5 package.

* Wed Apr 23 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Initial package. (using DAR)
