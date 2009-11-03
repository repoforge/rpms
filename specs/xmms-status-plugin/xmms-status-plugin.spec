# $Id$
# Authority: rudolf
# Upstream: Ian Campbell <ijc$hellion,org,uk>

%define xmms_generaldir %(xmms-config --general-plugin-dir)

Summary: docklet for XMMS
Name: xmms-status-plugin
Version: 1.0
Release: 0%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.hellion.org.uk/xmms-status-plugin/

Source: http://www.hellion.org.uk/source/xmms-status-plugin-%{version}.tar.gz
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
%makeinstall \
	XMMS_DATA_DIR="%{buildroot}%{_datadir}/xmms" \
	libdir="%{buildroot}%{xmms_generaldir}"
%find_lang %{name}
%{__strip} %{buildroot}%{xmms_generaldir}/*.so


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS NEWS README TODO
%{_datadir}/xmms/status_docklet/
%{xmms_generaldir}/*.so
%exclude %{xmms_generaldir}/*.la


%changelog
* Sun Mar 09 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
