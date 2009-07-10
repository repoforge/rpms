# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}
%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

#define prever -WIP1
%define real_version 1.51

Summary: Portable, freeware Super Nintendo Entertainment System (TM) emulator
Name: snes9x
Version: 1.51
Release: 1
License: Other
Group: Applications/Emulators
URL: http://www.snes9x.com/
Source: http://files.ipherswipsite.com/snes9x/snes9x-%{real_version}%{?prever}-src.tar.bz2
Patch0: snes9x-1.43-wmclass.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, zlib-devel, libpng-devel
BuildRequires: libGL-devel, libGLU-devel
%{!?_without_modxorg:BuildRequires: libXt-devel, libXext-devel, libXxf86dga-devel, libXxf86vm-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
BuildRequires: nasm

%description
Snes9x is a portable, freeware Super Nintendo Entertainment System (SNES)
emulator. It basically allows you to play most games designed for the SNES
and Super Famicom Nintendo game systems on your computer.


%prep
%setup -n %{name}-%{real_version}%{?prever:-dev}-src
%patch0 -p2 -b .wmclass


%build
# First, build the OpenGL version
%configure --with-netplay --with-opengl
# Replace OPTIMISE here, it's the best I've found...
%{__perl} -pi.orig -e 's|^OPTIMISE.*|OPTIMISE = %{optflags}|g' Makefile
%{__make} %{?_smp_mflags}

%{__make} clean

# Second, build the normal X11 version
%configure --with-netplay
# Replace OPTIMISE here, it's the best I've found...
%{__perl} -pi.orig -e 's|^OPTIMISE.*|OPTIMISE = %{optflags}|g' Makefile
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 0755 osnes9x %{buildroot}%{_bindir}/osnes9x
%{__install} -D -m 0755 snes9x %{buildroot}%{_bindir}/snes9x


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc doc/* unix/docs/readme_unix.txt
%{_bindir}/osnes9x
%{_bindir}/snes9x


%changelog
* Sat Aug 11 2007 Matthias Saou <http://freshrpms.net/> 1.51-1
- Update to 1.51.
- Bundle a second binary, osnes9x, the OpenGL version.
- Include useful readme_unix.txt.
- Remove no longer needed externc patch.

* Tue Oct 17 2006 Matthias Saou <http://freshrpms.net/> 1.50-1
- Update to 1.5... well, luckily it's also called 1.50 in some places, ugh.
- Update source URL.
- Include patch to fix C++ and C extern declarations.
- Remove no longer needed gcc4 patch.
- Remove no longer needed autoreconf and its build requirements.
- Remove no longer needed usagemsg patch, all now fits fine in 80 columns.
- Remove --without-assembler since build works again on i386 with it.
- Note : --with opengl doesn't work... some error in unix/opengl.cpp.

* Wed Mar 22 2006 Matthias Saou <http://freshrpms.net/> 1.43-7
- Add missing modular X build requirement.
- Add autoreconf call to fix configure's X detection.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.43-6
- Release bump to drop the disttag number in FC5 build.

* Tue Jan 24 2006 Matthias Saou <http://freshrpms.net/> 1.43-5
- Add wmclass patch from Bryan Moffit.

* Fri Jan 13 2006 Matthias Saou <http://freshrpms.net/> 1.43-4
- Add modular xorg build conditional.

* Thu Nov 10 2005 Matthias Saou <http://freshrpms.net/> 1.43-3
- Merge things from Ville's package : Usage message patch, optional OpenGL
  support using --with opengl.

* Thu May  5 2005 Matthias Saou <http://freshrpms.net/> 1.43-2
- Include gcc4 patch from Debian.
- Pass --without-assembler since build fails on i386/getset.S otherwise.

* Sun Apr 17 2005 Matthias Saou <http://freshrpms.net/> 1.43-1
- Update to 1.43 final (was WIP1).

* Sat Dec 18 2004 Matthias Saou <http://freshrpms.net/> 1.43-0
- Initial RPM release.

