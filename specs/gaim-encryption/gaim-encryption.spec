# $Id$
# Authority: dag

Summary: Openssl encryption plugin for gaim
Name: gaim-encryption
Version: 2.36
Release: 3
License: GPL
Group: Applications/Internet
URL: http://gaim-encryption.sourceforge.net/

Source: http://dl.sf.net/gaim-encryption/gaim-encryption-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildrequires: gtk2-devel, mozilla-nss-devel, mozilla-nspr-devel, gaim
Requires: gaim, mozilla-nss

%description
Openssl encryption support for gaim.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%{_libdir}/gaim/
%exclude %{_libdir}/gaim/encrypt.a
%exclude %{_libdir}/gaim/encrypt.la
%{_libdir}/gaim/encrypt.so

%changelog
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
