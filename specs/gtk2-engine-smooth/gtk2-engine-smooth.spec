# $Id$

Summary: Smooth theme engine and basic themes
Name: gtk2-engine-smooth
Version: 0.5.8
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://sourceforge.net/projects/smooth-engine/
Source0: http://dl.sf.net/smooth-engine/gtk-smooth-engine-%{version}.tar.gz
Source1: http://dl.sf.net/smooth-engine/smooth-themes-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gtk2 >= 2.4.0, gtk+
BuildRequires: gtk2-devel >= 2.4.0, gtk+-devel >= 1.2.9, gdk-pixbuf-devel
BuildRequires: gcc-c++

%description
The Smooth Theme Engine is a simple theme engine intended to be smooth, fast,
and highly configurable, such that it could eventually mimic most, if not all,
major theme engines to high degree of acuracy, while still retaining a small
footprint.
This package contains both the GTK2 and the GTK1 versions, as well as themes.


%prep
%setup -n gtk-smooth-engine-%{version} -a 1


%build
%configure \
    --enable-gtk-1 \
    --enable-gtk-2
%{__make} %{?_smp_mflags}

# The themes
pushd smooth-themes-%{version}
    %configure \
        --enable-gtk-1 \
        --enable-gtk-2
    %{__make} %{?_smp_mflags}
popd


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%{__make} -C smooth-themes-%{version} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README
%{_libdir}/gtk/themes/engines/libsmooth.*
%{_libdir}/gtk-2.0/2.4.0/engines/libsmooth.*
%{_datadir}/themes/*


%changelog
* Tue Nov  2 2004 Matthias Saou <http://freshrpms.net/> 0.5.8-1
- Initial RPM package.

