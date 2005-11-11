# $Id$
# Authority: dag
# Upstream: <vnc2swf-users$lists,sourceforge,net>

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}

Summary: Recording tool for VNC
Name: vnc2swf
Version: 0.5.0
Release: 1
License: GPL
Group: User Interface/Desktops
URL: http://www.unixuser.org/~euske/vnc2swf/

Source: http://www.unixuser.org/~euske/vnc2swf/vnc2swf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ming-devel, libdnet, libstdc++-devel, zlib-devel, gcc-c++
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
vnc2swf is a recoding tool for Flash.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.html LICENCE.TXT README*
#%doc docs/
%{_bindir}/recordwin
%{_bindir}/vnc2swf

%changelog
* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.0-1
- Updated to release 0.5.0.

* Tue Mar 15 2005 Dag Wieers <dag@wieers.com> - 0.4.2-2
- Build against newer ming.

* Thu Mar 10 2005 Dag Wieers <dag@wieers.com> - 0.4.2-2
- Updated to release 0.4.2.

* Fri May 14 2004 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Initial package. (using DAR)
