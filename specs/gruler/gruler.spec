# $Id$
# Authority: dag
# Upstream: Ian McIntosh <ian_mcintosh$linuxadvocate,org>

%define desktop_vendor rpmforge

%define real_name gruler

Summary: Customizable screen ruler
Name: gruler
Version: 0.6
Release: 1.2%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://linuxadvocate.org/projects/gruler/

Source: http://linuxadvocate.org/projects/gruler/downloads/gruler-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, libgnomeui-devel
BuildRequires: desktop-file-utils

%description
gruler is a customizable screen ruler.

%prep
%setup -n %{real_name}-%{version}

%{__cat} <<EOF >gruler.desktop.in
[Desktop Entry]
Name=Gruler Screen Measuring
Comment=Measure the metrics of screen objects
Exec=gruler
Encoding=UTF-8
Icon=gruler-icon.png
Categories=Application;Utility;
Terminal=false
Type=Application
EOF

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
        --add-category X-Red-Hat-Base              \
        --dir %{buildroot}%{_datadir}/applications \
        gruler.desktop

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_prefix}/doc/gruler/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/gruler
%{_includedir}/gruler/
%{_datadir}/pixmaps/gruler/gruler-icon.png
%exclude %{_datadir}/gnome/apps/Utilities/gruler.desktop
%{_datadir}/applications/%{desktop_vendor}-gruler.desktop
%{_datadir}/gruler/

%changelog
* Thu Feb 10 2005 Dan Allen <dan.allen@mojavelinux.com> - 0.6
- Updated to release 0.6.
- Improved desktop file.

* Sat Oct 02 2004 Dag Wieers <dag@wieers.com> - 0.4-1
- Initial package. (using DAR)
