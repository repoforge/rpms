# $Id$
# Authority: dag

# ExcludeDist: fc1 fc2 fc3 el4

Summary: MusicBrainz client library
Name: libmusicbrainz
Version: 2.0.1
Release: 0.2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.musicbrainz.org/

Source: ftp://ftp.musicbrainz.org/pub/musicbrainz/libmusicbrainz-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: automake, libtool, gcc-c++

Provides: musicbrainz
Obsoletes: musicbrainz

%description
The MusicBrainz client library serves as a tool to allow developers to
integrate MusicBrainz searches and metadata exchange functionality into
their applications.

The client library includes the following features:

    * Lookup Audio CD metadata using CD Index Discids
    * Calculate Relatable TRM acoustic fingerprints
    * Search for artist/album/track titles
    * Lookup metadata by name, TRM ids or MusicBrainz Ids

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

Provides: musicbrainz-devel
Obsoletes: musicbrainz-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%{__libtoolize} --force --copy
%configure \
	--enable-shared

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}/pkgconfig
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/musicbrainz/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.1-0.2
- Rebuild for Fedora Core 5.

* Fri May 09 2003 Dag Wieers <dag@wieers.com> - 2.0.1-0
- Initial package. (using DAR)
