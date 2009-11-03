# $Id$
# Authority: dag
# Upstream: Peter Eisenlohr <peter$eisenlohr,org>

%define xmms_outputdir %(xmms-config --output-plugin-dir 2>/dev/null || echo %{_libdir}/xmms/Output)

Summary: Crossfade output plugin for XMMS
Name: xmms-crossfade
Version: 0.3.14
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.eisenlohr.org/xmms-crossfade/

Source: http://www.eisenlohr.org/xmms-crossfade/xmms-crossfade-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: xmms, xmms-devel, gtk+-devel >= 1.2.7, libsamplerate-devel
# libtool *sigh*
BuildRequires: gcc-c++
Requires: xmms >= 1.0.0, glib >= 1.2.7, gtk+ >= 1.2.7

%description
A neat crossfade plugin for XMMS featuring crossfading and continuous output
between songs and a gap-killer.

%prep
%setup


%build
%configure --libdir="%{xmms_outputdir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall libdir="%{buildroot}%{xmms_outputdir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%{xmms_outputdir}/libcrossfade.so
%exclude %{xmms_outputdir}/libcrossfade.la

%changelog
* Tue Nov 27 2007 Dag Wieers <dag@wieers.com> - 0.3.14-1
- Updated to release 0.3.14.

* Thu Nov 22 2007 Dag Wieers <dag@wieers.com> - 0.3.13-1
- Updated to release 0.3.13.

* Fri Sep 15 2006 Matthias Saou <http://freshrpms.net/> 0.3.11-2
- Add xmms build requirement since it is required and the recent xmms-libs
  split makes it that it doesn't get installed with xmms-devel anymore.

* Wed Jul 19 2006 Dag Wieers <dag@wieers.com> - 0.3.11-1
- Updated to release 0.3.11.

* Wed Dec  7 2004 Matthias Saou <http://freshrpms.net/> 0.3.10-1
- Update to 0.3.10.

* Wed Nov 30 2004 Dag Wieers <dag@wieers.com> - 0.3.9-1
- Updated to release 0.3.9.

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 0.3.8-1
- Updated to release 0.3.8.

* Fri Sep 17 2004 Matthias Saou <http://freshrpms.net/> 0.3.6-1
- Update to 0.3.6.
- Now use libsamplerate.

* Sun Aug 08 2004 Dag Wieers <dag@wieers.com> - 0.3.5-1
- Updated to release 0.3.5.
- Updated URL and Upstream tags.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.3.4-3
- Rebuild for Fedora Core 2.
- Removed explicit stripping, that's for the debuginfo package now.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.3.4-2
- Rebuild for Fedora Core 1.

* Wed Oct  8 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.4.

* Mon Oct  6 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.3.

* Tue Apr 22 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.2.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Thu Mar 13 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.1.

* Sat Sep 28 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Changed the hard-coded Output dir to a value expanded from xmms-config.
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Mon Jun 11 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.9.

* Sat May 12 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.8.

* Mon Apr 23 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.7.

* Fri Apr 20 2001 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat 7.1.

* Sun Mar 25 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.6.

* Thu Mar 15 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.5.

* Mon Mar 12 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.4.

* Tue Jan  2 2001 Matthias Saou <http://freshrpms.net/>
- Initial RedHat 7.0 RPM release

