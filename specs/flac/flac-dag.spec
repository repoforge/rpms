# Authority: freshrpms
%define	plugindir %(xmms-config --input-plugin-dir)

Summary: Free lossless audio codec.
Name: flac
Version: 1.1.0
Release: 3
License: GPL
Group: Applications/Multimedia
URL: http://flac.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/flac/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: xmms-devel, id3lib-devel, libogg-devel, nasm
Obsoletes: flac-libs

%description
FLAC is an Open Source lossless audio codec developed by Josh Coalson.

FLAC is comprised of 1) `libFLAC', a library which implements
reference encoders and decoders, licensed under the GNU Lesser
General Public License (LGPL); 2) `flac', a command-line program for
encoding and decoding files, licensed under the GNU General public
License (GPL); 3) `metaflac', a command-line program for editing
FLAC metadata, licensed under the GPL; 4) player plugins for XMMS
and Winamp, licensed under the GPL; and 5) documentation, licensed
under the GNU Free Documentation License.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n xmms-flac
Summary: X MultiMedia System plugin to play FLAC files.
Group: Applications/Multimedia
Requires: xmms, id3lib, %{name} = %{version}-%{release}
Obsoletes: flac-xmms

%description -n xmms-flac
An input plugin that enables playback of FLAC files in xmms.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{plugindir}
%makeinstall xmmsinputplugindir="%{buildroot}%{plugindir}"
find doc/ -name "Makefile*" -exec %{__rm} -f {} \;

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la \
		%{buildroot}%{plugindir}/*.la

%post
/sbin/ldconfig &>/dev/null
%postun
/sbin/ldconfig &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING* README
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4
#exclude %{_libdir}/*.la

%files -n xmms-flac
%defattr(-, root, root, 0755)
%{plugindir}/*.so
#exclude %{plugindir}/*.la

%changelog
* Tue Jan 27 2004 Dag Wieers <dag@wieers.com> - 1.1.0-3
- Added Obsoletes-tag for flac-libs. (Ole Jacob Taraldset)

* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 1.1.0-2
- Rebuild against new id3lib-3.8.3 package.

* Thu Apr 03 2003 Dag Wieers <dag@wieers.com> - 1.1.0-1
- Renamed "flac-xmms" subpackage to "xmms-flac".

* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 1.1.0-0
- Initial package. (using DAR)
