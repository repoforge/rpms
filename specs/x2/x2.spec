# $Id$
# Authority: dag
# Upstream: Blair W. Thompson <blair$tangbu,com>

Summary: The X2 text editor
Name: x2
Version: 2.04.1
Release: 1
License: GPL
Group: Applications/Editors
URL: http://www.tangbu.com/

Source: http://www.tangbu.com/DOWNLOAD/xlinux.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
X2 is a text mode editor that is designed to make the code writing process as
fast and easy as possible. There are versions available for OS/2, DOS, Windows
NT, Windows 95, Linux, AIX and Sun Solaris.

X2 and Rexx together can make a very powerful combination. For example, Rexx
macros are available to turn X2 into a Usenet news reader or a POP mail client.

%prep
%setup -c %{name}-%{version}

%{__cat} <<EOF >x2.sh
export X2PATH="%{_datadir}/x2"
EOF

%build
./xprofile

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 x %{buildroot}%{_bindir}/x
%{__install} -Dp -m0755 xx %{buildroot}%{_bindir}/xx
%{__install} -Dp -m0755 xutils.so %{buildroot}%{_libdir}/xutils.so
%{__install} -Dp -m0644 xprofile %{buildroot}%{_datadir}/x2/xprofile
%{__install} -Dp -m0644 xprofile.def %{buildroot}%{_datadir}/x2/xprofile.def
%{__install} -Dp -m0644 xprofile.unx %{buildroot}%{_datadir}/x2/xprofile.unx
%{__install} -Dp -m0644 xunix.hlp %{buildroot}%{_datadir}/x2/X.HLP
%{__install} -Dp -m0644 XUNIX.PRO %{buildroot}%{_datadir}/x2/XUNIX.PRO
%{__install} -Dp -m0755 x2.sh %{buildroot}%{_sysconfdir}/profile.d/x2.sh

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
%config %{_sysconfdir}/profile.d/
%{_bindir}/*
%{_libdir}/*
%{_datadir}/x2/xprofile
%{_datadir}/x2/xprofile.def
%{_datadir}/x2/xprofile.unx
%{_datadir}/x2/X.HLP

%changelog
* Wed May 12 2004 Dag Wieers <dag@wieers.com> - 2.04.1-1
- Updated to release 2.04.1.

* Sat Nov 09 2002 Dag Wieers <dag@wieers.com> - 2.02.2-1
- Initial package. (using DAR)
