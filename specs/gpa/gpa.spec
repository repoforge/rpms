# $Id$
# Authority: dag
# Upstream: <gnupg-devel$gnupg,org>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)
%define desktop_vendor rpmforge

Summary: Graphical user interface for the GnuPG
Name: gpa
Version: 0.7.5
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.gnupg.org/gpa.html

#Source: ftp://ftp.gnupg.org/gcrypt/alpha/gpa/gpa-%{version}.tar.bz2
Source: ftp://ftp.gnupg.ca/gpa/alpha/gpa/gpa-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.0.6, gpgme-devel >= 0.4.0
Requires: gnupg, gtk2 >= 2.0.6, gpgme >= 0.4.0

%description
The GNU Privacy Assistant is a graphical user interface for the GNU Privacy
Guard (GnuPG). GnuPG is a system that provides you with privacy by
encrypting emails or other documents and with authentication of received
files by signature management.

%prep
%setup

%{__cat} <<EOF >gpa.desktop
[Desktop Entry]
Name=GNU Privacy Assistant
Comment=Organize and edit your keys and signatures
Icon=gpa.xpm
Exec=gpa
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;Application;Utility;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -Dp -m0644 pixmaps/keyring.xpm %{buildroot}%{_datadir}/pixmaps/gpa.xpm

%if %{dfi}
	%{__install} -Dp -m0644 gpa.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/gpa.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		gpa.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README* THANKS TODO
%{_bindir}/*
%{_datadir}/gpa/
%{_datadir}/pixmaps/*.xpm
%if %{dfi}
	%{_datadir}/gnome/apps/Utilities/*.desktop
%else
	%{_datadir}/applications/*.desktop
%endif
/usr/share/pixmaps/gpa.png

%changelog
* Thu Jan 01 2008 Heiko Adams <info-2007@fedora-blog.de> - 0.7.5-2
- version update to 0.7.5

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.0-1.2
- Rebuild for Fedora Core 5.

* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Make to work without atrpms package.

* Fri Feb 14 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Updated to release 0.6.1.

* Fri Jan 17 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- updated to release 0.6.0.
- synced with embedded specfile.

* Wed Nov 13 2002 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- updated to release 0.4.3, changed Group.

* Fri Aug  3 2001 Peter Hanecak <hanecak@megaloman.sk>
[0.4.1-1]
- initial spec
