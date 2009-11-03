# $Id$
# Authority: matthias

%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{!?dtag:%define _with_gettextdevel 1}
%{?el5:  %define _with_gettextdevel 1}
%{?fc6:  %define _with_gettextdevel 1}
%{?fc5:  %define _with_gettextdevel 1}
%{?fc4:  %define _with_gettextdevel 1}
%{?fc3:  %define _with_gettextdevel 1}

#define date 20041213
%define prever beta2

Summary: Complete GTK frontend for xmame
Name: gxmame
Version: 0.35
Release: 0.4%{?date:.%{date}}%{?prever:.%{prever}}%{?dist}
License: GPL
Group: Applications/Emulators
URL: http://gxmame.sourceforge.net/
Source: http://dl.sf.net/gxmame/gxmame-%{version}%{?date:cvs}%{?prever}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xmame >= 0.77.1
BuildRequires: gtk2-devel >= 2.4, zlib-devel, expat-devel, intltool, gettext
%{?_with_gettextdevel:BuildRequires: gettext-devel}

%description
GXMame is a frontend for XMame using the GTK library, the goal is to provide
the same GUI than mame32. For the moment it will just have the same gui, the
final goal is to be able to share config files with Mame32k (or any version
of mame32 that writes config files instead of saving data into windows
registery) allowing dual booter to have the same environment (favorite,
times played, last game selected, gui preference...) under windows and Linux.


%prep
%setup -n %{name}-%{version}%{?date:cvs}%{?prever}


%build
%configure \
    --with-xmame-dir="%{_datadir}/xmame" \
    --enable-joystick
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
%{_bindir}/gxmame
%{_datadir}/applications/gxmame.desktop
%{_datadir}/pixmaps/gxmame.png
%exclude %{_datadir}/pixmaps/gxmame.xpm
%{_datadir}/gxmame/
%{_mandir}/man6/gxmame.6*


%changelog
* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.35-0.4.beta2
- Release bump to drop the disttag number in FC5 build.

* Thu Jan 12 2006 Matthias Saou <http://freshrpms.net/> 0.35-0.3.beta2
- Add FC5 to the build conditionals.

* Sat Jul 30 2005 Matthias Saou <http://freshrpms.net/> 0.35-0.2.beta2
- Remove the xpm icon, only the png one is used.

* Thu May  5 2005 Matthias Saou <http://freshrpms.net/> 0.35-0.1.beta2
- Update to 0.35beta2.
- Remove optfree patch.

* Wed Mar 16 2005 Matthias Saou <http://freshrpms.net/> 0.35-0.beta1.2
- Add gxmame-0.35beta1-optfree.patch to fix crash, as reported by Motor.
- Add _with_gettextdevel build option.

* Mon Feb 14 2005 Matthias Saou <http://freshrpms.net/> 0.35-0.beta1.1
- Update to 0.35beta1.

* Mon Dec 13 2004 Matthias Saou <http://freshrpms.net/> 0.35-0.20041213.1
- Update to today's CVS.

* Mon Nov 29 2004 Matthias Saou <http://freshrpms.net/> 0.35-0.20041129.1
- Update to today's CVS version from the Next-Version-0-40 branch.
- Added --with-xmame-dir configure option.
- Enable joystick.

* Tue Oct  5 2004 Matthias Saou <http://freshrpms.net/> 0.35-0.20041005.1
- Update to today's CVS version, change the spec to build already "make dist"
  passed tarballs.

* Sat Aug 28 2004 Matthias Saou <http://freshrpms.net/> 0.35-0.20040828.1
- Update to today's CVS version to work with xmame 0.86 (xil option).

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

