# $Id: meld.spec 6395 2008-07-04 02:30:42Z dag $
# Authority: dag
# Upstream: Stephen Kennedy <steve9000$users,sf,net>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define desktop_vendor rpmforge

Summary: Graphical visual diff and merge tool
Name: meld
Version: 1.4.0
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://meld.sourceforge.net/

Source: http://ftp.gnome.org/pub/gnome/sources/meld/1.4/meld-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: gnome-python2 >= 1.99.14
BuildRequires: intltool
BuildRequires: perl(XML::Parser)
BuildRequires: pygtk2-devel >= 2.8
BuildRequires: python >= 2.4
BuildRequires: pyorbit-devel >= 1.99
BuildRequires: scrollkeeper
Requires: gnome-python2 >= 1.99
Requires: gnome-python2-canvas
Requires: gnome-python2-gconf >= 1.99
Requires: pygobject2 >= 2.8.0
Requires: pygtk2 >= 2.8
Requires: pygtk2-libglade

%description
Meld is a GNOME2 visual diff and merge tool. It integrates especially
well with CVS. The diff viewer lets you edit files in place (diffs
update dynamically), and a middle column shows detailed changes and
allows merges.

%prep
%setup

%build
%{__make} %{?_smp_mflags} prefix="%{_prefix}" libdir="%{_datadir}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" prefix="%{_prefix}" libdir="%{_datadir}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL NEWS
%{_bindir}/meld
#%{_datadir}/application-registry/meld.applications
%{_datadir}/applications/meld.desktop
%{_datadir}/gnome/help/meld/
%{_datadir}/icons/hicolor/*/apps/meld.png
%{_datadir}/icons/hicolor/*/apps/meld.svg
%{_datadir}/meld/
%{_datadir}/omf/meld/
%{_datadir}/pixmaps/meld.png
#%{python_sitelib}/meld/

%changelog
* Sun Nov 21 2010 Dag Wieers <dag@wieers.com> - 1.4.0-1
- Updated to release 1.4.0.

* Sun May 17 2009 Dag Wieers <dag@wieers.com> - 1.3.0-1
- Updated to release 1.3.0.

* Mon Jun 30 2008 Dag Wieers <dag@wieers.com> - 1.2-1
- Updated to release 1.2.

* Sun Jun 10 2007 Dag Wieers <dag@wieers.com> - 1.1.5-1
- Updated to release 1.1.5.

* Mon Jun 12 2006 Dag Wieers <dag@wieers.com> - 1.1.4-1
- Updated to release 1.1.4.

* Tue Feb 28 2006 Dag Wieers <dag@wieers.com> - 1.1.3-1
- Updated to release 1.1.3.

* Wed Dec 07 2005 Dries Verachtert <dries@ulyssis.org> - 1.1.2-2
- Fixes: vc/* and help/* subdirectories added. (James Begley)

* Wed Nov 30 2005 Dag Wieers <dag@wieers.com> - 1.1.2-1
- Updated to release 1.1.2.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Wed May 18 2005 Dag Wieers <dag@wieers.com> - 0.9.6-1
- Updated to release 0.9.6.

* Sun Feb 06 2005 Dag Wieers <dag@wieers.com> - 0.9.5-1
- Updated to release 0.9.5.

* Fri Nov 19 2004 Dag Wieers <dag@wieers.com> - 0.9.4.1-2
- Moved desktop entry from Utilities to Development. (Rudolf Kastl)

* Sun Jul 18 2004 Dag Wieers <dag@wieers.com> - 0.9.4.1-1
- Updated to release 0.9.4.1.

* Fri Jul 16 2004 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Wed May 26 2004 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Tue Apr 13 2004 Dag Wieers <dag@wieers.com> - 0.9.2.1-1
- Updated to release 0.9.2.1.

* Tue Feb 17 2004 Dag Wieers <dag@wieers.com> - 0.9.2-0
- Updated to release 0.9.2.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 0.9.1-0
- Updated to release 0.9.1.

* Mon Oct 13 2003 Dag Wieers <dag@wieers.com> - 0.9.0-0
- Updated to release 0.9.0.

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 0.8.5-1
- Fixed meld.sh to accept arguments. (Sinisa Segvic)

* Sun Aug 31 2003 Dag Wieers <dag@wieers.com> - 0.8.5-0
- Updated to release 0.8.5.

* Tue Jul 29 2003 Dag Wieers <dag@wieers.com> - 0.8.4-0
- Updated to release 0.8.4.

* Fri Jul 25 2003 Dag Wieers <dag@wieers.com> - 0.8.3-0
- Updated to release 0.8.3.

* Sun Jun 22 2003 Dag Wieers <dag@wieers.com> - 0.8.2-0
- Updated to release 0.8.2.

* Fri Jun 06 2003 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Added gnome-python2-gconf requirement. (Rudolf Kastl)

* Tue May 20 2003 Dag Wieers <dag@wieers.com> - 0.8.1-0
- Updated to release 0.8.1.

* Wed Apr 16 2003 Dag Wieers <dag@wieers.com> - 0.7.1-0
- Updated to release 0.7.1.

* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Updated to release 0.7.0.

* Wed Feb 12 2003 Dag Wieers <dag@wieers.com> - 0.6.6-0
- Initial package. (using DAR)
