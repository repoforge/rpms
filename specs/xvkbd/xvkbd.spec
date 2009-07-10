# $Id$
# Authority: dag
# Upstream: Tom Sato <VEF00200$nifty,ne,jp>

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

Summary: Virtual keyboard for X window system
Name: xvkbd
Version: 2.8
Release: 1
License: GPL
Group: User Interface/X
URL: http://homepage3.nifty.com/tsato/xvkbd/

Source: http://homepage3.nifty.com/tsato/xvkbd/xvkbd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: Xaw3d-devel
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libXaw-devel}
Requires: Xaw3d

%description
xvkbd is a virtual (graphical) keyboard program for X Window System
which provides facility to enter characters onto other clients
(softwares) by clicking on a keyboard displayed on the screen.  This
may be used for systems without a hardware keyboard such as kiosk
terminals or handheld devices.  This program also has facility to
send characters specified as the command line option to another
client.

%prep
%setup

%build
xmkmf
%{__make} %{?_smp_mflags} \
    LIBDIR="%{_datadir}/X11"

%install
%{__rm} -rf %{buildroot}
%{__make} install install.man \
    DESTDIR="%{buildroot}" \
    BINDIR="%{_bindir}" \
    LIBDIR="%{_datadir}/X11" \
    SHLIBDIR="%{_libdir}" \
    MANPATH="%{_mandir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man1/xvkbd.1x*
%{_bindir}/xvkbd
%{_datadir}/X11/app-defaults/XVkbd*

%changelog
* Fri Mar 02 2007 Dag Wieers <dag@wieers.com> - 2.8-1
- Initial package, based on contribution by Radouane.
