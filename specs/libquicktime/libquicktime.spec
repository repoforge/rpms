# $Id$
# Authority: matthias

#define prever pre1

Summary: A library for reading and writing quicktime files
Name: libquicktime
Version: 0.9.2
Release: %{?prever:0.%{prever}.}1
License: GPL
Group: System Environment/Libraries
URL: http://libquicktime.sourceforge.net/
Source: http://dl.sf.net/libquicktime/%{name}-%{version}%{?prever}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gtk+, libdv, libvorbis, libpng, libjpeg
%{!?_without_firewire:Requires: libraw1394 >= 0.9, libavc1394}
BuildRequires: gtk+-devel, libdv-devel, libvorbis-devel
BuildRequires: libpng-devel, libjpeg-devel
%{!?_without_firewire:BuildRequires: libraw1394-devel >= 0.9, libavc1394-devel}
# The configure automatically adds MMX stuff it detected
%ifarch i386
%{!?_without_mmx:BuildArch: i586}
%endif

%description
libquicktime is a library for reading and writing quicktime files. It
is based on the quicktime4linux library, with many extensions.

Available rpmbuild rebuild options :
--without : firewire mmx


%package devel
Summary: Development files from the libquicktime library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
libquicktime is a library for reading and writing quicktime files. It
is based on the quicktime4linux library, with many extensions.

You will need to install this development package if you intend to rebuild
programs that need to access quicktime files using libquicktime.


%prep
%setup -n %{name}-%{version}%{?prever}

%build
# Fix plugin compilation
#perl -pi -e 's|^LDFLAGS = |LDFLAGS = -L../../src/.libs |' plugins/*/Makefile
perl -pi -e 's|^LQT_LIBS = (.*)|LQT_LIBS = -L../../src/.libs $1|g' \
    plugins/Makefile plugins/*/Makefile
%configure \
    %{?_without_firewire:--disable-firewire}
    %{?_without_mmx:--disable-mmx}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/lqtplay
%{_bindir}/qt*
%{_libdir}/*.so.*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%{_mandir}/man1/*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/libquicktime_config
%{_bindir}/lqt-config
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.a
%exclude %{_libdir}/%{name}/*.la
%{_datadir}/aclocal/*.m4

%changelog
* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.9.2-1.fr
- Update to 0.9.2 final.
- Rebuild for Fedora Core 1.

* Tue Apr 22 2003 Matthias Saou <http://freshrpms.net/>
- Fix plugin compilation, thanks to Dag.

* Wed Apr  9 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

