# $Id$
# Authority: matthias

#define date           20031202

Summary: Complete GTK frontend for xmame
Name: gxmame
Version: 0.34b
Release: %{?date:0.%{date}.}3
License: GPL
Group: Applications/Emulators
URL: http://gxmame.sourceforge.net/
Source: http://dl.sf.net/gxmame/gxmame-%{!?date:%{version}}%{?date}.tar.gz
Patch: gxmame-xml.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xmame >= 0.77.1, %{_bindir}/xml2info
BuildRequires: gtk2-devel, zlib-devel, gettext
%if %{?date:1}%{!?date:0}
BuildRequires: automake, autoconf, cvs
%endif

%description
GXMame is a frontend for XMame using the GTK library, the goal is to provide
the same GUI than mame32. For the moment it will just have the same gui, the
final goal is to be able to share config files with Mame32k (or any version
of mame32 that writes config files instead of saving data into windows
registery) allowing dual booter to have the same environement (favorite,
times played, last game selected, gui preference...) under windows and Linux.


%prep
%setup -n %{name}-%{!?date:%{version}}%{?date}
%patch -p1 -b .xml


%build
test -x configure || ./autogen.sh
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot} _docs
%makeinstall
%find_lang %{name}

# Put the docs back into place
%{__mkdir} _docs
%{__mv} %{buildroot}%{_docdir}/%{name}*/* _docs/


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc _docs/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/%{name}.png
%{_datadir}/icons/mini/%{name}.xpm


%changelog
* Sun Jul 18 2004 Matthias Saou <http://freshrpms.net/> 0.34b-3
- Added patch for the -li option removed, so added %{_bindir}/xml2info req.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.34b-2
- Rebuilt for Fedora Core 2.

* Sun Jan  4 2004 Matthias Saou <http://freshrpms.net/> 0.34b-1
- Update to 0.34b.

* Tue Dec 16 2003 Matthias Saou <http://freshrpms.net/> 0.34-1
- Update to 0.34 final.

* Wed Nov 19 2003 Matthias Saou <http://freshrpms.net/> 0.34-0.20031202.1
- Update to today's CVS checkout.

* Wed Nov 19 2003 Matthias Saou <http://freshrpms.net/> 0.34-0.20031119.1
- Update to today's CVS checkout.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.33-3
- Rebuild for Fedora Core 1.

* Tue Oct 21 2003 Matthias Saou <http://freshrpms.net/>
- Added the patch to handle xmame >= 0.74 cleanly at last.

* Thu Jun 12 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.33.

* Tue May 27 2003 Matthias Saou <http://freshrpms.net/>
- Removed patch since xmame 0.69.1 is back to the old behavior.

* Fri May 23 2003 Matthias Saou <http://freshrpms.net/>
- Added patch to work with xmame 0.68.1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Mon Mar 24 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.32.

* Wed Mar 19 2003 Matthias Saou <http://freshrpms.net/>
- Added --without freedesktop build option.

* Mon Jan 13 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.31.

* Mon Nov 25 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.30 final.

* Tue Nov 12 2002 Matthias Saou <http://freshrpms.net/>
- Fixed menu entry by adding "ArcadeGame".
- Added XFX fix patch.

* Sun Oct 27 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.28.
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.

* Wed Aug  7 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.27.

* Thu Aug  1 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.
- Added missing pixmaps/gxmame to %%files.

