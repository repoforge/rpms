# Authority: freshrpms
# Upstream: Colin Walters <walters@verbum.org>

Summary: Music management application.
Name: rhythmbox
Version: 0.6.5
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://www.rhythmbox.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.rhythmbox.org/downloads/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gstreamer-devel >= 0.6, gstreamer-plugins-devel >= 0.6
BuildRequires: gtk2-devel >= 2.2.0, libgnomeui-devel >= 2.2.0
BuildRequires: flac-devel, libvorbis-devel, libmusicbrainz-devel >= 2.0.0, libid3tag-devel
#BuildRequires: scrollkeeper

#Requires(post): scrollkeeper
Requires: gstreamer-plugins >= 0.6

Obsoletes: net-rhythmbox <= 0.4.8

%description
Music management application with support for ripping audio-cd's,
playback of Ogg Vorbis and Mp3 and burning of cdroms.

%prep
%setup

%build
%configure \
	--disable-dependency-tracking \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

#desktop-file-install --vendor gnome --delete-original \
#	--add-category X-Red-Hat-Base                 \
#	--dir %{buildroot}%{_datadir}/applications    \
#	%{buildroot}%{_datadir}/applications/*.desktop

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/bonobo/*.a \
		%{buildroot}%{_libdir}/bonobo/*.la

### FIXME: scrollkeeper files are bogus. (please fix upstream)
%{__rm} -rf %{buildroot}%{_datadir}/omf/rhythmbox/

%post 
/sbin/ldconfig
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
#scrollkeeper-update -q || :

%postun
/sbin/ldconfig
#scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING DOCUMENTERS MAINTAINERS NEWS README THANKS TODO
%doc %{_datadir}/gnome/help/rhythmbox/
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_libdir}/bonobo/*.so
%{_libdir}/bonobo/servers/*.server
%{_libdir}/pkgconfig/*.pc
%{_datadir}/application-registry/*
%{_datadir}/applications/*.desktop
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/idl/*.idl
%{_datadir}/mime-info/*.keys
#{_datadir}/omf/rhythmbox/
%{_datadir}/pixmaps/*.png
%{_datadir}/rhythmbox/

%changelog
* Thu Jan 22 2004 Dag Wieers <dag@wieers.com> - 0.6.5-0
- Updated to release 0.6.5.

* Sat Jan 10 2004 Dag Wieers <dag@wieers.com> - 0.6.4-0
- Updated to release 0.6.4.

* Mon Dec 22 2003 Dag Wieers <dag@wieers.com> - 0.6.3-0
- Updated to release 0.6.3.

* Thu Dec 18 2003 Dag Wieers <dag@wieers.com> - 0.6.2-0
- Updated to release 0.6.2.

* Sat Nov 22 2003 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Updated to release 0.6.1.

* Tue Nov 18 2003 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Disable scrollkeeper in %%post.

* Tue Nov 11 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Updated to release 0.6.0.

* Tue Oct 28 2003 Dag Wieers <dag@wieers.com> - 0.5.4-0
- Updated to release 0.5.4.

* Sun Sep 07 2003 Dag Wieers <dag@wieers.com> - 0.5.3-0
- Updated to release 0.5.3.

* Wed Aug 27 2003 Dag Wieers <dag@wieers.com> - 0.5.2-0
- Updated to release 0.5.2.

* Mon Aug 18 2003 Dag Wieers <dag@wieers.com> - 0.5.1-0
- Updated to release 0.5.1.

* Sun Aug 17 2003 Dag Wieers <dag@wieers.com> - 0.5.0-0
- Renamed to rhythmbox.
- Updated to release 0.5.0.

* Fri May 09 2003 Dag Wieers <dag@wieers.com> - 0.4.8-0
- Initial package. (using DAR)
