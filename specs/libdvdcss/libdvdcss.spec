# $Id$
# Authority: matthias
# Upstream: <libdvdcss-devel$videolan,org>

Summary: Portable abstraction library for DVD decryption
Name: libdvdcss
Version: 1.2.10
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://developers.videolan.org/libdvdcss/

Source: http://download.videolan.org/pub/libdvdcss/%{version}/libdvdcss-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# For the documentation
BuildRequires: doxygen, gcc-c++

%description
This is a portable abstraction library for DVD decryption which is used by
the VideoLAN project, a full MPEG2 client/server solution.  You will need
to install this package in order to have encrypted DVD playback with the
VideoLAN client and the Xine navigation plugin.

%package devel
Summary: Development files from the libdvdcss DVD decryption library
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This is a portable abstraction library for DVD decryption which is used by
the VideoLAN project, a full MPEG2 client/server solution.  You will need
to install this package in order to have encrypted DVD playback with the
VideoLAN client and the Xine navigation plugin.

You will need to install these development files if you intend to rebuild
any of the above programs.

%prep
%setup

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/libdvdcss.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/html/
%{_includedir}/dvdcss/
%{_libdir}/libdvdcss.so
%{_libdir}/pkgconfig/libdvdcss.pc
%exclude %{_libdir}/libdvdcss.la

%changelog
* Mon Nov 10 2008 Dag Wieers <dag@wieers.com> - 1.2.10-1
- Updated to release 1.2.10.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.2.9-2
- Disable/remove static library, nothing seems to require it.

* Mon Jul 11 2005 Matthias Saou <http://freshrpms.net/> 1.2.9-1
- Update to 1.2.9.
- Include doxygen generated html doc. Don't include refman, it's too big.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.2.8-4
- Rebuild for Fedora Core 2.

* Tue Feb 24 2004 Matthias Saou <http://freshrpms.net/> 1.2.8-3
- Updated the URL and Source tags to point to the new locations.

* Thu Nov  6 2003 Matthias Saou <http://freshrpms.net/> 1.2.8-2
- Rebuild for Fedora Core 1.

* Sun Aug  3 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.8.

* Wed Jun 25 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.7.

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Tue Mar 11 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.6.

* Mon Feb  3 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.5.

* Fri Nov 15 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.4.

* Mon Oct 21 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.3.

* Thu Sep 26 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 8.0.

* Mon Aug 12 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.2.

* Mon Jun  3 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.1.

* Fri May 24 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.0.

* Thu May  2 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Mon Apr  8 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.1.1.

* Sun Nov  4 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Changed to the Ogle patched version of the lib.

* Mon Oct 22 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Initial RPM release.
- Decided to put libdvdcss in a separate package since both videolan and the
  xine DVD menu plugin use it.

