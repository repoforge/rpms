# $Id$
# Authority: dag
# ExcludeDist: fc6 el5

Summary: RSA encryption support for Gaim
Name: gaim-encryption
Version: 2.38
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://gaim-encryption.sourceforge.net/

Source: http://dl.sf.net/gaim-encryption/gaim-encryption-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gaim-devel, gtk2-devel, nss-devel, nspr-devel
Requires: gaim

%description
RSA encryption support for Gaim.

%prep
%setup

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

%changelog
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
