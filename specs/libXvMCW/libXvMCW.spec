# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

Summary: Wrapper for run-time loading of XvMC libraries
Name: libXvMCW
Version: 0.9.3
Release: 1%{?dist}
License: MIT
Group: User Interface/X
URL: http://sourceforge.net/projects/unichrome
Source: http://dl.sf.net/unichrome/libXvMCW-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
A Wrapper for XvMC libraries that allows the X server or user to specify the
hardware dependent library at run-time.


%package devel
Summary: Development files for the XvMC library wrapper
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
A Wrapper for XvMC libraries that allows the X server or user to specify the
hardware dependent library at run-time.

This package contains the files required to build software that will use the
XvMC Wrapper.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc README
%config %{_sysconfdir}/X11/XvMCConfig
%{_prefix}/X11R6/%{_lib}/libXvMCW.so.*

%files devel
%defattr(-, root, root, 0755)
%{_prefix}/X11R6/include/X11/extensions/vldXvMC.h
%{_prefix}/X11R6/%{_lib}/libXvMCW.a
%exclude %{_prefix}/X11R6/%{_lib}/libXvMCW.la
%{_prefix}/X11R6/%{_lib}/libXvMCW.so


%changelog
* Mon Jan  3 2005 Matthias Saou <http://freshrpms.net/> 0.9.3-1
- Spec file cleanup.
- Split off -devel package.

* Thu Sep 23 2004 Thomas Hellström <sthomas@shipmail.org>
- Initial release

