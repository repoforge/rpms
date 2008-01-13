# $Id$
# Authority: matthias
# Upstream: <gqclient-discuss$lists,sf,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge
%define langpack_version 1.2.1

Summary: graphical LDAP directory browser and editor
Name: gq
Version: 1.2.3
Release: 1
License: GPL
Group: Applications/Internet
URL: http://biot.com/gq/

Source0: http://dl.sf.net/gqclient/gq-%{version}.tar.gz
Source1: http://dl.sf.net/sourceforge/gqclient/gq-%{langpack_version}-langpack-1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.6, gtk2-devel >= 2.6, openldap-devel
BuildRequires: gnome-keyring-devel  >= 0.4.4, libglade2-devel
BuildRequires: krb5-devel, openssl-devel, libxml2-devel, perl(XML::Parser)
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
BuildRequires: gettext,

%description
GQ is a graphical browser for LDAP directories and schemas.  Using GQ,
an administrator can search through a directory and modify objects stored
in that directory.

%prep
%setup
%setup -T -D -a 1

%{__cat} <<EOF >src/gq.desktop
[Desktop Entry]
Name=GQ LDAP Client
Comment=Manage your LDAP directories
Exec=gq
Icon=redhat-system-tools.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=GNOME;Application;System;
EOF

gq-%{langpack_version}-langpack-1/langpack .
%{__cp} -av gq-%{langpack_version}-langpack-1/po/LINGUAS po/

%build
%configure \
    --disable-update-mimedb \
    --enable-browser-dnd \
    --enable-cache \
    --with-included-gettext
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%if %{!?_without_freedesktop:1}0
    %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
    desktop-file-install --vendor %{desktop_vendor} --delete-original \
        --add-category X-Red-Hat-Base                             \
        --dir %{buildroot}%{_datadir}/applications                \
        %{buildroot}%{_datadir}/applications/gq.desktop
%endif

%post
update-mime-database %{_datadir}/mime &>/dev/null || :

%postun
update-mime-database %{_datadir}/mime &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README* TODO
%{_bindir}/gq
%{_datadir}/gq/
%{_datadir}/mime/packages/gq-ldif.xml
%{_datadir}/pixmaps/gq/
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-gq.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Internet/gq.desktop}

%changelog
* Thu Jan 10 2008 Dag Wieers <dag@wieers.com> - 1.2.3-1
- Updated to release 1.2.3.

* Mon Apr 16 2007 Dag Wieers <dag@wieers.com> - 1.2.2-1
- Updated to release 1.2.2.

* Mon Oct 09 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.1-1
- Updated to release 1.2.1.

* Sat Sep 30 2006 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Updated to release 1.2.0.

* Wed Jun 09 2004 Dag Wieers <dag@wieers.com> - 0.6.0-4
- Merged SPEC file with my version.
- Changes to build on older releases.
- Added improved desktop file.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.beta1.1
- Update to 1.0beta1.
- Rebuild for Fedora Core 2.

* Thu Nov 13 2003 Matthias Saou <http://freshrpms.net/> 0.6.0-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Added new desktop entry.
- Added find_lang usage.

* Wed Jan 29 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.0.

* Tue May 21 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.0.

* Fri Feb 22 2002 Nalin Dahyabhai <nalin@redhat.com> 0.4.0-5
- rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 19 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Fri Mar  2 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Tue Feb 20 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 0.4.0, fixes bugs #24160, #24161

* Wed Dec 27 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 0.3.1

* Fri Dec  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Fri Nov 10 2000 Nalin Dahyabhai <nalin@redhat.com>
- initial package

