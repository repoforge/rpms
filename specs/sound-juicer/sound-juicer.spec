# $Id$
# Authority: dag
# Upstream: Ross Burton <ross$burtonini,com>

# ExcludeDist: fc3 el4


Summary: Clean and lean CD ripper
Name: sound-juicer
Version: 0.5.15
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.burtonini.com/blog/computers/sound-juicer/

Source: http://www.burtonini.com/computing/sound-juicer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libmusicbrainz-devel >= 2.0.1, libgnomeui-devel >= 2.0.0
BuildRequires: glib2-devel >= 2.0.0, gstreamer-devel >= 0.6.1
BuildRequires: GConf2-devel >= 2.0.0
BuildRequires: scrollkeeper
BuildRequires: intltool, perl(XML::Parser)

Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
GStreamer-based CD ripping tool. Saves audio CDs to ogg/vorbis, flac or wav.

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

desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--dir %{buildroot}%{_datadir}/applications    \
	%{buildroot}%{_datadir}/applications/sound-juicer.desktop

%clean
%{__rm} -rf %{buildroot}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_datadir}/gnome/help/sound-juicer/
%{_bindir}/sound-juicer
%{_sysconfdir}/gconf/schemas/sound-juicer.schemas
%{_datadir}/sound-juicer/
%{_datadir}/applications/gnome-sound-juicer.desktop
%{_datadir}/pixmaps/sound-juicer.png
%{_datadir}/omf/sound-juicer/
%exclude %{_localstatedir}/scrollkeeper

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.15-1.2
- Rebuild for Fedora Core 5.

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 0.5.15-1
- Updated to release 0.5.15.

* Mon May 03 2004 Dag Wieers <dag@wieers.com> - 0.5.11-1
- Updated to release 0.5.11.

* Fri Feb 13 2004 Dag Wieers <dag@wieers.com> - 0.5.10.1-0
- Updated to release 0.5.10.1.
- Updated to release 0.5.9.

* Mon Dec 01 2003 Dag Wieers <dag@wieers.com> - 0.5.8-0
- Updated to release 0.5.8.

* Sun Oct 19 2003 Dag Wieers <dag@wieers.com> - 0.5.5-0
- Updated to release 0.5.5.

* Fri Sep 12 2003 Dag Wieers <dag@wieers.com> - 0.5.2-0
- Updated to release 0.5.2.

* Fri May 02 2003 Dag Wieers <dag@wieers.com> - 0.2.1-0
- Initial package. (using DAR)
