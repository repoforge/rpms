# $Id$
# Authority: dag

# Dist: nodist

%define real_version 20050216

Summary: W32 Codec package for MPlayer on x86 UNIX systems
Name: w32codec
Version: 1.0
Release: 0.%{real_version}.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://mplayerhq.hu/homepage/design7/dload.html

Source: ftp://ftp.mplayerhq.hu/MPlayer/releases/codecs/all-%{real_version}.tar.bz2
NoSource: 0
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386

%description
W32 Codec package for MPlayer on x86 UNIX systems.

%prep
%setup -n all-%{real_version}

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}/win32
%{__install} -p -m0644 * %{buildroot}%{_libdir}/win32/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_libdir}/win32/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-0.%{real_version}.2
- Rebuild for Fedora Core 5.

* Sat Mar 19 2005 Dag Wieers <dag@wieers.com> - 1.0-0.20050216
- Transformed into nosrc package.

* Sat Jan 18 2003 Dag Wieers <dag@wieers.com> - 0.90.7-0
- Updated to newer codecs.
- Added more codecs.

* Sun May 27 2001 Dag Wieers <dag@wieers.com> - 20010122
- Simplified SPEC-file.

* Fri Mar 30 2001 Dag Wieers <dag@wieers.com> - 20010122
- Initial package.
