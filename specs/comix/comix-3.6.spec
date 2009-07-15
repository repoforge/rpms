# $Id$
# Authority: dries
# Upstream: <herrekberg$users,sourceforge,net>

Summary: Comic book viewer
Name: comix
Version: 3.6.5
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://comix.sourceforge.net/

Source: http://dl.sf.net/comix/comix-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: gtk2-devel
BuildRequires: pygtk2-devel
BuildRequires: python
BuildRequires: python-imaging
Requires: gtk2
Requires: pygtk2
Requires: python
Requires: python-imaging
Requires: rar

%description
Comix is a comic book viewer. It reads zip, rar, tar, tar.gz, and tar.bz2
archives (often called .cbz, .cbr and .cbt) as well as normal image files.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_prefix}
%{__python} install.py install --no-mime --installdir %{buildroot}%{_prefix}
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%doc %{_mandir}/man1/comix.1*
%{_bindir}/comix
%{_datadir}/applications/*comix.desktop
%{_datadir}/icons/hicolor/*/apps/comix.png
%{_datadir}/icons/hicolor/*/apps/comix.svg*
%{_datadir}/pixmaps/comix/
%{_datadir}/pixmaps/comix.png

%changelog
* Wed Jul 15 2009 Dag Wieers <dag@wieers.com> - 3.6.5-1
- Updated to release 3.6.5.

* Mon May 28 2007 Dries Verachtert <dries@ulyssis.org> - 3.6.4-1
- Updated to release 3.6.4.

* Mon Mar 19 2007 Dries Verachtert <dries@ulyssis.org> - 3.6.3-1
- Updated to release 3.6.3.

* Tue Feb 13 2007 Dries Verachtert <dries@ulyssis.org> - 3.6.2-1
- Updated to release 3.6.2.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 3.6.1-1
- Updated to release 3.6.1.

* Sat May 20 2006 Dries Verachtert <dries@ulyssis.org> - 3.1.3-1
- Updated to release 3.1.3.

* Fri May 19 2006 Dries Verachtert <dries@ulyssis.org> - 3.1.2-1
- Updated to release 3.1.2.

* Sat May 06 2006 Dries Verachtert <dries@ulyssis.org> - 3.1-1
- Updated to release 3.1.

* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 3.0.1-1
- Updated to release 3.0.1.

* Mon Apr 03 2006 Dries Verachtert <dries@ulyssis.org> - 3.0-1
- Updated to release 3.0.

* Wed Mar 01 2006 Dries Verachtert <dries@ulyssis.org> - 2.9-1
- Updated to release 2.9.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 2.8-1
- Updated to release 2.8.

* Mon Jan 30 2006 Dries Verachtert <dries@ulyssis.org> - 2.7-1
- Updated to release 2.7.

* Tue Jan 17 2006 Dag Wieers <dag@wieers.com> - 2.6-1
- Updated to release 2.6.

* Wed Jan 11 2006 Dries Verachtert <dries@ulyssis.org> - 2.5-1
- Updated to release 2.5.
- Added the python-imaging requirement, thanks to Gergely Gabor!

* Sun Jan 01 2006 Dries Verachtert <dries@ulyssis.org> - 2.4-1
- Updated to release 2.4.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 2.3-1
- Updated to release 2.3.

* Sat Dec 10 2005 Dries Verachtert <dries@ulyssis.org> - 2.2-1
- Updated to release 2.2.

* Sat Nov 26 2005 Dag Wieers <dag@wieers.com> - 2.1-1
- Updated to release 2.1.

* Mon Nov 21 2005 Dries Verachtert <dries@ulyssis.org> - 2.0-1
- Updated to release 2.0.

* Mon Nov 07 2005 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Initial package.
