# $Id$
# Authority: dries
# Upstream: <pcoupard$easyconnect,fr>

# Screenshot: http://webperso.easyconnect.fr/om.the/web/cwirc/images/screenshot.jpg

Summary: Plugin for x-chat for transmitting raw morse code
Name: cwirc
Version: 2.0.0
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://users.skynet.be/ppc/cwirc/

Source: http://users.skynet.be/ppc/cwirc/download/cwirc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel

%description
CWirc is a plugin for the X-Chat IRC client to transmit raw morse code over
the internet using IRC servers as reflectors. The transmitted morse code can
be received in near real-time by other X-Chat clients with the CWirc plugin.
CWirc tries to emulate a standard amateur radio rig : it sends and receives
morse over virtual channels, and it can listen to multiple senders
transmitting on the same channel. Morse code is keyed locally using a
straight or iambic key connected to a serial port, or using the mouse
buttons, and the sound is played through the soundcard, or through an
external sounder.

Note that CWirc doesn't do any morse decoding : it simply transmits and
receives morse code timing events. A standard IRC user on the same IRC
channel you're transmitting morse on will only see coded lines when morse
code is transmitted. Only other CWirc users can receive what you send.

%prep
%setup

%build
%{__make} %{?_smp_mflags} \
	TARGET_OS="LINUX" \
	CFLAGS="%{optflags} -DLINUX -fPIC" \
	PLUGIN_INSTALL_DIRECTORY="%{_libdir}/xchat/plugins" \
	FRONTEND_INSTALL_DIRECTORY="%{_bindir}" \
	CWIRC_EXTENSIONS_DIRECTORY="%{_libdir}/cwirc/extensions" \
	EXTRA_LDFLAGS=""

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	TARGET_OS="LINUX" \
	PLUGIN_INSTALL_DIRECTORY="%{buildroot}%{_libdir}/xchat/plugins" \
	FRONTEND_INSTALL_DIRECTORY="%{buildroot}%{_bindir}" \
	CWIRC_EXTENSIONS_DIRECTORY="%{buildroot}%{_libdir}/cwirc/extensions" \
	EXTRA_LDFLAGS=

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/*
%{_libdir}/xchat/plugins/cwirc.so

%changelog
* Sat May 21 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.0-1
- Update to release 2.0.0.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.8.8-1.2
- Rebuild for Fedora Core 5.

* Thu Jun 09 2005 Dries Verachtert <dries@ulyssis.org> - 1.8.8-1
- Update to release 1.8.8.

* Wed Jul 28 2004 Dries Verachtert <dries@ulyssis.org> - 1.8.7-1
- Update to version 1.8.7.

* Wed Jul 21 2004 Dries Verachtert <dries@ulyssis.org> - 1.8.6-1
- Update to version 1.8.6.

* Sun Jun 21 2004 Dries Verachtert <dries@ulyssis.org> - 1.8.4-1
- Update to version 1.8.4.

* Sun Jun 20 2004 Dag Wieers <dag@wieers.com> - 1.8.3-1
- Fixes for x86_64.

* Sat Jun 19 2004 Dries Verachtert <dries@ulyssis.org> 1.8.3-1
- Update to version 1.8.3.

* Sun May 2 2004 Dries Verachtert <dries@ulyssis.org> 1.8.1-1
- Initial package.
