# $Id$
# Authority: matthias
# Upstream: <gtktalog-devel$nongnu,org>

%define desktop_vendor rpmforge

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}


Summary: The GNOME disk catalog
Name: gtktalog
Version: 1.0.4
Release: 2%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://www.nongnu.org/gtktalog/

Source: ftp://ftp.gnu.org/savannah/files/gtktalog/gtktalog.pkg/%{version}/gtktalog-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gnome-libs-devel, gtk+-devel, desktop-file-utils, gcc-c++
%{!?_without_modxorg:BuildRequires: libSM-devel}
Requires: gnome-libs >= 1.2, zlib, eject, bzip2, /usr/bin/file

%description
GTKtalog is a disk catalog, it means you can use it to create a really small
database with images of files and folders of your CD-rom. So you can browse all
your CD's very quickly, see contents of certain files (tar.gz, rpm files ...).
You can give to each folder and file a category and a description. You can
search for files in your database with filename, category, description or file
information parameter, and find in which CD the file you are looking for is.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} --delete-original \
  --dir %{buildroot}%{_datadir}/applications                      \
  %{buildroot}%{_datadir}/gnome/apps/Applications/%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ABOUT-NLS AUTHORS ChangeLog NEWS README TODO
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%doc %{_datadir}/gnome/help/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.0.4-2.fr
- Rebuild for Fedora Core 1.

* Tue Nov  4 2003 Matthias Saou <http://freshrpms.net/> 1.0.4-1.fr
- Update to 1.0.4.

* Sun Aug  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.3.

* Fri Jun 13 2003 Matthias Saou <http://freshrpms.net/>
- Removed extra categories to avoid a bug.

* Mon Apr 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Tagged the GNOME help as doc.

* Wed Oct 30 2002 Matthias Saou <http://freshrpms.net/>
- Removed the smpeg dependency, doh!

* Mon Oct 21 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.0.

* Wed Oct  9 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0rc3.
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.
- Use %%find_lang.

* Wed Aug 21 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0rc2.

* Sun Aug  4 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0rc1.

* Thu Jul 11 2002 Matthias Saou <http://freshrpms.net/>
- Added program prefix to configure to fix build on PPC.

* Mon Jun 17 2002 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.99.20.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.99.19.
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Mon Apr  1 2002 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.99.18.

* Sun Dec 30 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.99.16.

* Mon Nov 19 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.99.15.

* Tue Nov  6 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.99.14.

* Mon Nov  5 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.99.13.

* Thu Sep 19 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.99.12.

* Thu Aug 16 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.99.11.

* Tue Aug 14 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.99.10.

* Mon Aug  6 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.99.9.

* Mon Jul 30 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.99.8.

* Sun Jul 22 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.99.7.

* Mon Jun 11 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.99.0, the end is near :-)

* Tue Jun  5 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.19.2.

* Thu May 31 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.19.1.

* Wed May 23 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.18.1.

* Sat May 12 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.18.1.

* Tue Apr 24 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.17.1 and rebuilt for Red Hat 7.1.

* Wed Mar 28 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.16.2

* Sat Mar 24 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.16.1

* Fri Mar 16 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.14.1

* Mon Mar 12 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.13.2

* Thu Mar  8 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.13.1

* Wed Feb 14 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.12.2

* Fri Feb  9 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.12.1

* Mon Feb  5 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.11.3

* Wed Jan 31 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.11.1

* Sat Jan 27 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.10.1

* Wed Jan 10 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.9.2

* Mon Jan  8 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.9.1
- Now requires smpeg (for the new mpeginfo plugin)

* Thu Dec 28 2000 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.9.0

* Fri Dec 22 2000 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.8.1

* Mon Dec 18 2000 Matthias Saou <http://freshrpms.net/>
- Fixed the group and removed some implicit dependencies.

* Sun Dec 17 2000 Matthias Saou <http://freshrpms.net/>
- Updated for RedHat 7.0, more unuseful stuff removed :-)

* Tue Nov 14 2000 Yves Mettier <ymettier@free.fr>
- I'm using mdk-7.2 and all major rpm-distributions seem to have rpm-4.x
  So I'm getting rid of some unuseful stuff.

* Sun Sep 24 2000 Yves Mettier <ymettier@free.fr>
- Updated to rpm 3.0.5 because there was some problems with the prefix.

