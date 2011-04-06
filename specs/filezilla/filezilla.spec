# $Id$
# Authority: shuff
# Upstream: Tim Kosse <tim.kosse$filezilla-project,org>

%{?el3:%define _with_bundled_gnutls 1}
%{?el4:%define _with_bundled_gnutls 1}
%{?el5:%define _with_bundled_gnutls 1}

%define gnutls_version 2.8.5

Summary: GUI SFTP/FTP client
Name: filezilla
Version: 3.4.0
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://filezilla-project.org/

Source0: http://prdownloads.sourceforge.net/project/filezilla/FileZilla_Client/%{version}/FileZilla_%{version}_src.tar.bz2
%{?_with_bundled_gnutls:Source1: http://ftp.gnu.org/pub/gnu/gnutls/gnutls-%{gnutls_version}.tar.bz2}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: dbus-devel
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: libidn-devel
BuildRequires: ncurses-devel
BuildRequires: pkgconfig >= 0.9.0
BuildRequires: wxGTK-devel
BuildRequires: xdg-utils

%if 0%{?_with_bundled_gnutls}
### For gnutls
BuildRequires: libgpg-error-devel
BuildRequires: libgcrypt-devel
BuildRequires: zlib-devel
%else
BuildRequires: gnutls-devel >= %{gnutls_version}
%endif

Requires: filesystem
Requires: gnome-icon-theme
Requires: xdg-utils

%description
FileZilla Client is a fast and reliable cross-platform FTP, FTPS and SFTP
client with lots of useful features and an intuitive graphical user interface.

%prep
%setup
%{?_with_bundled_gnutls:%setup -T -D -a 1}

%build
%if 0%{?_with_bundled_gnutls}
#### First, make a local gnutls
pushd gnutls-%{gnutls_version}
RESULT_DIR=`pwd`/result

./configure \
    --with-included-libcfg \
    --with-included-libtasn1 \
    --disable-dependency-tracking \
    --disable-shared \
    --enable-static \
    --disable-guile \
    --disable-rpath \
    --prefix="$RESULT_DIR" \
    --libdir="$RESULT_DIR/usr/%{_lib}"

%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" install
popd

export PKG_CONFIG_PATH="$RESULT_DIR/usr/%{_lib}/pkgconfig:$PKG_CONFIG_PATH"
%endif

### Now, make filezilla
%configure \
    --enable-static=%{?_with_bundled_gnutls:yes}%{!?_with_bundled_gnutls:no} \
    --enable-locales \
    --disable-dependency-tracking \
    --disable-manualupdatecheck \
    --with-tinyxml=builtin
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING docs/ GPL.html INSTALL NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/applications/filezilla.desktop
%{_datadir}/filezilla/
%{_datadir}/icons/hicolor/*/apps/filezilla.png
%{_datadir}/pixmaps/filezilla.png

%changelog
* Wed Apr 06 2011 Steve Huff <shuff@vecna.org> - 3.4.0-1
- Updated to version 3.4.0.
- On el6, use the system gnutls.
- Generate locale files.

* Fri Oct 29 2010 Steve Huff <shuff@vecna.org> - 3.3.4.1-1
- Updated to version 3.3.4.1.
- Captured missing wxGTK dependency.

* Mon Jun 14 2010 Steve Huff <shuff@vecna.org> - 3.3.3-1
- Updated to version 3.3.3.

* Fri Jun 11 2010 Steve Huff <shuff@vecna.org> - 3.3.2.1-1
- Updated to version 3.3.2.1.

* Sun Feb 21 2010 Steve Huff <shuff@vecna.org> - 3.3.2-1
- Updated to version 3.3.2.

* Tue Jan 05 2010 Steve Huff <shuff@vecna.org> - 3.3.1-1
- Updated to version 3.3.1.

* Tue Nov 17 2009 Steve Huff <shuff@vecna.org> - 3.3.0.1-1
- Updated to version 3.3.0.1.

* Wed Nov 11 2009 Yury V. Zaytsev <yury@shurup.com> - 3.3.0-2
- Minor fixes to the package: fix missing version and remove useless options.

* Tue Nov 10 2009 Steve Huff <shuff@vecna.org> - 3.3.0-1
- Initial package.
- Thanks to Yury Zaytsev for developing the bundled static library procedure.
