# $Id$

# Authority: dries
# Screenshot: http://www.dattalo.com/gnupic/desktop.0.18.1.gif
# ScreenshotURL: http://www.dattalo.com/gnupic/gpsim.html#shots

Summary: Software simulator for Microchip PIC microcontrollers
Name: gpsim
Version: 0.21.2
Release: 1.2
License: GPL
Group: Applications/Engineering
URL: http://www.dattalo.com/gnupic/gpsim.html

Source: http://www.dattalo.com/gnupic/gpsim-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: automake, autoconf, bison, gcc-c++, flex
BuildRequires: readline-devel, gtkextra-devel, gtk+-devel
BuildRequires: desktop-file-utils, pkgconfig

%description
gpsim is a full-featured software simulator for Microchip PIC
microcontrollers distributed under the GNU General Public License

gpsim has been designed to be as accurate as possible. Accuracy includes the
entire PIC - from the core to the I/O pins and including ALL of the internal
peripherals. Thus it's possible to create stimuli and tie them to the I/O
pins and test the PIC the same PIC the same way you would in the real world.

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

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=gpsim
Comment=Software simulator for Microchip PIC microcontrollers
Exec=gpsim
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Development;X-Red-Hat-Extra;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/gpsim
%{_libdir}/*.so.*
%{_datadir}/applications/*.desktop

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/gpsim
%{_includedir}/eXdbm
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.21.2-1.2
- Rebuild for Fedora Core 5.

* Mon Jan 10 2005 Dries Verachtert <dries@ulyssis.org> - 0.21.2-1
- Initial package.
