# $Id$
# Authority: matthias
# Upstream: Manuel Amador

%define desktop_vendor rpmforge

Summary: User control management tool for LDAP directories
Name: diradmin
Version: 1.6.0
Release: 1
License: GPL
Group: Applications/System
URL: http://diradmin.open-it.org/
Source: http://diradmin.open-it.org/directory_administrator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gnome-libs-devel, openldap-devel, desktop-file-utils
BuildRequires: openssl-devel
Obsoletes: directory_administrator <= 1.3.5

%description
Directory administrator is a smart LDAP directory management tool. It can be
used to manage UNIX and SAMBA user accounts and groups in a single sign-on
setup, corporate address book information, host-based access control and
advanced mail routing. It's extremely easy to install and use, yet powerful
at the same time. Along with popular software, it's the preferred solution
for single sign-on maintenance.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


# Replace desktop file, removing the categories
%{__rm} -f %{buildroot}%{_datadir}/applications/*
%{__cat} applnk/dragonfear-directory_administrator.desktop \
  | grep -v ^Categories > %{name}.desktop
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
  --dir %{buildroot}%{_datadir}/applications    \
  --add-category Application                    \
  --add-category System                         \
  %{name}.desktop


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS NEWS COPYING ChangeLog TODO README doc/
%{_bindir}/directory_administrator
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_datadir}/pixmaps/directory_administrator


%changelog
* Tue Jan 11 2005 Matthias Saou <http://freshrpms.net/> 1.6.0-1
- Update to 1.6.0.
- Added openssl-devel build dep.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 1.5.1-3
- Rebuild For Fedora Core 2.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.5.1-2
- Rebuild For Fedora Core 1.

* Wed Jul  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.5.1!
- Added %%{real_name} to spec file.
- Added obsoletes for the old directory_administrator packages.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Mar 20 2003 Matthias Saou <http://freshrpms.net/>
- Renamed to diradmin, directory_administrator is just too long :-)

* Wed Feb 12 2003 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup and minor fixes.

* Fri Dec 20 2002 Manuel Amador (Rudd-O) <amadorm@usm.edu.ec> 1.3-1
- Bugfixes
- From now on, this changelog shows only RPM spec changes

* Tue Nov 19 2002 Manuel Amador (Rudd-O) <amadorm@usm.edu.ec> 1.2.1-1
- Fixed compile issues in older platforms
- Fixed member list issues in group properties dialog (thanks to
  Christof Meerwald)
- Cosmetic fixes

* Mon Nov 18 2002 Manuel Amador (Rudd-O) <amadorm@usm.edu.ec> 1.2-1
- Keyboard navigation on the icon list, perfect for large directories
- Type ahead find to quickly locate an icon by typing its display
  name or part of it
- Enabled multiple icon selection for dragging and dropping several
  icons onto group lists, deleting several entries from the directory
  and (in the future) moving entries between organizational units

* Fri Nov 15 2002 Manuel Amador (Rudd-O) <amadorm@usm.edu.ec> 1.1.15-1
- Fixed bug which wouldn't let you grant access to particular servers
  or none at all when creating a user
- Unicode support for all attributes: accented characters are supported
  for all attributes which accept them

* Wed Nov 13 2002 Manuel Amador (Rudd-O) <amadorm@usm.edu.ec> 1.1.14-1
- Fixed bug that wouldn't let you modify entries without
  person/inetOrgPerson objectclass

* Tue Nov 12 2002 Manuel Amador (Rudd-O) <amadorm@usm.edu.ec> 1.1.13-1
- (Christof Meerwald) fixed bug whenever updating a SAMBA account would
  remove its password if it wasn't changed

* Fri Nov 08 2002 Manuel Amador (Rudd-O) <amadorm@usm.edu.ec> 1.1.12-1
- Made more robust against corrupted directory entries

* Thu Nov 07 2002 Manuel Amador (Rudd-O) <amadorm@usm.edu.ec> 1.1.11-1
- Fixed horrible compiled error that insulted you
- Improved SAMBA support (Christof Meerwald)
- Removed Mandrake menu support

* Wed Nov 06 2002 Manuel Amador (Rudd-O) <amadorm@usm.edu.ec> 1.1.10-1
- Fixed adding users as secondary members of groups
- Corrected handling of host "*", host-based access-control according to RFC
- Laid down initial infrastructure to support multiple views and directory tree
- Performance fixes: now entries are cached on a list in memory to be used in drop-down lists and the like

* Thu Jun 20 2002 Manuel Amador (Rudd-O) <amadorm@usm.edu.ec> 1.1.9-1mdk
- (you're welcome, Lenny! ;-)     )
- Fixed horrible bug that triggered on removal of any attribute
- Incorporated patch from Vincent Danen to fix md5 passwords

* Mon Jun 17 2002 Vincent Danen <vdanen@mandrakesoft.com> 1.1.8-2rph
- patch to fix how unix md5 passwords are stored

* Thu Jun 13 2002 Vincent Danen <vdanen@mandrakesoft.com> 1.1.8-1rph
- rebuild for rpmhelp.net (ML/8.2)

* Mon Apr 08 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.1.8-1mdk
- 1.1.8

* Wed Mar 27 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.1.7-1mdk
- updated to 1.1.7 ( thx Manuel Amador )

* Thu Dec 06 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.1.3-1mdk
- 1.1.3

