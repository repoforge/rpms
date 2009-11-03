# $Id$
# Authority: dag

%define real_name gst-editor

Summary: GStreamer streaming media editor and GUI tools
Name: gstreamer-editor
Version: 0.7.0
Release: 1.2%{?dist}
License: LGPL
Group: Applications/Multimedia
URL: http://gstreamer.net/apps/gst-editor/

Source: http://gstreamer.freedesktop.org/src/gst-editor/gst-editor-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.0, libxml2-devel >= 2.0.0, libgnomeui-devel >= 1.109.0
BuildRequires: libglade2-devel >= 2, gstreamer-devel >= 0.8.0, scrollkeeper
BuildRequires: gcc-c++, gettext

Requires(post): scrollkeeper

%description
This package contains gst-editor and a few graphical tools.
gst-editor is a development tool for graphically creating
applications based on GStreamer.
gst-launch-gui is an extension of gst-launch allowing you to dynamically
turn on logging domains.
gst-inspect-gui is a graphical element browser.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
##%{?__libtoolize:[ -f configure.in ] && %{__libtoolize} --copy --force} ; \
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{real_name}

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null
scrollkeeper-update -q || :
#%{_prefix}/bin/gst-register --gst-mask=0

%postun
/sbin/ldconfig 2>/dev/null
scrollkeeper-update -q || :

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/gst-editor/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_datadir}/omf/gst-editor/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/gst-editor-%{version}/
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.0-1.2
- Rebuild for Fedora Core 5.

* Thu May 20 2004 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Sun May 11 2003 Dag Wieers <dag@wieers.com> - 0.5.0-0
- Initial package. (using DAR)
