# $Id$
# Authority: dag
# Upstream: Kåre Sjölander <kare$speech,kth,se>


%{?rh9:%define _without_tcltk_devel 1}
%{?rh8:%define _without_tcltk_devel 1}
%{?rh7:%define _without_tcltk_devel 1}
%{?el2:%define _without_tcltk_devel 1}

%define _lib32dir %{_prefix}/lib
%define real_name snack

Summary: Snack Sound Toolkit
Name: libsnack
Version: 2.2.9
Release: 1.2%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.speech.kth.se/snack/

Source: http://www.speech.kth.se/~kare/snack%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: sphere-devel, libvorbis-devel
%{!?_without_tcltk_devel:BuildRequires: tcl-devel >= 8.3, tk-devel}
%{?_without_tcltk_devel:BuildRequires: tcl >= 8.3, tk}
Obsoletes: snack-ogg, snack-sphere
Provides: libsnack-ogg, libsnack-sphere

%description
The Snack Sound Toolkit is designed to be used with a scripting
language such as Tcl/Tk or Python. Using Snack you can create
powerful multi-platform audio applications with just a few lines
of code. Snack has commands for basic sound handling, e.g. sound
card and disk I/O. Snack also has primitives for sound
visualization, e.g. waveforms and spectrograms. It was developed
mainly to handle digital recordings of speech, but is just as
useful for general audio. Snack has also successfully been
applied to other one-dimensional signals.

This packages includes Ogg and NIST/Sphere libraries.

%prep
%setup -n %{real_name}%{version}

%{__perl} -pi.orig -e 's|playgrain = 100;|playgrain = 1;|' generic/jkSoundEngine.c

%build
cd unix
%configure \
	--with-tcl="%{_libdir}" \
	--with-tk="%{_libdir}" \
	--with-nist-include="%{_includedir}/sp" \
	--with-nist-lib="%{_libdir}/sp" \
	--with-ogg-include="%{_includedir}/ogg" \
	--with-ogg-lib="%{_libdir}"
%{__make} %{?_smp_mflags} clean all

%install
%{__rm} -rf %{buildroot}

%{__install} -d -m0755 %{buildroot}%{_lib32dir}/snack%{version}/
%makeinstall -C unix \
	VERSION="%{version}" \
	SNACK_INSTALL_PATH="%{buildroot}%{_lib32dir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc changes doc/* README
%{_lib32dir}/snack%{version}/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.9-1.2
- Rebuild for Fedora Core 5.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 2.2.9-1
- Updated to release 2.2.9.

* Sun Jul 18 2004 Dag Wieers <dag@wieers.com> - 2.2.7-1
- Updated to release 2.2.7.
- Build libsnackogg and libsnacksphere ourselves.

* Mon Jun 30 2003 Dag Wieers <dag@wieers.com> - 2.2.2-1
- Fixed the hardcoded playgrain timing issues. (Tom Wilkason)

* Fri Jun 07 2003 Dag Wieers <dag@wieers.com> - 2.2.2-0
- Updated to release 2.2.2.

* Wed May 07 2003 Dag Wieers <dag@wieers.com> - 2.2.1-2
- Updated to release 2.2.1.

* Sat Feb 01 2003 Dag Wieers <dag@wieers.com> - 2.2-2
- Added NIST/Sphere library and Provides/Obsoletes-tags.

* Tue Jan 14 2003 Dag Wieers <dag@wieers.com> - 2.2-0
- Renamed package from "snack" to "libsnack" because package newt provides "snack".

* Tue Dec 03 2002 Dag Wieers <dag@wieers.com> - 2.2
- Initial package.
