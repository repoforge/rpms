# $Id$
# Authority: dag
# Upstream: Lars Lindner <llando$gmx,de>
# Upstream: Nathan J. Conrad <t98502$users,sourceforge,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag: %define _without_mozilla 1}
%{?fc6: %define _without_mozilla 1}
%{?fc5: %define _without_mozilla 1}
%{?fc1: %define _without_mozilla 1}

%{!?dtag: %define with_dbus 1}
%{?el5: %define with_dbus 1}
%{?fc6: %define with_dbus 1}

%define mozilla xulrunner-devel nspr-devel
%{?el5:%define mozilla xulrunner-devel nspr-devel}
%{?el4:%define mozilla seamonkey-devel}
%{?el3:%define mozilla seamonkey-devel}
%{?rh9:%define mozilla mozilla-devel}
%{?rh7:%define mozilla mozilla-devel}
%{?el2:%define mozilla seamonkey-devel}

%define desktop_vendor rpmforge

Summary: RSS/RDF feed reader
Name: liferea
Version: 1.2.23
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://liferea.sourceforge.net/

Source: http://dl.sf.net/liferea/liferea-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, gcc-c++, desktop-file-utils
BuildRequires: gtk2 >= 2.4, GConf2-devel >= 2.2, gtkhtml2-devel
BuildRequires: libxml2-devel >= 2.6.27, libxslt >= 1.1.19
%{!?_without_mozilla:BuildRequires: %{mozilla}}
Requires: GConf2

%description
Liferea (Linux Feed Reader) is an RSS/RDF feed reader.
It's intended to be a clone of the Windows-only FeedReader.
It can be used to maintain a list of subscribed feeds,
browse through their items, and show their contents
using GtkHTML.

%prep
%setup

%build
%configure \
    --disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

desktop-file-install --delete-original         \
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
%doc %{_mandir}/pl/man1/liferea.1*
%config %{_sysconfdir}/gconf/schemas/liferea.schemas
%{_bindir}/liferea*
%{_datadir}/applications/%{desktop_vendor}-liferea.desktop
%{_datadir}/liferea/
%{_datadir}/icons/*/*/apps/liferea.png
%dir %{_libdir}/liferea/
%{_libdir}/liferea/*.so*
%exclude %{_libdir}/liferea/*.la

%changelog
* Sun Oct 21 2007 Dag Wieers <dag@wieers.com> - 1.2.23-1
- Updated to release 1.2.23.

* Thu Jun 07 2007 Dag Wieers <dag@wieers.com> - 1.2.16b-1
- Updated to release 1.2.16b.

* Thu May 31 2007 Dag Wieers <dag@wieers.com> - 1.2.15b-1
- Updated to release 1.2.15b.

* Sun Mar 18 2007 Dag Wieers <dag@wieers.com> - 1.2.8-1
- Updated to release 1.2.8.

* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.0-1
- Updated to release 1.2.0.

* Sat Dec 09 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.27-1
- Updated to release 1.0.27.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.24-1
- Updated to release 1.0.24.

* Thu Aug 10 2006 Dag Wieers <dag@wieers.com> - 1.0.21-1
- Updated to release 1.0.21.

* Wed Aug 09 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.20-1
- Updated to release 1.0.20.

* Wed Aug 02 2006 Dag Wieers <dag@wieers.com> - 1.0.19-1
- Updated to release 1.0.19.

* Tue Jul 25 2006 Dag Wieers <dag@wieers.com> - 1.0.18-1
- Updated to release 1.0.18.

* Wed Jul 19 2006 Dag Wieers <dag@wieers.com> - 1.0.17-1
- Updated to release 1.0.17.

* Tue Jun 20 2006 Dag Wieers <dag@wieers.com> - 1.0.15-1
- Updated to release 1.0.15.

* Sun May 07 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.12-1
- Updated to release 1.0.12.

* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.10-1
- Updated to release 1.0.10.

* Sun Mar 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.8-1
- Updated to release 1.0.8.

* Tue Mar 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.7-1
- Updated to release 1.0.7.

* Fri Mar 03 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.5-1
- Updated to release 1.0.5.

* Sun Feb 12 2006 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Updated to release 1.0.4.

* Wed Feb 01 2006 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Updated to release 1.0.3.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.2-1
- Updated to release 1.0.2.

* Tue Jan 17 2006 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Sun Dec 25 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Updated to release 1.0.

* Wed Dec 08 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-0.rc4
- Updated to release 1.0-RC4.

* Mon Sep 05 2005 Dag Wieers <dag@wieers.com> - 0.9.7b-1
- Updated to release 0.9.7b.

* Sat Sep 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.7-1
- Updated to release 0.9.7.

* Thu Aug 18 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.6-1
- Updated to release 0.9.6.

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
