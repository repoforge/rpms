# $Id$
# Authority: hadams

%define desktop_vendor rpmforge

Summary: Music player
Name: exaile
Version: 0.2.14
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.exaile.org/

Source0: http://www.exaile.org/files/exaile_%{version}.tar.gz
Patch0: exaile-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: desktop-file-utils
#BuildRequires: firefox-devel
BuildRequires: gettext
BuildRequires: gtk2-devel
BuildRequires: intltool
BuildRequires: pkgconfig
BuildRequires: perl(XML::Parser)
BuildRequires: pygtk2-devel
BuildRequires: python-devel
BuildRequires: xulrunner-devel
Requires: dbus-python
Requires: gamin-python
Requires: gnome-python2-gtkhtml2
Requires: gnome-python2-gtkmozembed
Requires: gstreamer-python >= 0.10
Requires: python-cddb
Requires: python-mutagen >= 1.8
Requires: python-sexy
Requires: python-sqlite2
Requires: pygtk2
Requires: xulrunner

%ifarch x86_64 ia64 ppc64 s390x
%define gre_conf %{_sysconfdir}/gre.d/gre64.conf
%else
%define gre_conf %{_sysconfdir}/gre.d/gre.conf
%endif 

%description
Exaile is a media player aiming to be similar to KDE's AmaroK, but for GTK+.
It incorporates many of the cool things from AmaroK (and other media players)
like automatic fetching of album art, handling of large libraries, lyrics
fetching, artist/album information via the wikipedia, last.fm support, optional
iPod support (assuming you have python-gpod installed).

In addition, Exaile also includes a built in shoutcast directory browser,
tabbed playlists (so you can have more than one playlist open at a time),
blacklisting of tracks (so they don't get scanned into your library),
downloading of guitar tablature from fretplay.com, and submitting played tracks
on your iPod to last.fm

%prep
%setup -n exaile-%{version}
%patch0 -p0 -b .fix

### remove shebangs from all files as none should be executable scripts
sed -e '/^#!\//,1 d' -i plugins/*.py xl/plugins/*.py xl/*.py exaile.py

%build
%{__make} #%{?_smp_mflags}
 
%install
%{__rm} -rf %{buildroot}

%{__make} install DESTDIR="%{buildroot}" \
    PREFIX="%{_prefix}" \
    LIBDIR="%{_libdir}"
%find_lang %{name}

desktop-file-install --delete-original          \
    --vendor="%{desktop_vendor}"                \
    --dir=%{buildroot}%{_datadir}/applications	\
    %{buildroot}%{_datadir}/applications/exaile.desktop

%{__chmod} 0755 %{buildroot}%{_bindir}/exaile
%{__chmod} 0755 %{buildroot}%{_libdir}/exaile/mmkeys.so

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc changelog COPYING INSTALL
%doc %{_mandir}/man1/exaile*.1*
%{_bindir}/exaile
%{_datadir}/applications/%{desktop_vendor}-exaile.desktop
%{_datadir}/exaile/
%{_datadir}/pixmaps/exaile.png
%{_libdir}/exaile/

%changelog
* Tue Apr 14 2009 Dag Wieers <dag@wieers.com> - 0.2.14-2
- Cosmetic changes.

* Sat Oct 18 2008 Heiko Adams <info@fedora-blog.de> - 0.2.14-1
- version update

* Sun Aug 24 2008 Heiko Adams <info@fedora-blog.de> - 0.2.13-2
- rebuild for CentOS 5.2

* Thu Apr 02 2008 Heiko Adams <info@fedora-blog.de> - 0.2.13-1
- version update

* Fri Mar 28 2008 Heiko Adams <info@fedora-blog.de> - 0.2.12-1
- version update

* Sat Nov 10 2007 Heiko Adams <info@fedora-blog.de> - 0.2.11.1-1
- version update

* Sun Jul 22 2007 Heiko Adams <info@fedora-blog.de> - 0.2.10-2
- Rebuild for rpmforge

* Sat Jun 30 2007 Deji Akingunola <dakingun@gmail.com> - 0.2.10-1
- New release

* Fri Mar 30 2007 Deji Akingunola <dakingun@gmail.com> - 0.2.9-1
- New release

* Tue Jan 09 2007 Deji Akingunola <dakingun@gmail.com> - 0.2.8-1
- New release

* Sat Dec 30 2006 Deji Akingunola <dakingun@gmail.com> - 0.2.7-1
- New release

* Wed Dec 27 2006 Deji Akingunola <dakingun@gmail.com> - 0.2.6-3
- Rework the python include patch

* Wed Dec 27 2006 Deji Akingunola <dakingun@gmail.com> - 0.2.6-2
- Rewrite the build patch to be more generic

* Tue Dec 26 2006 Deji Akingunola <dakingun@gmail.com> - 0.2.6-1
- First version for Fedora Extras
