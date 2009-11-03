# $Id$
# Authority: dag

# ExcludeDist: fc3 el4

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%{?rh7:%define _without_gtk2 1}
%{?el2:%define _without_gtk2 1}

%define desktop_vendor rpmforge

Summary: Mozilla Thunderbird mail/news client
Name: thunderbird
Version: 0.7.2
Release: 0.2%{?dist}
License: MPL/GPL
Group: Applications/Internet
URL: http://www.mozilla.org/projects/thunderbird/

Source: http://ftp.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/thunderbird-%{version}-source.tar.bz2
Source1: http://downloads.mozdev.org/enigmail/src/ipc-1.0.7.tar.gz
Source2: http://downloads.mozdev.org/enigmail/src/enigmail-0.85.0.tar.gz
Patch: thunderbird-0.7.2-gcc34.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: XFree86-devel, zlib-devel, zip, gzip, perl
BuildRequires: gtk+-devel, libpng-devel, libjpeg-devel
BuildRequires: ORBit-devel, vim-enhanced, csh, gcc-c++, krb5-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{!?_without_gtk2:BuildRequires: gtk2-devel, libIDL-devel, gnome-vfs2-devel}
%{?_without_gtk2:BuildRequires: gtk+-devel}

Obsoletes: phoenix, MozillaThunderbird, mozilla-thunderbird
Provides: mailclient

%description
Mozilla Thunderbird is a redesign of the Mozilla mail component.

%prep
%setup -q -n mozilla
%setup -T -D -a1 -n mozilla/extensions
%setup -T -D -a2 -n mozilla/extensions
# This is to get back into the main mozilla directory
%setup -T -D -n mozilla
%patch -p1

### FIXME: Shouldn't the default thunderbird config be part of original source ?
%{__cat} <<EOF >.mozconfig
ac_add_options --x-libraries="%{_prefix}/X11R6/%{_lib}"
ac_add_options --disable-debug
ac_add_options --disable-installer
ac_add_options --disable-jsd
ac_add_options --disable-profilesharing
ac_add_options --disable-tests
ac_add_options --enable-crypto
ac_add_options --enable-extensions="default"
ac_add_options --enable-official-branding
# We want to replace -O? with -Os to optimize compilation for size
ac_add_options --enable-optimize="-Os %(echo "%{optflags}" | sed 's/-O.//')"
ac_add_options --enable-single-profile
ac_add_options --with-pthreads
ac_add_options --with-system-jpeg
ac_add_options --with-system-png
ac_add_options --with-system-zlib
%{?_without_gtk2:ac_add_options --enable-default-toolkit="gtk"}
%{?_without_gtk2:ac_add_options --disable-freetype2}
%{!?_without_gtk2:ac_add_options --enable-default-toolkit="gtk2"}
%{!?_without_gtk2:ac_add_options --enable-xft}
%{!?_without_gtk2:ac_add_options --enable-xinerama}
EOF

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Thunderbird Email
Comment=Lightweight Mozilla-based mail client
Exec=thunderbird
Icon=thunderbird.xpm
Terminal=false
Type=Application
StartupNotify=false
Categories=Application;Network;
EOF

%{__cat} <<'EOF' >thunderbird.sh
#!/bin/sh

### Written by Dag Wieers <dag@wieers.com>
### Please send suggestions and fixes to me.

MOZILLA_FIVE_HOME="%{_libdir}/thunderbird"
MOZ_PROGRAM="$MOZILLA_FIVE_HOME/thunderbird"

LD_LIBRARY_PATH="$MOZILLA_FIVE_HOME:$MOZILLA_FIVE_HOME/plugins${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export MOZILLA_FIVE_HOME LD_LIBRARY_PATH

MOZARGS=""
MOZLOCALE="$(echo $LANG | sed 's|_\([^.]*\).*|-\1|g')"
if [ -f "$MOZILLA_FIVE_HOME/chrome/$MOZLOCALE.jar" ]; then
	MOZARGS="-UILocale $MOZLOCALE"
fi

$MOZ_PROGRAM -a thunderbird -remote 'ping()' &>/dev/null
RUNNING=$?
if [ $? -eq 2 ]; then RUNNING=0; fi

REMOTE=0
while [ "$1" ]; do
	case "$1" in
	  -mail|-email)
		if [ $RUNNING -eq 0 -a $REMOTE -ne 1 ]; then
			MOZARGS="-remote xfeDoCommand(openInbox) $MOZARGS"
			REMOTE=1
		fi;;
	  -compose|-editor)
		if [ $RUNNING -eq 0 -a $REMOTE -ne 1 ]; then
			MOZARGS="-remote xfeDoCommand(composeMessage) $MOZARGS"
			REMOTE=1
		fi;;
	  -register)
		if [ -x "/usr/X11R6/bin/Xvfb" ]; then
			export HOME="$(mktemp -d /tmp/thunderbird-rpm.$$)"
			mkdir -p $HOME/.thunderbird/default
			cp -rf $MOZILLA_FIVE_HOME/defaults/profile/* $HOME/.thunderbird/default/
			echo -e "[General]\nStartWithLastProfile=1\n\n[Profile0]\nName=default\nIsRelative=1\nPath=default" >$HOME/.thunderbird/profiles.ini
			/usr/X11R6/bin/Xvfb :69 -nolisten tcp -ac -terminate &
			DISPLAY=:69 $MOZILLA_FIVE_HOME/thunderbird -a thunderbird -install-global-extension -install-global-theme
			rm -rf $HOME
			exit 0
		else
			echo "/usr/X11R6/bin/Xvfb cannot be executed. Please run thunderbird once as root." >&2
			exit 1
		fi;;
	  -remote)
		if [ $REMOTE -ne 1 ]; then
			MOZARGS="-remote $2 $MOZARGS"
			REMOTE=1
		fi
		shift;;
	  -profile|-profile-manager)
		MOZARGS="$MOZARGS -profilemanager"
		REMOTE=1
		;;
	  -*)
		MOZARGS="$MOZARGS $1"
		;;
	  *)
		if [ $RUNNING -eq 0 -a $REMOTE -ne 1 ]; then
			MOZARGS="-remote \"xfeDoCommand(openInbox)\" $MOZARGS"
			REMOTE=1
		else
			MOZARGS="$MOZARGS ${1+"$@"}"
		fi;;
	esac
	shift
done

if [ $RUNNING -eq 0 -a $REMOTE -ne 1 ]; then
	exec $MOZ_PROGRAM -a thunderbird -remote "xfeDoCommand (openInbox)" $MOZARGS
else
	exec $MOZ_PROGRAM -a thunderbird $MOZARGS &
fi;
EOF

%build
export MOZ_THUNDERBIRD=1
%{__make} -f client.mk depend
%{__make} %{?_smp_mflags} -f client.mk libs

pushd extensions/ipc
	./makemake
	%{__make} %{?_smp_mflags}
popd
pushd extensions/enigmail
	./makemake
	%{__make} %{?_smp_mflags}
popd

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}

%{__make} -C xpinstall/packager \
	MOZILLA_BIN="\$(DIST)/bin/thunderbird-bin"

%{__install} -Dp -m0755 thunderbird.sh %{buildroot}%{_bindir}/thunderbird
%{__install} -Dp -m0644 other-licenses/branding/thunderbird/mozicon50.xpm %{buildroot}%{_datadir}/pixmaps/thunderbird.xpm

%{__tar} -xzv -C %{buildroot}%{_libdir} -f dist/thunderbird-*-linux-gnu.tar.gz

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 thunderbird.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/thunderbird.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		thunderbird.desktop
%endif

%post
/sbin/ldconfig 2>/dev/null
%{_bindir}/thunderbird -register &>/dev/null || :
%{_bindir}/update-desktop-database %{_datadir}/applications &>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
	%{__rm} -rf %{_libdir}/thunderbird/{chrome/overlayinfo,chrome/*.rdf,components,components.ini,extensions}
fi

%postun
/sbin/ldconfig 2>/dev/null
%{_bindir}/update-desktop-database %{_datadir}/applications &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LEGAL LICENSE README.txt
%{_bindir}/thunderbird
%{_libdir}/thunderbird/
%{_datadir}/pixmaps/thunderbird.xpm
%{?_without_freedesktop:%{_datadir}/gnome/apps/Internet/thunderbird.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-thunderbird.desktop}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.2-0.2
- Rebuild for Fedora Core 5.

* Tue Jul 27 2004 Matthias Saou <http://freshrpms.net/> 0.7.2-0
- Update to 0.7.2, major spec changes and updates.
- Copy all of Dag's changes to the latest Firefox package.

* Wed Jun  2 2004 Matthias Saou <http://freshrpms.net/> 0.6-1
- Update to 0.6.
- Removed all patches since they seem to have been applied upstream.
- Added Yellow Dog Linux 3.0 dependencies.
- Added libIDL-devel, gcc-c++ build dependencies.

* Sat Apr 03 2004 Dag Wieers <dag@wieers.com> - 0.5-1
- Updated to release 0.5.
- Fixed off-by-1 border for plugins. (Daniele Paoni)
- Open new window by default, added --profile-manager. (Gary Peck)
- Added x86_64 patch. (Oliver Sontag)

* Sun Dec 07 2003 Dag Wieers <dag@wieers.com> - 0.4-0
- Updated to release 0.4.

* Mon Nov 03 2003 Dag Wieers <dag@wieers.com> - 0.3-0
- Updated to release 0.3.

* Fri Sep 05 2003 Dag Wieers <dag@wieers.com> - 0.2-0
- Initial package. (using DAR)
