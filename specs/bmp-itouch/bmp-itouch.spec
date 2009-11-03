# $Id$
# Authority: dries
# Upstream: Jeremy Tan <jeremytan$users,sourceforge,net>

%define bmp_generalplugindir %(pkg-config --variable=general_plugin_dir bmp 2>/dev/null || echo %{_libdir}/bmp/General)
%define bmp_datadir %(pkg-config --variable=data_dir bmp 2>/dev/null || echo %{_libdir}/bmp)

Summary: iTouch keyboard control plugin for bmp
Name: bmp-itouch
Version: 1.0.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://bmp-itouch.sourceforge.net/

Source: http://dl.sf.net/bmp-itouch/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bmp-devel >= 0.9.7, gettext, pkgconfig
Requires: bmp >= 0.9.7

%description
With this BMP plugin you can take advantage of the multimedia (playback and
volume control) keys on your Logitech iTouch keyboard. When the plugin is
used you can use the keys regardless of the current input focus. The plugin
won't work if some other application (eg. xscreensaver) has grabbed the
keyboard.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall libdir=%{buildroot}%{bmp_generalplugindir} datadir=%{buildroot}%{bmp_datadir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{bmp_generalplugindir}/libitouch.so
%config(noreplace) %{bmp_datadir}/bmp-itouch.config
%exclude %{bmp_generalplugindir}/libitouch.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1.2
- Rebuild for Fedora Core 5.

* Sat Oct 08 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1
- Spec file provided by Saikat Guha added to rpmforge.
- Updated to 1.0.1.

* Wed Sep 28 2005 Saikat Guha <saikat@cs.cornell.edu>
- updated legacy tags
- added build requirements
- made files section explicit

* Tue Oct 5 2004 Jeremy Tan <jeremytan@users.sourceforge.net>
- update to version 1.0.0

* Tue Sep 29 2004 Jeremy Tan <jeremytan@users.sourceforge.net>
- update to version 0.1.4.3

* Tue Aug 30 2004 Jeremy Tan <jeremytan@users.sourceforge.net>
- update to version 0.1.4.2

* Sat Aug 28 2004 Jeremy Tan <jeremytan@users.sourceforge.net>
- bmp-itouch port
- initial relase

* Thu Aug 30 2001 Ville Syrjälä <syrjala@sci.fi>
- Minor cleanup.

* Sun Jan 14 2001 Ville Syrjälä <syrjala@sci.fi>
- Intial release.
