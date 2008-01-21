# $Id$
# Authority: dag
# Upstream: Edwin Young <edwin$sourceforge,net>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define desktop_vendor rpmforge

Summary: Program to generate and view fractals
Name: gnofract4d
Version: 3.8
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://gnofract4d.sourceforge.net/

Source: http://dl.sf.net/gnofract4d/gnofract4d-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: scrollkeeper, gcc-c++, pkgconfig, python-devel >= 2.4
BuildRequires: desktop-file-utils, GConf2-devel, gtk2-devel
Requires(post): scrollkeeper

%description
Gnofract 4D is a GNOME-based program to draw fractals. What sets it
apart from other fractal programs (and makes it "4D") is the way that
it treats the Mandelbrot and Julia sets as different views of the
same four-dimensional fractal object.

%prep
%setup

%build
python2 setup.py build

%install
%{__rm} -rf %{buildroot}
python2 setup.py install --root="%{buildroot}"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}/gnofract4d/

%post
update-mime-database %{_datadir}/mime &>/dev/null || :
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :
update-mime-database %{_datadir}/mime &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%doc %{_datadir}/gnome/help/gnofract4d/
%{_bindir}/gnofract4d
%{_datadir}/applications/gnofract4d.desktop
%{_datadir}/gnofract4d/
%{_datadir}/mime/packages/gnofract4d-mime.xml
%{_datadir}/pixmaps/gnofract4d/
%{_datadir}/pixmaps/gnofract4d-logo.png
%{python_sitelib}/fract4d/
%{python_sitelib}/fract4dgui/
%{python_sitelib}/fractutils/
#%exclude %{python_sitelib}/buildtools/

%changelog
* Sun Jan 20 2008 Dries Verachtert <dries@ulyssis.org> - 3.8-1
- Updated to release 3.8.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 3.7-1
- Updated to release 3.7.

* Mon Oct 29 2007 Dries Verachtert <dries@ulyssis.org> - 3.6-1
- Updated to release 3.6.

* Mon Oct 15 2007 Dag Wieers <dag@wieers.com> - 3.5-1
- Updated to release 3.5.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 3.4-1
- Updated to release 3.4.

* Sun Apr 15 2007 Dag Wieers <dag@wieers.com> - 3.3-1
- Updated to release 3.3.

* Fri Dec 15 2006 Dries Verachtert <dries@ulyssis.org> - 3.2-1
- Updated to release 3.2.

* Tue Sep 12 2006 Dag Wieers <dag@wieers.com> - 3.1-1
- Updated to release 3.1.

* Tue Jun 27 2006 Dag Wieers <dag@wieers.com> - 3.0-1
- Updated to release 3.0.

* Sun May 07 2006 Dries Verachtert <dries@ulyssis.org> - 2.14-1
- Updated to release 2.14.

* Mon Apr 17 2006 Dag Wieers <dag@wieers.com> - 2.13-1
- Updated to release 2.13.

* Mon Feb 13 2006 Dries Verachtert <dries@ulyssis.org> - 2.12-1
- Updated to release 2.12.

* Mon Nov 21 2005 Dries Verachtert <dries@ulyssis.org> - 2.11-1
- Updated to release 2.11.

* Sun Sep 11 2005 Dag Wieers <dag@wieers.com> - 2.10-1
- Updated to release 2.10.

* Mon May 16 2005 Dag Wieers <dag@wieers.com> - 2.9-1
- Updated to release 2.9.

* Fri Apr 29 2005 Dag Wieers <dag@wieers.com> - 2.8-1
- Updated to release 2.8.

* Tue Mar 22 2005 Dag Wieers <dag@wieers.com> - 2.7-1
- Updated to release 2.7.

* Sun Feb 06 2005 Dag Wieers <dag@wieers.com> - 2.6-1
- Updated to release 2.6.

* Fri Dec 24 2004 Dag Wieers <dag@wieers.com> - 2.5-1
- Updated to release 2.5.

* Fri Jul 30 2004 Dag Wieers <dag@wieers.com> - 2.1-1
- Updated to release 2.1.

* Mon Jun 28 2004 Dag Wieers <dag@wieers.com> - 2.0-1
- Updated to release 2.0.

* Sat Dec 13 2003 Dag Wieers <dag@wieers.com> - 1.9-0
- Updated to release 1.9.

* Sun Nov 02 2003 Dag Wieers <dag@wieers.com> - 1.8-0
- Updated to release 1.8.

* Sun Feb 09 2003 Dag Wieers <dag@wieers.com> - 1.7-0
- Initial package. (using DAR)
