# $Id$

# Authority: dag

# Upstream: Kåre Sjölander <kare@speech.kth.se>

%define real_name snack

Summary: Snack Sound Toolkit
Name: libsnack
Version: 2.2.2
Release: 2
License: GPL
Group: Development/Libraries
URL: http://www.speech.kth.se/snack/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.speech.kth.se/~kare/%{real_name}%{version}.tar.gz
Source1: http://www.speech.kth.se/~kare/ogg.tar.gz
Source2: http://www.speech.kth.se/~kare/sphere.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: tcl-devel
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
%setup -c -b0 -T -D -c -b1 -T -D -c -b2

%{__perl} -pi.orig -e 's|playgrain = 100;|playgrain = 1;|' generic/jkSoundEngine.c

%build
cd snack%{version}/unix
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%{__install} -d -m0755 %{buildroot}%{_libdir}/snack%{version}/
%makeinstall -C "snack%{version}/unix" \
	VERSION="%{version}" \
	SNACK_INSTALL_PATH="%{buildroot}%{_libdir}"

%{__install} _ogg/libsnackogg.so %{buildroot}%{_libdir}/snack%{version}/
%{__install} _sphere/libsnacksphere.so %{buildroot}%{_libdir}/snack%{version}/

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/%{name}stub%{version}.a

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc snack%{version}/README snack%{version}/changes snack%{version}/doc/*
%{_libdir}/snack%{version}/

%changelog
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
