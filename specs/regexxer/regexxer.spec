# $Id$
# Authority: dag
# Upstream: Daniel Elstner <daniel.elstner@gmx.net>

Summary: Graphical search/replace tool featuring Perl-style regular expressions
Name: regexxer
Version: 0.8
Release: 1
License: GPL
Group: Applications/Text
URL: http://regexxer.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/regexxer/regexxer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.0.7, gtk2-devel >= 2.0
BuildRequires: libsigc++-devel >= 1.2, gtkmm2-devel >= 2.0
BuildRequires: pcre >= 3.9

%description
regexxer is a nifty GUI search/replace tool featuring Perl-style
regular expressions.

%prep
%setup

%{__cat} <<EOF >regexxer.desktop
[Desktop Entry]
Name=Regular Expression Tool
Comment=Perform search and replace operations
Exec=regexxer
Icon=regexxer.png
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;Application;Development;
EOF

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--dir %{buildroot}%{_datadir}/applications    \
	regexxer.desktop

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/regexxer
%{_datadir}/applications/gnome-regexxer.desktop
%{_datadir}/pixmaps/regexxer.png

%changelog
* Fri Jul 09 2004 Dag Wieers <dag@wieers.com> - 0.8-1
- Updated to release 0.8.

* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 0.7-1
- Updated to release 0.7.

* Sun Dec 07 2003 Dag Wieers <dag@wieers.com> - 0.6-0
- Updated to release 0.6.

* Sun Nov 02 2003 Dag Wieers <dag@wieers.com> - 0.5-0
- Updated to release 0.5.

* Thu Jun 05 2003 Dag Wieers <dag@wieers.com> - 0.4-1
- Added docs.

* Thu Apr 03 2003 Dag Wieers <dag@wieers.com> - 0.4-0
- Initial package. (using DAR)
