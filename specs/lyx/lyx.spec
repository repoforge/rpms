# $Id$

# Authority: dag
# Upstream: <lyx-devel@lists.lyx.org>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: WYSIWYM (What You See Is What You Mean) frontend to LaTeX
Name: lyx
Version: 1.3.4
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://www.lyx.org/

Packager: Bert de Bruijn <bert@debruijn.be>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.lyx.org/pub/lyx/stable/lyx-%{version}.tar.bz2
Source1: lyx-icon.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: qt-devel 
Requires: qt >= 2.2.1, tetex-xdvi, tetex, tetex-latex
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

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=LyX LaTeX frontend
Comment=Write documents in a WYSIWYM way
Exec=lyx
Icon=lyx-icon.png
Type=Application
Terminal=false
Encoding=UTF-8
Categories=Application;Office;
EOF


%build
%{?rhfc1:export QTDIR="/usr/lib/qt-3.1"}
%{?rhel3:export QTDIR="/usr/lib/qt-3.1"}
%{?rh90:export QTDIR="/usr/lib/qt3"}
%{?rh80:export QTDIR="/usr/lib/qt3"}
%{?rh73:export QTDIR="/usr/lib/qt2"}
%{?rhel21:export QTDIR="/usr/lib/qt2"}
%{?rh62:export QTDIR="/usr/lib/qt-2.1.0"}
%configure \
	--with-frontend="qt" \
	--without-warnings \
	--disable-debug \
	--enable-optimization="%{optflags}"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

### Set up the lyx-specific class files where TeX can see them
%{__install} -d -m0755 %{buildroot}%{_datadir}/texmf/tex/latex/
%{__mv} -f %{buildroot}%{_datadir}/lyx/tex %{buildroot}%{_datadir}/texmf/tex/latex/lyx

### Miscellaneous files
%{__install} -m0644 lib/images/lyx.xpm %{buildroot}%{_datadir}/lyx/images/
%{__install} -m0644 lib/reLyX/README README.reLyX
%{__install} -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/

### Install desktop file and icon
%if %{dfi}
        %{__install} -D -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Applications/
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
        desktop-file-install --vendor kde        \
                --add-category X-Red-Hat-Extra   \
                --dir %{buildroot}%{_datadir}/applications \
                %{name}.desktop
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
%{_datadir}/texmf/tex/latex/lyx/
%{_datadir}/pixmaps/*.png
%if %{dfi}
        %{_datadir}/gnome/apps/Applications/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Thu Mar 18 2004 Bert de Bruijn <bert@debruijn.be> - 1.3.4-1
- Added .desktop file and icon.

* Thu Feb 19 2004 Dag Wieers <dag@wieers.com> - 1.3.4-0
- Updated to release 1.3.4.

* Sat Nov 22 2003 Dag Wieers <dag@wieers.com> - 1.3.3-0
- Updated to release 1.3.3.

* Sun May 11 2003 Dag Wieers <dag@wieers.com> - 1.3.2-0
- Initial package. (using DAR)
