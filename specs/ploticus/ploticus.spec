# $Id$
# Authority: dries
# Upstream: Steve Grubb <scg$jax,org>

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

%define real_version 241

Summary: Command line utility for creating charts and plots
Name: ploticus
Version: 2.41
Release: 1%{?dist}
License: GPL
Group: Applications/Publishing
URL: http://ploticus.sourceforge.net/

Source: http://dl.sf.net/ploticus/pl%{real_version}src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel, zlib-devel
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libXext-devel}

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

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' src/Makefile

%build
%{__make} -C src %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} %{buildroot}%{_datadir}/ploticus/pltestsuite/
%{__make} install -C src INSTALLBIN=%{buildroot}%{_bindir} DESTDIR="%{buildroot}"
%{__install} -D prefabs/* %{buildroot}%{_datadir}/ploticus
%{__install} -D pltestsuite/* %{buildroot}%{_datadir}/ploticus/pltestsuite

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/pl
%{_datadir}/ploticus/

%changelog
* Thu Mar 12 2009 Dries Verachtert <dries@ulyssis.org> - 2.41-1
- Updated to release 2.41.

* Sat Aug 12 2006 Dries Verachtert <dries@ulyssis.org> - 2.33-1
- Updated to release 2.33.

* Sat Apr 15 2006 Dag Wieers <dag@wieers.com> - 2.32-2
- Added x86_64 patch and included pltestsuite (Phil Schaffner)

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.32-1.2
- Rebuild for Fedora Core 5.

* Fri Oct 14 2005 Dries Verachtert <dries@ulyssis.org> - 2.32-2
- xorg/XFree86 buildreqs added.

* Wed Aug 31 2005 Dries Verachtert <dries@ulyssis.org> - 2.32-1
- Initial package.
