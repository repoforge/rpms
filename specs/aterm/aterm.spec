# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%define desktop_vendor rpmforge

Summary: Graphical VT102 emulator
Name: aterm
Version: 0.4.2
Release: 1.2
License: GPL
Group: User Interface/X
URL: http://aterm.sourceforge.net/

Source: http://dl.sf.net/aterm/aterm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_modxorg:BuildRequires: libX11-devel, libXt-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
aterm is a color vt102 terminal emulator, based on rxvt, intended as
an xterm(1) replacement for users who do not require features such as
Tektronix 4014 emulation and toolkit-style configurability. As a
result, aterm uses much less swap space -- a significant advantage on
a machine serving many X sessions.

%prep
%setup

%{__cat} <<EOF >aterm.desktop
[Desktop Entry]
Name=Aterm Terminal
Comment=VT102 emulator
Exec=aterm
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;System;
EOF

%build
%configure \
	--enable-background-image \
	--enable-fading \
	--enable-graphics \
	--enable-menubar \
	--enable-next-scroll \
	--enable-transparency \
	--enable-utmp \
	--enable-wtmp \
	--enable-xgetdefault \
	--with-term="xterm" \
	--with-x \
	--with-xpm
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall mandir="%{buildroot}%{_mandir}/man1"

%if %{?_without_freedesktop:1}0
        %{__install} -Dp -m0644 aterm.desktop %{buildroot}%{_datadir}/gnome/apps/System/aterm.desktop
%else
### Desktop entry
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install \
		--delete-original                          \
		--vendor %{desktop_vendor}                 \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		aterm.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog doc/BUGS doc/ChangeLog.rxvt doc/FAQ doc/README*
%doc doc/*.html doc/menu/* doc/TODO
%doc %{_mandir}/man1/aterm.1*
%{_bindir}/aterm
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-aterm.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/System/aterm.desktop}

%changelog
* Sun Mar 20 2005 Dag Wieers <dag@wieers.com> - 0.4.2-1
- Initial package. (using DAR)
