# $Id$
# Authority: dag
# Upstream: <mpeg4ip-discussion@lists.sourceforge.net>

Summary: MPEG-4 streaming tools
Name: mpeg4ip
Version: 1.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://mpeg4ip.sourceforge.net/

Source: http://dl.sf.net/mpeg4ip/mpeg4ip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel, lame-devel, libogg-devel, libvorbis-devel, libid3tag-devel
Requires: faad2

%description
MPEG-4 streaming tools

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

for dir in $(pwd) lib/rtp lib/SDLAudio; do
	pushd $dir
	%{__libtoolize} --force --copy
	%{__aclocal} #--force
	%{__autoheader}
	%{__automake} --add-missing -a --foreign
	%{__autoconf}
	popd
done
%{__ln_s} -f ../../libtool lib/SDLAudio/libtool

find . -type f | xargs %{__perl} -pi.orig -e 's|-Werror||g'

%build
rm -f libtool && cp -a `which libtool` . || :
%configure \
	--enable-server \
	--enable-player
%{__make}
%{__make} -C lib/mp4v2/test mp4broadcaster

%install
%{__rm} -rf %{buildroot}
#%makeinstall
%{__make} install \
	DESTDIR="%{buildroot}"

%{__install} -D -m0755 lib/mp4v2/test/mp4broadcaster %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/mpeg4ip/
%{_datadir}/mp4*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/manm/api.mpt*
%{_includedir}/*

%changelog
* Sat Jan 01 2004 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
