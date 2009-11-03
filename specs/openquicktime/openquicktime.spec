# $Id$
# Authority: dag

Summary: Portable library for handling Apples QuickTime(tm) format
Name: openquicktime
Version: 1.0
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.openquicktime.org/

Source: http://dl.sf.net/openquicktime/openquicktime-%{version}-src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, glib-devel, zlib-devel
Provides: libopenquicktime.so

%description
OpenQuicktime aims to be a portable library for handling Apples QuickTime
popular media files on Unix-like environments. It is aim is to provide
encoding, authoring and editing support as well as video playback.

%prep
%setup -n %{name}-%{version}-src

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
### FIXME: Makefile doesn't create %{_libdir}
%{__install} -d -m0755 %{buildroot}%{_libdir}
%makeinstall

### FIXME: Add a libmajor to libraries
for lib in %{buildroot}%{_libdir}/*.so; do
	%{__mv} -f $lib $lib.0
	%{__ln_s} -f $(basename $lib).0 $lib
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_includedir}/openquicktime/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 08 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Added provides for libopenquicktime.so. (Fridrich Strba)

* Thu Aug 28 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
