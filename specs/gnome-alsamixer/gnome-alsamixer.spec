# $Id$
# Authority: matthias

%define desktop_vendor freshrpms

Summary: A GNOME mixer interface for the Advanced Linux Sound Architecture.
Name: gnome-alsamixer
Version: 0.9.6
Release: 2
License: GPL
Group: Applications/Multimedia
Source0: ftp://ftp.paw.co.za/pub/PAW/sources/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
URL: http://www.paw.co.za/projects/gnome-alsamixer/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: libgnomeui >= 2.0.0, alsa-lib >= 0.9.0
BuildRequires: libgnomeui-devel >= 2.0.0, alsa-lib-devel >= 0.9.0
BuildRequires: desktop-file-utils, pkgconfig

%description
A sound mixer for GNOME which is written for the Advanced Linux Sound
Architecture (ALSA) version 0.9.x.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor}  \
  --dir %{buildroot}%{_datadir}/applications     \
  --add-category X-Red-Hat-Extra                 \
  --add-category Application                     \
  --add-category AudioVideo                      \
%{SOURCE1}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/%{name}

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.9.6-2.fr
- Rebuild for Fedora Core 1.
- Added missing libgnomeui-devel build dependency.

* Mon Sep 15 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.6.

* Mon Sep  8 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.5.

* Tue Apr  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.3.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Jan  2 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.9.2 for GNOME 2.

* Mon Nov 18 2002 Matthias Saou <http://freshrpms.net/>
- Changed ALSA dependency to 0.9.0.

* Fri Oct  4 2002 Matthias Saou <http://freshrpms.net/>
- Spec file rewrite for Red Hat Linux 8.0.
- Menu entry for GNOME 2.

* Sun Sep 22 2002 Dennis J Houy <djhouy@paw.co.za> - 0.1.0beta
- Initial release version.

