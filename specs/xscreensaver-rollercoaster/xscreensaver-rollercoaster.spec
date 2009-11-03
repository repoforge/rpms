# $Id$
# Authority: bert

%{?dtag: %{expand: %%define %dtag 1}}

Summary: OpenGL rollercoaster ride animation for xscreensaver
Name: xscreensaver-rollercoaster
Version: 1.1.0
Release: 0%{?dist}
License: GPL
Group: Amusements/Graphics
URL: http://plusplus.free.fr/rollercoaster/
Source: http://plusplus.free.fr/rollercoaster/rollercoaster-%{version}-src.tar.gz
# link is broken, mailed the author on 13/11/2005
Source1: http://plusplus.free.fr/rollercoaster/rollercoaster-1.0.0-src+ss.diff.gz
Source10: http://plusplus.free.fr/rollercoaster/freestyle.trk
Source11: http://plusplus.free.fr/rollercoaster/Midnight_madness.trk
Source12: http://plusplus.free.fr/rollercoaster/Hangtime2.trk
Source13: http://plusplus.free.fr/rollercoaster/QuadraPhase.trk
Source14: http://plusplus.free.fr/rollercoaster/DevilsTower.trk
Source15: http://plusplus.free.fr/rollercoaster/DizzyButterfly.trk
Source16: http://plusplus.free.fr/rollercoaster/speedy_loops.trk
Source17: http://plusplus.free.fr/rollercoaster/WildeMaus.trk
Source18: http://plusplus.free.fr/rollercoaster/WildeMaus2.trk
Source19: http://plusplus.free.fr/rollercoaster/Brainstorm.trk
Source20: http://plusplus.free.fr/rollercoaster/SunnyWE.trk
Source21: http://plusplus.free.fr/rollercoaster/millenium.trk
Source22: http://plusplus.free.fr/rollercoaster/rc2k.trk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xscreensaver

%description
rollercoaster is a module for xscreensaver that renders a rollercoaster
animation using OpenGL.

%prep
%setup -n rollercoaster-%{version}-src
gunzip -c %{SOURCE1} | patch -f || true

%build
%{__make} -f Makefile.linux screensaver


%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 bin/roller-ss %{buildroot}/usr/X11R6/lib/xscreensaver/roller-ss
mkdir -p %{buildroot}%{_datadir}/rollercoaster/
%{__install} -Dp -m0644 bin/*.tga bin/*.bmp %{buildroot}%{_datadir}/rollercoaster/


%clean
%{__rm} -rf %{buildroot}



%files
%defattr(-, root, root, 0755)
/usr/X11R6/lib/xscreensaver/roller-ss
%{_datadir}/rollercoaster


%changelog
* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 1.1.0-1
- Updated to release 1.1.0.

* Tue Sep  7 2004 Bert de Bruijn <bert@debruijn.be>
- Initial package for version 1.0.0.
