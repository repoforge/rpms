# Authority: dag
# Distcc: 0

%define	date 20030319
%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: The avifile library used to play AVI streams.
Name: avifile
Version: 0.7.38
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://avifile.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/avifile/avifile-0.7-%{version}.tar.gz
#Source: http://dl.sf.net/avifile/avifile-%{version}-%{date}.tgz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libstdc++-devel
BuildRequires: qt-devel >= 2.1.0, SDL-devel >= 1.1.3, esound-devel
BuildRequires: libvorbis-devel, libjpeg-devel, libpng-devel
BuildRequires: libmad-devel, lame-devel, a52dec-devel, divx4linux
BuildRequires: zlib-devel, xvidcore-devel

%description
Avifile is a library that allows you to read and write compressed AVI
files in most common video & audio formats (Indeo® Video, DivX, etc.)
under x86 Linux. Compression and decompression are performed with Win32
DLLs. It includes a simple AVI player and a Video4Linux capture program

To use this program, you will need to get the Win32 binaries from
%{url} and put uncompress them under /usr/lib/win32.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
#%setup -n %{name}0.7-%{version}
%setup -n %{name}-0.7-%{version}

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=AVI Player
Comment=%{summary}
Icon=%{name}.png
Exec=aviplay
Terminal=false
MimeType=video/x-msvideo
Type=Application
Categories=Application;AudioVideo;
EOF

%build
%{?rhfc1:export QTDIR="/usr/lib/qt-3.1"}
%{?rhel3:export QTDIR="/usr/lib/qt-3.1"}
%{?rh90:export QTDIR="/usr/lib/qt3"}
%{?rh80:export QTDIR="/usr/lib/qt3"}
%{?rh73:export QTDIR="/usr/lib/qt2"}
%{?rhel21:export QTDIR="/usr/lib/qt2"}
%{?rh62:export QTDIR="/usr/lib/qt-2.1.0"}
./autogen.sh
%configure \
	--program-prefix="%{?_program_prefix}" \
	--enable-static \
	--enable-quiet \
	--enable-release \
	--enable-lame-bin \
	--enable-win32 \
	--enable-x86opt
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#make install DESTDIR="%{buildroot}"
%makeinstall
%{__install} -m0644 -D bin/test.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%if %{dfi}
	%{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Multimedia/
	%{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/
%else
	%{__install} -m0755 -d %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor=net                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{name}.desktop
%endif

%{__rm} -f doc/Makefile*

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}{,/avifile0.7,/avifile0.7/vidix}/*.la

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README doc/CREDITS doc/EXCEPTIONS doc/KNOWN_BUGS doc/README-DEVEL doc/TODO doc/VIDEO-PERFORMANCE doc/WARNINGS
%doc %{_mandir}/man?/*
%dir %{_libdir}/avifile0.7/
%{_bindir}/avibench
%{_bindir}/avicap
%{_bindir}/avicat
%{_bindir}/avimake
%{_bindir}/aviplay
%{_bindir}/avirec
%{_bindir}/avirecompress
%{_bindir}/avitype
%attr(4755, root, root) %{_bindir}/kv4lsetup
%{_libdir}/*.so.*
%{_libdir}/avifile0.7/*.so
%{_libdir}/avifile0.7/vidix/*.so
%{_datadir}/avifile0.7/
%{_datadir}/pixmaps/*
%if %{dfi}
        %{_datadir}/gnome/apps/Multimedia/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/avifile-config
#%{_bindir}/mmxnow-config
%{_includedir}/avifile/
#%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/avifile0.7/*.a
%{_libdir}/avifile0.7/vidix/*.a
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*
#exclude %{_libdir}/*.la
#exclude %{_libdir}/avifile0.7/*.la
#exclude %{_libdir}/avifile0.7/vidix/*.la

%changelog
* Sat Dec 20 2003 Dag Wieers <dag@wieers.com> - 0.7.38-0
- Updated to release 0.7.38.

* Sat Aug 23 2003 Dag Wieers <dag@wieers.com> - 0.7.34-1
- Rebuild against xvidcore-0.9.2.

* Sat Apr 05 2003 Dag Wieers <dag@wieers.com> - 0.7.34-0
- Updated to release 0.7.34-20030319.

* Wed Feb 19 2003 Dag Wieers <dag@wieers.com> - 0.7.26-1
- Build against new lame-3.93.1-1 package.

* Sun Jan 19 2003 Dag Wieers <dag@wieers.com> - 0.7.26-0
- Initial package. (using DAR)
