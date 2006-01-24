# $Id$
# Authority: matthias

%{?dist: %{expand: %%define %dist 1}}
%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{!?dist:%define _with_modxorg 1}
%{?fc5:  %define _with_modxorg 1}

#define prever -WIP1

Summary: Portable, freeware Super Nintendo Entertainment System (TM) emulator
Name: snes9x
Version: 1.43
Release: 5
License: Other
Group: Applications/Emulators
URL: http://www.snes9x.com/
Source: http://www.lysator.liu.se/snes9x/%{version}%{?prever}/snes9x-%{version}%{?prever}-src.tar.gz
Patch0: snes9x-1.43-src-gcc4.patch
Patch1: snes9x-1.43-usagemsg.patch
Patch2: snes9x-1.43-wmclass.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, zlib-devel, libpng-devel
%{?_with_opengl:BuildRequires: %{_libdir}/libGL.so}
%{?_with_modxorg:BuildRequires: libXt-devel, libXext-devel}
%{!?_with_modxorg:BuildRequires: XFree86-devel}
%ifarch %{ix86} x86_64
BuildRequires: nasm
%endif

%description
Snes9x is a portable, freeware Super Nintendo Entertainment System (SNES)
emulator. It basically allows you to play most games designed for the SNES
and Super Famicom Nintendo game systems on your computer.


%prep
%setup -n %{name}-%{version}%{?prever:-dev}-src
%patch0 -p1 -b .gcc4
%patch1 -p0 -b .usagemsg
%patch2 -p1 -b .wmclass


%build
pushd snes9x
%configure \
    --without-assembler \
    %{?_with_opengl}
# Replace OPTIMISE here, it's the best I've found...
%{__perl} -pi.orig -e 's|^OPTIMISE.*|OPTIMISE = %{optflags}|g' Makefile
%{__make} %{?_smp_mflags}
popd


%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 0755 snes9x/snes9x %{buildroot}%{_bindir}/snes9x


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc faqs.txt license.txt readme.txt readme.unix
%doc snes9x_default_config.cfg
%{_bindir}/snes9x


%changelog
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

