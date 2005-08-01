# $Id$
# Authority: dag
# Upstream: Lars Lindner <llando$gmx,de>
# Upstream: Nathan J. Conrad <t98502$users,sourceforge,net>

%define desktop_vendor rpmforge

Summary: RSS/RDF feed reader
Name: liferea
Version: 0.9.5
Release: 1
License: GPL
Group: Applications/Internet
URL: http://liferea.sourceforge.net/

Source: http://dl.sf.net/liferea/liferea-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: GConf2-devel >= 2.2, gtkhtml2-devel, libxml2-devel >= 2.5.10
BuildRequires: gettext, gcc-c++, desktop-file-utils, gtk2 >= 2.4
Requires: GConf2

%description
Liferea (Linux Feed Reader) is an RSS/RDF feed reader. 
It's intended to be a clone of the Windows-only FeedReader. 
It can be used to maintain a list of subscribed feeds, 
browse through their items, and show their contents 
using GtkHTML.

%prep
%setup -n liferea-%{version}

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

desktop-file-install \
	--delete-original                          \
	--vendor %{desktop_vendor}                 \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/liferea.desktop

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null || :

%postun
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/liferea.1*
%config %{_sysconfdir}/gconf/schemas/liferea.schemas
%{_bindir}/liferea*
%{_datadir}/applications/%{desktop_vendor}-liferea.desktop
%{_datadir}/liferea/
%{_datadir}/pixmaps/liferea.png
%dir %{_libdir}/liferea/
%exclude %{_libdir}/liferea/*.la
%{_libdir}/liferea/*.so*

%changelog
* Sun Jul 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.5-1
- Updated to release 0.9.5.

* Sat Jul 23 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.4-1
- Updated to release 0.9.4.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Mon May 16 2005 Dag Wieers <dag@wieers.com> - 0.9.2-1
- Updated to release 0.9.2.

* Sun Mar 13 2005 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Wed Jan 19 2005 Dag Wieers <dag@wieers.com> - 0.9.0-2.b
- Updated to release 0.9.0b.

* Sat Jan 15 2005 Dag Wieers <dag@wieers.com> - 0.9.0-1
- Updated to release 0.9.0.

* Tue Nov 30 2004 Dag Wieers <dag@wieers.com> - 0.6.4-1
- Updated to release 0.6.4.

* Fri Nov 26 2004 Dag Wieers <dag@wieers.com> - 0.6.3-1
- Updated to release 0.6.3.

* Mon Nov 01 2004 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Updated to release 0.6.1.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Updated to release 0.6.0.

* Tue Aug 31 2004 Dag Wieers <dag@wieers.com> - 0.5.3-2.c
- Updated to release 0.5.3c.

* Tue Aug 24 2004 Dag Wieers <dag@wieers.com> - 0.5.3-2.b
- Updated to release 0.5.3b.

* Wed Aug 18 2004 Dag Wieers <dag@wieers.com> - 0.5.3-1
- Updated to release 0.5.3.

* Mon Aug 02 2004 Dag Wieers <dag@wieers.com> - 0.5.2-0.c
- Updated to release 0.5.2c.

* Sun Jul 24 2004 Dag Wieers <dag@wieers.com> - 0.5.2-0.b
- Updated to release 0.5.2b.

* Thu Jul 01 2004 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Updated to release 0.5.1.

* Sun Jun 20 2004 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Updated to release 0.5.0.

* Sun May 23 2004 Dag Wieers <dag@wieers.com> - 0.4.9-1
- Updated to release 0.4.9.

* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 0.4.8-2
- Added patch for building on RH90 and RHEL3. (Nathan Conrad)

* Fri May 07 2004 Dag Wieers <dag@wieers.com> - 0.4.8-1
- Initial package. (using DAR)
