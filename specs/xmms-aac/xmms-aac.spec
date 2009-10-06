# $Id$
# Authority: matthias
# Upstream: <info$audicoding,com>

Summary: X MultiMedia System input plugin to play AAC files
Name: xmms-aac
Version: 2.6.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.audiocoding.com/
Source: http://dl.sf.net/faac/faad2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# Since the library version doesn't get bumped as it should, hardcode this dep
Requires: faad2 = %{version}
BuildRequires: autoconf, automake, libtool
BuildRequires: xmms-devel, id3lib-devel, faad2-devel

%description
This xmms plugin reads AAC files with and without ID3 tags (version 2.x).
AAC files are MPEG2 or MPEG4 files that can be found in MPEG4 audio files
(.mp4). MPEG4 files with AAC inside can be read by RealPlayer or Quicktime.


%prep
%setup -n faad2
# Fix file modes (docs and sources shouldn't be executable)
find plugins/xmms/ -type f -exec chmod 644 {} \;
### Required to make automake < 1.7 work
%{__perl} -pi -e 's|dnl AC_PROG_CXX|AC_PROG_CXX|' configure.in


%build
# This is what the README.linux file recommends
autoreconf -vif
%configure --with-xmms --disable-dependency-tracking --disable-static
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 0755 plugins/xmms/src/.libs/libmp4.so \
    %{buildroot}%{_libdir}/xmms/Input/libmp4.so


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc COPYING plugins/xmms/AUTHORS plugins/xmms/README
%dir %{_libdir}/xmms/Input/
%{_libdir}/xmms/Input/libmp4.so


%changelog
* Tue Oct 06 2009 Steve Huff <shuff@vecna.org> - 2.6.1-1
- Updated to version 2.6.1.

* Tue Jan  9 2007 Matthias Saou <http://freshrpms.net/> 2.5-1
- Fork off xmms-aac as a separate package since users seem to be requesting it.
  (did I already mention that you should be using audacious?)
- Include patch to remove BMP and fix build.

