# Authority: dag

Summary: The X2 text editor
Name: x2
Version: 2.02.2
Release: 2
License: GPL
Group: Applications/Editors
URL: http://www.tangbu.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.tangbu.com/DOWNLOAD/xlinux.tgz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

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
%{__install} -d %{buildroot}{%{_bindir},%{_libdir},%{_datadir}/x2/,%{_sysconfdir}/profile.d/}
%{__install} x %{buildroot}%{_bindir}
%{__install} xx %{buildroot}%{_bindir}
%{__install} xutils.so %{buildroot}%{_libdir}
%{__install} xprofile %{buildroot}%{_datadir}/x2/
%{__install} xprofile.def %{buildroot}%{_datadir}/x2/
%{__install} xprofile.unx %{buildroot}%{_datadir}/x2/
%{__install} xunix.hlp %{buildroot}%{_datadir}/x2/X.HLP
%{__install} XUNIX.PRO %{buildroot}%{_datadir}/x2/
%{__install} x2.sh %{buildroot}%{_sysconfdir}/profile.d/

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
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
* Sat Nov 09 2002 Dag Wieers <dag@wieers.com> - 2.02.2
- Initial package. (using DAR)
