# Authority: dag
# Upstream: <nxtvepg-users@lists.sourceforge.net>
# Distcc: 0

Summary: NexTView EPG decoder and browser.
Name: nxtvepg
Version: 2.6.0
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://nxtvepg.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/nxtvepg/nxtvepg-%{version}.tar.gz
Source1: nxtvepg.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: XFree86-devel, tcl, tk
%{?rhfc1:BuildRequires: tcl-devel, tk-devel}
%{?rhel3:BuildRequires: tcl-devel, tk-devel}

%description
nxtvepg is a decoder and browser for nexTView - an Electronic TV Programme
Guide for the analog domain (as opposed to the various digital EPGs that
come with most digital broadcasts). It allows you to decode and browse TV
programme listings for most of the major networks in Germany, Austria,
France and Switzerland.

%prep
%setup

%{__perl} -pi.orig -e '
		s|/usr/lib|%{_datadir}|g;
		s|/usr/tmp|%{_localstatedir}/tmp|g;
		s|\$\(mandir\)|\$(mandir)/man1|g;
	' Makefile

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Nextview TV Browser
Comment=Browse through TV Nextview information.
Icon=nxtvepg.png
Exec=nxtvepg
Terminal=false
Type=Application
Categories=Application;AudioVideo;
EOF

%build
%{__make} %{?_smp_mflags} \
	prefix="%{_prefix}" \
	CCFLAGS="%{optflags}"

%install
%makeinstall \
	resdir="%{buildroot}%{_prefix}/X11R6/lib/X11" \
	SYS_DBDIR="%{buildroot}%{_localstatedir}/tmp/nxtvdb"

%{__install} -d -m0755 %{buildroot}%{_datadir}/pixmaps/
%{__install} -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop


%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc CHANGES COPYRIGHT README* TODO manual.html
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_localstatedir}/tmp/nxtvdb/
%{_prefix}/X11R6/lib/X11/app-defaults/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 2.6.0-1
- Initial package. (using DAR)
