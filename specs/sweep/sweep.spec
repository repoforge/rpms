# $Id$

# Authority: dag
# Conrad Parker <conrad@vergenet.net>

Summary: Sound wave editor
Name: sweep
Version: 0.8.2
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://sweep.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/sweep/sweep-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: tdb-devel >= 1.0.6, libsndfile-devel >= 1.0.1, libmad-devel
BuildRequires: gtk+-devel >= 1.2.0, libvorbis-devel, speex-devel

%description
Sweep is an editor for sound samples. It operates on files of various
formats such as .wav, .aiff and .au, and has multiple undo/redo levels
and filters. It supports audio filter plugins from the LADSPA project.

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
%configure \
	--libdir="%{_libdir}/sweep"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall libdir="%{buildroot}%{_libdir}/sweep"
%find_lang %{name}

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/sweep/*.{a,la,so.*}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog NEWS README* doc/*.txt
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/sweep/
%{_datadir}/pixmaps/*
%{_datadir}/sweep/
%{_datadir}/gnome/apps/Multimedia/*.desktop

%files devel
%defattr(-, root, root, 0755)
%doc doc/plugin_writers_guide.txt
%{_includedir}/sweep/

%changelog
* Fri May 02 2003 Dag Wieers <dag@wieers.com> - 0.8.2-0
- Initial package. (using DAR)
