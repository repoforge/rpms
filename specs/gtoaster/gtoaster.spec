# $Id$

# Authority: dag

Name: gtoaster
Summary: A versatile CD recording package for both sound and data.
Version: 1.0
Release: 1.beta6
License: GPL
Group: Applications/Archiving
URL: http://gnometoaster.rulez.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://gnometoaster.rulez.org/archive/%{name}1.0Beta5.tgz
Source1: gtoaster.desktop
Source2: gtoaster.console
Source3: gtoaster.pam
Source4: gtoaster.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: audiofile-devel gnome-libs-devel ORBit-devel
Requires: cdrecord cdrdao mkisofs cdda2wav sox mpg321
ExcludeArch: s390 s390x

%description
GNOME Toaster is a versatile CD creation suite.  It is designed to be
as user-friendly as possible, allowing you to create CD-ROMs with just
a few simple mouse clicks.  Audio and data CDs are both possible.
GNOME Toaster is also well integrated with the GNOME and KDE
filemanagers.

%prep
%setup -n %{name}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__mv} -f %{buildroot}%{_bindir}/gtoaster %{buildroot}%{_bindir}/gtoaster-root
%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/gtoaster

# helper stuff
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/{X11/applnk/Multimedia,security/console.apps,pam.d}/ \
	%{buildroot}%{_datadir}/pixmaps

%{__install} -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/X11/applnk/Multimedia
%{__install} -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/security/console.apps/gtoaster
%{__install} -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pam.d/gtoaster
%{__install} -m0644 %{SOURCE4} %{buildroot}%{_datadir}/pixmaps

%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr (-,root,root)
%doc AUTHORS ChangeLog* NEWS README TODO
%config %{_sysconfdir}/X11/applnk/Multimedia/gtoaster.desktop
%config(noreplace) %{_sysconfdir}/pam.d/gtoaster
%config(noreplace) %{_sysconfdir}/security/console.apps/gtoaster
%{_datadir}/pixmaps/*
%{_bindir}/*

%changelog
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
