# $Id: glabels.spec 5993 2007-11-16 02:17:11Z dag $
# Authority: dag
# Upstream: Jim Evins <evins$snaught,com>


#%{?el4:#define _without_shared_mime 1}
#%{?fc3:#define _without_shared_mime 1}
#%{?fc1:#define _without_shared_mime 1}
#%{?el3:#define _without_shared_mime 1}
#%{?rh9:#define _without_shared_mime 1}

Summary: GUI program to create labels and business cards
Name: glabels
Version: 2.0.4
Release: 1.2%{?dist}
License: GPL
Group: Applications/Publishing
URL: http://snaught.com/glabels/

Source: http://dl.sf.net/glabels/glabels-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libxml2-devel >= 2.4, libgnomeui-devel >= 2.0, libglade2-devel >= 2.0.1
BuildRequires: gtk+-devel >= 1.2, libgnomecanvas-devel >= 2.0, gcc-c++, gettext
BuildRequires: libgnomeprint22-devel, libgnomeprintui22-devel, scrollkeeper
BuildRequires: desktop-file-utils, intltool, perl(XML::Parser)
#BuildRequires: libgnomeprint-devel >= 0.115

%description
gLabels is a lightweight program for creating labels and
business cards for the GNOME desktop environment.
It is designed to work with various laser/ink-jet peel-off
label and business card sheets that you'll find at most office
supply stores.

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

%{__cat} <<EOF >data/desktop/glabels.desktop.in
[Desktop Entry]
Name=Glabels Label Designer
Comment=Create labels, business cards and media covers
Icon=glabels.png
Exec=glabels %F
Terminal=false
Type=Application
Categories=GNOME;Application;Office;
MimeType=application/x-glabels;
StartupNotify=true
Encoding=UTF-8
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	UPDATE_DESKTOP_DATABASE="echo" \
	UPDATE_MIME_DATABASE="echo"
%find_lang %{name}

desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--dir %{buildroot}%{_datadir}/applications    \
	%{buildroot}%{_datadir}/applications/glabels.desktop

%post
scrollkeeper-update -q || :
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :

%postun
scrollkeeper-update -q || :
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_datadir}/gnome/help/glabels/
%doc %{_mandir}/man1/glabels.1*
%{_bindir}/glabels*
%{_libdir}/libglabels.so.*
%{_datadir}/application-registry/glabels.applications
%{_datadir}/applications/gnome-glabels.desktop
%{_datadir}/glabels/
#%{_datadir}/mime/application/x-glabels.xml
#%exclude %{_datadir}/mime/XMLnamespaces
#%exclude %{_datadir}/mime/globs
#%exclude %{_datadir}/mime/magic
#%{!?_without_shared_mime:%{_datadir}/mime/application/x-glabels.xml}
#%{!?_without_shared_mime:%exclude %{_datadir}/mime/XMLnamespaces}
#%{!?_without_shared_mime:%exclude %{_datadir}/mime/globs}
#%{!?_without_shared_mime:%exclude %{_datadir}/mime/magic}
%{_datadir}/mime/packages/glabels.xml
%{_datadir}/mime-info/glabels.*
%{_datadir}/pixmaps/glabels/
%{_datadir}/pixmaps/glabels.png
%{_datadir}/pixmaps/glabels-application-x-glabels.png
%{_datadir}/omf/glabels/
%exclude %{_localstatedir}/scrollkeeper

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libglabels/
%{_libdir}/libglabels.so
%{_libdir}/libglabels.a
%exclude %{_libdir}/libglabels.la

%changelog
* Thu Dec 29 2005 Dag Wieers <dag@wieers.com> - 2.0.4-1
- Updated to release 2.0.4.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 2.0.3-1
- Updated to release 2.0.3.

* Mon Jan 24 2005 Dag Wieers <dag@wieers.com> - 2.0.2-1
- Updated to release 2.0.2.

* Sun Aug 15 2004 Dag Wieers <dag@wieers.com> - 2.0.1-1
- Updated to release 2.0.1.

* Mon Aug 09 2004 Dag Wieers <dag@wieers.com> - 2.0.0-1
- Updated to release 2.0.0.

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
