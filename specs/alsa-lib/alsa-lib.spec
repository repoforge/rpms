# $Id$
# Authority: matthias

### EL6 ships with alsa-lib-1.0.21-3.el6
### EL5 ships with alsa-lib-1.0.17-1.el5
### EL4 ships with alsa-lib-1.0.6-5.RHEL4
# ExclusiveDist: el2 el3

Summary: The Advanced Linux Sound Architecture (ALSA) library
Name: alsa-lib
Version: 1.0.4
Release: %{?prever:0.%{prever}.}1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.alsa-project.org/
Source: ftp://ftp.alsa-project.org/pub/lib/%{name}-%{version}%{?prever}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: alsa-driver >= %{version}, doxygen, pkgconfig

%description
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system. ALSA has the following
significant features: Efficient support for all types of audio interfaces,
from consumer soundcards to professional multichannel audio interfaces,
fully modularized sound drivers, SMP and thread-safe design, user space
library (alsa-lib) to simplify application programming and provide higher
level functionality as well as support for the older OSS API, providing
binary compatibility for most OSS programs.

This package includes the ALSA runtime libraries.


%package devel
Summary: Static libraries and header files from the ALSA library
Group: Development/Libraries
Requires: %{name} = %{version}
Requires: alsa-driver >= %{version}, pkgconfig

%description devel
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system. ALSA has the following
significant features: Efficient support for all types of audio interfaces,
from consumer soundcards to professional multichannel audio interfaces,
fully modularized sound drivers, SMP and thread-safe design, user space
library (alsa-lib) to simplify application programming and provide higher
level functionality as well as support for the older OSS API, providing
binary compatibility for most OSS programs.

This package includes the ALSA development libraries.


%prep
%setup -n %{name}-%{version}%{?prever}


%build
%configure \
    --enable-static=yes \
    --program-prefix=%{?_program_prefix}
%{__make} %{?_smp_mflags}
%{__make} doc


%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc COPYING ChangeLog TODO doc/asoundrc.txt
%{_bindir}/alsalisp
%{_bindir}/aserver
%{_libdir}/libasound.so*
%{_datadir}/alsa

%files devel
%defattr(-, root, root, 0755)
%doc doc/doxygen
%{_includedir}/alsa
%{_includedir}/sys/asoundlib.h
%{_libdir}/libasound.a
%exclude %{_libdir}/libasound.la
%{_libdir}/pkgconfig/alsa.pc
%{_datadir}/aclocal/alsa.m4


%changelog
* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 1.0.4-1
- Update to 1.0.4.

* Thu Jan 29 2004 Matthias Saou <http://freshrpms.net/> 1.0.2-1
- Update to 1.0.2.

* Sun Jan 11 2004 Matthias Saou <http://freshrpms.net/> 1.0.1-2
- Fix release tag.

* Fri Jan  9 2004 Matthias Saou <http://freshrpms.net/> 1.0.1-1
- Update to 1.0.1.

* Tue Dec  9 2003 Matthias Saou <http://freshrpms.net/> 1.0.0-0.rc2.1
- Update to 1.0.0rc2.

* Tue Dec  2 2003 Matthias Saou <http://freshrpms.net/> 1.0.0-0.rc1.1
- Update to 1.0.0rc1.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 0.9.8-2
- Rebuild for Fedora Core 1.

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
- Change alsa-driver deps from = to >= since it triggered an apt bug.

* Thu May  1 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.3.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Wed Mar 19 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.2.

* Tue Mar 11 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0rc8c.
- Update to 0.9.1!

* Mon Mar  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0rc8a.
- Now exclude .la files.

* Mon Feb  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0rc7.

* Mon Nov 18 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0rc6.
- Changed naming to move the "rcX" part to the release tag.

* Wed Oct 23 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0rc4, then rc5.
- Added pkgconfig file and dep.

* Fri Sep 27 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Wed Aug 28 2002 Matthias Saou <http://freshrpms.net/>
- Moved libasound.so link back into the main package as xmms-alsa expects.

* Tue Aug 27 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup for Red Hat Linux.
- Split into main and -devel packages.
- Added doxygen doc.
- Fixed %%files section.
- Force build of static libs too.

* Tue Nov 20 2001 Jaroslav Kysela <perex@suse.cz>
- changed BuildRoot from /tmp to /var/tmp
- use the standard RPM macros for prefix and paths
- added DESTDIR for make install

* Sun Nov 11 2001 Miroslav Benes <mbenes@tenez.cz>
- dangerous command "rpm -rf $RPM_BUILD_ROOT" checks $RPM_BUILD_ROOT variable
- unset key "Docdir" - on some new systems are documentation in /usr/share/doc

* Mon May 28 1998 Helge Jensen <slog@slog.dk>
- Made SPEC file

