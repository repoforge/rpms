# Authority: freshrpms
# Upstream: Tim Wright <tim@ignavus.net>

%define	_plugindir %(xmms-config --general-plugin-dir)

Summary: XOSD displays transparent text on your screen like the OSD of TVs
Name: xosd
Version: 2.2.1
Release: 0
License: GPL
Group: System Environment/Libraries
URL: http://www.ignavus.net/software.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.ignavus.net/xosd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, xmms-devel

%description
XOSD displays text on your screen, sounds simple right? The difference is
it is unmanaged and shaped, so it appears transparent. This gives the
effect of an On Screen Display, like your TV/VCR etc.. The package also
includes an xmms plugin, which automatically displays various interesting
things as they change (song name, volume etc...) 

%package devel
Summary: Development files for the XOSD on-screen display library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The xosd-devel package contains static libraries, header files and
documentation for developing applications that use the XOSD on-screen
display.

%package -n xmms-%{name}
Summary: XMMS plugin for on-screen display that uses the XOSD library
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}, xmms
Obsoletes: %{name}-xmms
Provides: %{name}-xmms

%description -n xmms-%{name}
An X MultiMedia System plugin to display information on-screen through the
XOSD library, similarly to TV OSD.

%prep
%setup

%build
%configure \
	--disable-dependency-tracking \
	--enable-old-plugin="yes" \
	--with-plugindir="%{_plugindir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

### FIXME: makeinstall-macro doesn't work ?
%{__make} install DESTDIR="%{buildroot}"

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
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/osd_cat*
%{_bindir}/osd_cat
%{_libdir}/*.so.*
%{_datadir}/xosd/

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/xosd-config*
%doc %{_mandir}/man3/*
%{_bindir}/xosd-config
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%{_datadir}/aclocal/*
#exclude %{_libdir}/*.la

%files -n xmms-xosd
%defattr(-, root, root, 0755)
%{_plugindir}/*

%changelog
* Sat Apr 19 2003 Dag Wieers <dag@wieers.com> - 2.2.1-0
- Updated to release 2.2.1.

* Sun Mar 09 2003 Dag Wieers <dag@wieers.com> - 2.1.3-1
- Renamed "xosd-xmms" into "xmms-xosd".

* Sun Mar 09 2003 Dag Wieers <dag@wieers.com> - 2.1.3-0
- Updated to release 2.1.3-0.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 2.1.2-0
- Updated to release 2.1.2-0.

* Wed Feb 17 2003 Dag Wieers <dag@wieers.com> - 2.1.1-0
- Updated to release 2.1.1-0.

* Wed Feb 05 2003 Dag Wieers <dag@wieers.com> - 2.1.0-0
- Initial package. (using DAR)
