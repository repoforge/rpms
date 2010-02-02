# $Id$
# Authority: shuff
# Upstream: http://www.webkitgtk.org/
# EnableDist: el5

# Test

%define real_name webkit
%define libsoup_major 2.25
%define libsoup_version 2.25.91

Summary: GTK+ port of the WebKit HTML renderer
Name: gtk-webkit
Version: 1.1.9
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.webkitgtk.org/

Source0: http://www.webkitgtk.org/webkit-%{version}.tar.gz
Source1: ftp://ftp.gnome.org/pub/GNOME/sources/libsoup/%{libsoup_major}/libsoup-%{libsoup_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc, gcc-c++, make, autoconf, automake
BuildRequires: bison
BuildRequires: cairo-devel
BuildRequires: enchant-devel
#BuildRequires: flex >= 2.5.33
BuildRequires: flex
BuildRequires: freetype-devel
BuildRequires: gail-devel
BuildRequires: gawk
#BuildRequires: glib2-devel >= 2.21.3
BuildRequires: glib2-devel
BuildRequires: gnome-keyring-devel
BuildRequires: gperf
BuildRequires: gstreamer-devel
BuildRequires: gtk-doc
BuildRequires: gtk2-devel
BuildRequires: libgail-gnome-devel
BuildRequires: libicu-devel
BuildRequires: librsvg2-devel
#BuildRequires: libsoup-devel
BuildRequires: libxslt-devel
BuildRequires: pango-devel
BuildRequires: perl
BuildRequires: pkgconfig
BuildRequires: sqlite-devel

%description
WebKit/GTK+ is the new GTK+ port of the WebKit, an open-source web content
engine that powers numerous applications such as web browsers, email clients,
feed readers, web and text editors, and a whole lot more.

%prep
%setup -n %{real_name}-%{version}
%setup -n %{real_name}-%{version} -T -D -a 1


%build
# First, make a local libsoup
pushd libsoup-%{libsoup_version}
RESULT_DIR=`pwd`/result

./configure \
    --disable-dependency-tracking \
    --disable-shared \
    --enable-static \
    --prefix="$RESULT_DIR" \
    --libdir="$RESULT_DIR/usr/%{_lib}"

%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" install
popd

# Now, make webkit
export PKG_CONFIG_PATH="$RESULT_DIR/usr/%{_lib}/pkgconfig:$PKG_CONFIG_PATH"
CFLAGS="%{optflags}" %configure --disable-dependency-tracking \
                                --enable-3D-transforms \
                                --enable-gnomekeyring \
                                --enable-gtk-doc
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog INSTALL README
%doc %{_mandir}/man?/*

%changelog
* Tue Feb 02 2010 Steve Huff <shuff@vecna.org> - 1.1.15.4-1
- Initial package.
