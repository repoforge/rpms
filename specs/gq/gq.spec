# $Id$

%define desktop_vendor freshrpms

Summary: A graphical LDAP directory browser and editor.
Name: gq
Version: 0.6.0
Release: 3.fr
Source: http://biot.com/gq/download/gq-%{version}.tar.gz
URL: http://biot.com/gq/
Group: Applications/Internet
License: GPL
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gtk+, openldap, krb5-libs, openssl
BuildRequires: gtk+-devel, openldap-devel, krb5-devel, openssl-devel
BuildRequires: desktop-file-utils

%description
GQ is a graphical browser for LDAP directories and schemas.  Using GQ,
an administrator can search through a directory and modify objects stored
in that directory.

%prep
%setup -q

%build
%configure --with-ldap-prefix=%{_prefix}
make

%install
rm -rf %{buildroot}
%makeinstall
%find_lang %{name}

# Desktop entry
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} --delete-original \
  --dir %{buildroot}%{_datadir}/applications                      \
  --add-category X-Red-Hat-Extra                                  \
  --add-category Application                                      \
  --add-category System                                           \
  %{buildroot}%{_datadir}/gnome/apps/Internet/%{name}.desktop

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc README COPYING ChangeLog NEWS TODO AUTHORS
%{_bindir}/*
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_datadir}/pixmaps/%{name}/*

%changelog
* Thu Nov 13 2003 Matthias Saou <http://freshrpms.net/> 0.6.0-3.fr
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

