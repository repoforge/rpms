# Authority: dag
# Upstream: Mike Newman <mike@gtnorthern.demon.co.uk>

Summary: A tool for determining versions of installed GNOME packages.
Name: gnome-pkgview
Version: 1.0.5
Release: 0
License: GPL
Group: Applications/System
URL: http://www.greatnorthern.demon.co.uk/gnome-pkgview.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.gtnorthern,demon.co.uk/packages/pkgview/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gtk2 >= 2.0.0, libxml2 >= 2.0.0, libgnomeui >= 2.0

%description
Displays version information for desktop components, and determines the
overall desktop version from the gnome-version.xml file.

%prep
%setup

%build
%configure \
	--disable-dependency-tracking \
	--disable-schemas-install
%{__cat} <<EOF >%{_builddir}/%{buildsubdir}/po/Makefile
all:
	echo "Nothing to do."
install:
	echo "Nothing to do."
EOF
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
#find_lang %{name}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q

%postun
scrollkeeper-update -q

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README TODO
%config %{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%{_datadir}/pixmaps/gnome-pkgview/*
%{_datadir}/applications/*

%changelog
* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 1.0.5-0
- Updated to release 1.0.5.

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Updated to release 1.0.1.

* Sat Feb 01 2003 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Initial package. (using DAR)
