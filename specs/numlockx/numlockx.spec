# $Id$
# Authority: dag
# Upstream: Lubos Lunak <l.lunak$kde,org>

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4: %define _without_modxorg 1}
%{?el3: %define _without_modxorg 1}
%{?rh9: %define _without_modxorg 1}
%{?rh7: %define _without_modxorg 1}
%{?el2: %define _without_modxorg 1}

Summary: Turns on NumLock when X starts
Name: numlockx
Version: 1.1
Release: 1%{?dist}
License: MIT
Group: Applications/System
URL: http://ktown.kde.org/~seli/numlockx/

Source: http://ktown.kde.org/~seli/numlockx/numlockx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_modxorg:BuildRequires: libX11-devel, libXtst-devel, libXext-devel, libXt-devel, /usr/bin/imake}
%{?_without_modxorg:BuildRequires: XFree86-devel, /usr/X11R6/bin/imake}
%{!?_without_modxorg:Requires: xorg-x11-xinit}
%{?_without_modxorg:Requires: xinitrc}

%description
numlockx turns on NumLock when X starts.

%prep
%setup

%{__cat} <<EOF >numlockx.sh
#!/bin/sh

%{_bindir}/numlockx
EOF

%build
%configure \
%{!?_without_modxorg:--x-libraries="%{_libdir}"} \
%{!?_without_modxorg:--x-includes="%{_includedir}"}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 numlockx.sh %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/numlockx.sh

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog LICENSE README TODO
%config %{_sysconfdir}/X11/xinit/xinitrc.d/numlockx.sh
%{_bindir}/numlockx

%changelog
* Sat Nov 10 2007 Dag Wieers <dag@wieers.com> - 1.1-1
- Initial package. (using DAR)
