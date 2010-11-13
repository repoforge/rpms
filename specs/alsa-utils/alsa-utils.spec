# $Id$
# Authority: matthias

### EL6 ships with alsa-utils-1.0.21-3.el6
### EL5 ships with alsa-utils-1.0.17-1.el5
### EL4 ships with alsa-utils-1.0.6-10
# ExclusiveDist: el2 el3 el4 el5

Summary: The Advanced Linux Sound Architecture (ALSA) utilities
Name: alsa-utils
Version: 1.0.4
Release: %{?prever:0.%{prever}.}1%{?dist}
License: GPL
Group: Applications/Multimedia
Source0: ftp://ftp.alsa-project.org/pub/utils/%{name}-%{version}%{?prever}.tar.bz2
Source1: alsactl.init
URL: http://www.alsa-project.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: alsa-lib >= 1.0.0, alsa-driver >= 1.0.0
BuildRequires: alsa-lib-devel >= 1.0.0, ncurses-devel

%description
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system. ALSA has the following
significant features: Efficient support for all types of audio interfaces,
from consumer soundcards to professional multichannel audio interfaces,
fully modularized sound drivers, SMP and thread-safe design, user space
library (alsa-lib) to simplify application programming and provide higher
level functionality as well as support for the older OSS API, providing
binary compatibility for most OSS programs.

This package includes utilities for systems using ALSA.

%prep
%setup -n %{name}-%{version}%{?prever}


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install
%{__install} -Dp -m755 %{SOURCE1} %{buildroot}%{_initrddir}/alsactl
%{__mkdir_p} %{buildroot}/etc/rc{0,6}.d
%{__ln_s} -f ../init.d/alsactl %{buildroot}/etc/rc0.d/S01alsactl
%{__ln_s} -f ../init.d/alsactl %{buildroot}/etc/rc6.d/S01alsactl


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc COPYING ChangeLog README TODO
%{_initrddir}/alsactl
/etc/rc0.d/S01alsactl
/etc/rc6.d/S01alsactl
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man?/*


%changelog
* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 1.0.4-1
- Update to 1.0.4.

* Thu Jan 29 2004 Matthias Saou <http://freshrpms.net/> 1.0.2-1
- Update to 1.0.2.

* Fri Jan  9 2004 Matthias Saou <http://freshrpms.net/> 1.0.1-1
- Update to 1.0.1.

* Tue Dec  9 2003 Matthias Saou <http://freshrpms.net/> 1.0.0-0.rc2.1
- Update to 1.0.0rc2.

* Tue Dec  2 2003 Matthias Saou <http://freshrpms.net/> 1.0.0-0.rc1.1
- Update to 1.0.0rc1.
- Re-added the "prever" macro...
- Require alsa-driver and alsa-lib >= 1.0.0 to work properly.

* Mon Oct 27 2003 Matthias Saou <http://freshrpms.net/> 0.9.8-1
- Removed the optional "prever" macro.

* Fri Oct  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.7.

* Sun Aug  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.6.

* Wed Jul  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.5.

* Thu Jun 12 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.4.

* Wed May  7 2003 Matthias Saou <http://freshrpms.net/>
- Change all alsa deps from = to >= since it triggered an apt bug.

* Thu May  1 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.3.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Wed Mar 19 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.2.

* Tue Mar 11 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0rc8a.
- Update to 0.9.1!

* Mon Mar  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0rc8.

* Mon Feb  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0rc7.

* Mon Nov 18 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0rc6.

* Wed Oct 23 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0rc4, then rc5.
- Added the alsactl init script.

* Fri Sep 27 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Tue Aug 27 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup for Red Hat Linux.

* Tue Nov 20 2001 Jaroslav Kysela <perex@suse.cz>
- changed BuildRoot from /tmp to /var/tmp
- %_prefix and %_mandir macros are used for configure and mkdir
- DESTDIR is used for make install

* Sun Nov 11 2001 Miroslav Benes <mbenes@tenez.cz>
- dangerous command "rpm -rf $RPM_BUILD_ROOT" checks $RPM_BUILD_ROOT variable
- unset key "Docdir" - on some new systems are documentation in /usr/share/doc

* Mon May 28 1998 Helge Jensen <slog@slog.dk>
- Made SPEC file

