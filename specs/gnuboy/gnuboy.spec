# $Id$
# Authority: matthias

%{?dist: %{expand: %%define %dist 1}}
%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{!?dist:%define _with_modxorg 1}
%{?fc5:%define _with_modxorg 1}

Summary: Nintendo GameBoy Color emulator
Name: gnuboy
Version: 1.0.3
Release: 8
License: GPL
Group: Applications/Emulators
Source: http://gnuboy.unix-fu.org/src/%{name}-%{version}.tar.gz
URL: http://gnuboy.unix-fu.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: SDL >= 1.2.0
BuildRequires: SDL-devel >= 1.2.0
%{?_with_modxorg:BuildRequires: libX11-devel}
%{!?_with_modxorg:BuildRequires: XFree86-devel}

%description
gnuboy (all lowercase) is a portable program for emulating the 
Nintendo GameBoy Color software platform.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags} LDFLAGS=""


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc COPYING docs/* README
%{_bindir}/*


%changelog
* Thu Jan 12 2006 Matthias Saou <http://freshrpms.net/> 1.0.3-8
- Add modular xorg build conditional.

* Fri Nov 11 2005 Dries verachtert <dries@ulyssis.org> 1.0.3-7
- Fixed the source url.

* Sun Jun  5 2005 Matthias Saou <http://freshrpms.net/> 1.0.3-6
- Remove LDFLAGS (-s) to get useful debuginfo package.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 1.0.3-5
- Rebuild for Fedora Core 2.

* Fri Dec 12 2003 Matthias Saou <http://freshrpms.net/> 1.0.3-4
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

