# $Id$
# Authority: dries
# Upstream: Steve Grubb <scg$jax,org>

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

%define real_version 232

Summary: Command line utility for creating charts and plots
Name: ploticus
Version: 2.32
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://ploticus.sourceforge.net/

Source: http://ploticus.sourceforge.net/download/pl%{real_version}src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel, zlib-devel
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
PLOTICUS is a command line utility for creating bar, line, pie, boxplot,
scatterplot, sweep, heatmap, vector, timeline, Venn diagrams, and other
types of charts and plots. ploticus is good for automated or just-in-time
graph generation. It handles date, time, and categorical data nicely, and
has some basic statistical capabilities. It can output to GIF, PNG, SVG,
SWF, JPEG, PostScript, EPS, and X11. You can use convenient preset options
or create complex scripts with rich and detailed color and style operations.

%prep
%setup -n pl%{real_version}src

%build
cd src
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} %{buildroot}%{_datadir}/ploticus
cd src
%makeinstall BIN=%{buildroot}%{_bindir}
%{__install} -D ../prefabs/* %{buildroot}%{_datadir}/ploticus

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/pl
%{_datadir}/ploticus

%changelog
* Fri Oct 14 2005 Dries Verachtert <dries@ulyssis.org> - 2.32-2
- xorg/XFree86 buildreqs added.

* Wed Aug 31 2005 Dries Verachtert <dries@ulyssis.org> - 2.32-1
- Initial package.
