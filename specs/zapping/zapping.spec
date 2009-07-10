# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}
%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

%define prever cvs6

Summary: TV viewer for GNOME
Name: zapping
Version: 0.10
Release: 0.4%{?prever:.%{prever}}
License: GPL
Group: Applications/Multimedia
URL: http://zapping.sourceforge.net/
Source: http://dl.sf.net/zapping/zapping-%{version}%{?prever}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libgnomeui-devel, libglade2-devel, gtk2-devel >= 2.4
BuildRequires: scrollkeeper, gettext, libjpeg-devel, libpng-devel
BuildRequires: zvbi-devel, arts-devel, lirc-devel
BuildRequires: python-devel, desktop-file-utils, gcc-c++, intltool
%{!?_without_modxorg:BuildRequires: libXt-devel, libXv-devel, libXmu-devel, libXxf86dga-devel, libXxf86vm-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_rte:BuildRequires: rte-devel >= 0.5}
# This one is to get /usr/bin/consolehelper
BuildRequires: usermode

%description
Zapping is a TV viewer for the GNOME desktop. It has all the needed
features, plus extensibility through a plugin system.


%prep
%setup -n %{name}-%{version}%{?prever}


%build
%configure
# Workaround (still required in 0.10cvs)
%{__perl} -pi.orig -e 's|\${prefix}/lib/|\${libdir}/|g' configure*
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}


%post
scrollkeeper-update -q || :
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%postun
scrollkeeper-update -q || :


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README* THANKS TODO
%config %{_sysconfdir}/gconf/schemas/%{name}.schemas
%config %{_sysconfdir}/pam.d/zapping_setup_fb
%config %{_sysconfdir}/security/console.apps/zapping_setup_fb
%{_bindir}/*
%{_libdir}/%{name}/
%exclude %{_libdir}/%{name}/plugins/*.la
%{_sbindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome/help/%{name}/
%{_datadir}/omf/%{name}/
%{_datadir}/pixmaps/%{name}/
%{_datadir}/%{name}/
%{_mandir}/man1/*


%changelog
* Mon Jun 09 2008 Dag Wieers <dag@wieers.com> - 0.10-0.4.cvs6
- Rebuild against zvbi-0.2.30.

* Mon Sep 18 2006 Matthias Saou <http://freshrpms.net/> 0.10-0.3.cvs6
- Update to 0.10cvs6.

* Wed Mar 22 2006 Matthias Saou <http://freshrpms.net/> 0.10-0.3.cvs4
- Add missing modular X build requirements.
- Re-enable rte on all archs since it builds on x86_64 and ppc again.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.10-0.2.cvs4
- Update to 0.10cvs4.

* Fri Jan 13 2006 Matthias Saou <http://freshrpms.net/> 0.10-0.1.cvs
- Update to 0.10cvs.
- Add modular xorg build conditional.
- Exclude .la files from plugins.
- Update lib vs. lib64 workaround for the plugins.

* Mon Jul 18 2005 Matthias Saou <http://freshrpms.net/> 0.9.7-0.1.cvs
- Update to 0.9.7cvs.

* Sun Apr 17 2005 Matthias Saou <http://freshrpms.net/> 0.9.3-1
- Update to 0.9.3.

* Tue Mar  1 2005 Matthias Saou <http://freshrpms.net/> 0.9.2-1
- Update to 0.9.2.
- Man pages are back.
- Added new GConf entry and import in %%post.

* Sun Feb 20 2005 Matthias Saou <http://freshrpms.net/> 0.9.1-1
- Update to 0.9.1.
- Man pages are no longer installed automatically.
- Disable rte support on non-x86 as rte only builds on x86 (asm).

* Thu Nov 11 2004 Matthias Saou <http://freshrpms.net/> 0.8-1
- Update to 0.8.
- Change desktop file installation, as it's a GNOME 2 one at last.

* Sat Oct 16 2004 Matthias Saou <http://freshrpms.net/> 0.7.3-2
- Added scrollkeeper-update scriplet calls.

* Wed Oct 13 2004 Matthias Saou <http://freshrpms.net/> 0.7.3-1
- Update to 0.7.3.

* Mon Oct  4 2004 Matthias Saou <http://freshrpms.net/> 0.7.2-1
- Update to 0.7.2.

* Thu Jul 15 2004 Matthias Saou <http://freshrpms.net/> 0.7-1
- Update to 0.7 final.

* Fri May 21 2004 Matthias Saou <http://freshrpms.net/> 0.7.0-0.cvs7.1
- Rebuild for Fedora Core 2.
- Update to 0.7cvs7.
- Removed explicit stripping, that's for the debuginfo now.
- No longer require the "absolute buildroot path in symlink" fix.

* Tue Jan 20 2004 Matthias Saou <http://freshrpms.net/> 0.7.0-0.cvs6.1
- Update to 0.7cvs6.
- Major spec file changes to relect the GNOME1 -> GNOME2 step.

* Fri Dec 12 2003 Matthias Saou <http://freshrpms.net/> 0.6.8-1
- Update to 0.6.8.
- Rebuild for Fedora Core 1 at last.

* Mon Jun  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.7.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Mar 20 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.6.

* Wed Oct  9 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.5.

* Sat Sep 28 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.

* Tue Aug  6 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.4.
- Spec file cleanup.

* Thu Nov 22 2001 Matthias Saou <http://freshrpms.net/>
- Update (at last!) to 0.6.1.
- Added the manpages and quick spec file cleanup as usual.

* Tue May 15 2001 Matthias Saou <http://freshrpms.net/>
- Replaced the pre/post sections with a real link in the package.

* Fri Feb  2 2001 Tim Powers <timp@redhat.com>
- pamified zapping_setup_fb, now no need for suid root bits, and no
crippling of the app :)

* Thu Sep 12 2000 Iñaki García Etxebarria <garetxe@users.sourceforge.net>
- Removed the LibPng dependency, now libjpeg is used.

* Mon Sep 11 2000 Iñaki García Etxebarria <garetxe@users.sourceforge.net>
- Added the dependency to GdkPixbuf and LibPng

* Mon Jun 19 2000 Iñaki García Etxebarria <garetxe@users.sourceforge.net>
- Added the desktop entry and removed the specified --datadir

* Mon Jun 12 2000 Iñaki García Etxebarria <garetxe@users.sourceforge.net>
- Fixed, it didn't include the translations properly.

* Thu Jun 06 2000 Iñaki García Etxebarria <garetxe@users.sourceforge.net>
- Created, it works fine.

