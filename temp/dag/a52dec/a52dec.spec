# Authority: freshrpms

Summary: Free library for decoding ATSC A/52 (aka AC-3) streams.
Name: a52dec
Version: 0.7.4
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://liba52.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://liba52.sourceforge.net/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
liba52 is a free library for decoding ATSC A/52 streams. It is released
under the terms of the GPL license. The A/52 standard is used in a
variety of applications, including digital television and DVD. It is
also known as AC-3.

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

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING HISTORY NEWS README TODO doc/liba52.txt
%doc %{_mandir}/man?/*
%{_bindir}/*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/a52dec/
%{_libdir}/*.a
#exclude %{_libdir}/*.la

%changelog
* Sun Jan 19 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
