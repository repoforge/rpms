# $Id$
# Authority: matthias
# Upstream: Moritz Bunkus <moritz$bunkus,org>

Summary: Tools for Ogg media streams
Name: ogmtools
Version: 1.5
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.bunkus.org/videotools/ogmtools/
Source: http://www.bunkus.org/videotools/ogmtools/ogmtools-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, libdvdread-devel, libogg-devel, libvorbis-devel

%description
These tools allow information about (ogminfo) or extraction from (ogmdemux) or
creation of (ogmmerge) OGG media streams. Note that OGM is used for "OGG media
streams".


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.5-2
- Release bump to drop the disttag number in FC5 build.

* Mon Nov  8 2004 Matthias Saou <http://freshrpms.net/> 1.5-1
- Update to 1.5.

* Fri Aug  6 2004 Matthias Saou <http://freshrpms.net/> 1.4.1-1
- Update to 1.4.1.

* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 1.4-1
- Update to 1.4.

* Fri Nov 21 2003 Matthias Saou <http://freshrpms.net/> 1.2-1
- Update to 1.2.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.1-2
- Rebuild for Fedora Core 1.

* Wed Oct 29 2003 Matthias Saou <http://freshrpms.net/> 1.1-1
- Update to 1.1.

* Tue May 20 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.3.

* Mon May  5 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.2.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Tue Mar  4 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.1.

* Sun Mar  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.0.

* Sun Feb 16 2003 Matthias Saou <http://freshrpms.net/>
- Rebuild against new libdvdread.

* Thu Jan 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.973.

* Fri Jan  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.972.

* Mon Nov 18 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.

* Fri Nov 15 2002 Michel Alexandre Salim <salimma@users.sourceforge.net> 0.960-ms1
- new upstream

* Fri Oct 25 2002 Michel Alexandre Salim <salimma@freeshell.org> 0.954-ms1
- new upstream

* Tue Oct 01 2002 Moritz Bunkus <moritz@bunkus.org> 0.951-1
- new upstream

* Sun Sep 22 2002 Moritz Bunkus <moritz@bunkus.org> 0.950-1
- changes to the description and version number

* Sun Sep 22 2002 Marc Lavallée <odradek@videotron.ca> 0.931-1
- initial spec file

