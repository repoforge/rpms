# $Id$
# Authority: dag

Summary: Full-featured IDE for Mono and Gtk#
Name: monodevelop
Version: 0.5.1
Release: 1
License: GPL
Group: Development/Environment
URL: http://www.monodevelop.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.go-mono.com/archive/1.0.5/monodevelop-%{version}.tar.gz
Patch: monodevelop-remove-mime-update.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, gtksourceview-sharp >= 0.3,
BuildRequires: mono-core >= 0.96, monodoc >= 0.17, gtk-sharp >= 0.98
BuildRequires: gecko-sharp >= 0.5, intltool, gettext
Requires: pkgconfig, gtksourceview, mono-core, gtk-sharp

%description
This is MonoDevelop which is intended to be a
full-featured integrated development environment (IDE) for
mono and Gtk#. It was originally a port of SharpDevelop 0.98.

%prep
%setup
%patch -p1

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}" \
	GACUTIL_FLAGS="/package gtk-sharp /root %{buildroot}%{_libdir}"
%find_lang %{name}

%post
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :

%postun
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog INSTALL README
%{_bindir}/monodevelop
%{_datadir}/applications/monodevelop.desktop
%{_datadir}/mime/packages/monodevelop.xml
%{_datadir}/pixmaps/monodevelop.png
%{_libdir}/monodevelop/

%changelog
* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Initial package. (using DAR)
