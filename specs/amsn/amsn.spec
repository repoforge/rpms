# $Id$
# Authority: dries
# Upstream: Alvaro J. Iradier Muro <airadier$users,sourceforge,net>

# Screenshot: http://amsn.sf.net/shots/contactlist.jpg
# ScreenshotURL: http://amsn.sf.net/shots.htm

# ExcludeDist: fc1

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh9:%define _without_tcltk_devel 1}
%{?rh8:%define _without_tcltk_devel 1}

%{?rh7:%define _without_freedesktop 1}
%{?rh7:%define _without_tcltk_devel 1}

%{?el2:%define _without_freedesktop 1}
%{?el2:%define _without_tcltk_devel 1}

%{?rh6:%define _without_freedesktop 1}
%{?rh6:%define _without_tcltk_devel 1}

%define desktop_vendor rpmforge

%define tls_maj 1.4
%define tls_min 1

Summary: Full featured MSN Messenger clone
Name: amsn
Version: 0.96
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.amsn-project.net/

Source: http://dl.sf.net/amsn/amsn-%{version}.tar.gz
#Source1: http://dl.sf.net/amsn/tls%{tls_maj}.%{tls_min}-src.tar.bz2
Source2: http://dl.sf.net/amsn/tls%{tls_maj}.%{tls_min}-linux-x86.tar.gz
# Makefile is completely different
#Patch: amsn-0.83-makefile.patch
Patch1: amsn-0.92-login.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386 x86_64
BuildRequires: tcl >= 8.4, tk >= 8.4, openssl-devel, gcc-c++
BuildRequires: imlib-devel, libpng-devel, libtiff-devel
%{!?_without_tcltk_devel:BuildRequires: tcl-devel >= 8.4, tk-devel}
%{?_without_tcltk_devel:BuildRequires: tcl >= 8.4, tk}
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: tcl >= 8.4, tk >= 8.4

%description
amsn is a Tcl/Tk clone that implements the Microsoft Messenger (MSN) for
Unix, Windows, or Macintosh platforms. It supports file transfers,
groups, and many more features.

%prep
%setup -a 2
#patch1 -p0

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} rpm-install INSTALL_PREFIX="%{buildroot}"

%{__install} -Dp -m0644 %{buildroot}%{_datadir}/amsn/icons/48x48/msn.png %{buildroot}%{_datadir}/pixmaps/amsn.png

%{__install} -d -m0755 %{buildroot}%{_datadir}/amsn/plugins/tls%{tls_maj}/
%{__install} -p -m0755 tls%{tls_maj}/libtls%{tls_maj}.so tls%{tls_maj}/pkgIndex.tcl tls%{tls_maj}/tls.tcl %{buildroot}%{_datadir}/amsn/plugins/tls%{tls_maj}/

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 %{buildroot}%{_datadir}/amsn/amsn.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/amsn.desktop
#	%{__install} -Dp -m0644 amsn.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/amsn.desktop
%else
%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{buildroot}%{_datadir}/amsn/amsn.desktop
#		amsn.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AGREEMENT CREDITS FAQ GNUGPL HELP INSTALL README TODO
%{_bindir}/amsn
%{_bindir}/amsn-remote
%{_bindir}/amsn-remote-CLI
%{_datadir}/amsn/
%{_datadir}/pixmaps/amsn.png
%{?_without_freedesktop:%{_datadir}/gnome/apps/Internet/amsn.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-amsn.desktop}

%changelog
* Mon Mar 26 2007 Dag Wieers <dag@wieers.com> - 0.96-1
- Updated to release 0.96.

* Wed Jan 11 2006 Dag Wieers <dag@wieers.com> - 0.95-2
- Really include release 0.95. (Jaime Ventura)

* Tue Dec 27 2005 Dag Wieers <dag@wieers.com> - 0.95-1
- Updated to release 0.95.

* Sat Nov 06 2004 Dag Wieers <dag@wieers.com> - 0.94-1
- Updated to release 0.94.

* Sun Aug 29 2004 Dag Wieers <dag@wieers.com> - 0.93-1
- Updated to release 0.93.

* Mon May 31 2004 Dries Verachtert <dries@ulyssis.org> - 0.92-1
- update to version 0.92
- added Encoding tag to desktop file

* Sun May 30 2004 Dag Wieers <dag@wieers.com> - 0.91-1
- Updated to release 0.91.

* Sun Feb 22 2004 Dag Wieers <dag@wieers.com> - 0.90-0
- Updated to release 0.90.

* Sun Jan 11 2004 Dag Wieers <dag@wieers.com> - 0.83-1
- Added FAQ to %%{_datadir}.

* Sat Jan 03 2004 Dag Wieers <dag@wieers.com> - 0.83-0
- Initial package. (using DAR)
