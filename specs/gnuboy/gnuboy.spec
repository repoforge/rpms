# $Id: gnuboy.spec,v 1.1 2004/02/26 17:54:29 thias Exp $

Summary: A Nintendo GameBoy Color emulator.
Name: gnuboy
Version: 1.0.3
Release: 4.fr
License: GPL
Group: Applications/Emulators
Source: http://gnuboy.unix-fu.org/%{name}-%{version}.tar.gz
URL: http://gnuboy.unix-fu.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: SDL >= 1.2.0
BuildRequires: SDL-devel >= 1.2.0, XFree86-devel

%description
gnuboy (all lowercase) is a portable program for emulating the 
Nintendo GameBoy Color software platform.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc docs/* COPYING README 
%{_bindir}/*

%changelog
* Fri Dec 12 2003 Matthias Saou <http://freshrpms.net/> 1.0.3-4.fr
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Oct 10 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Mon Jul  8 2002 Matthias Saou <http://freshrpms.net/>
- Spec file update.
- Update to 1.0.3.

* Tue Jul 03 2001 Henri Gomez <hgomez@slib.fr>
- gnuboy 1.0.0 RPM release 2
- added docs in docdir

* Tue Jul 03 2001 Henri Gomez <hgomez@slib.fr>
- Initial RPM release
- for i386 platform use nasm for better performance.
- Built under Redhat 6.2 with updates with rpm 3.0.5

