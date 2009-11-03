# $Id$
# Authority: matthias

%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

%define svn 908

Summary: Quake 3 Arena tournament 3D shooter game
Name: quake3
Version: 1.34
Release: 0.1.rc2%{?svn:.svn%{svn}}%{?dist}
Group: Amusements/Games
License: GPL
URL: http://www.icculus.org/quake3/
# SVN checkout then "make dist"
## svn co svn://svn.icculus.org/quake3/trunk quake3
# svn co svn://svn.icculus.org/quake3/branches/1.34 quake3
Source0: %{name}-%{version}-rc2.tar.bz2
Source1: quake3.png
Patch0: quake3-1.34-nostrip.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel, openal-devel, nasm, subversion
%{!?_without_modxorg:BuildRequires: libXt-devel, libGL-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
This is Quake 3 Arena.
In addition to this package, you will need to copy the pak?.pk3 files from
the original 1.32 Quake 3 Arena point release as well as pak0.pk3 from the
original CD-ROM to %{_prefix}/games/quake3/.


%prep
%setup -n %{name}-%{version}-rc2
%patch0 -p1 -b .nostrip


%build
# Note that using %{optflags} instead of the flags in the Makefiles screw up
# the binary badly! So... don't :-(
%{__make} %{?_smp_mflags} OPTFLAGS="%{optflags}"


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
./ioquake3 "$@"
exit $?
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc BUGS ChangeLog COPYING.txt id-readme.txt md4-readme.txt NOTTODO README TODO
%attr(0755, root, root) %{_bindir}/quake3
%{_prefix}/games/quake3/
%{_datadir}/applications/quake3.desktop
%{_datadir}/pixmaps/quake3.png


%changelog
* Mon Sep 18 2006 Matthias Saou <http://freshrpms.net/> 1.34-0.1.rc2.svn908
- Update to today's svn code (rev. 908), rc2 from the 1.34 branch.

* Mon May 29 2006 Matthias Saou <http://freshrpms.net/> 1.34-0.1.rc1.svn792
- Update to today's svn code (rev. 792).
- Update the nostrip patch.
- Fix wrapper script since the binary has been renamed from quake3 to
  ioquake3.<arch>, which we rename to plain ioquake3 (in the patch).
- Include new documentation.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.34-0.1.rc1.svn649
- Update to today's svn code (rev. 649).
- Update nostrip patch, now pass OPTFLAGS to the build too.
- Build requires subversion (required for make dist).

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

