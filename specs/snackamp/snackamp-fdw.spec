# $Id$
# Authority: dag
# Upstream: Tom Wilkason <tom,wilkason$cox,net>

# Tag: rft

%define real_name snackAmp
%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Versatile music player
Name: snackamp
Version: 2.2
Release: 4.fdw.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://snackamp.sourceforge.net/

Source: http://dl.sf.net/snackamp/snackAmp-%{version}_FDW.tar.gz
Source1: snackamp.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: dos2unix
Requires: libsnack

Obsoletes: snackamp

%description
SnackAmp is a multi-platform music player with normal music player
abilities with a multi-user support and a powerful auto-play list
feature. Currently mp3, wav, ogg vorbis,and many other sound files
are indexed by SnackAmp depending on your preferences.

%prep
%setup -n %{real_name}.vfs

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}/tcl/snackAmp/ \
		%{buildroot}%{_bindir} \
		%{buildroot}%{_datadir}/pixmaps/
dos2unix docs/*.tml docs/*/*.tml docs/*.css docs/*/*.css
dos2unix lib/*.tcl lib/tablelist/*.tcl lib/tablelist/scripts/*.tcl lib/mySnack/*.tcl *.tcl
%{__cp} -afp docs lib %{buildroot}%{_libdir}/tcl/snackAmp/
find %{buildroot}%{_libdir}/tcl/snackAmp/ -type f -exec chmod 0644 {} \;
find %{buildroot}%{_libdir}/tcl/snackAmp/ -type d -exec chmod 0755 {} \;
#%{__install} -p -m0755 icons/snackAmp.ico %{buildroot}%{_datadir}/pixmaps/
%{__install} -p -m0755 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/
%{__install} -Dp -m0755 snackAmp.tcl %{buildroot}%{_libdir}/tcl/snackAmp/snackAmp.tcl
%{__install} -p -m0644 main.tcl snackAmphotKeys.tcl %{buildroot}%{_libdir}/tcl/snackAmp/
%{__ln_s} -f %{_libdir}/tcl/snackAmp/snackAmp.tcl %{buildroot}%{_bindir}/snackamp
%{__ln_s} -f %{_libdir}/tcl/snackAmp/snackAmp.tcl %{buildroot}%{_bindir}/snackAmp

cat <<EOF >%{name}.desktop
[Desktop Entry]
Name=SnackAmp Audio Player
Comment=%{summary}
Icon=%{name}.png
Exec=snackamp
Terminal=false
Type=Application
EOF

%if %{dfi}
	%{__install} -Dp -m0644 snackamp.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/snackamp.desktop
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications
        desktop-file-install --vendor %{desktop_vendor}    \
                --add-category X-Red-Hat-Base              \
                --add-category Application                 \
                --add-category AudioVideo                  \
                --dir %{buildroot}%{_datadir}/applications \
                snackamp.desktop
%endif

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/snackAmp/lib/mySnack/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc readme.txt
#%doc ChangeLog
%{_bindir}/*
%{_libdir}/tcl/snackAmp/
%{_datadir}/pixmaps/*
%if %{dfi}
	%{_datadir}/gnome/apps/Multimedia/*.desktop
%else
	%{_datadir}/applications/*.desktop
%endif

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.2-4.fdw.2
- Rebuild for Fedora Core 5.

* Tue Jun 24 2003 Dag Wieers <dag@wieers.com> - 2.2-0.fdw
- Updated to release 2.2_FDW.

* Wed May 21 2003 Dag Wieers <dag@wieers.com> - 2.2-0
- Updated to release 2.2.

* Sun Apr 27 2003 Dag Wieers <dag@wieers.com> - 2.1.81-0
- Updated to release 2.2B1.

* Thu Jan 30 2003 Dag Wieers <dag@wieers.com> - 2.1.1-1
- Second release of 2.1.1 due to problems with earlier official tarball.

* Tue Dec 03 2002 Dag Wieers <dag@wieers.com> - 2.0.1-0
- Initial package.
