# Authority: dag

### FIXME: openquicktime: Depends: libopenquicktime.so but it is not installable

Summary: A portable library for handling Apples QuickTime(tm) format.
Name: openquicktime
Version: 1.0
Release: 0
License: GPL
Group: System Environment/Libraries
URL: http://www.openquicktime.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/openquicktime/%{name}-%{version}-src.tgz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
OpenQuicktime aims to be a portable library for handling Apples QuickTime
popular media files on Unix-like environments. It is aim is to provide
encoding, authoring and editing support as well as video playback.

%prep
%setup -n %{name}-%{version}-src

%build
%configure \
	--disable-dependency-tracking
%{__make} %{_smp_mflags}

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
* Thu Aug 28 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
