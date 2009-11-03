# $Id$
# Authority: dag
# Upstream: Daniel Elstner <daniel,elstner$gmx,net>

Summary: Graphical search/replace tool featuring Perl-style regular expressions
Name: regexxer
Version: 0.9
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://regexxer.sourceforge.net/

Source: http://dl.sf.net/regexxer/regexxer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.12, gtk2-devel >= 2.0
BuildRequires: libsigc++-devel >= 1.2, gtkmm2-devel >= 2.0
BuildRequires: libglademm24-devel, pcre-devel, gettext
BuildRequires: pcre >= 3.9, gtkmm24-devel, gcc-c++, gconfmm26-devel
BuildRequires: desktop-file-utils

%description
regexxer is a nifty GUI search/replace tool featuring Perl-style
regular expressions.

%prep
%setup

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/regexxer
%{_datadir}/applications/regexxer.desktop
%{_datadir}/icons/hicolor/48x48/apps/regexxer.png
%{_datadir}/regexxer/

%changelog
* Mon Feb 19 2007 Dag Wieers <dag@wieers.com> - 0.9-1
- Updated to release 0.9.

* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.8-3
- Fixed files section.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.8-2
- gconfmm26-devel added to buildrequirements.

* Fri Jul 09 2004 Dag Wieers <dag@wieers.com> - 0.8-1
- Updated to release 0.8.

* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 0.7-1
- Updated to release 0.7.

* Sun Dec 07 2003 Dag Wieers <dag@wieers.com> - 0.6-0
- Updated to release 0.6.

* Sun Nov 02 2003 Dag Wieers <dag@wieers.com> - 0.5-0
- Updated to release 0.5.

* Thu Jun 05 2003 Dag Wieers <dag@wieers.com> - 0.4-1
- Added docs.

* Thu Apr 03 2003 Dag Wieers <dag@wieers.com> - 0.4-0
- Initial package. (using DAR)
