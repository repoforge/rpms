# $Id$
# Authority: matthias

Summary: Reference encoder and encoding library for MPEG2/4 AAC
Name: faac
Version: 1.23.5
Release: 1
License: GPL
Group: Applications/Multimedia
Source0: http://dl.sf.net/faac/%{name}-%{version}.tar.gz
URL: http://www.audiocoding.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: autoconf, automake, libtool, gcc-c++

%description
FAAC is an AAC audio encoder. It currently supports MPEG-4 LTP, MAIN and LOW
COMPLEXITY object types and MAIN and LOW MPEG-2 object types. It also supports
multichannel and gapless encoding.


%package devel
Summary: Development libraries of the FAAC AAC encoder.
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
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc COPYING ChangeLog README TODO
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so

%changelog
* Thu Feb 26 2004 Matthias Saou <http://freshrpms.net/> 1.23.5-1.fr
- Update to 1.23.5.
- Changed license tag to GPL.

* Mon Nov 17 2003 Matthias Saou <http://freshrpms.net/> 1.23.1-1.fr
- Initial rpm release.

