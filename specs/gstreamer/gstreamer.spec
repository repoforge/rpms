%define		majorminor	0.8
%define 	_glib2		2.2
%define 	_libxml2	2.4.0
%define		gstreamer	gstreamer
%define		register	%{_bindir}/gst-register-%{majorminor} >/dev/null 2>&1 || :

Name: 		%{gstreamer}
Version: 	0.8.1
Release: 	0
Summary: 	GStreamer streaming media framework runtime

Group: 		Applications/Multimedia
License: 	LGPL
URL:		http://gstreamer.net/
Source: 	http://freedesktop.org/~gstreamer/src/gstreamer/gstreamer-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	gstreamer-tools >= %{version}

Obsoletes:	gstreamer08

BuildRequires: 	glib2-devel >= %{_glib2}
BuildRequires: 	libxml2-devel >= %{_libxml2}
BuildRequires: 	bison
BuildRequires: 	flex
BuildRequires: 	m4
BuildRequires: 	gtk-doc >= 1.1
BuildRequires: 	gcc
BuildRequires: 	zlib-devel
BuildRequires:  popt > 1.6
BuildRequires:	gettext
# because AM_PROG_LIBTOOL was used in configure.ac
BuildRequires:	gcc-c++
Requires(pre):	/sbin/ldconfig
Requires(post):	/sbin/ldconfig

### documentation requirements; work on rh9 and f1
BuildRequires:  python2
BuildRequires:  openjade
BuildRequires:  jadetex
BuildRequires:	libxslt
BuildRequires:  docbook-style-dsssl
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook-utils
BuildRequires:	transfig
BuildRequires:  xfig
BuildRequires:  netpbm-progs
BuildRequires:  tetex-dvips
BuildRequires:  ghostscript

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

%package devel
Summary: 	Libraries/include files for GStreamer streaming media framework
Group: 		Development/Libraries

Requires: 	%{name} = %{version}
Requires: 	glib2-devel >= %{_glib2}
Requires: 	libxml2-devel >= %{_libxml2}

Obsoletes:	gstreamer08-devel

%description devel
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new   
plugins.

This package contains the libraries and includes files necessary to develop
applications and plugins for GStreamer, as well as general and API
documentation.

%package -n gstreamer-tools
Summary: 	common tools and files for GStreamer streaming media framework
Group: 		Applications/Multimedia

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
%setup -q -n gstreamer-%{version}

# 0.7.5 tarball was generated with glib 2.3, and the gstmarshal files
# are included; so delete them to regenerate them.
rm -f gst/gstmarshal.{c,h}

%build
%configure \
  --enable-debug \
  --with-cachedir=%{_localstatedir}/cache/gstreamer-%{majorminor} \
  --disable-tests \
  --disable-examples

make %{?_smp_mflags}

%install  
rm -rf $RPM_BUILD_ROOT

# Install doc temporarily in order to be included later by rpm
%makeinstall docdir="`pwd`/installed-doc"

%find_lang gstreamer-%{majorminor}
# Clean out files that should not be part of the rpm. 
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/gstreamer-%{majorminor}
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
# Create empty cache directory
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/gstreamer-%{majorminor}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%{register}

%postun
/sbin/ldconfig
rm -rf %{_localstatedir}/cache/gstreamer-%{majorminor} || :

%files -f gstreamer-%{majorminor}.lang
%defattr(-, root, root, -)
%doc AUTHORS COPYING NEWS README RELEASE TODO REQUIREMENTS DOCBUILDING
%dir %{_libdir}/gstreamer-%{majorminor}
%{_libdir}/libgstreamer-%{majorminor}.so.*
%{_libdir}/libgstcontrol-%{majorminor}.so.*
%{_libdir}/gstreamer-%{majorminor}/libgstbasicgthreadscheduler.so
%{_libdir}/gstreamer-%{majorminor}/libgstbasicomegascheduler.so
%{_libdir}/gstreamer-%{majorminor}/libgstentrygthreadscheduler.so
%{_libdir}/gstreamer-%{majorminor}/libgstentryomegascheduler.so
%{_libdir}/gstreamer-%{majorminor}/libgstoptscheduler.so
%{_libdir}/gstreamer-%{majorminor}/libgstoptomegascheduler.so
%{_libdir}/gstreamer-%{majorminor}/libgstoptgthreadscheduler.so
%{_libdir}/gstreamer-%{majorminor}/libgstelements.so
%{_libdir}/gstreamer-%{majorminor}/libgstgetbits.so
%{_libdir}/gstreamer-%{majorminor}/libgstspider.so
%{_libdir}/gstreamer-%{majorminor}/libgstindexers.so
%{_libdir}/gstreamer-%{majorminor}/libgstbytestream.so
%{_bindir}/gst-complete-%{majorminor}
%{_bindir}/gst-compprep-%{majorminor}
%{_bindir}/gst-feedback-%{majorminor}
%{_bindir}/gst-inspect-%{majorminor}
%{_bindir}/gst-launch-%{majorminor}
%{_bindir}/gst-md5sum-%{majorminor}
%{_bindir}/gst-register-%{majorminor}
%{_bindir}/gst-typefind-%{majorminor}
%{_bindir}/gst-xmlinspect-%{majorminor}
%{_bindir}/gst-xmllaunch-%{majorminor}
%{_mandir}/man1/gst-complete-%{majorminor}.*
%{_mandir}/man1/gst-compprep-%{majorminor}.*
%{_mandir}/man1/gst-feedback-%{majorminor}.*
%{_mandir}/man1/gst-inspect-%{majorminor}.*
%{_mandir}/man1/gst-launch-%{majorminor}.*
%{_mandir}/man1/gst-md5sum-%{majorminor}.*
%{_mandir}/man1/gst-register-%{majorminor}.*
%{_mandir}/man1/gst-typefind-%{majorminor}.*
%{_mandir}/man1/gst-xmllaunch-%{majorminor}.*
%dir %{_localstatedir}/cache/gstreamer-%{majorminor}

%files -n gstreamer-tools
%defattr(-, root, root, -)
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
%defattr(-, root, root, -)
%doc installed-doc/*
%dir %{_includedir}/gstreamer-%{majorminor}
%dir %{_includedir}/gstreamer-%{majorminor}/gst
%{_includedir}/gstreamer-%{majorminor}/gst/*.h
%dir %{_includedir}/gstreamer-%{majorminor}/gst/control
%{_includedir}/gstreamer-%{majorminor}/gst/control/*.h
%dir %{_includedir}/gstreamer-%{majorminor}/gst/getbits
%{_includedir}/gstreamer-%{majorminor}/gst/getbits/getbits.h
%{_includedir}/gstreamer-%{majorminor}/gst/bytestream/bytestream.h
%{_libdir}/libgstreamer-%{majorminor}.so
%{_libdir}/libgstcontrol-%{majorminor}.so
%{_datadir}/aclocal/gst-element-check-%{majorminor}.m4
%{_libdir}/pkgconfig/gstreamer-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-control-%{majorminor}.pc

%doc %{_datadir}/gtk-doc/html/gstreamer-%{majorminor}/*
%doc %{_datadir}/gtk-doc/html/gstreamer-libs-%{majorminor}/*

%changelog
* Mon Apr 19 2004 Mattias Saou <http://fresrhrpms.net/> 0.8.1-0
- Nothing :-)

* Thu Apr 15 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.1-0.fdr.1: update for new GStreamer release

* Thu Apr 15 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- add entry schedulers, clean up scheduler file section

* Tue Mar 16 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.0-0.fdr.1: update for new GStreamer release, renamed base to gstreamer

* Tue Mar 09 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.6-0.fdr.1: updated for new GStreamer release, with maj/min set to 0.8

* Mon Mar 08 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.5-0.fdr.3: fix postun script

* Fri Mar 05 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.5-0.fdr.2: new release

* Wed Feb 11 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.4-0.fdr.1: synchronize with Matthias's package

* Sat Feb 07 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- make the package name gstreamer07 since this is an unstable release

* Wed Feb 04 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- put versioned tools inside base package, and put unversioned tools in tools

* Mon Dec 01 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- changed documentation buildrequires

* Sun Nov 09 2003 Christian Schaller <Uraeus@gnome.org>
- Fix spec to handle new bytestream library 

* Sun Aug 17 2003 Christian Schaller <uraeus@gnome.org>
- Remove docs build from RPM as the build is broken
- Fix stuff since more files are versioned now
- Remove wingo schedulers
- Remove putbits stuff

* Sun May 18 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- devhelp files are now generated by gtk-doc, changed accordingly

* Sun Mar 16 2003 Christian F.K. Schaller <Uraeus@gnome.org>
- Add gthread scheduler

* Sat Dec 07 2002 Thomas Vander Stichele <thomas at apestaart dot org>
- define majorminor and use it everywhere
- full parallel installability

* Tue Nov 05 2002 Christian Schaller <Uraeus@linuxrising.org>
- Add optwingo scheduler
* Sat Oct 12 2002 Christian Schaller <Uraeus@linuxrising.org>
- Updated to work better with default RH8 rpm
- Added missing unspeced files
- Removed .a and .la files from buildroot

* Sat Sep 21 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added gst-md5sum

* Tue Sep 17 2002 Thomas Vander Stichele <thomas@apestaart.org>
- adding flex to buildrequires

* Fri Sep 13 2002 Christian F.K. Schaller <Uraeus@linuxrising.org>
- Fixed the schedulers after the renaming
* Sun Sep 08 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added transfig to the BuildRequires:

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

