# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

Summary: Set the background of your X Windows desktop under water
Name: xdesktopwaves
Version: 1.3
Release: 1%{?dist}
License: GPL
Group: Amusements/Graphics
URL: http://xdesktopwaves.sourceforge.net/

Source: http://dl.sf.net/xdesktopwaves/xdesktopwaves-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_modxorg:BuildRequires: libX11-devel, libXext-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
xdesktopwaves is a cellular automata setting the background of your X Windows
desktop under water. Windows and mouse are like ships on the sea. Each movement
of these ends up in moving water waves. You can even have rain and/or storm
stirring up the water.


%prep
%setup


%build
%{__make} %{?_smp_mflags} LFLAGS="-L/usr/X11R6/%{_lib}"


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}{%{_bindir},%{_mandir}/man1}
%{__make} install \
    BINDIR=%{buildroot}%{_bindir} \
    MAN1DIR=%{buildroot}%{_mandir}/man1


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/xdesktopwaves
%{_mandir}/man1/xdesktopwaves.1*


%changelog
* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 1.3-1
- Updated to release 1.3.

* Tue Dec 07 2004 Dag Wieers <dag@wieers.com> - 1.2-1
- Updated to release 1.2.

* Wed Dec  1 2004 Matthias Saou <http://freshrpms.net/> 1.1-1
- Remove i386 exclusivearch.
- Add LFLAGS override to fix linking on 64bit archs.

* Wed Dec 01 2004 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Fri Nov 19 2004 Matthias Saou <http://freshrpms.net/> 1.0-1
- Initial RPM release.

