# $Id$
# Authority: dag
# Upstream: Tom Wilkason <tom,wilkason$cox,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge
%define real_name snackAmp

Summary: Versatile music player
Name: snackamp
Version: 3.1.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://snackamp.sourceforge.net/

Source: http://dl.sf.net/snackamp/snackAmp-%{version}.tar.gz
Source1: snackamp.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: dos2unix, tcl >= 8.4
Requires: tcl >= 8.4, tk, libsnack, metakit
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
SnackAmp is a multi-platform music player with normal music player
abilities with a multi-user support and a powerful auto-play list
feature. Currently mp3, wav, ogg vorbis,and many other sound files
are indexed by SnackAmp depending on your preferences.

%prep
%setup -n %{real_name}.vfs

%{__cat} <<EOF >snackamp.desktop
[Desktop Entry]
Name=SnackAmp Audio Player
Exec=snackamp
Comment=%{summary}
Icon=snackamp.png
Terminal=false
Type=Application
Categories=Application;AudioVideo;
EOF

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}/tcl/snackAmp/ \
		%{buildroot}%{_bindir}
### FIXME: add docs/*.tml in next release
#dos2unix docs/*.tml docs/*/*.tml docs/*.css docs/*/*.css
dos2unix docs/*/*.tml docs/*.css
#dos2unix lib/*.tcl lib/tablelist/*.tcl lib/tablelist/scripts/*.tcl lib/mySnack/*.tcl *.tcl
dos2unix *.tcl */*.tcl */*/*.tcl
%{__cp} -afp docs lib %{buildroot}%{_libdir}/tcl/snackAmp/
find %{buildroot}%{_libdir}/tcl/snackAmp/ -type f -exec chmod 0644 {} \;
find %{buildroot}%{_libdir}/tcl/snackAmp/ -type d -exec chmod 0755 {} \;
#%{__install} -p -m0755 icons/snackAmp.ico %{buildroot}%{_datadir}/pixmaps/
%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/snackamp.png
%{__install} -Dp -m0755 snackAmp.tcl %{buildroot}%{_libdir}/tcl/snackAmp/snackAmp.tcl
%{__install} -p -m0644 main.tcl snackAmphotKeys.tcl %{buildroot}%{_libdir}/tcl/snackAmp/
%{__ln_s} -f %{_libdir}/tcl/snackAmp/snackAmp.tcl %{buildroot}%{_bindir}/snackamp
%{__ln_s} -f %{_libdir}/tcl/snackAmp/snackAmp.tcl %{buildroot}%{_bindir}/snackAmp

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 snackamp.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/snackamp.desktop
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
        desktop-file-install --vendor %{desktop_vendor}    \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
                snackamp.desktop
%endif

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/tcl/snackAmp/lib/mySnack/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc readme.txt
#%doc ChangeLog
%{_bindir}/*
%{_libdir}/tcl/snackAmp/
%{_datadir}/pixmaps/*
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/snackamp.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-snackamp.desktop}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.1.2-1.2
- Rebuild for Fedora Core 5.

* Fri Aug 12 2005 Dag Wieers <dag@wieers.com> - 3.1.2-2
- This is NOT a noarch package.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 3.1.2-1
- Updated to release 3.1.2.

* Thu Aug 05 2004 Dag Wieers <dag@wieers.com> - 3.0.2-1
- Updated to release 3.0.2.

* Sun Jul 18 2004 Dag Wieers <dag@wieers.com> - 3.0.0-1
- Updated to release 3.0.0.

* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 2.2.1-1
- Updated to release 2.2.1.

* Sat Jul 05 2003 Dag Wieers <dag@wieers.com> - 2.2.1-0.beta1
- Updated to release 2.2.1.
- Added tk requirement. (Peter Peltonen)

* Wed May 21 2003 Dag Wieers <dag@wieers.com> - 2.2-0
- Updated to release 2.2.

* Sun Apr 27 2003 Dag Wieers <dag@wieers.com> - 2.1.81-0
- Updated to release 2.2B1.

* Thu Jan 30 2003 Dag Wieers <dag@wieers.com> - 2.1.1-1
- Second release of 2.1.1 due to problems with earlier official tarball.

* Tue Dec 03 2002 Dag Wieers <dag@wieers.com> - 2.0.1-0
- Initial package.
