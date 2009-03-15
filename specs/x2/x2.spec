# $Id$
# Authority: dag
# Upstream: Blair W. Thompson <blair$tangbu,com>

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

Summary: The X2 text editor
Name: x2
Version: 2.08.1
Release: 1
License: GPL
Group: Applications/Editors
URL: http://www.tangbu.com/

Source: http://www.tangbu.com/DOWNLOAD/xlinux.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386
BuildRequires: ncurses-devel
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
X2 is a text mode editor that is designed to make the code writing process as
fast and easy as possible. There are versions available for OS/2, DOS, Windows
NT, Windows 95, Linux, AIX and Sun Solaris.

X2 and Rexx together can make a very powerful combination. For example, Rexx
macros are available to turn X2 into a Usenet news reader or a POP mail client.

%prep
%setup -c %{name}-%{version}

%{__cat} <<'EOF' >x.sh
#!/bin/sh
export X2PATH="%{_datadir}/x2"
exec %{_datadir}/x2/x $@
EOF

%{__cat} <<'EOF' >xx.sh
#!/bin/sh
export X2PATH="%{_datadir}/x2"
exec %{_datadir}/x2/xx $@
EOF

%build
./xprofile

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 x.sh %{buildroot}%{_bindir}/x
%{__install} -Dp -m0755 xx.sh %{buildroot}%{_bindir}/xx
%{__install} -Dp -m0755 x %{buildroot}%{_datadir}/x2/x
%{__install} -Dp -m0755 xx %{buildroot}%{_datadir}/x2/xx
%{__install} -Dp -m0755 xutils.so %{buildroot}%{_libdir}/xutils.so
%{__install} -Dp -m0755 xprofile %{buildroot}%{_datadir}/x2/xprofile
%{__install} -Dp -m0644 xprofile.def %{buildroot}%{_datadir}/x2/xprofile.def
%{__install} -Dp -m0644 xprofile.unx %{buildroot}%{_datadir}/x2/xprofile.unx
%{__install} -Dp -m0644 xunix.hlp %{buildroot}%{_datadir}/x2/X.HLP
%{__install} -Dp -m0644 XUNIX.PRO %{buildroot}%{_datadir}/x2/XUNIX.PRO
%{__install} -Dp -m0644 cpp.xprofile %{buildroot}%{_datadir}/x2/cpp.xprofile
%{__install} -Dp -m0644 html.xprofile %{buildroot}%{_datadir}/x2/html.xprofile
%{__install} -Dp -m0644 rexx.xprofile %{buildroot}%{_datadir}/x2/rexx.xprofile

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%config %{_datadir}/x2/XUNIX.PRO
%{_bindir}/x
%{_bindir}/xx
%{_libdir}/xutils.so
%dir %{_datadir}/x2/
%{_datadir}/x2/x
%{_datadir}/x2/xx
%{_datadir}/x2/xprofile
%{_datadir}/x2/xprofile.def
%{_datadir}/x2/xprofile.unx
%{_datadir}/x2/cpp.xprofile
%{_datadir}/x2/html.xprofile
%{_datadir}/x2/rexx.xprofile
%{_datadir}/x2/X.HLP

%changelog
* Sun Feb 22 2009 Dag Wieers <dag@wieers.com> - 2.08.1-1
- Updated to release 2.08.1.

* Mon May 09 2005 Dag Wieers <dag@wieers.com> - 2.05.1-2
- Added missing syntax files. (Alain Rykaert)

* Tue May 03 2005 Dag Wieers <dag@wieers.com> - 2.05.1-1
- Updated to release 2.05.1.

* Wed May 12 2004 Dag Wieers <dag@wieers.com> - 2.04.1-1
- Updated to release 2.04.1.

* Sat Nov 09 2002 Dag Wieers <dag@wieers.com> - 2.02.2-1
- Initial package. (using DAR)
