# $Id$

Summary: Lightweight, purely OSD based xine frontend.
Name: oxine
Version: 0.2
Release: 3.fr
License: GPL
Group: Applications/Multimedia
Source: http://dl.sf.net/oxine/%{name}-%{version}.tar.gz
URL: http://oxine.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xine-lib >= 1.0.0
BuildRequires: xine-lib-devel >= 1.0.0

%description
oxine is a lightweight gui for the famous xine engine which uses the on screen
display functionality of xine to display its user interface elements like
buttons, lists sliders and so on. Due to this, oxine can easily be ported to
any video output device the xine library provides (e.g. frame buffer, dxr3,...)
and is particularly suitable for appliances like set-top boxes, home
entertainment systems or kiosk systems.

%prep
%setup -q

%build
%configure --datadir=%{_datadir}/%{name}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall datadir=%{buildroot}%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO doc/doc.html
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.2-3.fr
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Mon Mar 24 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.

* Tue Mar 18 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

