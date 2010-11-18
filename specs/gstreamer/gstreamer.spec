# ExclusiveDist: rh9

%define _glib2		2.3.0
%define _libxml2	2.4.9

Name: gstreamer
Version: 0.8.7
# keep in sync with the VERSION.  gstreamer can append a .0.1 to CVS snapshots.
%define majmin  0.8
%define po_package %{name}-%{majmin}

Release: 0%{?dist}
Summary: GStreamer streaming media framework runtime.
Group: Applications/Multimedia
License: LGPL
URL: http://gstreamer.net/
Source: http://gstreamer.net/releases/%{version}/src/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# There was problems generating pdf and postscript:
Patch1: gstreamer-0.7.5-nops.patch

Requires: glib2 >= %_glib2
Requires: libxml2 >= %_libxml2
Requires: popt > 1.6

BuildRequires: glib2-devel >= %_glib2
BuildRequires: libxml2-devel >= %_libxml2
BuildRequires: bison flex
BuildRequires: gtk-doc >= 1.1
BuildRequires: zlib-devel
BuildRequires: popt > 1.6
BuildRequires: gettext
# for autopoint, should be depended on by gettext-devel
BuildRequires: cvs
BuildRequires: flex
BuildRequires: ghostscript
Prereq: /sbin/ldconfig

### documentation requirements
BuildRequires: openjade
BuildRequires: python2
BuildRequires: docbook-style-dsssl
BuildRequires: docbook-style-xsl
BuildRequires: docbook-dtds
BuildRequires: docbook-utils
BuildRequires: transfig xfig
BuildRequires: netpbm-progs

BuildRequires: autoconf, automake, libtool

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

%package devel
Summary: Libraries/include files for GStreamer streaming media framework.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel >= %_glib2
Requires: libxml2-devel >= %_libxml2

%description devel
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains the libraries and includes files necessary to develop
applications and plugins for GStreamer.

%package tools
Summary: tools for GStreamer streaming media framework.
Group: Applications/Multimedia

%description tools
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains the basic command-line tools used for GStreamer, like
gst-register and gst-launch.  It is split off to allow parallel-installability
in the future.

%prep
%setup -q
%patch1 -p1 -b .nops

# openjade doesn't support xml catalogs, so we have to patch in the right dtd reference
find -name "*.xml" | xargs grep -l "http://www.oasis-open.org/docbook/xml/4.2/docbookx.dtd" | xargs perl -pi -e 's#http://www.oasis-open.org/docbook/xml/4.2/docbookx.dtd#/usr/share/sgml/docbook/xml-dtd-4.2-1.0-24/docbookx.dtd#g'

# The nopdf patch touches automake makefile sources
NOCONFIGURE=1 ./autogen.sh

%build

## FIXME should re-enable the docs build when it works
%configure --disable-plugin-builddir --disable-tests --disable-examples \
	 --with-cachedir=%{_localstatedir}/cache/gstreamer-%{majmin} \
	--enable-docs-build --with-html-dir=$RPM_BUILD_ROOT%{_datadir}/gtk-doc/html \
	--enable-debug

make %{?_smp_mflags}

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

# build documentation to a different location so it doesn't end up in
# a gstreamer-devel-(version) dir and doesn't get deleted by %doc scripts
%makeinstall docdir=$RPM_BUILD_ROOT%{_datadir}/gstreamer-%{majmin}/doc

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/gstreamer-%{majmin}

/bin/rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majmin}/*.a
/bin/rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majmin}/*.la
/bin/rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
/bin/rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
/bin/rm -f $RPM_BUILD_ROOT%{_libdir}/libgstmedia-info*.so.0.0.0

%find_lang %{po_package}

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
env DISPLAY= %{_bindir}/gst-register-%{majmin} > /dev/null 2> /dev/null

%postun -p /sbin/ldconfig

%files -f %{po_package}.lang
%defattr(-, root, root, 0755)
%doc ABOUT-NLS AUTHORS COPYING DOCBUILDING README REQUIREMENTS TODO
%dir %{_libdir}/gstreamer-%{majmin}
%dir %{_localstatedir}/cache/gstreamer-%{majmin}
%{_libdir}/gstreamer-%{majmin}/*.so*
%{_libdir}/*.so.*
%{_bindir}/*-%{majmin}
%{_mandir}/man1/*-%{majmin}.1.gz

%files devel
%defattr(-, root, root, 0755)
%dir %{_includedir}/%{name}-%{majmin}
%{_includedir}/%{name}-%{majmin}/*
%{_libdir}/libgstreamer-%{majmin}.so
%{_libdir}/libgstcontrol-%{majmin}.so
%{_libdir}/pkgconfig/gstreamer*.pc
%{_datadir}/aclocal/*
%{_datadir}/gtk-doc/html/*
%{_datadir}/gstreamer-%{majmin}/doc

%files tools
%defattr(-, root, root, 0755)
%{_bindir}/*
%exclude %{_bindir}/*-%{majmin}
%{_mandir}/man1/*
%exclude %{_mandir}/man1/*-%{majmin}.1.gz

%changelog
* Wed Oct 13 2004 Colin Walters <walters@redhat.com> 0.8.7-3
- Quote %%configure in changelog (135412)

* Thu Oct 07 2004 Colin Walters <walters@redhat.com> 0.8.7-2
- BuildRequire gettext-devel

* Wed Oct  6 2004 Alexander Larsson <alexl@redhat.com> - 0.8.7-1
- update to 0.8.7

* Tue Oct  5 2004 Alexander Larsson <alexl@redhat.com> - 0.8.6-1
- update to 0.8.6
- Put the real lib .so symlinks in the -devel package
- Do not put .so plugins in the -devel package
- Correct docbook dtd version reference

* Tue Sep 28 2004 Colin Walters <walters@redhat.com> 0.8.5-2
- Move .so symlinks to -devel package

* Tue Aug 16 2004 Colin Walters <walters@redhat.com> 0.8.5-1
- Update to 0.8.5

* Tue Jul 26 2004 Colin Walters <walters@redhat.com> 0.8.4-1
- Update to 0.8.4

* Tue Jul 20 2004 Colin Walters <walters@redhat.com> 0.8.3.3-1
- Update

* Tue Jul 05 2004 Colin Walters <walters@redhat.com> 0.8.3-3
- Another rebuild to placate beehive!

* Tue Jul 05 2004 Colin Walters <walters@redhat.com> 0.8.3-2
- Rebuild to placate beehive

* Wed Jun 23 2004 Colin Walters <walters@redhat.com> 0.8.3-1
- Update to 0.8.3, now that I am convinced it is safe.
- Remove backported cpufix patch.
- "cvs remove" a bunch of obsoleted patches.

* Mon Jun 21 2004 Colin Walters <walters@redhat.com> 0.8.1-5
- BuildRequire gettext-devel

* Mon Jun 21 2004 Colin Walters <walters@redhat.com> 0.8.1-4
- BuildRequire ghostscript

* Mon Jun 21 2004 Colin Walters <walters@redhat.com> 0.8.1-3
- Apply register-clobbering patch from upstream CVS.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com> 0.8.1-2
- rebuilt

* Mon Apr 15 2004 Colin Walters <walters@redhat.com> 0.8.1-1
- Update to 0.8.1
- Delete registry patches which have been upstreamed
- COPYING.LIB is gone

* Mon Apr 05 2004 Colin Walters <walters@redhat.com> 0.8.0-4
- I have discovered that it is helpful, when adding patches
  to a package, to actually add the "%patchN" lines.

* Mon Mar 22 2004 Colin Walters <walters@redhat.com> 0.8.0-3
- Add BuildRequires on flex
- Add patch to avoid calling opendir() on files

* Mon Mar 22 2004 Colin Walters <walters@redhat.com> 0.8.0-2
- Add patch to avoid setting mtime on registry

* Tue Mar 16 2004 Alex Larsson <alexl@redhat.com> 0.8.0-1
- update to 0.8.0

* Wed Mar 10 2004 Alexander Larsson <alexl@redhat.com> 0.7.6-1
- update to 0.7.6

* Thu Mar  4 2004 Jeremy Katz <katzj@redhat.com> - 0.7.5-2
- fix plugin dir with respect to %%_lib

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 24 2004 Alexander Larsson <alexl@redhat.com> 0.7.5-1
- update to 0.7.5
- clean up specfile some
- enable docs

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb  4 2004 Bill Nottingham <notting@redhat.com> 0.7.3-4
- fix %%post

* Wed Jan 28 2004 Alexander Larsson <alexl@redhat.com> 0.7.3-3
- add s390 patch

* Tue Jan 27 2004 Jonathan Blandford <jrb@redhat.com> 0.7.3-1
- new version

* Thu Sep 11 2003 Alexander Larsson <alexl@redhat.com> 0.6.3-1
- Update to 0.6.3 (gnome 2.4 final)

* Tue Aug 19 2003 Alexander Larsson <alexl@redhat.com> 0.6.2-6
- 0.6.2

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 17 2003 Elliot Lee <sopwith@redhat.com> 0.6.0-5
- ppc64 patch

* Wed Feb 12 2003 Bill Nottingham <notting@redhat.com> 0.6.0-4
- fix group

* Tue Feb 11 2003 Bill Nottingham <notting@redhat.com> 0.6.0-3
- prereq, not require, gstreamer-tools

* Tue Feb 11 2003 Jonathan Blandford <jrb@redhat.com> 0.6.0-2
- unset the DISPLAY when running gst-register

* Mon Feb  3 2003 Jonathan Blandford <jrb@redhat.com> 0.6.0-1
- yes it is needed.  Readding

* Sat Feb 01 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- remove "tools" sub-rpm, this is not needed at all

* Thu Jan 30 2003 Jonathan Blandford <jrb@redhat.com> 0.5.2-7
- stopped using %%configure so we need to pass in all the args

* Mon Jan 27 2003 Jonathan Blandford <jrb@redhat.com>
- remove -Werror explicitly as the configure macro isn't working.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 19 2002 Elliot Lee <sopwith@redhat.com> 0.5.0-10
- Add patch1 to fix C++ plugins on ia64

* Wed Dec 18 2002 Jonathan Blandford <jrb@redhat.com>
- %post -p was wrong

* Tue Dec 17 2002 Jonathan Blandford <jrb@redhat.com> 0.5.0-7
- explicitly add %{_libdir}/libgstreamer-{majmin}.so
- explicitly add %{_libdir}/libgstcontrol-{majmin}.so

* Mon Dec 16 2002 Jonathan Blandford <jrb@redhat.com>
- bump release

* Fri Dec 13 2002 Jonathan Blandford <jrb@redhat.com>
- move .so files out of -devel

* Tue Dec 10 2002 Jonathan Blandford <jrb@redhat.com>
- new version 0.5.0
- require docbook-style-xsl
- add gstreamer-tools package too
- New patch to use the right docbook prefix.

* Tue Dec 10 2002 Jonathan Blandford <jrb@redhat.com>
- downgrade to a release candidate.  Should work better on other arches
- build without Werror

* Mon Dec  9 2002 Jonathan Blandford <jrb@redhat.com>
- update to new version.  Remove ExcludeArch

* Tue Dec  3 2002 Havoc Pennington <hp@redhat.com>
- excludearch some arches

* Mon Dec  2 2002 Havoc Pennington <hp@redhat.com>
- import into CVS and build "officially"
- use smp_mflags
- temporarily disable docs build, doesn't seem to work

* Thu Nov  7 2002 Jeremy Katz <katzj@redhat.com>
- 0.4.2

* Mon Sep 23 2002 Jeremy Katz <katzj@redhat.com>
- 0.4.1

* Sun Sep 22 2002 Jeremy Katz <katzj@redhat.com>
- minor cleanups

* Sat Jun 22 2002 Thomas Vander Stichele <thomas@apestaart.org>
- moved header location

* Mon Jun 17 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added popt
- removed .la

* Fri Jun 07 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added release of gstreamer to req of gstreamer-devel
- changed location of API docs to be in gtk-doc like other gtk-doc stuff
- reordered SPEC file

* Mon Apr 29 2002 Thomas Vander Stichele <thomas@apestaart.org>
- moved html docs to gtk-doc standard directory

* Tue Mar 5 2002 Thomas Vander Stichele <thomas@apestaart.org>
- move version defines of glib2 and libxml2 to configure.ac
- add BuildRequires for these two libs

* Sun Mar 3 2002 Thomas Vander Stichele <thomas@apestaart.org>
- put html docs in canonical place, avoiding %doc erasure
- added devhelp support, current install of it is hackish

* Sat Mar 2 2002 Christian Schaller <Uraeus@linuxrising.org>
- Added documentation to build

* Mon Feb 11 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added libgstbasicscheduler
- renamed libgst to libgstreamer

* Fri Jan 04 2002 Christian Schaller <Uraeus@linuxrising.org>
- Added configdir parameter as it seems the configdir gets weird otherwise

* Thu Jan 03 2002 Thomas Vander Stichele <thomas@apestaart.org>
- split off gstreamer-editor from core
- removed gstreamer-gnome-apps

* Sat Dec 29 2001 Rodney Dawes <dobey@free.fr>
- Cleaned up the spec file for the gstreamer core/plug-ins split
- Improve spec file

* Sat Dec 15 2001 Christian Schaller <Uraeus@linuxrising.org>
- Split of more plugins from the core and put them into their own modules
- Includes colorspace, xfree and wav
- Improved package Require lines
- Added mp3encode (lame based) to the SPEC

* Wed Dec 12 2001 Christian Schaller <Uraeus@linuxrising.org>
- Thomas merged mpeg plugins into one
* Sat Dec 08 2001 Christian Schaller <Uraeus@linuxrising.org>
- More minor cleanups including some fixed descriptions from Andrew Mitchell

* Fri Dec 07 2001 Christian Schaller <Uraeus@linuxrising.org>
- Added logging to the make statement

* Wed Dec 05 2001 Christian Schaller <Uraeus@linuxrising.org>
- Updated in preparation for 0.3.0 release

* Fri Jun 29 2001 Christian Schaller <Uraeus@linuxrising.org>
- Updated for 0.2.1 release
- Split out the GUI packages into their own RPM
- added new plugins (FLAC, festival, quicktime etc.)

* Sat Jun 09 2001 Christian Schaller <Uraeus@linuxrising.org>
- Visualisation plugins bundled out togheter
- Moved files sections up close to their respective descriptions

* Sat Jun 02 2001 Christian Schaller <Uraeus@linuxrising.org>
- Split the package into separate RPMS,
  putting most plugins out by themselves.

* Fri Jun 01 2001 Christian Schaller <Uraeus@linuxrising.org>
- Updated with change suggestions from Dennis Bjorklund

* Tue Jan 09 2001 Erik Walthinsen <omega@cse.ogi.edu>
- updated to build -devel package as well

* Sun Jan 30 2000 Erik Walthinsen <omega@cse.ogi.edu>
- first draft of spec file

