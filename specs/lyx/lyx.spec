# $Id$
# Authority: dag
# Upstream: <lyx-devel$lists,lyx,org>

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: WYSIWYM (What You See Is What You Mean) frontend to LaTeX
Name: lyx
Version: 1.5.6
Release: 1%{?dist}
License: GPL
Group: Applications/Publishing
URL: http://www.lyx.org/

Source: ftp://ftp.lyx.org/pub/lyx/stable/lyx-%{version}.tar.bz2
Source1: lyx-icon.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt4-devel, gcc-c++
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: qt4 >= 4.1.1, tetex-xdvi, tetex, tetex-latex
Obsoletes: tetex-lyx

%description
LyX is a modern approach to writing documents which breaks with the
obsolete "typewriter paradigm" of most other document preparation
systems.

It is designed for people who want professional quality output
with a minimum of time and effort, without becoming specialists in
typesetting.

The major innovation in LyX is WYSIWYM (What You See Is What You Mean).
That is, the author focuses on content, not on the details of formatting.
This allows for greater productivity, and leaves the final typesetting
to the backends (like LaTeX) that are specifically designed for the task.

With LyX, the author can concentrate on the contents of his writing,
and let the computer take care of the rest.


%prep
%setup

%{__cat} <<EOF >lyx.desktop
[Desktop Entry]
Name=LyX LaTeX Frontend
Comment=Write documents in a WYSIWYM way
Exec=lyx
Icon=lyx.png
Type=Application
Terminal=false
Encoding=UTF-8
Categories=Application;Office;
EOF

%build
%configure \
    --disable-assertions \
    --disable-concept-checks \
    --disable-debug \
    --disable-dependency-tracking \
    --disable-rpath \
    --disable-stdlib-debug \
    --enable-compression-support \
    --enable-optimization="%{optflags}" \
    --with-aiksaurus \
    --with-aspell \
    --with-frontend="qt4" \
    --with-qt4-dir="%{_libdir}/qt4" \
    --without-warnings
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

### Set up the lyx-specific class files where TeX can see them
%{__install} -d -m0755 %{buildroot}%{_datadir}/texmf/tex/latex/
%{__mv} -f %{buildroot}%{_datadir}/lyx/tex %{buildroot}%{_datadir}/texmf/tex/latex/lyx

### Miscellaneous files
%{__install} -Dp -m0644 lib/images/lyx.xpm %{buildroot}%{_datadir}/lyx/images/lyx.xpm
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/lyx.png
#%{__install} -p -m0644 lib/reLyX/README README.reLyX

### Install desktop file and icon
%if %{?_without_freedesktop:1}0
        %{__install} -Dp -m0644 lyx.desktop %{buildroot}%{_datadir}/gnome/apps/Applications/
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
        desktop-file-install --vendor %{desktop_vendor} \
                --add-category X-Red-Hat-Extra          \
                --dir %{buildroot}%{_datadir}/applications \
                lyx.desktop
%endif

%post
### Make TeX understand where LyX-specific packages are
texhash &>/dev/null

### Before configuring lyx for the local system PATH needs to be imported
if [ -r /etc/profile ]; then
    . /etc/profile
fi

### Now configure LyX
cd %{_datadir}/lyx/
%configure --srcdir &>/dev/null

### Fix reLyX perl program if the prefix is non-standard
%{__perl} -pi -e 's|/usr/share/lyx|%{_datadir}/lyx|' %{_bindir}/reLyX

%postun
### Fix the TeX file hash
texhash &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ANNOUNCE ChangeLog COPYING NEWS README* UPGRADING
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/lyx/
%{_datadir}/pixmaps/lyx.png
%{_datadir}/texmf/tex/latex/lyx/
%{?_without_freedesktop:%{_datadir}/gnome/apps/Applications/lyx.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-lyx.desktop}

%changelog
* Sat Nov 08 2008 Christoph Maser <cmr@financial.com> - 1.5.6-1
- Updated to release 1.5.6.

* Sat Aug 11 2007 Dag Wieers <dag@wieers.com> - 1.5.1-1
- Updated to release 1.5.1.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.4.1-1
- Updated to release 1.4.1.

* Fri Nov 05 2004 Dag Wieers <dag@wieers.com> - 1.3.5-1
- Updated to release 1.3.5.

* Thu Mar 18 2004 Bert de Bruijn <bert@debruijn.be> - 1.3.4-1
- Added .desktop file and icon.

* Thu Feb 19 2004 Dag Wieers <dag@wieers.com> - 1.3.4-0
- Updated to release 1.3.4.

* Sat Nov 22 2003 Dag Wieers <dag@wieers.com> - 1.3.3-0
- Updated to release 1.3.3.

* Sun May 11 2003 Dag Wieers <dag@wieers.com> - 1.3.2-0
- Initial package. (using DAR)
