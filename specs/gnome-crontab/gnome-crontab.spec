# $Id$

# Authority: dag

# Upstream: Gavin Brown <jodrell@spod.uk.net>

Summary: A graphical interface to the crontab program.
Name: gnome-crontab
Version: 0.0.5
Release: 0
License: GPL
Group: Applications/System
URL: http://jodrell.net/projects/gnome-crontab/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://jodrell.net/download.html?file=/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: perl >= 0:5.00503
#Requires: perl >= 0:5.00503
#Requires: Gtk-Perl, perl(Locale::Maketext), perl(Gtk::HandyCList)
#Requires: perl(ExtUtils::Depends), perl(Gnome2), perl(Gtk2)
#AutoReq: no

%description
Greenwich is a graphical whois client for GNOME. It is written in Perl and
makes use of the GNOME bindings for Perl.

Greenwich transparently handles almost all gTLDs, first- and second-level
ccTLDs and whois servers run by private domain registries (like CentralNic).
It can also do lookups against IP addresses.

%prep
%setup

### FIXME: Use standard autotool directories. (Fix upstream please)
%{__perl} -pi.orig -e '
		s|^PREFIX=.*$|prefix=/usr\ndatadir=/usr/share|;
		s|^LIBDIR=.*$|libdir=/usr/lib|;
		s|^MANDIR=.*$|mandir=/usr/share/man/man1|;
		s|^BINDIR=.*$|bindir=/usr/bin/|;
		s|\$\(PREFIX\)|\$(prefix)|g;
		s|\$\(MANDIR\)|\$(mandir)/man1|g;
		s|\$\(LIBDIR\)|\$(libdir)/gnome-crontab|g;
		s|\$\(BINDIR\)|\$(bindir)|g;
		s|\$\(PIXMAPDIR\)|\$(datadir)/pixmaps|g;
		s|\$\(DESKTOPDIR\)|\$(datadir)/applications|g;
	' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Crontab Editor
Comment=Edit scheduled crontab tasks
Type=Application
Exec=gnome-crontab
Icon=gnome-crontab.png
Terminal=false
Categories=GNOME;Application;System;Utility;
EOF

desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--dir %{buildroot}%{_datadir}/applications    \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog HACKING LICENSE README
%{_bindir}/*
%{_libdir}/gnome-crontab/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*

%changelog
* Sun Oct 12 2003 Dag Wieers <dag@wieers.com> - 0.0.5-0
- Initial package. (using DAR)
