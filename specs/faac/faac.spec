# $Id$
# Authority: matthias

Summary: Reference encoder and encoding library for MPEG2/4 AAC
Name: faac
Version: 1.24
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.audiocoding.com/
Source: http://dl.sf.net/faac/faac-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: autoconf, automake, libtool, gcc-c++

%description
FAAC is an AAC audio encoder. It currently supports MPEG-4 LTP, MAIN and LOW
COMPLEXITY object types and MAIN and LOW MPEG-2 object types. It also supports
multichannel and gapless encoding.


%package devel
Summary: Development libraries of the FAAC AAC encoder
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
FAAC is an AAC audio encoder. It currently supports MPEG-4 LTP, MAIN and LOW
COMPLEXITY object types and MAIN and LOW MPEG-2 object types. It also supports
multichannel and gapless encoding.

This package contains development files and documentation for libfaac.


%prep
%setup -n %{name}


%build
sh bootstrap
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null


%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la


%changelog
* Mon May  3 2004 Matthias Saou <http://freshrpms.net/> 1.24-1
- Update to 1.24.

* Thu Feb 26 2004 Matthias Saou <http://freshrpms.net/> 1.23.5-1
- Update to 1.23.5.
- Changed license tag to GPL.

* Mon Nov 17 2003 Matthias Saou <http://freshrpms.net/> 1.23.1-1
- Initial rpm release.

