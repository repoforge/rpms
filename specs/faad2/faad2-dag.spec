# Authority: freshrpms
%define plugindir %(xmms-config --input-plugin-dir)
%define rversion 2.0_rc1

Summary: Library and frontend for decoding MPEG2/4 AAC
Name: faad2
Version: 2.0
Release: 0.rc1
License: GPL
Group: Applications/Multimedia
URL: http://www.audiocoding.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.audiocoding.com/files/%{name}_%{rversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libsndfile-devel >= 1.0.0
BuildRequires: xmms-devel, id3lib-devel, gtk+-devel

%description
FAAD 2 is a LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder, completely
written from scratch. FAAD 2 is licensed under the GPL.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n xmms-aac
Summary: X MultiMedia System input plugin to play AAC files
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}, xmms, id3lib

%description -n xmms-aac
This xmms plugin reads AAC files with and without ID3 tags (version 2.x).
AAC files are MPEG2 or MPEG4 files that can be found in MPEG4 audio files
(.mp4). MPEG4 files with AAC inside can be read by RealPlayer or Quicktime.

%prep
%setup -c %{name}-%{version}

%build
. bootstrap
%configure \
	--disable-dependency-tracking
#export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:%{_builddir}/%{name}-%{version}/libfaad"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la \
		%{buildroot}%{plugindir}/*.la

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
#exclude %{_libdir}/*.la

%files -n xmms-aac
%defattr(-, root, root)
%doc plugins/xmms/AUTHORS plugins/xmms/NEWS plugins/xmms/README plugins/xmms/TODO
%{plugindir}/*.so
#exclude %{plugindir}/*.la

%changelog
* Thu Sep 18 2003 Dag Wieers <dag@wieers.com> - 2.0-0.rc1
- Updated to release 2.0_rc1.
- Resync with Matthias Saou (FreshRPMS).

* Wed Apr 09 2003 Dag Wieers <dag@wieers.com> - 1.1.0.20030409-0
- Initial package. (using DAR)
