# $Id$
# Authority: dag

# ExcludeDist: fc2 fc3 el4

Summary: HTTP library implementation
Name: libsoup
Version: 1.99.26
Release: 0.2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: ftp://ftp.gnome.org/pub/gnome/sources/libsoup/

Source: ftp://ftp.gnome.org/pub/gnome/sources/libsoup/1.99/libsoup-%{version}.tar.bz2
Patch: libsoup-1.99.26-fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel, openssl-devel, gnutls-devel >= 0.8.10, libgcrypt-devel >= 1.1.12
BuildRequires: gettext
%{?fc4:BuildRequires: gettext-devel}
Obsoletes: soup <= %{version}

%description
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.
libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it).

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: soup-devel <= %{version}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch -p0

%build
if pkg-config openssl; then
	export CFLAGS="%{optflags} $(pkg-config --cflags openssl)"
	export CPPFLAGS="%{optflags} $(pkg-config --cflags openssl)"
	export LDFLAGS="$(pkg-config --libs-only-L openssl)"
fi

%configure \
	--disable-dependency-tracking \
	--enable-gtk-doc \
	--disable-more-warnings \
	--enable-ssl
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/*.so.*
#%{_libexecdir}/libsoup-ssl-proxy

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/soup-2.0/
%{_libdir}/pkgconfig/*.pc

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.99.26-0.2
- Rebuild for Fedora Core 5.

* Wed Dec 31 2003 Dag Wieers <dag@wieers.com> - 1.99.26-0
- Initial package. (using DAR)
