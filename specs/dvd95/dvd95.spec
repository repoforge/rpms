# $Id$
# Authority: dag
# Upstream: JF Coulon <jf-coulon$users,sourceforge,net>

Summary: Graphical dvd9 to dvd5 converter
Name: dvd95
Version: 1.4p0
Release: 1%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://dvd95.sourceforge.net/

Source: http://dl.sf.net/dvd95/dvd95-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libdvdread-devel
BuildRequires: libgnomeui-devel
BuildRequires: mpeg2dec-devel

%description
DVD95 is a GNOME application to convert DVD9 (8.5G) to DVD5 (4.7G).

It needs no additional packages, an onboard version of vamps and dvdauthor
is used, to be as fast as possible. Interface is pretty simple yo use.
Shrinking factor may be computed for best results, or an adaptive
compression ratio method may be used.

Dvd can be converted to a file tree or an ISO file. The result can be played
with xine, vlc, or mplayer or burned using third party software (k3b).

DVD95 support two copy modes :
 - Without menus, one video title set, multiple audio and subtitles.
 - With menus, one video title set, multiple audio and subtitles.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" prefix="%{_prefix}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/dvd95
%{_datadir}/applications/dvd95.desktop
%{_datadir}/pixmaps/dvd95/

%changelog
* Mon Aug 11 2008 Dag Wieers <dag@wieers.com> - 1.4p0-1
- Updated to release 1.4p0.

* Tue Jan  1 2008 Matthias Saou <http://freshrpms.net/> 1.3p1-1
- Update to 1.3p1.
- Replace gtk2-devel with proper libgnomeui-devel build requirement.
- Add missing mpeg2dec-devel build requiremnt.
- Remove empty NEWS file.

* Fri Mar 30 2007 Dag Wieers <dag@wieers.com> - 1.2p0-1
- Initial package. (using DAR)

