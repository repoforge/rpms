# Authority: dag

%define rname mplayerplug-in

Summary: MPlayer plugin for Mozilla.
Name: mozilla-mplayer
Version: 0.95
Release: 1
License: GPL
Group: Applications/Internet
URL: http://mplayerplug-in.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://download.sourceforge.net/project/mplayerplug-in/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: XFree86-devel
Requires: mplayer >= 0.90, mozilla
Obsoletes: mplayerplug-in < %{version}
Provides: mplayerplug-in

%description
This package contains a plugin for the Mozilla browser that makes it
possible to use the MPlayer movie player in Mozilla.

%prep
%setup -n %{rname}

%{__cat} <<'EOF' >mplayerplug-in.conf.dag
#debug=1
#logfile=$HOME/mpp.log
vo=xv,x11
ao=esd,oss,arts
download=1
#dload-dir=$HOME/tmp
#noembed=1
#cachesize=256
#use-mimetypes=1
#enable-real=1
#enable-wm=0
#enable-qt=0
#enable-mpeg=0
EOF

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}/mozilla/plugins/ \
			%{buildroot}%{_sysconfdir}
%{__install} -m0755 mplayerplug-in.so %{buildroot}%{_libdir}/mozilla/plugins/
%{__install} -m0755 mplayerplug-in.types %{buildroot}%{_sysconfdir}
%{__install} -m0755 mplayerplug-in.conf.dag %{buildroot}%{_sysconfdir}/mplayerplug-in.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README TODO mplayerplug-in.types mplayerplug-in.conf
%config(noreplace) %{_sysconfdir}/*
%{_libdir}/mozilla/plugins/*.so

%changelog
* Fri Oct 10 2003 Dag Wieers <dag@wieers.com> - 0.95-1
- Disabled using MIME-types and fix config files.

* Mon Oct 06 2003 Dag Wieers <dag@wieers.com> - 0.95-0
- Updated to release 0.95.

* Thu Sep 11 2003 Dag Wieers <dag@wieers.com> - 0.91-0
- Updated to release 0.91.

* Sun Apr 20 2003 Dag Wieers <dag@wieers.com> - 0.71-0
- Initial package. (using DAR)
