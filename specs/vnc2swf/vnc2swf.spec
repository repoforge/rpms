# $Id$
# Authority: dag
# Upstream: <vnc2swf-users$lists,sourceforge,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: Recording tool for VNC
Name: vnc2swf
Version: 0.5.0
Release: 2
License: GPL
Group: User Interface/Desktops
URL: http://www.unixuser.org/~euske/vnc2swf/

Source: http://www.unixuser.org/~euske/vnc2swf/vnc2swf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libdnet-devel, libstdc++-devel, zlib-devel, gcc-c++
%{!?_without_modxorg:BuildRequires: libXt-devel, libXext-devel, libXaw-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
vnc2swf is a recoding tool for Flash.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENCE.TXT README* docs/*.html
%{_bindir}/recordwin
%{_bindir}/vnc2swf

%changelog
* Sun Nov 12 2006 Dag Wieers <dag@wieers.com> - 0.5.0-2
- Removed ming requirement.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.0-1
- Updated to release 0.5.0.

* Tue Mar 15 2005 Dag Wieers <dag@wieers.com> - 0.4.2-2
- Build against newer ming.

* Thu Mar 10 2005 Dag Wieers <dag@wieers.com> - 0.4.2-2
- Updated to release 0.4.2.

* Fri May 14 2004 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Initial package. (using DAR)
