# $Id$

# Authority: dag

Summary: Free AC-3 stream decoder.
Name: ac3dec
Version: 0.6.1
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://www.au.linuxvideo.org/ac3dec/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://gusnet.cx/aaron/codecs/tarballs/ac3dec-%{version}.tar.gz
Patch0: ac3dec-0.6.1-libac3-memcpy.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
Free AC-3 stream decoder. See also a52dec.

%prep
%setup
%patch0 -p1 -b .memcpy

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING README TODO
%{_bindir}/*

%changelog
* Tue Feb 09 2004 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Initial package. (using DAR)
