# $Id$
# Authority: dag
# Upstream: Adam Feakin <adamf$snika,uklinux,net>

# Distcc: 0

%define xmms_generaldir %(xmms-config --general-plugin-dir)

Summary: General plugin for using xmms as an alarm clock
Name: xmms-alarm
Version: 0.3.5
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.snika.uklinux.net/?p=xmms-alarm

Source: http://www.snika.uklinux.net/xmms-alarm/xmms-alarm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: xmms-devel, glib-devel >= 1.2.6, gtk+-devel >= 1.2.6

%description
xmms plugin for using xmms as an alarm clock.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall \
	libdir="%{buildroot}%{xmms_generaldir}"


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog INSTALL NEWS README
%{xmms_generaldir}/*.so
%exclude %{xmms_generaldir}/*.la

%changelog
* Fri Apr 02 2004 Dag Wieers <dag@wieers.com> - 0.3.5-1
- Updated to release 0.3.5.

* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 0.3.4-1
- Updated to release 0.3.4.

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 0.3.3-0
- Updated to release 0.3.3.

* Tue Feb 11 2003 Dag Wieers <dag@wieers.com> - 0.3.2-0
- Initial package. (using DAR)
