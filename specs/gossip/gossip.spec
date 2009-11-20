# $Id$
# Authority: shuff
# ExcludeDist el3 el4

%define with_dbus 1

Name:           gossip
Version:        0.26
Release:        2%{?dist}
Summary:        Gnome Jabber Client

Group:          Applications/Communications
License:        GPL
URL:		http://www.imendio.com/projects/gossip/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	glib2-devel >= 2.12.0
BuildRequires:	loudmouth-devel >= 1.4.1
BuildRequires:	libgnomeui-devel
BuildRequires:	libxml2-devel >= 2.6.16
BuildRequires:	libxslt-devel
BuildRequires:	libXScrnSaver-devel
BuildRequires:	libXt-devel
BuildRequires:	xorg-x11-proto-devel
BuildRequires:	libnotify-devel
BuildRequires:	desktop-file-utils
BuildRequires:	aspell-devel
BuildRequires:	gettext
BuildRequires:  scrollkeeper
BuildRequires:	iso-codes-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig >= 0.16


%if %{with_dbus}
BuildRequires:	dbus-devel >= 0.60
%endif

Requires(pre): GConf2
Requires(post):	GConf2
Requires(post): scrollkeeper
Requires(preun): GConf2
Requires(postun): scrollkeeper

%description
Gossip aims at making Jabber easy to use and tries to give GNOME users a
real user friendly way of chatting with their friends.


%prep
%setup

%build
%configure --disable-scrollkeeper	\
	--disable-schemas-install	\
	--with-backend=gnome		\
	--enable-libnotify=yes		\
%if %{with_dbus}
	--enable-dbus=yes
%else
	--enable-dbus=no
%endif

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

desktop-file-install --vendor fedora --delete-original	\
  --dir $RPM_BUILD_ROOT%{_datadir}/applications   	\
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :
fi


%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
  %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
fi


%postun
scrollkeeper-update -q || :
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README NEWS
%{_bindir}/%{name}
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_sysconfdir}/sound/events/%{name}.soundlist
%{_datadir}/applications/fedora-%{name}.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}/
%{_datadir}/sounds/%{name}/
%{_datadir}/omf/%{name}/
%{_datadir}/gnome/help/%{name}/
%if %{with_dbus} 
%{_libexecdir}/*
%{_libdir}/bonobo/servers/*
%endif


%changelog
* Fri Nov 20 2009 Steve Huff <shuff@vecna.org> - 0.26-2
- Caught a few more missing dependencies, now it builds on el5.

* Wed Nov 21 2007 Heiko Adams <info@fedora-blog.de> - 0.26-1
- Update to 0.26
- rebuild for rpmforge

* Sun Jan 14 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.22-1
- Update to 0.22.
- Drop message focus patch.  Fixed upstream.

* Tue Jan  9 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.21-2
- Add patch to fix new message focus bug. (#221926)

* Sat Jan  6 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.21-1
- Update to 0.21.

* Fri Dec  8 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.20-1
- Update to 0.20.

* Sun Nov 19 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.19-1
- Update to 0.19.
- Remove X-Fedora category from desktop file.

* Mon Oct 16 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.18-1
- Update to 0.18.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.17-2
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sun Sep 24 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.17-1
- Update to 0.17.
- Drop ChangeLog, since NEWS file is already packaged.

* Sat Sep 16 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.16-1
- Update to 0.16.

* Wed Aug 30 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.15-4
- Update for FC6.

* Fri Aug 25 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.15-3
- Add BR on perl(XML::Parser).

* Fri Aug 25 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.15-2
- Update to 0.15.
- Use disable-schemas configure flag.

* Fri Aug  4 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.14-3
- Update to 0.14.
- Change dbus requirement to 0.60.
- Drop dbus crash patch, fixed upstream.

* Thu Aug  3 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.13-3
- Update to 0.13.
- Add patch to fix dbus crash.
- Minor changes to files section.

* Wed Jul 26 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.12-3
- Update to 0.12.
- Hold off from building peekaboo applet until it's more stable.

* Sat Jul 22 2006 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.11.2-4
- Rebuild because of dbus soname change (#199794).

* Sun Jun 11 2006 Brian Pepple <bdpepple@ameritech.net> - 0.11.2-3
- Update to 0.11.2.

* Mon May 29 2006 Brian Pepple <bdpepple@ameritech.net> - 0.11.1-3
- Update to 0.11.1.

* Sat May 20 2006 Brian Pepple <bdpepple@ameritech.net> - 0.11-4
- Build with libnotify support.

* Mon May  1 2006 Brian Pepple <bdpepple@ameritech.net> - 0.11-3
- Update to 0.11.
- Add scriptlets for gtk+ icon cache.
- Add icons to files.

* Sat Mar 18 2006 Brian Pepple <bdpepple@ameritech.net> - 0.10.2-3
- Update to 0.10.2.
- Add BR for iso-codes-devel & gnome-doc-utils.

* Sat Feb 25 2006 Brian Pepple <bdpepple@ameritech.net> - 0.10.1-2
- Bump to make upgrade path.

* Sat Feb 25 2006 Brian Pepple <bdpepple@ameritech.net> - 0.10.1-1
- Update to 0.10.1.
- Drop kill gconfd-2 call in scriptlets.

* Sat Feb 18 2006 Brian Pepple <bdpepple@ameritech.net> - 0.10-2
- Update to 0.10.
- Add help files.
- Add scriptlets & BR for scrollkeeper.

* Thu Feb 16 2006 Brian Pepple <bdpepple@ameritech.net> - 0.9-10
- Remove unnecessary BR (libxml2-devel, libglade2-devel, GConf2-devel,
  gnome-vfs2-devel, libgcrypt-devel).

* Mon Feb 13 2006 Brian Pepple <bdpepple@ameritech.net> - 0.9-9
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Dec 26 2005 Brian Pepple <bdpepple@ameritech.net> - 0.9-8
- Rebuild for new loudmouth.

* Mon Dec  5 2005 Brian Pepple <bdpepple@ameritech.net> - 0.9-7
- Add BR for libXScrnSaver-devel, libXt-devel & xorg-x11-proto-devel.

* Fri Dec  2 2005 Brian Pepple <bdpepple@ameritech.net> - 0.9-6
- Rebuild for new dbus.

* Wed Aug 31 2005 Brian Pepple <bdpepple@ameritech.net> - 0.9-5
- Add missing COPYING file to docs.

* Tue Aug 16 2005 Brian Pepple <bdpepple@ameritech.net> - 0.9-4
- Rebuild for cairo dep.

* Sun Aug 14 2005 Brian Pepple <bdpepple@ameritech.net> - 0.9-3
- Add aspell-devel BR, so spell-checking is enabled.

* Sun Aug 14 2005 Brian Pepple <bdpepple@ameritech.net> - 0.9-2
- Remove dbus patch.
- Add version for loudmouth & dbus deps.
- Change location of wav files.
- Add soundlist & dtd to files.
- Update to 0.9.

* Mon May 23 2005 Brian Pepple <bdpepple@ameritech.net> - 0.8-5
- Add patch to fix dbus support, and build.

* Fri May 13 2005 Brian Pepple <bdpepple@ameritech.net> - 0.8-4
- Add dist tag.

* Fri May  6 2005 Brian Pepple <bdpepple@ameritech.net> - 0.8-3
- Add ownership for unclaimed directories.
- Disable dbus support due to api changes, and since it is experimental in Gossip anyway.

* Sun May  1 2005 Brian Pepple <bdpepple@ameritech.net> - 0.8-2
- Actually package the protocols.

* Sun May  1 2005 Brian Pepple <bdpepple@ameritech.net> - 0.8-1
- Initial Fedora build.

