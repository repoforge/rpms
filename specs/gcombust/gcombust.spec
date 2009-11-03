# $Id$
# Authority: matthias

Summary: Powerful GTK+ front-end for mkisofs and cdrecord
Name: gcombust
Version: 0.1.55
Release: 2%{?dist}
Epoch: 1
License: GPL
Group: Applications/Archiving
URL: http://www.abo.fi/~jmunsin/gcombust/
Source: http://www.abo.fi/~jmunsin/gcombust/gcombust-%{version}.tar.gz
Requires: cdrecord >= 1.10, mkisofs >= 1.10
Requires: cdda2wav >= 1.10, cdlabelgen >= 1.5.0
BuildRequires: gtk+-devel, perl
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Gcombust is a GUI front-end for mkisofs, mkhybrid, cdda2wav, cdrecord
and cdlabelgen, written in C using the GTK+ widget set. Gcombust
includes primitive support for controlling the directory (root)
structure and size of the disk image without copying files/symlinking
or writing ten lines of arguments and it can maximize disk usage by
hinting which directories and files to use.


%prep
%setup
%{__perl} -pi -e 's|^static GtkWidget \*opt_try_harder|GtkWidget *opt_try_harder|g;' src/optimize_usage.c
%{__perl} -pi -e 's|^static GtkWidget \*rip_path_entry|GtkWidget *rip_path_entry|g;' src/rip_audio.c

%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FAQ.shtml NEWS README README.ms THANKS TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm


%changelog
* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 1:0.1.55-3
- Rebuild for Fedora Core 2.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1:0.1.55-2
- Rebuild for Fedora Core 1.

* Thu Jul 24 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.1.55.
- Simplified the spec now that the menu entry is the freedesktop type.
- Escaped %%install later in the changelog.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sat Feb  1 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.1.54.

* Sun Dec 22 2002 Ville Skyttä <ville.skytta at iki.fi> - 1:0.1.53-fr1
- Update to 0.1.53.
- Fix desktop menu entry and build requirements.

* Sun Sep 29 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.

* Tue Jul  9 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.1.52.

* Thu Jun 13 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.1.51.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Tue Apr  2 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.1.49.

* Mon Oct 22 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.1.47.

* Thu Aug  9 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.1.46.

* Mon May  7 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.1.43 and added dependencies on newer cdrecord/mkisofs.

* Tue Feb 27 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.1.42

* Sat Feb  3 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.1.41

* Sun Jan  7 2001 Matthias Saou <http://freshrpms.net/>
- Updated to 0.1.40
- Simplified the %%install to reflect changes

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jul 03 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Wed May 10 2000 Tim Powers <timp@redhat.com>
- updated to 0.1.32
- added locale to the files list

* Wed Nov 10 1999 Tim Powers <timp@redhat.com>
- updated to 0.1.25

* Mon Sep 20 1999 Preston Brown <pbrown@redhat.com>
- 0.1.23 bugfix release

* Mon Sep 07 1999 Preston Brown <pbrown@redhat.com>
- upgraded to 0.1.21 bugfix release.

* Sun Aug 22 1999 Preston Brown <pbrown@redhat.com>
- adopted for Powertools

