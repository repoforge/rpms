# $Id$
# Authority: dries
# Upstream: dieter,landolt$secs,ch
# Screenshot: http://www.truesoft.ch/dieter/kkeyled/help/en/HTML/screenshot.png
# ScreenshotURL: http://www.truesoft.ch/dieter/kkeyled-screens.html

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}

Summary: Displays the LED states of the keyboard
Name: kkeyled
Version: 0.8.11
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.truesoft.ch/dieter/kkeyled.html

Source: http://www.truesoft.ch/dieter/kkeyled/software/kkeyled-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, libpng-devel, libart_lgpl-devel
BuildRequires: arts-devel, gcc-c++, gettext
BuildRequires: zlib-devel, qt-devel, libjpeg-devel
BuildRequires: kdelibs-devel, automake, autoconf
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
KKeyled is a KDE panel tray widget which displays the LED states of
the keyboard (ie. Caps Lock, Num Lock, and Scroll Lock). It is
particularly useful for wireless keyboards without LEDs, and can be
used to set the LED states of the keyboard aswell.

%prep
%setup -n %{name}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--add-category Utility                     \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applnk/Utilities/%{name}.desktop
%{__rm} -f %{buildroot}%{_datadir}/applnk/Utilities/%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_datadir}/config/kkeyledrc
%{_datadir}/apps/kkeyled
%{_datadir}/applications/*kkeyled.desktop
%{_datadir}/locale/de/LC_MESSAGES/kkeyled.mo
%{_datadir}/doc/HTML/en/kkeyled
%{_datadir}/doc/HTML/de/kkeyled
%{_datadir}/icons/*/*/apps/kkeyled.png
%{_bindir}/kkeyled

%changelog
* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.8.11-1
- Update to release 0.8.11.

* Sat Mar 12 2005 Dries Verachtert <dries@ulyssis.org> - 0.8.10-1
- Initial package.
