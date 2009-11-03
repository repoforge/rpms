# $Id$
# Authority: dag


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: Linux/UNIX tool suite for various mobile phones
Name: gnokii
Version: 0.6.22
Release: 1%{?dist}
License: GPL
Group: Applications/Communications
URL: http://gnokii.org/

Source: http://www.gnokii.org/download/gnokii/gnokii-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, flex, gtk+-devel >= 1.2.0, bluez-libs-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
BuildRequires: gcc-c++, gtk2-devel

%description
Gnokii is a Linux/UNIX tool suite and a modem/fax driver for
Nokia's mobile phones, released under the GPL.

%package gui
Summary: Graphical Linux/UNIX tool suite for Nokia mobile phones
Group: Applications/Internet
Obsoletes: gnokii-xgnokii, gnokii-gtk, xgnokii

%description gui
Xgnokii is a graphical Linux/UNIX tool suite for Nokia's mobile phones. It
allows you to edit your contacts book, send/read SMS's from/in your
computer and more.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

### FIXME: Fix broken configure with xgettext options (Please fix upstream)
%{__perl} -pi.orig -e 's| --msgid-bugs-address=||' configure
%{__perl} -pi.orig -e 's| --msgid-bugs-address=.+||' po/Makefile.in.in

%build
#./autogen.sh
%configure \
    --disable-static \
    --enable-nls \
    --enable-security \
    --with-gnu-ld \
    --with-x
%{__make} %{?_smp_mflags}
#%{__make} %{?_smp_mflags} -C smsd all libpq.so libmysql.so libfile.so

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%makeinstall
#makeinstall -C smsd
%find_lang %{name}

%{__install} -Dp -m0644 Docs/sample/gnokiirc %{buildroot}%{_sysconfdir}/gnokiirc

%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__install} -p -m0644 Docs/man/*.1 Docs/man/*.1x %{buildroot}%{_mandir}/man1/

%{__install} -d -m0755 %{buildroot}%{_mandir}/man8/
%{__install} -p -m0644 Docs/man/*.8 %{buildroot}%{_mandir}/man8/

%pre
/usr/sbin/groupadd -r -f gnokii &>/dev/null || :

%post -p /sbin/ldconfig

%postun
/sbin/ldconfig
/usr/sbin/groupdel gnokii &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING Docs/Bugs Docs/CREDITS Docs/DataCalls-QuickStart MAINTAINERS TODO
%doc Docs/FAQ Docs/README* Docs/gnokii-IrDA-Linux Docs/gnokii-ir-howto Docs/ringtones.txt
%doc Docs/protocol/ Docs/sample/ utils/gnapplet.sis
%doc %{_mandir}/man1/gnokii.1*
%doc %{_mandir}/man1/sendsms.1*
%doc %{_mandir}/man8/gnokiid.8*
%doc %{_mandir}/man8/mgnokiidev.8*
%config(noreplace) %{_sysconfdir}/gnokiirc
%{_bindir}/gnokii
%{_bindir}/sendsms
%{_libdir}/libgnokii.so.*
%{_sbindir}/gnokiid

%defattr(4750, root, gnokii, 0755)
%{_sbindir}/mgnokiidev
%exclude %{_docdir}/gnokii/gnapplet.sis

%files gui -f %{name}.lang
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/xgnokii.1x*
%{_bindir}/xgnokii
%{_datadir}/xgnokii/
%{_datadir}/applications/xgnokii.desktop

%files devel
%defattr(-, root, root, 0755)
#%{_includedir}/gnokii/
#%{_includedir}/gnokii.h
#%{_libdir}/pkgconfig/gnokii.pc
#%{_libdir}/pkgconfig/xgnokii.pc
#%{_libdir}/libgnokii.a
%exclude %{_libdir}/libgnokii.la
%{_libdir}/libgnokii.so

%changelog
* Sun Nov 25 2007 Dag Wieers <dag@wieers.com> - 0.6.22-1
- Updated to release 0.6.22.

* Sat Oct 06 2007 Dag Wieers <dag@wieers.com> - 0.6.19-1
- Updated to release 0.6.19.

* Sun Jun 24 2007 Dag Wieers <dag@wieers.com> - 0.6.17-1
- Updated to release 0.6.17.

* Wed May 09 2007 Dag Wieers <dag@wieers.com> - 0.6.15-1
- Updated to release 0.6.15.

* Tue Aug 29 2006 Dag Wieers <dag@wieers.com> - 0.6.14-1
- Updated to release 0.6.14.

* Mon Jun 19 2006 Dag Wieers <dag@wieers.com> - 0.6.13-1
- Updated to release 0.6.13.

* Sat Apr 15 2006 Dag Wieers <dag@wieers.com> - 0.6.12-1
- Updated to release 0.6.12.

* Tue Feb 28 2006 Dag Wieers <dag@wieers.com> - 0.6.11-1
- Updated to release 0.6.11.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.10-1
- Updated to release 0.6.10.

* Fri Jul 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.8-1
- Updated to release 0.6.8.

* Fri Jul 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.7-1
- Updated to release 0.6.7.

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 0.6.4-1
- Updated to release 0.6.4.

* Sun Jul 04 2004 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Updated to release 0.6.2.

* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Updated to release 0.6.1.

* Mon Feb 23 2004 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Updated to release 0.6.0.

* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 0.5.10-0
- Updated to release 0.5.10.

* Fri Jan 02 2004 Dag Wieers <dag@wieers.com> - 0.5.8-0
- Updated to release 0.5.8.

* Sun Dec 21 2003 Dag Wieers <dag@wieers.com> - 0.5.6-0
- Updated to release 0.5.6.

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 0.5.5-0
- Updated to release 0.5.5.

* Tue Sep 23 2003 Dag Wieers <dag@wieers.com> - 0.5.4-0
- Updated to release 0.5.4.

* Fri Jun 13 2003 Dag Wieers <dag@wieers.com> - 0.5.2-0
- Updated to release 0.5.2.

* Fri May 30 2003 Dag Wieers <dag@wieers.com> - 0.5.1-0
- Updated to release 0.5.1.

* Sat May 17 2003 Dag Wieers <dag@wieers.com> - 0.5.0-0
- Initial package. (using DAR)
