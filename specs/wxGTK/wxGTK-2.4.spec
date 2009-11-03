# $Id: wxGTK.spec 2396 2004-11-03 09:56:48Z dude $
# Authority: matthias

Summary: The GTK port of the wxWindows library
Name: wxGTK
Version: 2.4.2
Release: 5%{?dist}
License: Other
Group: System Environment/Libraries
URL: http://www.wxwindows.org/
Source: http://dl.sf.net/wxwindows/wxGTK-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, gtk+-devel >= 1.2.0, zlib-devel
BuildRequires: libjpeg-devel, libpng-devel, libtiff-devel
# all packages providing an implementation of wxWindows library (regardless of
# the toolkit used) should provide the (virtual) wxwin package, this makes it
# possible to require wxwin instead of requiring "wxgtk or wxmotif or wxqt..."
Provides: wxwin

%description
wxWindows is a free C++ library for cross-platform GUI development.
With wxWindows, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.


%package devel
Summary: Develoment files of the GTK port of the wxWindows library
Group: Development/Libraries
Requires: %{name} = %{version}, gtk+-devel, pkgconfig
Requires: libpng-devel, libjpeg-devel, libtiff-devel

%description devel
Header files for wxGTK, the GTK port of the wxWindows library.


%package gl
Summary: OpenGL add-on of the the GTK port of the wxWindows library
Group: System Environment/Libraries
Requires: %{name} = %{version}

%description gl
OpenGL add-on library for wxGTK, the GTK port of the wxWindows library.


%package xrc
Summary: The XML-based resource system for the wxWindows library
Group: System Environment/Libraries
Requires: %{name} = %{version}

%description xrc
The XML-based resource system, known as XRC, allows user interface
elements such as dialogs, menu bars and toolbars, to be stored in
text files and loaded into the application at run-time.


%package stc
Summary: Styled text control add-on for the wxWindows library
Group: System Environment/Libraries
Requires: %{name} = %{version}

%description stc
Styled text control add-on for wxGTK. Based on the Scintillia project.


%prep
%setup
%{__perl} -pi.orig -e 's| /usr/lib| %{_libdir} %{_prefix}/X11R6/%{_lib}|g' \
    configure


%build
# For the shared libs
%configure \
    --x-libraries="%{_prefix}/X11R6/%{_lib}" \
    --enable-soname \
    --enable-optimise \
    --with-opengl
#   --enable-gtk2 \
%{__make} %{?_smp_mflags}

pushd contrib/src
    make -C xrc %{?_smp_mflags}
    make -C stc %{?_smp_mflags}
popd


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang wxstd

pushd contrib/src/
    %makeinstall -C xrc
    %makeinstall -C stc
popd


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post gl -p /sbin/ldconfig
%postun gl -p /sbin/ldconfig

%post xrc -p /sbin/ldconfig
%postun xrc -p /sbin/ldconfig

%post stc -p /sbin/ldconfig
%postun stc -p /sbin/ldconfig

%files -f wxstd.lang
%defattr(-, root, root, 0755)
%doc COPYING.LIB *.txt
%{_libdir}/libwx_gtk-*
%{_datadir}/wx/

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/*-config
%{_includedir}/wx/
%{_libdir}/wx/
%{_datadir}/aclocal/*.m4

%files gl
%defattr(-, root, root, 0755)
%{_libdir}/libwx_gtk_gl-*

%files xrc
%defattr(-, root, root, 0755)
%{_libdir}/libwx_gtk_xrc-*

%files stc
%defattr(-, root, root, 0755)
%{_libdir}/libwx_gtk_stc-*


%changelog
* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 2.4.2-4
- Rebuilt for Fedora Core 2.

* Mon Nov 17 2003 Matthias Saou <http://freshrpms.net/> 2.4.2-3
- Revert back to gtk+, as gtk2 makes too many apps crash :-(

* Wed Nov 12 2003 Matthias Saou <http://freshrpms.net/> 2.4.2-2
- Disable unicode as it breaks building for most applications (thanks to
  Fabrice Bellet).

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 2.4.2-1
- Rebuild for Fedora Core 1.
- Update to 2.4.2.
- Switch to gtk2 by default.

* Sun Jun 15 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.4.1.

* Thu May 29 2003 Matthias Saou <http://freshrpms.net/>
- Fixed dependencies by adding --enable-soname thanks to Fabrice Bellet.
- Added stc sub-package thanks to Jean-Michel POURE.

* Tue May 27 2003 Matthias Saou <http://freshrpms.net/>
- Added xrc sub-package thanks to Bruno Postle.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sun Mar 23 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.4.0

* Sun Aug  4 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt without the NVIDIA_GLX package to fix dependencies.

* Thu Aug  1 2002 Matthias Saou <http://freshrpms.net/>
- Major spec file cleanup.

