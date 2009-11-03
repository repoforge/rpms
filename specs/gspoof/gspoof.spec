# $Id$
# Authority: dag
# Upstream: Embyte <embyte$madlab,it>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)
%define desktop_vendor rpmforge

Summary: Network tool to build and send TCP/IP packets
Name: gspoof
Version: 3.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://gspoof.sourceforge.net/

Source: http://dl.sf.net/gspoof/gspoof-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libnet >= 1.1.0

%description
Gspoof is a tool which make easier and accurate the building and sending
of TCP/IP packets. It works from console (command line) and has an
interface graphics written in GTK+ too.

%prep
%setup

%{__perl} -pi.orig -e 's|chown |#chown |' Makefile.in

%{__cat} <<EOF >gspoof.desktop
[Desktop Entry]
Name=Gspoof
Comment=Build and send crafted TCP/IP packets
Icon=gspoof.png
Exec=gspoof
Terminal=false
Type=Application
Categories=GNOME;Application;Network;
StartupNotify=true
EOF

%build
%configure

### FIXME: Make Makefile use autotool directory standard. (Please fix upstream)
%{__perl} -pi.orig -e '
		s|/usr/bin|\$(bindir)|;
		s|/usr/share|\$(datadir)|;
	' Makefile

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

### FIXME: Makefile doesn't create target directories (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_datadir}/gspoof/

%makeinstall

%{__install} -Dp -m0644 pixmap/icon.png %{buildroot}%{_datadir}/pixmaps/gspoof.png

%if %{dfi}
	%{__install} -Dp -m0644 gspoof.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/gspoof.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		gspoof.desktop
%endif


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGELOG LICENSE README TODO
%{_bindir}/*
%{_datadir}/pixmaps/*.png
%if %{dfi}
	%{_datadir}/gnome/apps/Internet/*.desktop
%else
	%{_datadir}/applications/*.desktop
%endif
%exclude %{_datadir}/gspoof/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.2-1.2
- Rebuild for Fedora Core 5.

* Sun Apr 11 2004 Dag Wieers <dag@wieers.com> - 3.2-1
- Initial package. (using DAR)
