# $Id$
# Authority: dag
# Conrad Parker <conrad@vergenet.net>

%define desktop_vendor rpmforge

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: Sound wave editor
Name: sweep
Version: 0.9.2
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://sweep.sourceforge.net/

Source: http://dl.sf.net/sweep/sweep-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, glib2-devel >= 2.2, gtk2-devel >= 2.4
BuildRequires: libvorbis-devel, speex-devel, libsndfile-devel >= 1.0.1, libmad-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Sweep is an editor for sound samples. It operates on files of various
formats such as .wav, .aiff and .au, and has multiple undo/redo levels
and filters. It supports audio filter plugins from the LADSPA project.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
	--libdir="%{_libdir}/sweep"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall libdir="%{buildroot}%{_libdir}/sweep"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog NEWS README* doc/*.txt
%doc %{_mandir}/man1/sweep.1*
%{_bindir}/sweep
%dir %{_libdir}/sweep/
%{_libdir}/sweep/*.so
%{_datadir}/pixmaps/sweep.svg
%{_datadir}/sweep/
%{_datadir}/applications/sweep.desktop

%files devel
%defattr(-, root, root, 0755)
%doc doc/plugin_writers_guide.txt
%{_includedir}/sweep/
%dir %{_libdir}/sweep/
#%{_libdir}/sweep/*.a
#%{_libdir}/sweep/*.la

%changelog
* Wed Feb 07 2007 Dag Wieers <dag@wieers.com> - 0.9.2-1
- Updated to release 0.9.2.

* Tue Jan 31 2006 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Fri Jan 27 2006 Dag Wieers <dag@wieers.com> - 0.9.0-1
- Updated to release 0.9.0.

* Sat Jun 06 2004 Dag Wieers <dag@wieers.com> - 0.8.3-2
- Add improved desktop file.

* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 0.8.3-1
- Updated to release 0.8.3.

* Fri May 02 2003 Dag Wieers <dag@wieers.com> - 0.8.2-0
- Initial package. (using DAR)
