# $Id$
# Authority: dries
# Upstream: Petri Damstén <petri,damsten$iki,fi>

Summary: Template-based DVD authoring tool
Name: kmediafactory
Version: 0.6.0
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.iki.fi/damu/software/kmediafactory/index.html

Source: http://aryhma.oy.cx/damu/software/kmediafactory/kmediafactory-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, kdelibs-devel, gcc-c++, libdvdread-devel, xine-lib-devel

%description
KMediaFactory is easy to use template-based DVD authoring tool for KDE. You 
can quickly create DVD menus for home videos and TV recordings in three simple 
steps. The actual authoring is done with tools like dvdauthor, ffmpeg, 
ImageMagick and others.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" UNOPKG=echo kde_widgetdir=%{buildroot}%{_libdir}/kde3/plugins/designer
%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL NEWS README TODO
%{_bindir}/kmediafactory
%{_bindir}/kmediafactoryplayer
%{_bindir}/kmf_dvb_edit.sh
%{_libdir}/kde3/kmediafactory*
%{_libdir}/kde3/plugins/designer/kmfwidgets.*
%{_datadir}/applnk/Utilities/kmediafactory*
%{_datadir}/apps/kmediafactory/
%{_datadir}/apps/kmediafactory_dvimport/
%{_datadir}/apps/kmediafactory_output/
%{_datadir}/apps/kmediafactory_slideshow/
%{_datadir}/apps/kmediafactory_template/
%{_datadir}/apps/kmediafactory_video/
%{_datadir}/apps/kmfwidgets/
%{_datadir}/doc/HTML/en/kmediafactory/
%{_datadir}/icons/crystalsvg/*/*/kmediafactory*
%{_datadir}/icons/crystalsvg/*/*/add_video.*
%{_datadir}/mimelnk/application/x-kmediafactory.desktop
%{_datadir}/services/kmediafactory_*.desktop
%{_datadir}/services/*plugin.kcfg
%{_datadir}/servicetypes/kmediafactoryplugin.desktop
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/kmediafactory_*.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/kmediafactory_*.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/libkmf.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/libkmf.mo
%{_libdir}/libkmediafactoryinterfaces.so.*
%{_libdir}/libkmediafactoryinterfaces.la
%{_libdir}/libkmf.so.*
%{_libdir}/libkmf.la

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/kmediafactory/
%{_includedir}/koStore*.h
%{_libdir}/libkmediafactoryinterfaces.so
%{_libdir}/libkmf.so

%changelog
* Thu Feb  7 2008 Dries Verachtert <dries@ulyssis.org> - 0.6.0-1
- Updated to release 0.6.0.

* Fri Aug 11 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.1-1
- Initial package.
