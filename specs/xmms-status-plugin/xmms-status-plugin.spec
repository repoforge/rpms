# $Id$

# Authority: newrpms
# Upstream: Ian Campbell <ijc@hellion.org.uk>

%define plugindir %(xmms-config --general-plugin-dir)

Summary: A docklet for XMMS
Name: xmms-status-plugin
Version: 1.0
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://www.hellion.org.uk/xmms-status-plugin/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.hellion.org.uk/source/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: xmms-devel

%description
A status docklet for XMMS, docks into the GNOME Status dock. 

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall XMMS_DATA_DIR="%{buildroot}%{_datadir}/xmms"
%find_lang %{name}
%{__strip} %{buildroot}%{plugindir}/*.so

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS NEWS README TODO
%{_datadir}/xmms/status_docklet/
%{plugindir}/*.so
%exclude %{plugindir}/*.la

%changelog
* Sun Mar 09 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
