# $Id$
# Authority: dag
# Distcc: 0

%{?dist: %{expand %%define %dist 1}}

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Mozilla Thunderbird mail/news client
Name: thunderbird
Version: 0.5
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.mozilla.org/projects/thunderbird/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/thunderbird-%{version}-source.tar.bz2
Source1: http://downloads.mozdev.org/enigmail/src/ipc-1.0.5.tar.gz
Source2: http://downloads.mozdev.org/enigmail/src/enigmail-0.83.3.tar.gz
Source3: thunderbird-icon.png
Patch1: mozilla-1.4-x86_64.patch
Patch2: mozilla-xremote.patch
Patch1001: mozilla-1.6-gtk2xtbin.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: XFree86-devel, zlib-devel, zip, perl
BuildRequires: gtk+-devel, libpng-devel, libmng-devel, libjpeg-devel, ORBit-devel
BuildRequires: vim-enhanced, csh
%{?fc1:BuildRequires: gtk2-devel}
%{?el3:BuildRequires: gtk2-devel}
%{?rh9:BuildRequires: gtk2-devel}
%{?rh8:BuildRequires: gtk2-devel}
%{?rh7:BuildRequires: gtk+-devel}
%{?el2:BuildRequires: gtk+-devel}
%{?rh6:BuildRequires: gtk+-devel}

Obsoletes: phoenix, MozillaThunderbird, mozilla-thunderbird

%description
Mozilla Thunderbird is a redesign of the Mozilla mail component.

%prep
%setup -n mozilla
%patch1001
%patch1 -p1 -b .x86_64
%patch2 -p0 -b .xremote
%setup -T -D -a1 -n mozilla/extensions
%setup -T -D -a2 -n mozilla/extensions
%setup -T -D -n mozilla

### FIXME: Shouldn't the default thunderbird config be part of original source ?
%{__cat} <<EOF >.mozconfig
export MOZ_THUNDERBIRD="1"
mk_add_options MOZ_THUNDERBIRD="1"
ac_add_options --with-system-jpeg
ac_add_options --with-system-zlib
ac_add_options --with-system-png
ac_add_options --with-system-mng
ac_add_options --with-pthreads
ac_add_options --disable-tests
ac_add_options --disable-debug
ac_add_options --disable-mathml
ac_add_options --disable-installer
ac_add_options --disable-activex
ac_add_options --disable-activex-scripting
ac_add_options --disable-oji
ac_add_options --disable-necko-disk-cache
ac_add_options --disable-profilesharing
ac_add_options --enable-optimize="%{optflags}"
ac_add_options --enable-crypto
ac_add_options --enable-strip
ac_add_options --enable-strip-libs
ac_add_options --enable-reorder
ac_add_options --enable-xinerama
ac_add_options --enable-extensions="wallet,spellcheck,xmlextras"
ac_add_options --enable-necko-protocols="http,file,jar,viewsource,res,data"
ac_add_options --enable-image-decoders="png,gif,jpeg,bmp"
%{?fc1:ac_add_options --enable-xft}
%{?fc1:ac_add_options --enable-default-toolkit="gtk2"}
%{?el3:ac_add_options --enable-xft}
%{?el3:ac_add_options --enable-default-toolkit="gtk2"}
%{?rh9:ac_add_options --enable-xft}
%{?rh9:ac_add_options --enable-default-toolkit="gtk2"}
%{?rh8:ac_add_options --enable-xft}
%{?rh8:ac_add_options --enable-default-toolkit="gtk2"}
%{?rh7:ac_add_options --disable-xft}
%{?rh6:ac_add_options --disable-xft}
EOF

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Thunderbird Email
Comment=Lightweight Mozilla-based mail client
Exec=thunderbird
Icon=thunderbird.png
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;Network;
EOF

%{__cat} <<'EOF' >%{name}.sh
#!/bin/sh

### Written by Dag Wieers <dag@wieers.com>
### Please send suggestions and fixes to me.

ulimit -c 0

MOZ_PROGRAM="%{_libdir}/thunderbird/thunderbird-bin"

MOZILLA_FIVE_HOME="%{_libdir}/thunderbird"
LD_LIBRARY_PATH="$MOZILLA_FIVE_HOME:$MOZILLA_FIVE_HOME/plugins:$LD_LIBRARY_PATH"
export MOZILLA_FIVE_HOME LD_LIBRARY_PATH

MOZARGS=""
MOZLOCALE="$(echo $LANG | sed 's|_\([^.]*\).*|-\1|g')"
if [ -f "$MOZILLA_FIVE_HOME/chrome/$MOZLOCALE.jar" ]; then
	MOZARGS="-UILocale $MOZLOCALE"
fi

$MOZ_PROGRAM -remote 'ping()' &>/dev/null
RUNNING=$?

case "$1" in
  -mail|-email)
	if [ $RUNNING -eq 0 ]; then
		exec $MOZ_PROGRAM -remote "mailto($2)" $MOZARGS ${2+"$@"}
	else
		exec $MOZ_PROGRAM -compose "to=$2" $MOZARGS ${2+"$@"}
	fi;;
  -compose|-editor)
	if [ $RUNNING -eq 0 ]; then
		ADDRESS="$(echo $2 | sed 's|.*to=||;s|,.*||')"
		exec $MOZ_PROGRAM -remote "mailto($ADDRESS)" $MOZARGS ${2+"$@"}
	else
		exec $MOZ_PROGRAM -compose $MOZARGS ${1+"$@"}
	fi;;
  -remote)
	exec $MOZ_PROGRAM -remote "$2" $MOZARGS ${2+"$@"};;
  -profile|-profile-manager)
	exec $MOZ_PROGRAM $MOZARGS $@ &;;
  -*);;
  '');;
  *)
	if [ $RUNNING -eq 0 ]; then
		$MOZ_PROGRAM -remote "xfeDoCommand(openInbox)" $MOZARGS ${1+"$@"} && exit 0
	else
		$MOZ_PROGRAM $MOZARGS ${1+"$@"} && exit 0
	fi;;
esac

if [ $RUNNING -eq 0 ]; then
	exec $MOZ_PROGRAM -remote "xfeDoCommand (openInbox)" $MOZARGS $@
else
	exec $MOZ_PROGRAM $MOZARGS $@ &
fi;
EOF

%build
export MOZ_THUNDERBIRD="1"
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%{__make} -f client.mk export
%{__make} %{?_smp_mflags} -f client.mk libs

export LANG="en_US"
cd extensions/ipc
./makemake
%{__make} %{?_smp_mflags}
cd -

cd extensions/enigmail
./makemake
%{__make} %{?_smp_mflags}
cd -

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_libdir} \
			%{buildroot}%{_datadir}/pixmaps/

%{__make} -C xpinstall/packager \
	MOZ_PKG_APPNAME="thunderbird" \
	MOZILLA_BIN="\$(DIST)/bin/thunderbird-bin"

%{__install} -m0755 %{name}.sh %{buildroot}%{_bindir}/thunderbird

tar -xzv -C %{buildroot}%{_libdir} -f dist/thunderbird-*-linux-gnu.tar.gz

%{__install} -m0644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/thunderbird.png

%if %{dfi}
	%{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Internet/
	%{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor net                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LEGAL LICENSE README.txt
%{_bindir}/*
%{_libdir}/thunderbird/
%{_datadir}/pixmaps/*
%if %{dfi}
	%{_datadir}/gnome/apps/Internet/*.desktop
%else
	%{_datadir}/applications/*.desktop
%endif

%changelog
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
