# $Id$
# Authority: dag
# Upstream: <A,Eckleder$bigfoot,com>

### Goes into a loop with fc2/x86_64 (Please investigate)
##ExcludeDist: fc2i fc2a

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define real_version 1.0Beta6

Name: gtoaster
Summary: Versatile CD recording package for both sound and data
Version: 1.0
Release: 2.beta6.2%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://gnometoaster.rulez.org/

Source0: http://gnometoaster.rulez.org/archive/gtoaster%{real_version}.tgz
Source1: gtoaster.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: audiofile-devel, gnome-libs-devel, ORBit-devel
BuildRequires: libtool, autoconf, automake
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: cdrecord, cdrdao, mkisofs, cdda2wav, sox, mpg321
ExcludeArch: s390 s390x

%description
GNOME Toaster is a versatile CD creation suite.  It is designed to be
as user-friendly as possible, allowing you to create CD-ROMs with just
a few simple mouse clicks.  Audio and data CDs are both possible.
GNOME Toaster is also well integrated with the GNOME and KDE
filemanagers.

%prep
%setup -n %{name}

%{__cat} <<EOF >gtoaster.desktop
[Desktop Entry]
Name=Gnome Toaster
Comment=Create audio and data CDs
Icon=gtoaster.png
Exec=gtoaster
Terminal=false
Type=Application
Encoding=UTF-8
Categories=GNOME;Application;AudioVideo;
EOF

%{__cat} <<EOF >gtoaster.console
USER=root
PROGRAM=%{_bindir}/gtoaster-root
SESSION=true
EOF

%{__cat} <<EOF >gtoaster.pam
#%PAM-1.0
auth       sufficient	/lib/security/pam_rootok.so
auth       required	/lib/security/pam_stack.so service=system-auth
session	   required	/lib/security/pam_permit.so
session    optional	/lib/security/pam_xauth.so
account    required	/lib/security/pam_permit.so
EOF

%build
%{__libtoolize} --force
#%{__aclocal} --force
#%{__automake} -a
%{__autoconf} --force
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
#%find_lang %{name}

%{__mv} -f %{buildroot}%{_bindir}/gtoaster %{buildroot}%{_bindir}/gtoaster-root
%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/gtoaster

%{__install} -Dp -m0644 gtoaster.console %{buildroot}%{_sysconfdir}/security/console.apps/gtoaster
%{__install} -Dp -m0644 gtoaster.pam %{buildroot}%{_sysconfdir}/pam.d/gtoaster
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/gtoaster.png

%if %{!?_without_freedesktop:1}0
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome --delete-original \
		--add-category X-Red-Hat-Base                 \
		--dir %{buildroot}%{_datadir}/applications    \
		gtoaster.desktop
%else
	%{__install} -Dp -m0644 gtoaster.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/gtoaster.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog* COPYING INSTALL NEWS README TODO
%config(noreplace) %{_sysconfdir}/pam.d/gtoaster
%config(noreplace) %{_sysconfdir}/security/console.apps/gtoaster
%{!?_without_freedesktop:%{_datadir}/applications/gnome-gtoaster.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/gtoaster.desktop}
%{_datadir}/pixmaps/*
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-2.beta6.2
- Rebuild for Fedora Core 5.

* Tue Jun 08 2004 Dag Wieers <dag@wieers.com> - 1.0-2.beta6
- Added improved desktop file.
- Cosmetic cleanup.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 1.0-1.beta6
- Updated to release 1.0Beta6.

* Fri Feb 08 2002 John Thacker <thacker@math.cornell.edu>
- update to 1.0Beta5

* Sat Jul 21 2001 Tim Powers <timp@redhat.com>
- require mpg321 not mpd123 now

* Fri Jul 20 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- do not build for s390,s390x

* Mon Jul 02 2001 Than Ngo <than@redhat.com>
- update to 1.0 beta 2

* Wed Jun 06 2001 Than Ngo <than@redhat.com>
- update to 1.0 beta 1
- add german translation in destop file
- remove unneeded patch file

* Tue Apr  3 2001 Preston Brown <pbrown@redhat.com>
- Red Hat style .spec.
- use mkstemp not tempnam.

* Wed Sep 27 2000 Eric Sandeen <eric_sandeen@bigfoot.com>
- gtoaster2000092620

* Wed Aug 30 2000 Georges Seguin «okki@wanadoo.fr»
- gtoaster 0.4.2000082921

* Sun Aug 13 2000 Georges Seguin «okki@wanadoo.fr»
- gtoaster 0.4.2000081318
- RPM specification file has been improved

* Thu May 26 2000 Georges Seguin «crow@planete.net»
- First RPM
