# $Id$
# Authority: dag
# Upstream: Mark McLoughlin <mark$skynet,ie>

# ExcludeDist: el4

Summary: Network interface status applet
Name: gnome-netstatus
Version: 2.6.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://ftp.gnome.org/pub/GNOME/sources/gnome-netstatus/

Source: http://ftp.gnome.org/pub/GNOME/sources/gnome-netstatus/2.6/gnome-netstatus-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.4, libgnomeui-devel >= 2.6
BuildRequires: libglade2-devel >= 2.0, gettext
BuildRequires: gnome-panel-devel >= 2.6, gcc-c++
BuildRequires: intltool, perl(XML::Parser)

%description
gnome-netstatus is a network interface status applet.

%prep
%setup

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

for lang in C de es fr it ja ko sv zh_CN zh_HK zh_TW; do
	for file in %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/*.png; do
		%{__ln_s} -f $(echo $file | sed -e 's|%{buildroot}||') %{buildroot}%{_datadir}/gnome/help/gnome-netstatus/$lang/figures/
	done
done

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
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_datadir}/gnome/help/gnome-netstatus/
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_libdir}/bonobo/servers/*.server
%{_libexecdir}/*
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/gnome-netstatus/
%{_datadir}/icons/hicolor/48x48/apps/*.png
%{_datadir}/pixmaps/*
%{_datadir}/omf/gnome-netstatus/
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.6.2-1.2
- Rebuild for Fedora Core 5.

* Sat Jun 26 2004 Dag Wieers <dag@wieers.com> -  2.6.2-1
- Updated to release 2.6.2.

* Fri May 21 2004 Dag Wieers <dag@wieers.com> -  2.6.1-1
- Updated to release 2.6.1.

* Tue Feb 17 2004 Dag Wieers <dag@wieers.com> -  0.16-0
- Updated to release 0.16.

* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> -  0.14-0
- Updated to release 0.14.

* Thu Jan 15 2004 Dag Wieers <dag@wieers.com> -  0.13-0
- Updated to release 0.13.

* Thu Jan 08 2004 Dag Wieers <dag@wieers.com> -  0.12-0
- Updated to release 0.12.

* Sun Jul 13 2003 Dag Wieers <dag@wieers.com> -  0.11-0
- Updated to release 0.11.

* Thu Jun 12 2003 Dag Wieers <dag@wieers.com> -  0.10-0
- Updated to release 0.10.

* Wed Jun 11 2003 Dag Wieers <dag@wieers.com> -  0.9-0
- Initial package. (using DAR)
