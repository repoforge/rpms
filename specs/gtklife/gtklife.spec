# $Id: _template.spec 201 2004-04-03 15:24:49Z dag $
# Authority: dag
# Upstream: <tril$igs,net>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Conway's game of life.
Name: gtklife
Version: 2.1
Release: 1
License: GPL
Group: Amusements/Games
URL: http://www.igs.net/~tril/gtklife/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.igs.net/~tril/gtklife/gtklife-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel >= 1.2.0

%description
GtkLife is a fast and user-friendly implementation of Conway's Life program.
It is something comparable to the venerable XLife in speed, but with a more
modern and featureful GUI. It is not tied to any particular desktop
environment.

%prep
%setup

### FIXME: Make Makefile use autotool directory standard. (Please fix upstream)
%{__perl} -pi.orig -e '
		s|\$\(BINDIR\)|\$(bindir)|g;
		s|\$\(DATADIR\)|\$(datadir)/gtklife|g;
		s|\$\(DOCDIR\)|\$(datadir)/doc/%{name}-%{version}|g;
	' Makefile

%{__cat} <<EOF >gtklife.desktop
[Desktop Entry]
Name=Conway's Game Of Life
Comment=Create patterns and see them evolve
Icon=gtklife.png
Exec=gtklife
Terminal=false
Type=Application
Categories=GNOME;Application;Game;
EOF

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}" \
	datadir="%{_datadir}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -D -m0644 icon_48x48.png %{buildroot}%{_datadir}/pixmaps/gtklife.png

%if %{dfi}
	%{__install} -D -m0644 gtklife.desktop %{buildroot}%{_datadir}/gnome/apps/Games/gtklife.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		gtklife.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README TAGS doc/*
%{_bindir}/*
%if %{dfi}
	%{_datadir}/gnome/apps/Games/*.desktop
%else
	%{_datadir}/applications/*.desktop
%endif
%{_datadir}/gtklife/
%{_datadir}/pixmaps/*.png

%changelog
* Sat Apr 10 2004 Dag Wieers <dag@wieers.com> - 2.1-1
- Updated to release 2.1.

* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 2.0-2
- Small cosmetic changes.

* Mon Apr 05 2004 Dag Wieers <dag@wieers.com> - 2.0-1
- Initial package. (using DAR)
