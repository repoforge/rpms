# $Id$
# Authority: dag

Summary: Graphical user interface for the GnuPG
Name: gpa
Version: 0.6.1
Release: 0.2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.gnupg.org/gpa.html

Source: ftp://ftp.gnupg.org/gcrypt/alpha/gpa/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.0.6, gpgme-devel >= 0.4.0
Requires: gnupg, gtk2 >= 2.0.6, gpgme >= 0.4.0

%description
The GNU Privacy Assistant is a graphical user interface for the GNU Privacy
Guard (GnuPG). GnuPG is a system that provides you with privacy by
encrypting emails or other documents and with authentication of received
files by signature management.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README* THANKS TODO
%{_bindir}/*
%{_datadir}/gpa/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.1-0.2
- Rebuild for Fedora Core 5.

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Make to work without atrpms package.

* Fri Feb 14 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Updated to 0.6.1.

* Fri Jan 17 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- updated to 0.6.0.
- synced with embedded specfile.

* Wed Nov 13 2002 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- updated to 0.4.3, changed Group.

* Fri Aug  3 2001 Peter Hanecak <hanecak@megaloman.sk>
[0.4.1-1]
- initial spec
