# $Id$
# Authority: dag

Summary: Simple programming interface for Ogg files and streams
Name: liboggz
Version: 1.1.1
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://www.annodex.net/

#Source: http://www.annodex.net/software/liboggz/download/liboggz-%{version}.tar.gz
Source: http://downloads.xiph.org/releases/liboggz/liboggz-%{version}.tar.gz
### Always have oggz_off_t == loff_t even on 64-bit platforms
Patch0: liboggz-1.1.1-multilib.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: docbook-utils
BuildRequires: doxygen
BuildRequires: libogg-devel >= 1.0

%description
Oggz provides a simple programming interface for reading and writing
Ogg files and streams. Ogg is an interleaving data container developed
by Monty at Xiph.Org, originally to support the Ogg Vorbis audio
format.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libogg-devel >= 1.0
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package doc
Summary: Documentation for liboggz
Group: Documentation
Requires: liboggz = %{version}-%{release}

%description doc
Oggz provides a simple programming interface for reading and writing
Ogg files and streams. Ogg is an interleaving data container developed
by Monty at Xiph.Org, originally to support the Ogg Vorbis audio
format.

This package contains HTML documentation needed for development using
liboggz.

%prep
%setup
%patch0 -p1 -b .multilib

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall docdir="%{buildroot}%{_datadir}/doc/%{name}-doc-%{version}" \
         INSTALL="%{__install} -p"

# not particularly interested in the tex docs, the html version has everything
%{__rm} -rf %{buildroot}%{_datadir}/doc/%{name}-doc-%{version}/latex

# Multilib fix: ensure generated headers have timestamps
# independent of build time
(cd include/oggz &&
    touch -r oggz_off_t_generated.h.in.multilib \
      %{buildroot}%{_includedir}/oggz/oggz_off_t_generated.h
)

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/*
%{_bindir}/oggz*
%{_libdir}/liboggz.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/oggz
%{_libdir}/liboggz.so
%{_libdir}/pkgconfig/oggz.pc
%exclude %{_libdir}/*.la

%files doc
%defattr(-, root, root, 0755)
%doc %{_docdir}/%{name}-doc-%{version}

%changelog
* Wed Nov 17 2010 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Initial package. (based on fedora)
