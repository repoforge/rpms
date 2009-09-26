# $Id$
# Authority: shuff
# Upstream: Stephen Anthony <stephena$users,sf,net>

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: Atari 2600 Video Computer System emulator
Name: stella
Version: 3.0
Release: 1
License: GPL
Group: Emulators
URL: http://stella.sourceforge.net/

Source: http://dl.sf.net/stella/stella-%{version}-src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel
BuildRequires: zlib-devel
#%{?_without_modxorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU}
%{?_without_modxorg:BuildRequires: XFree86-devel, xorg-x11-Mesa-libGLU}
%{!?_without_modxorg:BuildRequires: mesa-libGL-devel, mesa-libGLU-devel}

%description
The Atari 2600 Video Computer System (VCS), introduced in 1977, was the most
popular home video game system of the early 1980's.  This emulator will run
most Atari ROM images, so that you can play your favorite old Atari 2600 games
on your PC.

%prep
%setup

%build
export CXXFLAGS="%{optflags}"
./configure \
    --prefix="%{_prefix}" \
    --docdir="/rpm-doc" \
    --x-libraries="%{_prefix}/X11R6/%{_lib}" \
    --enable-cheats \
    --enable-debugger \
    --enable-gl \
    --enable-joystick \
    --enable-shared \
    --enable-sound
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Move documentation back into pwd
%{__mv} %{buildroot}/rpm-doc .

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc rpm-doc/*
%{_bindir}/*
%{_datadir}/applications/stella.desktop
%{_datadir}/icons/stella.png
%{_datadir}/icons/mini/stella.png
%{_datadir}/icons/large/stella.png

%changelog
* Sat Sep 12 2009 Greg Bailey <gbailey@lxpro.com> - 3.0-1
- Initial RPMforge package.

* Fri Sep 11 2009 Stephen Anthony <stephena@users.sf.net> 3.0-1
- Version 3.0 release

* Thu Jul 4 2009 Stephen Anthony <stephena@users.sf.net> 2.8.4-1
- Version 2.8.4 release

* Thu Jun 25 2009 Stephen Anthony <stephena@users.sf.net> 2.8.3-1
- Version 2.8.3 release

* Tue Jun 23 2009 Stephen Anthony <stephena@users.sf.net> 2.8.2-1
- Version 2.8.2 release

* Fri Jun 19 2009 Stephen Anthony <stephena@users.sf.net> 2.8.1-1
- Version 2.8.1 release

* Tue Jun 9 2009 Stephen Anthony <stephena@users.sf.net> 2.8-1
- Version 2.8 release

* Tue May 1 2009 Stephen Anthony <stephena@users.sf.net> 2.7.7-1
- Version 2.7.7 release

* Tue Apr 14 2009 Stephen Anthony <stephena@users.sf.net> 2.7.6-1
- Version 2.7.6 release

* Fri Mar 27 2009 Stephen Anthony <stephena@users.sf.net> 2.7.5-1
- Version 2.7.5 release

* Mon Feb 9 2009 Stephen Anthony <stephena@users.sf.net> 2.7.3-1
- Version 2.7.3 release

* Tue Jan 27 2009 Stephen Anthony <stephena@users.sf.net> 2.7.2-1
- Version 2.7.2 release

* Mon Jan 26 2009 Stephen Anthony <stephena@users.sf.net> 2.7.1-1
- Version 2.7.1 release

* Sat Jan 17 2009 Stephen Anthony <stephena@users.sf.net> 2.7-1
- Version 2.7 release

* Thu May 22 2008 Stephen Anthony <stephena@users.sf.net> 2.6.1-1
- Version 2.6.1 release

* Fri May 16 2008 Stephen Anthony <stephena@users.sf.net> 2.6-1
- Version 2.6 release

* Wed Apr 9 2008 Stephen Anthony <stephena@users.sf.net> 2.5.1-1
- Version 2.5.1 release

* Fri Mar 28 2008 Stephen Anthony <stephena@users.sf.net> 2.5-1
- Version 2.5 release

* Mon Aug 27 2007 Stephen Anthony <stephena@users.sf.net> 2.4.1-1
- Version 2.4.1 release
