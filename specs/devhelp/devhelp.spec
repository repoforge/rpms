# $Id$
# Authority: dag
# Upstream: Mikael Hallendal <micke$imendio,com>

# ExcludeDist: el4

Summary: API document browser
Name: devhelp
Version: 0.9.3
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://www.imendio.com/projects/devhelp/

Source: http://ftp.gnome.org/pub/GNOME/sources/devhelp/0.9/devhelp-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.3.1, libgnomeui-devel >= 2.2, gnome-vfs2-devel >= 2.2
BuildRequires: gtkhtml2-devel >= 2.0.0, intltool, gcc-c++, mozilla-devel, gettext

%description
devhelp is an API document browser for GNOME.

%package devel
Summary: Library to embed Devhelp in other applications
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Library of Devhelp for embedding into other applications.

%prep
%setup

%{__cat} <<'EOF' >devhelp.sh
#!/bin/sh

### Written by Dag Wieers <dag@wieers.com>
### Please send suggestions and fixes to me.

[ -f "$MOZILLA_FIVE_HOME/libgtkembedmoz.so" ] || export MOZILLA_FIVE_HOME="%{_libdir}/mozilla-1.6"
[ -f "$MOZILLA_FIVE_HOME/libgtkembedmoz.so" ] || export MOZILLA_FIVE_HOME="%{_libdir}/mozilla-1.7"
[ -f "$MOZILLA_FIVE_HOME/libgtkembedmoz.so" ] || export MOZILLA_FIVE_HOME="%{_libdir}/mozilla-1.7.2"
[ -f "$MOZILLA_FIVE_HOME/libgtkembedmoz.so" ] || export MOZILLA_FIVE_HOME="%{_libdir}/mozilla-1.7.3"
[ -f "$MOZILLA_FIVE_HOME/libgtkembedmoz.so" ] || export MOZILLA_FIVE_HOME="%{_libdir}/mozilla-1.8"
[ -f "$MOZILLA_FIVE_HOME/libgtkembedmoz.so" ] || export MOZILLA_FIVE_HOME="%{_libdir}/mozilla"

export LD_LIBRARY_PATH="$MOZILLA_FIVE_HOME:$LD_LIBRARY_PATH"
export MOZ_PLUGIN_PATH="$MOZ_PLUGIN_PATH:%{_libdir}/mozilla/plugins:$MOZILLA_FIVE_HOME/plugins"

exec %{_bindir}/devhelp-bin $@
EOF

%build
#intltoolize
%configure \
	--disable-schemas-install \
	--with-html-widget="gtkhtml2"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
#%find_lang %{name}

%{__install} -Dp -m0755 devhelp.sh %{buildroot}%{_bindir}/devhelp

%{__ln_s} -f libdevhelp-1.so.0.0.0 %{buildroot}%{_libdir}/libdevhelp-1.so.0
%{__ln_s} -f libdevhelp-1.so.0.0.0 %{buildroot}%{_libdir}/libdevhelp-1.so

%clean
%{__rm} -rf %{buildroot}

%files
# -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%config %{_sysconfdir}/gconf/schemas/devhelp.schemas
%{_bindir}/devhelp*
%{_datadir}/applications/devhelp.desktop
%{_datadir}/devhelp/
%{_datadir}/mime-info/devhelp.*
%{_datadir}/pixmaps/devhelp.png
%{_libdir}/libdevhelp-1.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/devhelp-1.0/
%{_libdir}/libdevhelp-1.so
%exclude %{_libdir}/libdevhelp-1.a
%exclude %{_libdir}/libdevhelp-1.la
%{_libdir}/pkgconfig/libdevhelp-1.0.pc

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.3-1
- Updated to release 0.9.3.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.2-1.2
- Rebuild for Fedora Core 5.

* Mon Sep 27 2004 Dag Wieers <dag@wieers.com> - 0.9.2-1
- Updated to release 0.9.2.

* Mon Aug 30 2004 Dag Wieers <dag@wieers.com> - 0.9.1-3
- Fix for newly release mozilla 1.7.

* Fri Jul 30 2004 Dag Wieers <dag@wieers.com> - 0.9.1-2
- Added seperate devel subpackage to be in line with Red Hat. (Mads Kiilerich)

* Fri Jul 30 2004 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Wed Mar 17 2004 Dag Wieers <dag@wieers.com> - 0.9-0
- Updated to release 0.9.

* Mon Feb 16 2004 Dag Wieers <dag@wieers.com> - 0.8.1-0
- Updated to release 0.8.1.

* Sun Jun 29 2003 Dag Wieers <dag@wieers.com> - 0.7-0
- Updated to release 0.7.

* Sun Apr 27 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Initial package. (using DAR)
