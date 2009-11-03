# $Id$
# Authority: dag
# ExclusiveDist: fc6 el5

%define prever beta8

Summary: RSA encryption support for Gaim
Name: gaim-encryption
Version: 3.0
Release: 0.2.%{prever}%{?dist}
License: GPL
Group: Applications/Internet
URL: http://gaim-encryption.sourceforge.net/

Source: http://downloads.sf.net/gaim-encryption/gaim-encryption-%{version}%{?prever}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gaim-devel >= 2.0.0, gtk2-devel, nss-devel, nspr-devel
Requires: gaim >= 2.0.0

%description
RSA encryption support for Gaim.

%prep
%setup -n %{name}-%{version}%{?prever}

%build
%configure \
    --with-nspr-includes="`nspr-config --includedir`" \
    --with-nspr-libs="`nspr-config --libdir`" \
    --with-nss-includes="`nss-config --includedir`" \
    --with-nss-libs="`nss-config --libdir`"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING NOTES README TODO WISHLIST
%dir %{_libdir}/gaim/
%exclude %{_libdir}/gaim/encrypt.a
%exclude %{_libdir}/gaim/encrypt.la
%{_libdir}/gaim/encrypt.so
%{_datadir}/pixmaps/gaim/gaim-encryption/crypto.png

%changelog
* Tue Apr 10 2007 Matthias Saou <http://freshrpms.net/> 3.0-0.2.beta8
- Rebuild againt latest FC6 gaim.

* Thu Mar  7 2007 Matthias Saou <http://freshrpms.net/> 3.0-0.1.beta8
- Update to 3.0beta8.

* Fri Nov 10 2006 Matthias Saou <http://freshrpms.net/> 3.0-0.1.beta6
- Update to 3.0beta6, compatible with gaim 2.0.0beta4 (FC6) release.

* Wed Sep 20 2006 Matthias Saou <http://freshrpms.net/> 3.0-0.1.beta5
- Update to 3.0beta5, compatible with gaim 2.0.0beta releases.
- Include new crypto.png image.

* Thu Apr 20 2006 Matthias Saou <http://freshrpms.net/> 2.38-2
- Fix FC5 build by passing configure arguments and requiring correct package
  names (this might break for older distros, but gaim 1.5.0 probably doesn't
  build there anyway).
- Add docs to the package (including license).

* Wed Jul 27 2005 Dag Wieers <dag@wieers.com> - 2.38-1
- Updated to release 2.38.

* Sat May 21 2005 Dag Wieers <dag@wieers.com> - 2.36-4
- Rebuild against gaim 1.3.0-1 (FC3).

* Tue Apr 05 2005 Dag Wieers <dag@wieers.com> - 2.36-3
- Rebuild against gaim 1.2.1-0.

* Tue Mar 22 2005 Dag Wieers <dag@wieers.com> - 2.36-2
- Rebuild against gaim 1.2.0-0.

* Sun Mar 20 2005 Dag Wieers <dag@wieers.com> - 2.36-1
- Updated to release 2.36.

* Fri Mar 11 2005 Dag Wieers <dag@wieers.com> - 2.35-3
- Build against gaim 1.1.4-1.

* Sun Mar 06 2005 Dag Wieers <dag@wieers.com> - 2.35-2
- Build against gaim 1.1.4.

* Sun Feb 27 2005 Dag Wieers <dag@wieers.com> - 2.35-1
- Updated to release 2.35.

* Mon Jan 31 2005 Chris Weyl <cweyl@alumni.drew.edu> - 2.34-1
- Updated gaim-e release

* Sat Apr 18 2004 Che
- Merged some fixes from Chris Weyl (thanks!)

* Tue Aug 05 2003 Che
- argh... fixed a typo

* Mon Jun 02 2003 Che
- initial rpm release.
- hacked from matthias saous original gaim spec
