# $Id: $
# Authority: dries
# Upstream: rzyjontko <rzyj$plusnet,pl>
# Screenshot: http://elmo.sourceforge.net/screenshots/elmo-main.png
# ScreenshotURL: http://elmo.sourceforge.net/index.php?s=look&lang=en

Summary: Feature rich highly configurable console mail client
Name: elmo
Version: 1.2.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://elmo.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/elmo/elmo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# It compiles but does not work without gpgme-devel
BuildRequires: gpgme-devel, openssl-devel, bison
BuildRequires: ncurses-devel, flex, gettext

%description
Elmo is a feature-rich console mail client for power users. It integrates
functionality commonly realised by separate pieces of software in other
mailers and competes with Mutt.

%prep
%setup

%build
%configure --enable-debug
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ADVOCACY AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%doc doc/README.txt TODO doc/sample.elmorc doc/tutorial.gpg
%doc %{_mandir}/man?/*
%{_bindir}/elmo
%{_bindir}/elmoconf.pl
%{_datadir}/elmo

%changelog
* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.0-1
- Initial package.
