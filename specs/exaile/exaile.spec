# $Id$
# Authority:    hadams

%define real_version 0.2.13

Summary:	A music player
Name:		exaile
Version:	0.2.13
Release:	1
Group:		Applications/Multimedia
License:	GPL
URL:		http://www.exaile.org
Source0:	http://www.exaile.org/files/%{name}_%{real_version}.tar.gz
Patch0:		exaile0212-makefile.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	python-devel
BuildRequires:	pygtk2-devel
BuildRequires:	gtk2-devel
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig
BuildRequires:	gettext intltool perl(XML::Parser)
BuildRequires:	firefox-devel

Requires:	python-mutagen >= 1.8
Requires:	dbus-python
Requires:	gstreamer-python >= 0.10
Requires:	python-sqlite2
Requires:	pygtk2
Requires:	gnome-python2-gtkhtml2
Requires:	gnome-python2-gtkmozembed
Requires:	python-CDDB
Requires:	python-sexy
Requires:	gamin-python

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
%setup -n %{name}_%{real_version}
%patch0 -p0 -b .fix

# remove shebangs from all files as none should be executable scripts
sed -e '/^#!\//,1 d' -i plugins/*.py xl/plugins/*.py xl/*.py exaile.py

%build
make #%{?_smp_mflags}
 
%install
rm -rf %{buildroot}

make install PREFIX=%{_prefix} LIBDIR=%{_libdir}	\
	FIREFOX=%{firefox_lib} DESTDIR=%{buildroot}

desktop-file-install --delete-original			\
	--vendor="fedora"				\
	--dir=%{buildroot}%{_datadir}/applications	\
	%{buildroot}%{_datadir}/applications/%{name}.desktop

chmod 755 %{buildroot}%{_bindir}/exaile

chmod 755 %{buildroot}%{_libdir}/exaile/mmkeys.so

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc changelog COPYING INSTALL
%{_bindir}/exaile
%{_libdir}/exaile
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/exaile.png
%{_datadir}/exaile/
%{_mandir}/man1/exaile*.*

%changelog
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
