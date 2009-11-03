# $Id$
# Authority: dag
# Upstream: Pascal Brochart <pbrochart$tuxfamily,org>

%define xmms_visualdir %(xmms-config --visualization-plugin-dir 2>/dev/null || echo %{_libdir}/xmms/Visualization)


%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

Summary: OpenGL visual plugin for XMMS
Name: xmms-nebulus
Version: 0.8.0
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://nebulus.tuxfamily.org/

Source: http://nebulus.tuxfamily.org/xmms-nebulus-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: xmms-devel, SDL-devel, SDL_ttf-devel, gcc-c++, gettext
%{!?_without_modxorg:BuildRequires: mesa-libGL-devel, mesa-libGLU-devel}

%description
Nebulus is an OpenGL visual plugin for XMMS.


%prep
%setup


%build
%configure \
	--enable-shared \
	--libdir="%{xmms_visualdir}"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall \
	libdir="%{buildroot}%{xmms_visualdir}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{xmms_visualdir}/*.so
%exclude %{xmms_visualdir}/*.la

%changelog
* Tue Jan 09 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.0-1
- Updated to release 0.8.0.

* Sun May 28 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.0-1
- Updated to release 0.7.0.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.0-0.2
- Rebuild for Fedora Core 5.

* Mon Sep 15 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Updated to release 0.6.0.

* Fri Apr 04 2003 Dag Wieers <dag@wieers.com> - 0.5.0-0
- Initial package. (using DAR)
