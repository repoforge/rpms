# $Id$
# Authority: dag
# Upstream: Carlos Garcia Campos <elkalmail$yahoo,es>

Summary: CPU frequency scaling monitor applet
Name: gnome-cpufreq-applet
Version: 0.1.3
Release: 1
License: GPL
Group: User Interface/Desktops
URL: http://linups.org/~kal/gnome-cpufreq-applet/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://linups.org/~kal/gnome-cpufreq-applet/gnome-cpufreq-applet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
GNOME CPUFreq Applet is a CPU Frequency Scaling Monitor for GNOME Panel.

%prep
%setup

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper/ 

%post
scrollkeeper-update -q || :
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/cpufreq-applet.schemas &>/dev/null

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* INSTALL NEWS README TODO
%doc %{_datadir}/gnome/help/gnome-cpufreq-applet/
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_libexecdir}/*
%{_datadir}/gnome-cpufreq-applet/
%{_datadir}/pixmaps/gnome-cpufreq-applet/
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/omf/gnome-cpufreq-applet/
%{_libdir}/bonobo/servers/*.server

%changelog
* Wed May 12 2004 Dag Wieers <dag@wieers.com> - 0.1.3-1
- Updated to release 0.1.3.

* Mon Mar 29 2004 Dag Wieers <dag@wieers.com> - 0.1.2-1
- Updated to release 0.1.2.

* Wed Mar 03 2004 Dag Wieers <dag@wieers.com> - 0.1.1-0
- Initial package. (using DAR)
