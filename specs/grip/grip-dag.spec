# $Id$
# Authority: matthias
# Upstream: Mike Oliphant <oliphant@gtk.org>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: GNOME CD player, CD ripper and MP3 encoder frontend
Name: grip
Version: 3.0.7
Release: 0
Epoch: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.nostatic.org/grip/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.nostatic.org/grip/grip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gnome-libs-devel, libghttp-devel, cdparanoia-devel
BuildRequires: id3lib-devel, gettext

%description
Grip is a CD player and CD ripper for GNOME. It has the ripping capabilities
of cdparanoia built in, but can also use external rippers (such as
cdda2wav). It also provides an automated frontend for MP3 encoders, letting
you take a disc and transform it easily straight into MP3s. The CDDB
protocol is supported for retrieving track information from disc database
servers.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%if %{dfi}
%else
	install -d -m0755 %{buildroot}%{_datadir}/applications
	desktop-file-install --vendor gnome --delete-original \
		--add-category X-Red-Hat-Base                 \
		--add-category Application                    \
		--add-category AudioVideo                     \
		--dir %{buildroot}%{_datadir}/applications    \
	%{buildroot}%{_datadir}/gnome/apps/Multimedia/%{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog CREDITS README TODO
%doc %{_datadir}/gnome/help/grip/
%{_bindir}/*
%{_datadir}/pixmaps/*
%if %{dfi}
	%{_datadir}/gnome/apps/Multimedia/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Fri Apr 25 2003 Dag Wieers <dag@wieers.com> - 3.0.7-0
- Updated to release 3.0.7.

* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 3.0.6-1
- Rebuild against new id3lib-3.8.3 package.

* Tue Feb 11 2003 Dag Wieers <dag@wieers.com> - 3.0.5-0
- Initial package. (using DAR)
