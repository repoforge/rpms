# $Id$

# Authority: dag
# Upstream: Adam Feakin <adamf@snika.uklinux.net>

%define plugindir %(xmms-config --general-plugin-dir)

Summary: General plugin for using xmms as an alarm clock
Name: xmms-alarm
Version: 0.3.4
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.snika.uklinux.net/?p=xmms-alarm

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.snika.uklinux.net/xmms-alarm/xmms-alarm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: xmms-devel, glib-devel >= 1.2.6, gtk+-devel >= 1.2.6

%description
xmms General plugin for using xmms as an alarm clock.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall libdir="%{buildroot}%{plugindir}"

### Clean up buildroot
%{__rm} -f %{buildroot}%{plugindir}/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog INSTALL NEWS README
%{plugindir}/*.so
#exclude %{plugindir}/*.la

%changelog
* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 0.3.4-1
- Updated to release 0.3.4.

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 0.3.3-0
- Updated to release 0.3.3.

* Tue Feb 11 2003 Dag Wieers <dag@wieers.com> - 0.3.2-0
- Initial package. (using DAR)
