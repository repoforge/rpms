# $Id$
# Authority: matthias

Summary: Library for encoding and decoding H264/AVC video streams
Name: x264
Version: 0.0.281
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://developers.videolan.org/x264.html
# Available through "svn co svn://svn.videolan.org/x264/trunk x264"
# find x264 -name .svn | xargs rm -rf
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: xorg-x11-devel, nasm
# version.sh requires svnversion
BuildRequires: subversion

%description
x264 is a free library for encoding H264/AVC video streams, written from
scratch.


%package devel
Summary: Development files for the x264 library
Group: Development/Libraries
# Only an include file and a static lib, so don't require the main package
#Requires: %{name} = %{version}

%description devel
x264 is a free library for encoding H264/AVC video streams, written from
scratch.


%prep
%setup
# AUTHORS file is in iso-8859-1
iconv -f iso-8859-1 -t utf-8 -o AUTHORS.utf8 AUTHORS
mv -f AUTHORS.utf8 AUTHORS


%build
%configure \
    --enable-pthread \
    --enable-visualize \
    --enable-debug \
    --extra-cflags="%{optflags}"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


#post
#/sbin/ldconfig

#postun
#/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING TODO
%{_bindir}/x264

%files devel
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING TODO
%{_includedir}/x264.h
%{_libdir}/libx264.a


%changelog
* Tue Aug  2 2005 Matthias Saou <http://freshrpms.net/> 0.0.281-1
- Update to svn 281.

* Mon Jul 11 2005 Matthias Saou <http://freshrpms.net/> 0.0.273-1
- Initial RPM release.

