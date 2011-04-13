Name:		wifi-radar
Summary:	A utility for managing WiFi profiles
Version:	1.9.8
Release:	1%{?dist}
License:	GPL
Group:		Applications/Internet
URL:		http://wifi-radar.systemimager.org/
Source0:	http://wifi-radar.systemimager.org/pub/wifi-radar-%{version}.tar.bz2
Source1:	fedora-wifi-radar.desktop
Source2:	wifi-radar-pam.d
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Requires:	pygtk2 net-tools wireless-tools dhclient usermode
BuildRequires:	desktop-file-utils

%description
WiFi Radar is a straightforward utility, which scans for available wireless
networks, and manages their associated profiles.

%prep
%setup -q

%build
%__make

%install
# An empty config file
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/wifi-radar
touch $RPM_BUILD_ROOT/%{_sysconfdir}/wifi-radar/wifi-radar.conf
# The actual executable
mkdir -p $RPM_BUILD_ROOT/%{_sbindir}
cp wifi-radar.localized $RPM_BUILD_ROOT/%{_sbindir}/wifi-radar
# The symlink for normal users
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
ln -s consolehelper $RPM_BUILD_ROOT/%{_bindir}/wifi-radar
# consolehelper file
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/security/console.apps
cat > $RPM_BUILD_ROOT/%{_sysconfdir}/security/console.apps/wifi-radar <<EOF
USER=root
PROGRAM=%{_sbindir}/wifi-radar
SESSION=true
EOF
# PAM file
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/pam.d
cp %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/pam.d/wifi-radar
# man pages
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
cp wifi-radar.1 $RPM_BUILD_ROOT/%{_mandir}/man1/
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man5
cp wifi-radar.conf.5 $RPM_BUILD_ROOT/%{_mandir}/man5/
# Daemon init script
#mkdir -p $RPM_BUILD_ROOT/%{_initrddir}
#cp init_script $RPM_BUILD_ROOT/%{_initrddir}/wifi-radar
# Icons
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/pixmaps
cp pixmaps/wifi-radar.{png,svg} $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
# Desktop menus
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
#cp %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/applications/
desktop-file-install --vendor fedora --dir $RPM_BUILD_ROOT/%{_datadir}/applications	\
	--add-category X-Fedora %{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0700,root,root) %dir %{_sysconfdir}/wifi-radar
%attr(0600,root,root) %ghost %config(missingok,noreplace) %{_sysconfdir}/wifi-radar/wifi-radar.conf
%attr(0755,root,root) %{_sbindir}/wifi-radar
%{_bindir}/wifi-radar
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/security/console.apps/wifi-radar
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pam.d/wifi-radar
%attr(0644,root,root) %{_mandir}/man1/*
%attr(0644,root,root) %{_mandir}/man5/*
#%attr(0755,root,root) %{_initrddir}/wifi-radar
%attr(0644,root,root) %{_datadir}/pixmaps/*
%attr(0644,root,root) %{_datadir}/applications/fedora-wifi-radar.desktop
%defattr(0644,root,root,0755)
#%doc AUTHORS ChangeLog COPYING DEVELOPER_GUIDELINES README TODO
%doc CHANGE.LOG COPYING DEVELOPER_GUIDELINES README TODO

%changelog
* Wed Nov 21 2007 Heiko Adams <info@fedora-blog.de> 1.9.8-1
- rebuild for rpmforge
- update to 1.9.8

* Sun Sep 17 2006 Ian Pilcher <i.pilcher@comcast.net> 1.9.6-3
- Bump release for FC6 rebuild
- Fix dates in previous changelog entries (It's 2006, duh!)

* Thu Jun  1 2006 Ian Pilcher <i.pilcher@comcast.net> 1.9.6-2
- Use desktop-file-install (and BuildRequire desktop-file-utils)
- Add noreplace flag to config file
- Fix doc directory permissions

* Fri May 12 2006 Ian Pilcher <i.pilcher@comcast.net> 1.9.6-1
- Initial SPEC file for Fedora Extras
