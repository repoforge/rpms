# $Id$
# Authority: shuff
# Upstream: Jelmer Vernooij <jelmer$samba,org>
# ExcludeDist el3 el4

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define nautilus_extensiondir %(pkg-config --variable=extensiondir libnautilus-extension)

Summary: GNOME/GTK+ integration for Bazaar
Name: bzr-gtk
Version: 0.99.0
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://wiki.bazaar.canonical.com/bzr-gtk/

Source: http://edge.launchpad.net/bzr-gtk/trunk/%{version}/+download/bzr-gtk-%{version}.tar.gz
Patch0: bzr-gtk-0.99.0_pickle.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pycairo-devel >= 1.0
BuildRequires: pygtk2-devel >= 2.8
BuildRequires: python-nautilus-devel
BuildRequires: bzr >= 2.0
Requires: python-nautilus
Requires: bzr >= 2.0
Requires: hicolor-icon-theme

%description
bzr-gtk is a plugin for Bazaar that aims to provide GTK+ interfaces to most
Bazaar operations.

It will also integrate with the GNOME desktop environment, if GNOME python
bindings are found.

%prep
%setup
%patch0 -p1

%build
CFLAGS="%{optflags}" %{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
CFLAGS="%{optflags}" %{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%post
/usr/bin/gtk-update-icon-cache -f -t %{_iconsbasedir} >/dev/null 2>&1 

%postun
/usr/bin/gtk-update-icon-cache -f -t %{_iconsbasedir} >/dev/null 2>&1 

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING HACKING NEWS README TODO
%{nautilus_extensiondir}/*
%{python_sitearch}/bzrlib/plugins/gtk/
%{_bindir}/*
%{_datadir}/application-registry/*
%{_datadir}/bzr-gtk/
%{_datadir}/pixmaps/*
%{_desktopdir}/*
%{_iconsbasedir}/scalable/emblems/*

%changelog
* Wed Oct 20 2010 Steve Huff <shuff@vecna.org> - 0.99.0-1
- Initial package.
