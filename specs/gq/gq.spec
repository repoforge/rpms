# $Id$
# Authority: matthias
# Upstream: <gqclient-discuss@lists.sf.net>

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor freshrpms
%define prever         beta1

Summary: graphical LDAP directory browser and editor
Name: gq
<<<<<<< .mine
Version: 1.0
Release: %{?prever:0.%{prever}.}1
=======
Version: 0.6.0
Release: 4
>>>>>>> .r1288
License: GPL
Group: Applications/Internet
URL: http://biot.com/gq/
Source: http://dl.sf.net/gqclient/gq-%{version}%{?prever}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gtk+, openldap, krb5-libs, openssl
<<<<<<< .mine
BuildRequires: gtk+-devel, openldap-devel, krb5-devel, openssl-devel
BuildRequires: desktop-file-utils
=======
BuildRequires: gtk+-devel, openldap-devel >= 2.0, krb5-devel, openssl-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: gtk+, openldap >= 2.0, krb5-libs, openssl
>>>>>>> .r1288

%description
GQ is a graphical browser for LDAP directories and schemas.  Using GQ,
an administrator can search through a directory and modify objects stored
in that directory.


%prep
%setup -n %{name}-%{version}%{?prever}

<<<<<<< .mine

=======
%{__cat} <<EOF >src/gq.desktop
[Desktop Entry]
Name=GQ LDAP Client
Comment=Manage your LDAP directories
Exec=gq
Icon=redhat-system_tools.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=GNOME;Application;System;
EOF

>>>>>>> .r1288
%build
<<<<<<< .mine
%configure --with-ldap-prefix=%{_prefix}
%{__make} %{?_smp_mflags}
=======
%configure \
	--enable-cache \
	--enable-browser-dnd
>>>>>>> .r1288

<<<<<<< .mine

=======
%{__make} %{?_smp_mflags}

>>>>>>> .r1288
%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

<<<<<<< .mine
# Desktop entry
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} --delete-original \
  --dir %{buildroot}%{_datadir}/applications                      \
  --add-category Application                                      \
  --add-category System                                           \
  %{buildroot}%{_datadir}/gnome/apps/Internet/%{name}.desktop
=======
%if %{!?_without_freedesktop:1}0
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor} --delete-original \
		--add-category X-Red-Hat-Base                             \
		--dir %{buildroot}%{_datadir}/applications                \
		%{buildroot}%{_datadir}/gnome/apps/Internet/gq.desktop
%endif
>>>>>>> .r1288


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README* TODO
%{_bindir}/*
%{_datadir}/pixmaps/%{name}/
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-gq.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Internet/gq.desktop}


%changelog
<<<<<<< .mine
* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.beta1.1
- Update to 1.0beta1.
- Rebuild for Fedora Core 2.

* Thu Nov 13 2003 Matthias Saou <http://freshrpms.net/> 0.6.0-3
=======
* Wed Jun 09 2004 Dag Wieers <dag@wieers.com> - 0.6.0-4
- Merged SPEC file with my version.
- Changes to build on older releases.
- Added improved desktop file.

* Thu Nov 13 2003 Matthias Saou <http://freshrpms.net/> 0.6.0-3
>>>>>>> .r1288
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

