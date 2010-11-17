# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Libraries to handle the Kate bitstream format
Name: libkate
Version: 0.3.7
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://code.google.com/p/libkate/

Source: http://libkate.googlecode.com/files/libkate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison
BuildRequires: flex
BuildRequires: doxygen
BuildRequires: libogg-devel
BuildRequires: liboggz
BuildRequires: libpng-devel
BuildRequires: python-devel
 
%description
This is libkate, the reference implementation of a codec for the Kate bitstream
format. Kate is a karaoke and text codec meant for encapsulation in an Ogg
container.  It can carry text, images, and animate them.

Kate is meant to be used for karaoke alongside audio/video streams (typically
Vorbis and Theora), movie subtitles, song lyrics, and anything that needs text
data at arbitrary time intervals.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libogg-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package utils
Summary: Encoder/Decoder utilities for %{name}
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}
Requires: liboggz

%description utils
The %{name}-utils package contains the katedec/kateenc binaries for %{name}.

%package docs
Summary: Documentation for %{name}
Group: Documentation
#BuildArch: noarch

%description docs
The %{name}-docs package contains the docs for %{name}.

%prep
%setup

### We regenerate theses files at built step
%{__rm} tools/kate_parser.{c,h}
%{__rm} tools/kate_lexer.c

%build
%configure --disable-static \
  --docdir=%{_docdir}/%{name}-%{version}

### Remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALL="install -p"

### Fix for header timestamps
touch -r %{buildroot}%{_includedir}/kate/{kate_config.h,kate.h}

%check
%{__make} check

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc %{_docdir}/libkate-%{version}
%{_libdir}/*.so.*
%exclude %{_docdir}/libkate-%{version}/html

%files devel
%defattr(-, root, root, 0755)
%doc examples/
%{_includedir}/kate/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/*.la

%files utils
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/KateDJ.*
%doc %{_mandir}/man1/katalyzer.*
%doc %{_mandir}/man1/katedec.*
%doc %{_mandir}/man1/kateenc.*
%{_bindir}/KateDJ
%{_bindir}/katalyzer
%{_bindir}/katedec
%{_bindir}/kateenc
%{python_sitelib}/kdj/

%files docs
%defattr(-, root, root, 0755)
%doc %{_docdir}/libkate-%{version}/html

%changelog
* Wed Nov 17 2010 Dag Wieers <dag@wieers.com> - 0.3.7-1
- Initial package. (based on fedora)
