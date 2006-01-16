# $Id$
# Authority: matthias

%{?dist: %{expand: %%define %dist 1}}
%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{!?dist:%define _with_modxorg 1}
%{?fc5:  %define _with_modxorg 1}

%define svn 470

Summary: Quake 3 Arena tournament 3D shooter game
Name: quake3
Version: 1.33
Release: 0.2%{?svn:.svn%{svn}}
Group: Amusements/Games
License: GPL
URL: http://www.icculus.org/quake3/
# SVN checkout, then "make dist"
# svn co svn://svn.icculus.org/quake3/trunk quake3
Source0: %{name}-%{version}%{?svn:_SVN%{svn}}.tar.bz2
Source1: quake3.png
Patch0: quake3-1.33-nostrip.patch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel, openal-devel, nasm
%{?_with_modxorg:BuildRequires: libXt-devel, mesa-libGL-devel}
%{!?_with_modxorg:BuildRequires: XFree86-devel}

%description
This is Quake 3 Arena.
In addition to this package, you will need to copy the pak?.pk3 files from
the original 1.32 Quake 3 Arena point release as well as pak0.pk3 from the
original CD-ROM to %{_prefix}/games/quake3/.


%prep
%setup -n %{name}-%{version}%{?svn:_SVN%{svn}}
%patch0 -p1 -b .nostrip


%build
# Note that using %{optflags} instead of the flags in the Makefiles screw up
# the binary badly! So... don't :-(
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_prefix}/games/quake3/baseq3/
%{__make} copyfiles COPYDIR="%{buildroot}%{_prefix}/games/quake3"

%{__install} -D -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/pixmaps/quake3.png

# Desktop file
%{__mkdir_p} %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/quake3.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Quake 3 Arena
Comment=Tournament 3D shooter game
Exec=quake3
Icon=quake3.png
Terminal=false
Type=Application
Categories=Application;Game;
EOF

# Wrapper script
%{__mkdir_p} %{buildroot}%{_bindir}/
%{__cat} > %{buildroot}%{_bindir}/quake3 << 'EOF'
#!/bin/sh
# Needed to make symlinks/shortcuts work.
# Run Quake III with some default arguments

cd %{_prefix}/games/quake3
./quake3 "$@"
exit $?
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc BUGS ChangeLog COPYING.txt id-readme.txt README TODO
%attr(0755, root, root) %{_bindir}/quake3
%{_prefix}/games/quake3/
%{_datadir}/applications/quake3.desktop
%{_datadir}/pixmaps/quake3.png


%changelog
* Fri Jan 13 2006 Matthias Saou <http://freshrpms.net/> 1.33-0.2.svn470
- Update to today's svn sode (rev. 470).
- Add modular xorg build conditional.
- Revisit nostrip patch for the new code.
- Add (new?) openal-devel build requirement.
- Update %%doc files.

* Sun Nov 13 2005 Matthias Saou <http://freshrpms.net/> 1.33-0.1.svn338
- Update to GPL'ed 1.33 and spec file cleanup.

* Sun Oct 15 2000 Matthias Saou <http://freshrpms.net/> 1.17-1
- Initial RPM based on Loki's 1.17 point release

