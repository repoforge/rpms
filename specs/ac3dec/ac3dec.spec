# $Id$
# Authority: dag

Summary: Free AC-3 stream decoder
Name: ac3dec
Version: 0.6.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://liba52.sourceforge.net/downloads.html

Source: http://liba52.sourceforge.net/files/ac3dec-%{version}.tar.gz
Patch0: ac3dec-0.6.1-libac3-memcpy.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
%{_bindir}/ac3dec
%{_bindir}/extract_ac3

%changelog
* Tue Feb 09 2004 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Initial package. (using DAR)
