# $Id$

# Authority: dag

### FIXME: configure has problems finding flex output using soapbox on RHEL3
# Soapbox: 0

Summary: GNOME Chess game.
Name: gnome-chess
Version: 0.3.3
Release: 0
License: GPL
Group: Amusements/Games
URL: http://www.gnome.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-chess/%{name}-%{version}.tar.bz2
Source1: %{name}-32.png
Source2: %{name}-48.png
Source3: %{name}-16.png
Patch0: gnome-chess-mime.patch.bz2
Patch1: gnome-chess-0.3.3-quit.patch.bz2
### Fix scrollkeeper file to be DTD compliant
Patch2: gnome-chess-0.3.3-scrollkeeper.patch.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: flex, gdk-pixbuf-devel, gnome-print-devel, libglade-devel, scrollkeeper

Requires(post): scrollkeeper

%description
GNOME Chess is part of the GNOME project and is a graphical chess interface. It
can provide and interface to GNU Chess, Crafty, chess servers and PGN files.

%prep
%setup
%patch0 -p1 -b .mimetypes
%patch1 -p1 -b .quit
%patch2 -p1 -b .scrollkeeper

xml-i18n-toolize
%{__aclocal} -I macros
%{__autoconf}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/pixmaps/ \
			%{buildroot}%{_datadir}/applications

%{__install} -m0644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/

desktop-file-install --vendor gnome --delete-original \
	--add-category X-Red-Hat-Base                 \
	--add-category Application                    \
	--add-category Games                          \
	--dir %{buildroot}%{_datadir}/applications    \
        %{buildroot}%{_datadir}/gnome/apps/Games/%{name}.desktop

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper/

%post
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_datadir}/gnome/help/gnome-chess-manual/
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop
%{_datadir}/gnome-chess/
%{_datadir}/mime-info/*
%{_datadir}/omf/gnome-chess/*

%changelog
* Mon May 26 2003 Dag Wieers <dag@wieers.com> - 0.3.3-0
- Initial package. (using DAR)
