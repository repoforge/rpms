# $Id$
# Authority: dag

Summary: Openssl encryption plugin for gaim
Name: gaim-encryption
Version: 2.34
Release: 1
License: GPL
Group: Applications/Internet
URL: http://gaim-encryption.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gaim-encryption/gaim-encryption-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

Buildrequires: gtk2-devel, mozilla-nss-devel, mozilla-nspr-devel, gaim
Requires: gaim mozilla-nss

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
* Mon Jan 31 2005 Chris Weyl <cweyl@us.ibm.com> - 2.34-1
- Updated gaim-e release

* Sat Apr 18 2004 Che
- Merged some fixes from Chris Weyl (thanks!)

* Tue Aug 05 2003 Che
- argh... fixed a typo

* Mon Jun 02 2003 Che
- initial rpm release.
- hacked from matthias saous original gaim spec
