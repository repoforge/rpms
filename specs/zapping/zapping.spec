# Authority: freshrpms

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: A TV viewer for GNOME.
Name: zapping
Version: 0.6.8
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://zapping.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/zapping/zapping-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gnome-libs-devel, libxml-devel, libglade-devel, gdk-pixbuf-devel
BuildRequires: libunicode-devel, librte-devel, libzvbi-devel
#BuildRequires: lirc

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.  GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on free software.

This is a TV viewer for the GNOME desktop. It has all the needed
features, plus extensibility through a plugin system.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__make} install DESTDIR="%{buildroot}"
%makeinstall \
	pixmapdir="%{buildroot}%{_datadir}/pixmaps" \
	PLUGIN_DEFAULT_DIR="%{buildroot}%{_libdir}/zapping/plugins"
%find_lang %{name}

%{__ln_s} -f %{_bindir}/zapping %{buildroot}%{_bindir}/zapzilla
%{__ln_s} -f %{_sbindir}/zapping_setup_fb %{buildroot}%{_bindir}/zapping_setup_fb

%if %{dfi}
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
	desktop-file-install --vendor "gnome" --delete-original \
		--add-category X-Red-Hat-Base                   \
		--add-category Application                      \
		--add-category AudioVideo                       \
		--dir %{buildroot}%{_datadir}/applications      \
		%{buildroot}%{_datadir}/gnome/apps/Multimedia/%{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr (-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog NEWS README* THANKS TODO
%doc %{_mandir}/man1/*
%doc %{_datadir}/gnome/help/zapping/
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/zapping/
%{_datadir}/pixmaps/zapping/
%{_datadir}/zapping/
%if %{dfi}
        %{_datadir}/gnome/apps/Multimedia/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 0.6.8-0
- Updated to 0.6.8.

* Fri Feb 28 2003 Dag Wieers <dag@wieers.com> - 0.6.6-0
- Updated to 0.6.6.

* Sun Jan 05 2003 Dag Wieers <dag@wieers.com> - 0.6.5.20030105-0
- Initial package. (using DAR)
