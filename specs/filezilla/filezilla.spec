# $Id$
# Authority: shuff
# Upstream: Tim Kosse <tim.kosse$filezilla-project,org>

%define gnutls_version 2.8.5

Summary: GUI SFTP/FTP client
Name: filezilla
Version: 3.3.0
Release: 2%{?dist}
License: GPL
Group: Applications/Net
URL: http://filezilla-project.org/

Source0: http://downloads.sourceforge.net/project/filezilla/FileZilla_Client/%{version}/FileZilla_%{version}_src.tar.bz2
Source1: http://ftp.gnu.org/pub/gnu/gnutls/gnutls-%{gnutls_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: automake, autoconf, binutils, gcc, gcc-c++, make
BuildRequires: dbus-devel
BuildRequires: gettext
BuildRequires: libidn-devel
BuildRequires: ncurses-devel
BuildRequires: pkgconfig >= 0.9.0

# For gnutls
BuildRequires: libgpg-error-devel, libgcrypt-devel, zlib-devel

Requires: filesystem
Requires: gnome-icon-theme

%description
FileZilla Client is a fast and reliable cross-platform FTP, FTPS and SFTP
client with lots of useful features and an intuitive graphical user interface.

%prep
%setup
%setup -T -D -a 1

%build

# First, make a local gnutls
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

# Now, make filezilla
export PKG_CONFIG_PATH="$RESULT_DIR/usr/%{_lib}/pkgconfig:$PKG_CONFIG_PATH"
%configure \
    --disable-dependency-tracking \
    --disable-manualupdatecheck
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING docs/ GPL.html INSTALL NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/*
%dir %{_datadir}/pixmaps
%{_datadir}/filezilla
%{_datadir}/pixmaps/*
%{_datadir}/locale/*/LC_MESSAGES/*
%dir %{_desktopdir}
%{_desktopdir}/*
%{_iconsbasedir}/*/apps/*
%{_libdir}/*

%changelog
* Wed Nov 11 2009 Yury V. Zaytsev <yury@shurup.com> - 3.3.0-2
- Minor fixes to the package: fix missing version and remove useless options.

* Tue Nov 10 2009 Steve Huff <shuff@vecna.org> - 3.3.0-1
- Initial package.
- Thanks to Yury Zaytsev for developing the bundled static library procedure.
