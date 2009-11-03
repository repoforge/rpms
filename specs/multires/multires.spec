# $Id$
# Authority: dag
# Upstream: Chris Picton <cpicton$users,sourceforge,net>

Summary: Allows changing of desktop resolution and refresh rate
Name: multires
Version: 0.4
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://multires.sourceforge.net/

Source: http://dl.sf.net/multires/multires-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgnomeui-devel >= 2.0
#BuildRequires: gnome-panel-devel

%description
GNOME Multires is an applet for the GNOME 2 panel which allows changing
of desktop resolution and refresh rate.

%prep
%setup

%{__perl} -pi.orig -e 's|/usr/X11R6/lib|%{_prefix}/X11R6/%{_lib}|' configure

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
%doc AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/multires-applet-2
%{_libdir}/bonobo/servers/GNOME_MultiresApplet.server
%{_datadir}/multires/
%{_datadir}/pixmaps/gnome-multires.png

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.4-1.2
- Rebuild for Fedora Core 5.

* Sun Aug 29 2004 Dag Wieers <dag@wieers.com> - 0.4-1
- Updated to release 0.4.
- Fix for x86_64.

* Mon Mar 10 2003 Dag Wieers <dag@wieers.com> - 0.2.4-0
- Initial package. (using DAR)
