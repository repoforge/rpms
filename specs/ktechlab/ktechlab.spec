# $Id$

# Authority: dries
# Screenshot: http://ktechlab.fadedminds.com/screenshots/555_counter.png
# ScreenshotURL: http://ktechlab.fadedminds.com/screenshots/

# ExcludeDist: el3

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Development and simulation of microcontrollers and electronic circuits
Name: ktechlab
Version: 0.3
Release: 2%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://ktechlab.org/

Source: http://ktechlab.org/download/ktechlab-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gpsim-devel, gcc, make, libpng-devel, libart_lgpl-devel
BuildRequires: arts-devel, gcc-c++, gettext, glib2-devel, glib-devel
BuildRequires: zlib-devel, qt-devel, libjpeg-devel, readline-devel
BuildRequires: kdelibs-devel, desktop-file-utils
%{?el4:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}
Requires: gputils, gpsim

%description
KTechlab is a development and simulation environment for microcontrollers
and electronic circuits, distributed under the GNU General Public License.

KTechlab consists of several well-integrated components:
A circuit simulator, capable of simulating logic, linear devices and some
nonlinear devices.
* Integration with gpsim, allowing PICs to be simulated in circuit.
* A schematic editor, which provides a rich real-time feedback of the
simulation.
* A flowchart editor, allowing PIC programs to be constructed visually.
* MicroBASIC; a BASIC-like compiler for PICs, written as a companion program
to KTechlab.
* An embedded Kate part, which provides a powerful editor for PIC programs.
* Integrated assembler and disassembler via gpasm and gpdasm.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/ktechlab
%{_bindir}/microbe
%{_datadir}/apps/ktechlab
%{_datadir}/apps/katepart/syntax/microbe.xml
%{_datadir}/config.kcfg/ktechlab.kcfg
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/applnk/Development/ktechlab.desktop
%{_datadir}/doc/HTML/en/ktechlab
%{_datadir}/icons/*/*/*/*.png
#%{_libdir}/libktechlab_gpsim.*

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Thu Jan 05 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Update to release 0.3.

* Mon Aug 01 2005 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Update to release 0.2.

* Mon Jan 10 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.2-1
- Initial package.
