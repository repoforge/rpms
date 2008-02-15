# $Id$
# Authority: dries

# Screenshot: http://memaid.sourceforge.net/screenshoots/kmemaid_screenshots/thumbs/edit_elements_correct.png
# ScreenshotURL: http://memaid.sourceforge.net/screenshoots/kmemaid_screenshots/

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Helps you to memorise question/answer pairs
Name: kmemaid
Version: 0.4.7.0
Release: 4
License: GPL
Group: Applications/Text
URL: http://memaid.sourceforge.net/

Source: http://dl.sf.net/memaid/kmemaid-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel, kdelibs-devel, gcc, make
BuildRequires: gcc-c++, qt-devel
%{?el4:BuildRequires:libselinux-devel}
%{?fc3:BuildRequires:libselinux-devel}
%{?fc2:BuildRequires:libselinux-devel}
Requires: kdelibs

%description
MemAid is a program to help you memorise question/answer pairs. It uses a
neural network to schedule the best time for an item to come up for review.

%description -l nl
MemAid is een programma dat u help om vraag/antwoord paren te onthouden. Het
gebruikt een neuraal netwerk om het ideale moment te bepalen om een bepaalde
vraag te stellen.

%prep
%setup

%build
. /etc/profile.d/qt.sh
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README TODO
%{_bindir}/kmemaid
%{_datadir}/applnk/Applications/kmemaid.desktop
%{_datadir}/apps/kmemaid/kmemaidui.rc
%{_datadir}/doc/HTML/en/kmemaid
%{_datadir}/icons/locolor/*/apps/kmemaid.png

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.7.0-4
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Wed Apr 21 2004 Dries Verachtert <dries@ulyssis.org> 0.4.7.0-3
- spec cleanup

* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 0.4.7.0-2
- completion of spec file
- added some BuildRequires

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 0.4.7.0-1
- first packaging for Fedora Core 1

