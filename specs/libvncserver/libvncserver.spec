# $Id$
# Authority: dag
# Upstream: Johannes Schindelin <Johannes,Schindelin$gmx,de>

### EL6 ships with libvncserver-0.9.7-4.el6
# ExclusiveDist: el2 el3 el4 el5

%define real_name LibVNCServer

Summary: Library to make writing a vnc server easy
Name: libvncserver
Version: 0.9.7
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://libvncserver.sourceforge.net/

Source: http://dl.sf.net/libvncserver/LibVNCServer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Provides: LibVNCServer = %{version}-%{release}
Obsoletes: LibVNCServer <= %{version}-%{release}

%description
LibVNCServer makes writing a VNC server (or more correctly, a program
exporting a framebuffer via the Remote Frame Buffer protocol) easy.

It hides the programmer from the tedious task of managing clients and
compression schemata.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
#Requires: %{name} = %{version}-%{release}

Provides: LibVNCServer-devel = %{version}-%{release}
Obsoletes: LibVNCServer-devel <= %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%{expand: %%define optflags %{optflags} -fPIC -DPIC}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot (RH9/EL3 produces this binary, can't find why)
%{__rm} -f %{buildroot}%{_bindir}/LinuxVNC

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libvncclient.so.*
%{_libdir}/libvncserver.so.*

%files devel
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/libvncserver-config
%{_includedir}/rfb/
%{_libdir}/libvncclient.so
%{_libdir}/libvncserver.so
%exclude %{_libdir}/libvncclient.a
%exclude %{_libdir}/libvncclient.la
%exclude %{_libdir}/libvncserver.a
%exclude %{_libdir}/libvncserver.la

%changelog
* Fri Nov 12 2010 Dag Wieers <dag@wieers.com> - 0.9.7-1
- Updated to release 0.9.7.

* Sun Apr 15 2007 Dag Wieers <dag@wieers.com> - 0.9-1
- Updated to release 0.9.

* Sun Mar 25 2007 Dag Wieers <dag@wieers.com> - 0.8.2-1
- Initial package. (using DAR)
