# $Id$
# Authority: axel
# PackageDir: /forbidden

%define real_version 0.90pre7
%define nversion 0.90

Summary: W32 Codec package for MPlayer on x86 UNIX systems
Name: w32codec
Version: 0.90.7
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://divx.euro.ru/binaries-010122.zip

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://ftp.lug.udel.edu/MPlayer/releases/%{name}-%{real_version}.tar.bz2
Source1: http://ftp.lug.udel.edu/MPlayer/releases/codecs/win32codecs.tar.bz2
Source2: http://ftp.lug.udel.edu/MPlayer/releases/codecs/qt6dlls.tar.bz2
Source3: http://ftp.lug.udel.edu/MPlayer/releases/codecs/qtextras.tar.bz2
Source4: http://ftp.lug.udel.edu/MPlayer/releases/codecs/rp8codecs.tar.bz2
Source5: http://ftp.lug.udel.edu/MPlayer/releases/codecs/rp9codecs.tar.bz2
Source6: http://ftp.lug.udel.edu/MPlayer/releases/codecs/xanimdlls.tar.bz2
Source7: http://ftp.lug.udel.edu/MPlayer/releases/codecs/mjpeg2kdlls.tar.bz2
Source8: http://ftp.lug.udel.edu/MPlayer/releases/codecs/dmocodecs.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
W32 Codec package for MPlayer on x86 UNIX systems.

%prep
%setup -c
%setup -T -D -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}/win32
%{__install} -m0644 w32codec-%{nversion}/* %{buildroot}%{_libdir}/win32/
%{__install} -m0644 win32codecs/* %{buildroot}%{_libdir}/win32/
%{__install} -m0644 qt6dlls/* %{buildroot}%{_libdir}/win32/
%{__install} -m0644 qtextras/* %{buildroot}%{_libdir}/win32/
%{__install} -m0644 rp8codecs/* %{buildroot}%{_libdir}/win32/
%{__install} -m0644 rp9codecs/* %{buildroot}%{_libdir}/win32/
%{__install} -m0644 xanimdlls/* %{buildroot}%{_libdir}/win32/
%{__install} -m0644 mjpeg2kdlls/* %{buildroot}%{_libdir}/win32/
%{__install} -m0644 dmocodecs/* %{buildroot}%{_libdir}/win32/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libdir}/win32/

%changelog
* Sat Jan 18 2003 Dag Wieers <dag@wieers.com> - 0.90.7-0
- Updated to newer codecs.
- Added more codecs.

* Sun May 27 2001 Dag Wieers <dag@wieers.com> - 20010122
- Simplified SPEC-file.

* Fri Mar 30 2001 Dag Wieers <dag@wieers.com> - 20010122
- Initial package.
