# $Id$
# Authority: matthias

Summary: Powerful image loading and rendering library
Name: imlib2
Version: 1.0.6
Release: 1
License: BSD
Group: System Environment/Libraries
URL: http://enlightenment.org/pages/imlib2.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/enlightenment/imlib2-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libjpeg-devel, libpng-devel, libungif-devel, edb-devel >= 1.0.2
BuildRequires: XFree86-devel, freetype-devel >= 1.2

%description
Imlib2 is an advanced replacement library for libraries like libXpm that
provides many more features with much greater flexibility and speed than
standard libraries, including font rasterization, rotation, RGBA space
rendering and blending, dynamic binary filters, scripting, and more.

%package devel
Summary: Imlib2 headers, static libraries and documentation
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Headers, static libraries and documentation for Imlib2.

%prep
%setup

%build
%configure
%{__ln_s} -f .libs/libImlib2.so src/libImlib2.so
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la \
		%{buildroot}%{_libdir}/loaders/filter/*.{a,la} \
		%{buildroot}%{_libdir}/loaders/image/*.{a,la}

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog README TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/loaders/

%files devel
%defattr(-, root, root, 0755)
%doc doc/
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
#exclude %{_libdir}/*.la

%changelog
* Fri Apr 11 2003 Dag Wieers <dag@wieers.com> - 1.0.6-1
- Build against new edb-1.0.3-0 package.

* Sun Feb 09 2003 Dag Wieers <dag@wieers.com> - 1.0.6-0
- Initial package. (using DAR)
