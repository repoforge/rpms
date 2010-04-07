# $Id$
# Authority: shuff
# Upstream: Tim Kosse <tim.kosse$filezilla-project,org>

%define gnutls_version 2.8.5

Summary: GUI SFTP/FTP client
Name: filezilla
Version: 3.3.2
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://filezilla-project.org/

Source0: http://dl.sf.net/project/filezilla/FileZilla_Client/%{version}/FileZilla_%{version}_src.tar.bz2
Source1: http://ftp.gnu.org/pub/gnu/gnutls/gnutls-%{gnutls_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: dbus-devel
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: libidn-devel
BuildRequires: ncurses-devel
BuildRequires: pkgconfig >= 0.9.0
BuildRequires: xdg-utils

### For gnutls
BuildRequires: libgpg-error-devel
BuildRequires: libgcrypt-devel
BuildRequires: zlib-devel

Requires: filesystem
Requires: gnome-icon-theme
Requires: xdg-utils

%description
FileZilla Client is a fast and reliable cross-platform FTP, FTPS and SFTP
client with lots of useful features and an intuitive graphical user interface.

%prep
%setup
%setup -T -D -a 1

%build
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

### Now, make filezilla
export PKG_CONFIG_PATH="$RESULT_DIR/usr/%{_lib}/pkgconfig:$PKG_CONFIG_PATH"
%configure \
    --disable-dependency-tracking \
    --disable-manualupdatecheck
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING docs/ GPL.html INSTALL NEWS README
%doc %{_mandir}/man1/filezilla.1*
%doc %{_mandir}/man1/fzputtygen.1*
%doc %{_mandir}/man1/fzsftp.1*
%doc %{_mandir}/man5/fzdefaults.xml.5*
%{_bindir}/filezilla
%{_bindir}/fzputtygen
%{_bindir}/fzsftp
%{_datadir}/applications/filezilla.desktop
%{_datadir}/filezilla/
%{_datadir}/icons/hicolor/*/apps/filezilla.png
%{_datadir}/pixmaps/filezilla.png

%changelog
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
