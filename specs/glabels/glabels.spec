# Authority: dag
# Upstream: Jim Evins <evins@snaught.com>

Summary: GUI program to create labels and business cards.
Name: glabels
Version: 1.93.3
Release: 0
License: GPL
Group: Applications/Publishing
URL: http://snaught.com/glabels/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/glabels/glabels-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libxml2-devel >= 2.4, libgnomeui-devel >= 2.0, libglade2-devel >= 2.0.1
BuildRequires: gtk+-devel >= 1.2, libgnomecanvas-devel >= 2.0
#BuildRequires: libgnomeprint-devel >= 0.115

%description
gLabels is a lightweight program for creating labels and
business cards for the GNOME desktop environment.
It is designed to work with various laser/ink-jet peel-off
label and business card sheets that you'll find at most office
supply stores.

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

%{__cat} <<EOF >data/%{name}.desktop.in
[Desktop Entry]
Name=Glabels Label Designer
Comment=Create labels, business cards and media covers.
Icon=glabels.png
Exec=glabels
Terminal=false
Type=Application
Categories=GNOME;Application;Office;
StartupNotify=true
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--dir %{buildroot}%{_datadir}/applications    \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/*.la

%post
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_datadir}/gnome/help/glabels/
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/application-registry/*.applications
%{_datadir}/applications/*.desktop
%{_datadir}/glabels/
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/glabels/
%{_datadir}/pixmaps/*.png
%{_datadir}/omf/glabels/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libglabels/
%{_libdir}/*.a

%changelog
* Sun Feb 22 2004 Dag Wieers <dag@wieers.com> - 1.93.3-0
- Updated to release 1.93.3.

* Sun Jan 04 2004 Dag Wieers <dag@wieers.com> - 1.93.2-0
- Updated to release 1.93.2.

* Wed Dec 24 2003 Dag Wieers <dag@wieers.com> - 1.93.1-0
- Updated to release 1.93.1.

* Mon Dec 01 2003 Dag Wieers <dag@wieers.com> - 1.93.0-0
- Updated to release 1.93.0.

* Mon Nov 17 2003 Dag Wieers <dag@wieers.com> - 1.92.3-0
- Updated to release 1.92.3.

* Sun Nov 02 2003 Dag Wieers <dag@wieers.com> - 1.92.2-0
- Updated to release 1.92.2.

* Tue Oct 28 2003 Dag Wieers <dag@wieers.com> - 1.92.1-0
- Removed duplicate desktop entry. (Zdravko Nikolov)
- Updated to release 1.92.1.

* Mon Sep 22 2003 Dag Wieers <dag@wieers.com> - 1.92.0-1
- Added a proper desktop file.

* Thu Sep 04 2003 Dag Wieers <dag@wieers.com> - 1.92.0-0
- Updated to release 1.92.0.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 1.91.1-0
- Updated to release 1.91.1.

* Wed Jan 01 2003 Dag Wieers <dag@wieers.com> - 1.91.0-0
- Updated to release 1.91.0.

* Mon Dec 30 2002 Dag Wieers <dag@wieers.com> - 1.90.0-0
- Updated to release 1.90.0.

* Sat Oct 05 2002 Dag Wieers <dag@wieers.com> - 0.4.4
- Made use of macros.

* Sat May 19 2001 Jim Evins <evins@snaught.com>
- Initial release.
