# $Id:$
# Authority: hadams

Name:           mugshot
Version:        1.1.58
Release:        1%{?dist}
Summary:        Companion software for mugshot.org

Group:          Applications/Internet
License:        GPL
URL:            http://mugshot.org/
Source0:        http://developer.mugshot.org/download/sources/linux/mugshot-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Patching:
#
# If you add any patches to this RPM, change the define below to something like:
#
# %%define about_message "Adapted for ExampleLinux".
#
# If, however, the patches alter the user experience in significant ways or change
# the default server that the client connects to, you must remove the Mugshot
# trademarks from the source code.
#
# See http://mugshot.org/trademark for full details.
#
%define about_message ""

BuildRequires:  glib2-devel >= 2.6
BuildRequires:  gtk2-devel >= 2.6
BuildRequires:  loudmouth-devel >= 1.0.3-3
BuildRequires:  dbus-devel >= 0.61
BuildRequires:  dbus-glib-devel >= 0.61 
BuildRequires:  curl-devel >= 7.15
BuildRequires:  GConf2-devel >= 2.8
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libjpeg-devel >= 6b
BuildRequires:  pcre-devel >= 6.3
BuildRequires:  gnome-desktop-devel >= 2.10.0
BuildRequires:  gnome-vfs2-devel
BuildRequires:  firefox-devel >= 1.5.0.4
BuildRequires:  desktop-file-utils
BuildRequires:  sqlite-devel >= 3.0.0

# 1.0.3-3 has a backport from 1.0.4 to fix various segfaults
Requires:       loudmouth >= 1.0.3-3

Requires(pre): GConf2
Requires(preun): GConf2
Requires(post): GConf2
Requires(post): gtk2


%description
Mugshot works with the server at mugshot.org to extend 
the panel, web browser, music player and other parts of the desktop with 
a "live social experience" and interoperation with online services you and 
your friends use. It's fun and easy.

%package devel
Summary: Development headers for Online Desktop
Group: Development/Languages
Requires: dbus-devel

%description devel
This package contains libraries for Online Desktop.

%prep
%setup -q

%build
%configure --with-about-message=%{about_message}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

# Don't package a .la file for the component .so
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

# Run desktop-file-install to so we get validation (and to make
# things fedora-packaging-guidelines compliant)
desktop-file-install 					\
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications 	\
  --vendor=mugshot   					\
  mugshot.desktop
desktop-file-install 					\
  --dir=$RPM_BUILD_ROOT%{_datadir}/gnome/autostart 	\
  --vendor=mugshot   					\
  mugshot-autostart.desktop

%clean
rm -rf $RPM_BUILD_ROOT

# Annoyingly, firefox installs itself into versioned directories,
# so we have to make a new symlink into the right directory when
# firefox is installed or upgraded. But we would rather not leave
# our old symlinks behind, since that will cause the firefox
# directories not to be removed. (flash-player leaves its old
# symlinks behind, but that's no excuse for us to do the same...)
#
# Because I don't know any way of finding out what the new version
# is on installation or old version on uninstallation, we have
# to do things in a somewhat non-intuitive way
#
# The order on upgrade of firefox is:
#
#  1. new package installed
#  2. triggerin for new package - we add all symlinks
#  3. triggerun for old package - we remove all symlinks
#  4. old package uninstalled
#  5. triggerpostun for old package - we add all symlinks
#
# Triggers are also run on self-upgrade, in that case we do:
#
#  1. new package installed
#  2. triggerin for new package - we add all symlinks
#  3. triggerun for old package - we remove all symlinks
#  4. old package uninstalled
#  5. postun for old package - we add all symlinks
#  6. triggerpostun for old package - NOT RUN (contrary to RPM docs)

%pre
# On upgrade, remove old schemas before installing the new ones
# Note that the SCHEMAS value should be the name of any schema
# files installed by *previous* versions of this package
if [ $1 -gt 1 ] ; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    SCHEMAS="mugshot-uri-handler.schemas"

    for S in $SCHEMAS; do
        gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/$S > /dev/null || :
    done

    # Necessary for FC5/FC6 only because of 
    #  https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=214214
    killall -q -HUP gconfd-2 || :
fi

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
SCHEMAS="mugshot-uri-handler.schemas"

for S in $SCHEMAS; do
    gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/$S > /dev/null || :
done

touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi
%{_datadir}/mugshot/firefox-update.sh install

killall -q -HUP gconfd-2 || :

echo %{version} > %{_datadir}/mugshot/version

%preun
# On removal (but not upgrade), remove our schemas
if [ $1 = 0 ] ; then
    %{_datadir}/mugshot/firefox-update.sh remove

    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    SCHEMAS="mugshot-uri-handler.schemas"

    for S in $SCHEMAS; do
        gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/$S > /dev/null || :
    done

    killall -q -HUP gconfd-2 || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi
# This is needed not to reverse the effect of our preun, which
# is guarded against upgrade, but because of our triggerun,
# which is run on self-upgrade, though triggerpostun isn't
if [ "$1" != 0 ] ; then
  test -x %{_datadir}/mugshot/firefox-update.sh && %{_datadir}/mugshot/firefox-update.sh install
fi

%triggerin -- firefox
%{_datadir}/mugshot/firefox-update.sh install

%triggerun -- firefox
%{_datadir}/mugshot/firefox-update.sh remove

%triggerpostun -- firefox
# Guard against being run post-self-uninstall, even though that
# doesn't happen currently (see comment above)
if [ "$1" != 0 ] ; then
  test -x %{_datadir}/mugshot/firefox-update.sh && %{_datadir}/mugshot/firefox-update.sh install
fi

%files
%defattr(-,root,root,-)
%doc LICENSE

%{_bindir}/mugshot
%{_bindir}/mugshot-uri-handler
%{_datadir}/icons/hicolor/16x16/apps/*.png
%{_datadir}/icons/hicolor/22x22/apps/*.png
%{_datadir}/icons/hicolor/24x24/apps/*.png
%{_datadir}/icons/hicolor/32x32/apps/*.png
%{_datadir}/icons/hicolor/48x48/apps/*.png
%{_datadir}/icons/hicolor/64x64/apps/*.png
%{_datadir}/icons/hicolor/128x128/apps/*.png
%{_datadir}/mugshot
%ghost %{_datadir}/mugshot/version
%{_libdir}/mugshot
%{_libdir}/*.so.*
%{_datadir}/dbus-1/services/*.service
%{_datadir}/applications/mugshot.desktop
%{_datadir}/gnome/autostart/mugshot-autostart.desktop
%{_sysconfdir}/gconf/schemas/*.schemas

%files devel
%dir %{_includedir}/ddm-1
%{_includedir}/ddm-1/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
* Sun Jan 27 2008 Heiko Adams <info-2007@fedora-blog.de> - 1.1.58-1
- 1.1.58

* Sat Oct 19 2007 Heiko Adams <info@fedora-blog.de> - 1.1.56-1
- 1.1.56

* Sun Jul 29 2007 Heiko Adams <info@fedora-blog.de> - 1.1.48-1
- 1.1.48

* Sat Jul 14 2007 Heiko Adams <info@fedora-blog.de> - 1.1.45-2
- rebuild for rpmforge

* Tue Jun 19 2007 Owen Taylor <otaylor@redhat.com> - 1.1.45-1
- 1.1.45

* Fri Jun 15 2007 Owen Taylor <otaylor@redhat.com> - 1.1.44-1
- 1.1.44 (fix crash when Pidgin not running)

* Fri Jun 15 2007 Owen Taylor <otaylor@redhat.com> - 1.1.43-1
- 1.1.43

* Thu Apr 26 2007 Owen Taylor <otaylor@redhat.com> - 1.1.42-2
- 1.1.42

* Wed Apr 25 2007 Owen Taylor <otaylor@redhat.com> - 1.1.41-2
- Package the D-BUS service file

* Wed Apr 25 2007 Owen Taylor <otaylor@redhat.com> - 1.1.41-1
- 1.1.41

* Thu Mar 29 2007 Owen Taylor <otaylor@redhat.com> - 1.1.40-1
- 1.1.40

* Mon Mar 26 2007 Owen Taylor <otaylor@redhat.com> - 1.1.39-3
- Fix some minor 64-bit problems

* Mon Mar 26 2007 Owen Taylor <otaylor@fresnel.dumbhippo.com> - 1.1.39-1
- 1.1.39
- Package mugshot.desktop for the menus as well

* Fri Mar 23 2007 Owen Taylor <otaylor@fresnel.dumbhippo.com> - 1.1.38-1
- Create %%{_datadir}/mugshot/version at the end of %%post to avoid
  the client prematurely prompting to restart itself

* Mon Mar 19 2007 Owen Taylor <otaylor@redhat.com> - 1.1.38-1
- Don't package the .la file for libhippofirefox
- Use desktop-file-install to validate mugshot.spec and make
  the Fedora packaging guidelines happy

* Thu Mar 15 2007 Owen Taylor <otaylor@fresnel.dumbhippo.com> - 1.1.38-1
- Add coments about trademark requirements
- 1.1.38

* Thu Mar  1 2007 Owen Taylor <otaylor@redhat.com> - 1.1.37-1
- 1.1.37

* Thu Mar  1 2007 Owen Taylor <otaylor@redhat.com> - 1.1.36-1
- 1.1.36

* Wed Feb 28 2007 Owen Taylor <otaylor@redhat.com> - 1.1.35-1
- 1.1.35

* Fri Feb 16 2007 Owen Taylor <otaylor@redhat.com> - 1.1.34-1
- 1.1.34

* Fri Feb  9 2007 Owen Taylor <otaylor@redhat.com> - 1.1.33-1
- 1.1.33

* Thu Feb  1 2007 Owen Taylor <otaylor@redhat.com> - 1.1.32-1
- Version 1.1.32

* Tue Dec 19 2006 Owen Taylor <otaylor@redhat.com> - 1.1.30-1
- 1.1.30

* Fri Dec  8 2006 Owen Taylor <otaylor@redhat.com> - 1.1.29-1
- 1.1.29

* Wed Dec  6 2006 Owen Taylor <otaylor@redhat.com> - 1.1.28-1
- 1.1.28

* Wed Dec  6 2006 Owen Taylor <otaylor@redhat.com> - 1.1.27-1
- 1.1.27

* Thu Nov 30 2006 Owen Taylor <otaylor@redhat.com> - 1.1.26-1
- 1.1.26

* Tue Nov 21 2006 Owen Taylor <otaylor@redhat.com> - 1.1.25-1
- 1.1.25

* Wed Nov  8 2006 Owen Taylor <otaylor@redhat.com> - 1.1.24-1
- 1.1.24

* Mon Nov  6 2006 Owen Taylor <otaylor@redhat.com> - 1.1.23-2
- On upgrade/removal clean up GConf schemas

* Wed Nov  1 2006 Owen Taylor <otaylor@redhat.com> - 1.1.23-1
- 1.1.23

* Wed Oct 25 2006 Owen Taylor <otaylor@redhat.com> - 1.1.21-1
- 1.1.21

* Mon Oct 22 2006 Owen Taylor <otaylor@redhat.com> - 1.1.20-1
- Make work with fc6
- 1.1.20

* Mon Oct 16 2006 Havoc Pennington <hp@redhat.com> - 1.1.18-1
- 1.1.18

* Sat Oct 14 2006 Havoc Pennington <hp@redhat.com> - 1.1.17-1
- 1.1.17

* Sat Sep 26 2006 Owen Taylor <otaylor@redhat.com> - 1.1.16-1
- Fix triggers/scriptlets to work right on upgrades

* Sat Aug 19 2006 Owen Taylor <otaylor@redhat.com> - 1.1.12-1
- Add firefox extension

* Wed Jul 19 2006 Colin Walters <walters@redhat.com> - 1.1.11-1
- 1.1.11

* Wed Jul 19 2006 Colin Walters <walters@redhat.com> - 1.1.10-1
- 1.1.10

* Sat Jul 15 2006 Havoc Pennington <hp@redhat.com> - 1.1.9-1
- 1.1.9

* Thu Jul 13 2006 Havoc Pennington <hp@redhat.com> - 1.1.8-1
- 1.1.8

* Tue Jul 11 2006 Havoc Pennington <hp@redhat.com> - 1.1.7-1
- 1.1.7

* Wed Jun 28 2006 Havoc Pennington <hp@redhat.com> - 1.1.6-1
- 1.1.6

* Fri Jun  9 2006 Havoc Pennington <hp@redhat.com> - 1.1.5-1
- 1.1.5

* Mon May 29 2006 Havoc Pennington <hp@redhat.com> - 1.1.3-1
- 1.1.3

* Sat May 27 2006 Havoc Pennington <hp@redhat.com> - 1.1.2-2
- add requirement on patched loudmouth

* Fri May 26 2006 Havoc Pennington <hp@redhat.com> - 1.1.2-1
- 1.1.2

* Mon May 22 2006 Havoc Pennington <hp@redhat.com> - 1.1.1-1
- 1.1.1

* Mon May 22 2006 Havoc Pennington <hp@redhat.com> - 1.1.0-1
- Initial package

