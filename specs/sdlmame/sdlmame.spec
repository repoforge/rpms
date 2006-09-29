# $Id$
# Authority: matthias

%define mamever 109

Summary: SDL MAME
Name: sdlmame
Version: 0.%{mamever}
Release: 1
License: MAME
Group: Applications/Emulators
URL: http://rbelmont.mameworld.info/
# Get with wget --user-agent="" ...
Source: http://rbelmont.mameworld.info/sdlmame0%{mamever}.zip
Patch0: sdlmame0109-genericbuild.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel, expat-devel, zlib-devel

%description
SDL MAME.


%prep
%setup -n sdlmame0%{mamever}
%patch0 -p1 -b .genericbuild
# Create the required set of empty directories in "dirs" to be included as doc
# (we don't want 'obj' which is currently empty but used during the build)
touch obj/foo
for file in *; do
    if rmdir $file 2>/dev/null; then
        mkdir -p dirs/$file
    fi
done


%build
# PTR64 and PPC control some optimizations and disable incompatible stuff
%ifarch x86_64
export PTR64=1
%endif
%ifarch ppc
export PPC=1
%endif
# Don't use our own optflags since they make the build fail (0109)
# SYMBOLS=1 is to get useful debuginfo packages
%{__make} %{?_smp_mflags} \
    SYMBOLS=1 \
    PREFIX="sdl"


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m 0755 chdman romcmp sdlmame %{buildroot}%{_bindir}/


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc docs/*.txt *.txt dirs/
%{_bindir}/chdman
%{_bindir}/romcmp
%{_bindir}/sdlmame


%changelog
* Thu Sep 28 2006 Matthias Saou <http://freshrpms.net/> 0.109-1
- Initial RPM release.

