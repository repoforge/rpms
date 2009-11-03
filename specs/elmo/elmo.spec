# $Id$
# Authority: dries
# Upstream: rzyjontko <rzyj$plusnet,pl>
# Screenshot: http://elmo.sourceforge.net/screenshots/elmo-main.png
# ScreenshotURL: http://elmo.sourceforge.net/index.php?s=look&lang=en

Summary: Feature rich highly configurable console mail client
Name: elmo
Version: 1.3.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://elmo.sourceforge.net/

Source: http://dl.sf.net/elmo/elmo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

### It compiles but does not work without gpgme-devel
BuildRequires: gpgme-devel, openssl-devel, bison, gcc-c++
BuildRequires: ncurses-devel, flex, gettext, krb5-devel

%description
Elmo is a feature-rich console mail client for power users. It integrates
functionality commonly realised by separate pieces of software in other
mailers and competes with Mutt.

%prep
%setup

%build
%configure --enable-debug CPPFLAGS="-I/usr/kerberos/include"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ADVOCACY AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%doc doc/README.txt doc/sample.elmorc doc/tutorial.gpg
%doc %{_mandir}/man1/elmo.1*
%doc %{_mandir}/man1/elmoconf.pl.1*
%{_bindir}/elmo
%{_bindir}/elmoconf.pl
%{_datadir}/elmo/

%changelog
* Thu Jun 09 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.2-1
- Update to release 1.3.2.

* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.0-1
- Initial package.
