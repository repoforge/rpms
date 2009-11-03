# $Id$
# Authority: matthias

%define desktop_vendor rpmforge

Summary: Full-featured GTK+ based fast e-mail client
Name: sylpheed
Version: 2.0.4
Release: 0%{?dist}
License: GPL
Group: Applications/Internet
URL: http://sylpheed.good-day.net/
Source: http://sylpheed.good-day.net/sylpheed/v2.0/sylpheed-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk2-devel >= 2.0.0, gdk-pixbuf-devel >= 0.8.0
BuildRequires: flex, gettext, desktop-file-utils, gcc-c++
BuildRequires: openssl-devel >= 0.9.6
%{!?_without_gpgme:BuildRequires: gpgme-devel >= 0.4.5}
%{!?_without_ldap:BuildRequires: openldap-devel}
%{!?_without_compface:BuildRequires: compface-devel}
%{?_with_pilot:BuildRequires: pilot-link-devel}

%description
Sylpheed is an e-mail client (and news reader) based on GTK+, running on
X Window System, and aiming for quick responses, a graceful and
sophisticated interface, easy configuration, intuitive operation and
abundant features.
The appearance and interface are similar to some popular e-mail clients for
Windows, such as Outlook Express, Becky!, and Datula. The interface is also
designed to emulate the mailers on Emacsen, and almost all commands are
accessible with the keyboard.

Available rpmbuild rebuild options :
--with : pilot
--without : gpgme, ldap, compface


%prep
%setup


%build
# Workaround for missing krb5 includes (on RHL9 was it?)
if pkg-config openssl; then
    CFLAGS="%{optflags} `pkg-config --cflags openssl`"
    LDFLAGS="$LDFLAGS `pkg-config --libs-only-L openssl`"
fi

%configure \
    --program-prefix="%{?_program_prefix}" \
    --enable-ssl \
    %{!?_without_gpgme: --enable-gpgme} \
    %{!?_without_ldap: --enable-ldap} \
    %{?_without_compface: --disable-compface} \
    %{?_with_pilot: --enable-jpilot}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}
%{__install} -Dp -m 0644 %{name}-64x64.png \
    %{buildroot}%{_datadir}/pixmaps/%{name}.png

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications  \
    --add-category Application                  \
    --add-category Network                      \
    %{name}.desktop


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog* COPYING README* TODO*
%{_bindir}/sylpheed
%{_datadir}/applications/%{desktop_vendor}-sylpheed.desktop
%{_datadir}/pixmaps/sylpheed.png
%{_datadir}/sylpheed/


%changelog
* Tue Nov  8 2005 Matthias Saou <http://freshrpms.net/> 2.0.4-0
- Update to 2.0.4.

* Wed Oct 19 2005 Matthias Saou <http://freshrpms.net/> 2.0.3-0
- Update to 2.0.3.

* Mon Oct 10 2005 Matthias Saou <http://freshrpms.net/> 2.0.2-0
- Update to 2.0.2.

* Tue Sep 13 2005 Matthias Saou <http://freshrpms.net/> 2.0.1-0
- Update to 2.0.1.

* Mon Jul 11 2005 Matthias Saou <http://freshrpms.net/> 1.0.5-0
- Update to 1.0.5.

* Tue Apr  5 2005 Matthias Saou <http://freshrpms.net/> 1.0.4-0
- Update to 1.0.4.

* Fri Mar  4 2005 Matthias Saou <http://freshrpms.net/> 1.0.3-0
- Update to 1.0.3.

* Tue Mar  1 2005 Matthias Saou <http://freshrpms.net/> 1.0.2-0
- Update to 1.0.2.
- Update gpgme dependency to gpgme >= 0.4.5.

* Mon Jan  3 2005 Matthias Saou <http://freshrpms.net/> 1.0.0-1
- Update to 1.0.0 final!
- Update gpgme dependency to gpgme03.

* Wed Oct 13 2004 Matthias Saou <http://freshrpms.net/> 0.9.99-1
- Update to 0.9.99.

* Thu Jun 17 2004 Matthias Saou <http://freshrpms.net/> 0.9.12-1
- Update to 0.9.12.
- Make ssl and ipv6 support defaults now.

* Tue Jun  1 2004 Matthias Saou <http://freshrpms.net/> 0.9.11-1
- Update to 0.9.11.

* Tue May 11 2004 Matthias Saou <http://freshrpms.net/> 0.9.10-1
- Added compface (X-Face) support.

* Sun Feb 29 2004 Matthias Saou <http://freshrpms.net/> 0.9.10-1
- Update to 0.9.10.

* Thu Jan 29 2004 Matthias Saou <http://freshrpms.net/> 0.9.9-1
- Update to 0.9.9.

* Mon Dec 15 2003 Matthias Saou <http://freshrpms.net/> 0.9.8a-1
- Update to 0.9.8a.

* Fri Dec 12 2003 Matthias Saou <http://freshrpms.net/> 0.9.8-1
- Update to 0.9.8.
- First rebuild for Fedora Core 1.

* Wed Oct 15 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.7.

* Wed Sep 17 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.6.

* Tue Sep  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.5.

* Fri Jul 25 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.4.

* Sat Jul  5 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.3.

* Wed Jun 11 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.2.

* Tue May 27 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.1.

* Fri May 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Added pkgconfig trick to workaround openssl/krb5 include problem.

* Fri Mar  7 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.11.

* Tue Feb  4 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.10.

* Fri Jan 17 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.9.

* Thu Jan  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.8.

* Fri Nov 15 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.6.
- Sync up the rebuild options with my claws build.
- Default to build in the LDAP support.

* Thu Oct  3 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.5.

* Tue Oct  1 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.4.

* Sun Sep 29 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.

* Wed Sep 18 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.3.

* Tue Aug 27 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.2.

* Thu Jul 25 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.1.

* Tue Jul 16 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.0.
- Changed the pixmap from the 48x48 to the 64x64 instead.

* Thu Jul 11 2002 Matthias Saou <http://freshrpms.net/>
- Added program prefix to configure to fix build on YDL.

* Mon Jun 17 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.8.

* Mon Jun 10 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.7.

* Mon May 13 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.6.
- Use %%find_lang.
- Replaced icon with the new one.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Mon Apr 22 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.5.

* Thu Mar 14 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.4.

* Sat Feb 16 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.2.

* Mon Feb 11 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.1.

* Mon Jan  7 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.0.

* Mon Dec 17 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.6.

* Wed Nov  7 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.5.

* Mon Oct 22 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.4.

* Mon Oct  8 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.3.

* Mon Sep 17 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.2.

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

