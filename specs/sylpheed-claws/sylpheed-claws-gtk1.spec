# $Id$
# Authority: matthias

%define desktop_vendor rpmforge
#define extraver

Summary: DEVELOPMENT branch of the sylpheed e-mail client
Name: sylpheed-claws
Version: 1.0.5
Release: 1%{?extraver:.%{extraver}}%{?dist}
License: GPL
Group: Applications/Internet
URL: http://claws.sylpheed.org/
Source: http://dl.sf.net/sylpheed-claws/sylpheed-claws-%{version}%{?extraver}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gtk+ >= 1.2.6, gdk-pixbuf >= 0.8.0
%{!?_without_aspell:Requires: aspell >= 0.50}
%{?_with_pilot:Requires: pilot-link}
BuildRequires: gtk+-devel >= 1.2.6, gdk-pixbuf-devel >= 0.8.0
BuildRequires: flex, pkgconfig, gcc-c++
BuildRequires: openssl-devel, gpgme03-devel >= 0.3.10, openldap-devel
BuildRequires: compface-devel, startup-notification-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{!?_without_aspell:BuildRequires: aspell-devel >= 0.50}
%{?_with_pilot:BuildRequires: pilot-link-devel}
Conflicts: sylpheed

%description
Sylpheed is an e-mail client (and news reader) based on GTK+, running on
X Window System, and aiming for quick responses, a graceful and
sophisticated interface, easy configuration, intuitive operation and
abundant features.
The appearance and interface are similar to some popular e-mail clients for
Windows, such as Outlook Express, Becky!, and Datula. The interface is also
designed to emulate the mailers on Emacsen, and almost all commands are
accessible with the keyboard.

This is the BLEEDING EDGE, DEVELOPMENT branch of sylpheed!
You have been warned ;-)

Available rpmbuild rebuild options :
--with : pilot
--without : aspell freedesktop


%prep
%setup -n %{name}-%{version}%{?extraver}


%build
# Workaround for missing krb5 includes (on RHL9 was it?)
if pkg-config openssl; then
    CFLAGS="%{optflags} `pkg-config --cflags openssl`"
    LDFLAGS="$LDFLAGS `pkg-config --libs-only-L openssl`"
fi

%configure \
    --program-prefix="%{?_program_prefix}" \
    --enable-openssl \
    --enable-ldap \
    %{!?_without_aspell: --enable-aspell} \
    %{?_with_pilot: --enable-jpilot} \
    --enable-spamassassin-plugin \
    --disable-mathml-viewer-plugin \
    --disable-clamav-plugin
%{__make} %{?_smp_mflags}

# Fix this path for the make install stage
%{__perl} -pi -e 's|gnomedatadir = .*|gnomedatadir = \$\(datadir\)|g' Makefile


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%if %{!?_without_freedesktop:1}0
# Convert the menu entry
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --delete-original \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    --add-category Application \
    --add-category Network \
    %{buildroot}%{_datadir}/gnome/apps/Internet/sylpheed.desktop
%endif


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog* README* TODO*
%{_bindir}/sylpheed
%{_includedir}/sylpheed-claws
%{_libdir}/pkgconfig/sylpheed-claws.pc
%dir %{_libdir}/sylpheed-claws
%dir %{_libdir}/sylpheed-claws/plugins
# Who needs the static lib for that!?
%exclude %{_libdir}/sylpheed-claws/plugins/*.a
%exclude %{_libdir}/sylpheed-claws/plugins/*.la
%{_libdir}/sylpheed-claws/plugins/*.so
%if %{!?_without_freedesktop:1}0
%{_datadir}/applications/%{desktop_vendor}-sylpheed.desktop
%else
%{_datadir}/gnome/apps/Internet/sylpheed.desktop
%endif
%{_datadir}/pixmaps/sylpheed.png
%{_datadir}/sylpheed-claws/
%{_mandir}/man1/sylpheed.1*


%changelog
* Mon Jul 11 2005 Matthias Saou <http://freshrpms.net/> 1.0.5-1
- Update to 1.0.5.

* Fri May 27 2005 Matthias Saou <http://freshrpms.net/> 1.0.4a-1
- Update to 1.0.4a.

* Wed Mar 30 2005 Matthias Saou <http://freshrpms.net/> 1.0.4-1
- Update to 1.0.4.

* Mon Mar 14 2005 Matthias Saou <http://freshrpms.net/> 1.0.3-1
- Update to 1.0.3.

* Mon Feb 28 2005 Matthias Saou <http://freshrpms.net/> 1.0.1-1
- Update to 1.0.1.

* Wed Jan 19 2005 Matthias Saou <http://freshrpms.net/> 1.0.0-1
- Update to 1.0.0.

* Thu Dec  9 2004 Matthias Saou <http://freshrpms.net/> 0.9.13-1
- Update to 0.9.13.

* Mon Sep 27 2004 Matthias Saou <http://freshrpms.net/> 0.9.12b-1
- Update to 0.9.12b.
- Re-enable LDAP support.

* Wed Jun 30 2004 Matthias Saou <http://freshrpms.net/> 0.9.12-1
- Update to 0.9.12.
- Changes from "sylpheed" to "sylpheed-claws" here and there to reflect
  upstream changes.

* Mon Jun  1 2004 Matthias Saou <http://freshrpms.net/> 0.9.11-1
- Update to 0.9.11claws.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.9.10-2
- Rebuilt for Fedora Core 2.

* Tue May 11 2004 Matthias Saou <http://freshrpms.net/> 0.9.10-1
- Added compface (X-Face) support.
- Left only aspell and pilot conditional builds.

* Mon Mar  8 2004 Matthias Saou <http://freshrpms.net/> 0.9.10-1
- Update to 0.9.10claws.

* Mon Feb  9 2004 Matthias Saou <http://freshrpms.net/> 0.9.9-1
- Update to 0.9.9claws.

* Sun Jan  4 2004 Matthias Saou <http://freshrpms.net/> 0.9.8-1
- Update to 0.9.8claws.

* Mon Dec  1 2003 Matthias Saou <http://freshrpms.net/> 0.9.7-1
- Update to 0.9.7claws.

* Thu Nov 13 2003 Matthias Saou <http://freshrpms.net/> 0.9.6-3
- Re-enabled aspell support by default.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.9.6-2
- Rebuild for Fedora Core 1.

* Fri Oct  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.6claws.
- Remove claws from the version as it's already in the name.
- Added stripping of plugins, to work with rpm 4.1.x.

* Sat Sep 13 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.5claws.
- Added include files and pkgconfig entry.

* Mon Aug  4 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.4claws.

* Sun Jul 13 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.3claws.

* Sat May 24 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0claws.
- Enable the image viewer, spamassassin and tray icon plugins by default.

* Mon May 12 2003 Matthias Saou <http://freshrpms.net/>
- Rebuild against Rawhide to enable spell checking again.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Added pkgconfig trick to workaround openssl/krb5 include problem.
- Update the gnomedir to gnomedatadir for the desktop entry.

* Wed Mar 12 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.11claws.

* Tue Mar  4 2003 Matthias Saou <http://freshrpms.net/>
- Disabled aspell by default as the version required is way too recent.

* Wed Feb 19 2003 Matthias Saou <http://freshrpms.net/>
- Fixed openssl support s/ssl/openssl/ thanks to Steffen Prohaska.

* Wed Feb 12 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.10claws.

* Fri Jan 24 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.9claws.

* Thu Jan  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.8claws.

* Mon Nov 25 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.6claws.

* Tue Oct  8 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.5claws.

* Sun Sep 29 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.

* Mon Sep 23 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.3claws.
- Added many "--without" options.
- Changed pspell to aspell, and disabled for now since >= 0.50 is needed.

* Tue Sep 10 2002 Matthias Saou <http://freshrpms.net/>
- Added "--with pilot" support to the rpm build.

* Wed Aug 28 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.2claws.

* Wed Jul 31 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.1claws.
- Added man page and the program-prefix to fix its name.

* Wed Jul 24 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.0claws.

* Mon Jun 17 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.8claws.
- Use %%find_lang.

* Mon May 20 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.6claws.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Sun Apr 28 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.5claws.

* Mon Apr 22 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.4claws97.

* Tue Apr 16 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.4claws81.

* Tue Mar 19 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.4claws23.

* Thu Mar 14 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.4claws7.

* Sat Feb 16 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.1claws7.

* Mon Feb 11 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.0claws57.

* Wed Jan 16 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.0claws5.
- Changed the package name to "sylpheed-claws" to avoid having the same
  name as the main branch, and thus solve problems with apt-get.

* Mon Jan 14 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.0claws.

* Tue Jan  1 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.6claws34.

* Mon Dec 17 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.6claws.

* Fri Nov 30 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.5claws46.

* Tue Nov 13 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.5claws8.

* Mon Nov 12 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.5claws7.
- Added LDAP support.

* Wed Nov  7 2001 Matthias Saou <http://freshrpms.net/>
- Got a bit impatient and updated to 0.6.5claws1 CVS version.

* Wed Oct 17 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.3claws.
- Addedd pspell support, libs are recent enough on Red Hat 7.2.

* Mon Oct  1 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.2claws.
- Added a quick build fix for the zh_TW.Big5 problem.
- Didn't add pspell support since version >= .12.2 is required and
  seawolf has only .11.2.

* Thu Sep 13 2001 Matthias Saou <http://freshrpms.net/>
- Start of the claws branch, I want to have fun too :-)

* Sun Sep  2 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.1.

* Thu Aug 30 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.0.

* Tue Aug 14 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.3.

* Wed Aug  1 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.2.

* Thu Jul  5 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.1 (previous 0.5preX wouldn't build).

* Tue Jun 19 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.99.

* Tue May  8 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.66.

* Tue May  1 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.65.

* Tue Apr 17 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.64.

* Tue Apr 10 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.63.

* Sat Feb  3 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.62.

* Sat Feb  3 2001 Matthias Saou <http://freshrpms.net/>
- General spec rewrite and rpm built for RedHat 7.0

* Sat Feb 3 2001 Yoichi Imai <yoichi@silver-forest.com>
- update to 0.4.61

* Sat Jan 1 2000 Yoichi Imai <yoichi@silver-forest.com>
- first release for version 0.1.0

