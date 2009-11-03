# $Id$
# Authority: dag
# Upstream: George Farris <farrisg$mala,bc,ca>

%define real_version 0.7.3-1

Summary: The GNOME Fax Application
Name: gfax
Version: 0.7.3.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/Communications
URL: http://gfax.cowlug.org/

Source: http://gfax.cowlug.org/gfax-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: mono >= 0.30
#BuildRequires: gtk-sharp-devel >= 0.9
#Requires: gnome-libs >= 1.2, libglade >= 0.7, python >= 1.5.2
Requires: mono >= 0.30, gtk-sharp >= 0.15

BuildArch: noarch

%description
Gfax is a popup tool for easily sending facsimilies by printing
to a fax printer.

%prep
%setup -n %{name}

### FIXME: makeinstall without DESTDIR/autotool paths
%{__perl} -pi.orig -e '
		if (! m|^INSTALL|) {
			s| /usr/bin| \$(DESTDIR)\$(bindir)|;
			s| /usr/lib| \$(DESTDIR)\$(libdir)|;
			s| /usr/share| \$(DESTDIR)\$(datadir)|;
			s| /var| \$(DESTDIR)\$(localstatedir)|;
			s|env GCONF_CONFIG_SOURCE|#env GCONF_CONFIG_SOURCE|;
		}
	' Makefile

%{__perl} -pi.orig -e 's|GtkSharp.ToggledArgs|Gtk.ToggledArgs|' src/*.cs

%build
%{__make} schema
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
### FIXME: Directories should be created by Makefile
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_libdir} \
			%{buildroot}%{_datadir}/applications \
			%{buildroot}%{_datadir}/pixmaps \
			%{buildroot}%{_sysconfdir}/gconf/schemas/ \
			%{buildroot}%{_localstatedir}/spool/gfax \
			%{buildroot}%{_datadir}/gnome-print/profiles
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall

%{__install} -Dp -m0644 data/gfax.schema %{buildroot}%{_sysconfdir}/gconf/schemas/gfax.schemas

### FIXME: Install fax printer profile for GNOME 1.x
#%{__install} -m0644 data/fax-g3.profile %{buildroot}%{_datadir}/gnome-print/profiles/

### FIXME: Install fax printer profile for GNOME 2.x
#for dir in /usr/share/libgnomeprint/*; do
#	%{__install} -p -m0644 data/GFAX.xml $dir/printers
#	%{__install} -p -m0644 data/GNOME-GFAX-PS.xml $dir/models
#done

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
%{_datadir}/gfax/printer-setup.sh --install

%preun
%{_datadir}/gfax/printer-setup.sh --remove

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/*.txt hylafax.txt INSTALL NEWS README TODO
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/applications/*.desktop
#%{_datadir}/gnome-print/profiles/*
%{_datadir}/gfax/
%{_datadir}/pixmaps/*

%defattr(-, root, root, 0777)
%{_localstatedir}/spool/gfax/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.3.1-1.2
- Rebuild for Fedora Core 5.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.3.1-1
- Updated to release 0.7.3.1.

* Wed Mar 03 2004 Dag Wieers <dag@wieers.com> - 0.6-0.beta9
- Updated to release 0.6.beta9.

* Sat Feb 28 2004 Dag Wieers <dag@wieers.com> - 0.6-0.beta8
- Updated to release 0.6.beta8.

* Thu Jan 01 2004 Dag Wieers <dag@wieers.com> - 0.6-0.beta5
- Updated to release 0.6.beta5.

* Tue Jun 17 2003 Dag Wieers <dag@wieers.com> - 0.6-0.beta4
- Updated to release 0.6beta4.

* Sun May 18 2003 Dag Wieers <dag@wieers.com> - 0.6-0.beta3
- Updated to release 0.6beta3.

* Sun Mar 30 2003 Dag Wieers <dag@wieers.com> - 0.5-0
- Initial package. (using DAR)
