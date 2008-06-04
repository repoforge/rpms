# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Collection of Linux tools to interface with the Nintendo Wiimote
Name: cwiid
Version: 0.6.00
Release: 1
License: GPL
Group: Applications/System
URL: http://abstrakraft.org/cwiid/

Source: http://abstrakraft.org/cwiid/downloads/cwiid-%{version}.tgz
#Patch0: cwiid-0.6.00-flex.patch
Patch0: cwiid-0.6.00-flex2.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison
BuildRequires: flex
BuildRequires: python-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
### We patch the source to not require the newer flex
#BuildRequires: flex >= 2.5.33

%description
Collection of Linux tools to interface with the Nintendo Wiimote.

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
%patch -p0 -b .flex2

for file in */README; do %{__cp} -v $file README.$(dirname $file); done

%{__cat} <<EOF >wminput.rules
KERNEL=="uinput", GROUP="wheel"
EOF

%{__cat} <<EOF >wmgui.desktop
[Desktop Entry]
Name=Wiimote Test Utility
Comment=Test your Nintendo Wiimote functionality
Icon=redhat-system_settings.png
Exec=wmgui
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;System;Application;X-Red-Hat-Base;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" LDCONFIG="echo ldconfig disabled"

%{__install} -Dp -m0644 wminput.rules %{buildroot}%{_sysconfdir}/udev/rules.d/wminput.rules

%if %{?_without_freedesktop:1}0
    %{__install} -D -m0644 wmgui.desktop %{buildroot}%{_datadir}/gnome/apps/Applications/wmgui.desktop
%else
    %{__install} -d -m0755 %{buildroot}%{_datadir}/applications
    desktop-file-install --vendor %{desktop_vendor} \
        --dir %{buildroot}%{_datadir}/applications  \
        wmgui.desktop
%endif


### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README* doc/Xmodmap doc/wminput.list
%doc %{_mandir}/man1/wmgui.1*
%doc %{_mandir}/man1/wminput.1*
%config(noreplace) %{_sysconfdir}/cwiid/
%config(noreplace) %{_sysconfdir}/udev/rules.d/wminput.rules
%{_bindir}/lswm
%{_bindir}/wmgui
%{_bindir}/wminput
%{_libdir}/libcwiid.so.*
%{_libdir}/cwiid/
%{python_sitearch}/cwiid.so
%{?_without_freedesktop:%{_datadir}/gnome/apps/Applications/wmgui.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-wmgui.desktop}

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/cwiid.h
%{_libdir}/libcwiid.so
%exclude %{_libdir}/libcwiid.a

%changelog
* Sat May 24 2008 Dag Wieers <dag@wieers.com> - 0.6.00-1
- Initial package. (using DAR)
