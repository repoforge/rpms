%define glib2minver   2.0.1
%define libxml2minver 2.4.0
%define major         0
%define minor         7
%define micro         5
%define majmin        %{major}.%{minor}

Summary: GStreamer streaming media framework runtime
Name: gstreamer07
Version: %{majmin}.%{micro}
Release: 0.1%{?dist}
Group: Applications/Multimedia
License: LGPL
URL: http://gstreamer.net/
Source: http://freedesktop.org/~gstreamer/src/gstreamer-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: gstreamer-tools >= %{version}
Requires: glib2 >= %{glib2minver}
Requires: libxml2 >= %{libxml2minver}
Requires: popt > 1.6
Requires(post,postun): /sbin/ldconfig

Provides: gstreamer = %{version}-%{release}
Provides: gstreamer = %{majmin}

BuildRequires: glib2-devel >= %{glib2minver}
BuildRequires: libxml2-devel >= %{libxml2minver}
BuildRequires: zlib-devel, gtk-doc >= 1.1, popt > 1.6
BuildRequires: m4, bison, flex, gcc-c++, gettext
BuildRequires: autoconf, automake, libtool
BuildRequires: libgnomeui-devel >= 2.0

### documentation requirements
BuildRequires: openjade, python2, jadetex, libxslt
BuildRequires: docbook-style-dsssl, docbook-utils
BuildRequires: transfig, xfig, netpbm-progs, ghostscript

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.


%package devel
Summary: Libraries/include files for GStreamer streaming media framework
Group: Development/Libraries
Requires: %{name} = %{version}
Requires: glib2-devel >= %{glib2minver}
Requires: libxml2-devel >= %{libxml2minver}
Provides: gstreamer-devel = %{version}-%{release}
Provides: gstreamer-devel = %{majmin}

%description devel
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains the libraries and includes files necessary to develop
applications and plugins for GStreamer %{majmin}, as well as general and API
documentation.


%package -n gstreamer-tools
Summary: Common tools and files for the GStreamer media framework
Group: Applications/Multimedia

%description -n gstreamer-tools
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains wrapper scripts for the command-line tools that work
with different major/minor versions of GStreamer.


%prep
%setup -n gstreamer-%{version}
# Workaround a glib 2.3 problem for now
%{__rm} -f gst/gstmarshal.{c,h}


%build
#{?__libtoolize:[ -f configure.in ] && %{__libtoolize} --copy --force}
%configure \
    --disable-docs-build \
    --disable-tests \
    --disable-examples \
    --enable-debug \
    --with-cachedir=%{_localstatedir}/cache/gstreamer-%{majmin}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang gstreamer-%{majmin}

# Remove .la files and static libs that we don't want in the packages
%{__rm} -f %{buildroot}%{_libdir}/gstreamer-%{majmin}/*.{a,la}
%{__rm} -f %{buildroot}%{_libdir}/*.{a,la}
# Create empty cache directory
%{__mkdir_p} %{buildroot}%{_localstatedir}/cache/gstreamer-%{majmin}


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig
%{_bindir}/gst-register-%{majmin} &>/dev/null || :

%postun -p /sbin/ldconfig


%files -f gstreamer-%{majmin}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING* ChangeLog DEVEL NEWS README TODO
%{_bindir}/gst-complete-%{majmin}
%{_bindir}/gst-compprep-%{majmin}
%{_bindir}/gst-feedback-%{majmin}
%{_bindir}/gst-inspect-%{majmin}
%{_bindir}/gst-launch-%{majmin}
%{_bindir}/gst-md5sum-%{majmin}
%{_bindir}/gst-register-%{majmin}
%{_bindir}/gst-typefind-%{majmin}
%{_bindir}/gst-xmlinspect-%{majmin}
%{_bindir}/gst-xmllaunch-%{majmin}
%{_libdir}/gstreamer-%{majmin}
%{_libdir}/*.so.*
%{_mandir}/man1/gst-complete-%{majmin}.*
%{_mandir}/man1/gst-compprep-%{majmin}.*
%{_mandir}/man1/gst-feedback-%{majmin}.*
%{_mandir}/man1/gst-inspect-%{majmin}.*
%{_mandir}/man1/gst-launch-%{majmin}.*
%{_mandir}/man1/gst-md5sum-%{majmin}.*
%{_mandir}/man1/gst-register-%{majmin}.*
%{_mandir}/man1/gst-typefind-%{majmin}.*
%{_mandir}/man1/gst-xmllaunch-%{majmin}.*
%dir %{_localstatedir}/cache/gstreamer-%{majmin}


%files -n gstreamer-tools
%defattr(-, root, root, 0755)
%{_bindir}/gst-complete
%{_bindir}/gst-compprep
%{_bindir}/gst-feedback
%{_bindir}/gst-inspect
%{_bindir}/gst-launch
%{_bindir}/gst-md5sum
%{_bindir}/gst-register
%{_bindir}/gst-typefind
%{_bindir}/gst-xmlinspect
%{_bindir}/gst-xmllaunch


%files devel
%defattr(-, root, root, 0755)
%{_includedir}/gstreamer-%{majmin}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4


%changelog
* Fri Feb 27 2004 Matthias Saou <http://freshrpms.net/> 0.7.5-0.1
- Update to 0.6.5 and 0.7.5.
- Major spec file changes to sync 0.6 and 0.7 builds.
- Removed obsolete patches for 0.7.
- Update %%files to include %%{majmin} where required for 0.6 too.

* Fri Feb  6 2004 Matthias Saou <http://freshrpms.net/> 0.6.4-0.1
- Update to 0.6.4.
- Added missing BuildRequires for rebuilding with mach.

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
- stopped using %configure so we need to pass in all the args

* Mon Jan 27 2003 Jonathan Blandford <jrb@redhat.com>
- remove -Werror explicitly as the configure macro isn't working.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 19 2002 Elliot Lee <sopwith@redhat.com> 0.5.0-10
- Add patch1 to fix C++ plugins on ia64

* Wed Dec 18 2002 Jonathan Blandford <jrb@redhat.com>
- %post -p was wrong

* Tue Dec 17 2002 Jonathan Blandford <jrb@redhat.com> 0.5.0-7
- explicitly add %{_libdir}/libgstreamer-{major}.so
- explicitly add %{_libdir}/libgstcontrol-{major}.so

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

