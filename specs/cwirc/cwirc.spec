# $Id: $

# Authority: dries
# Upstream: 

Summary: Plugin for x-chat for transmitting raw morse code
Name: cwirc
Version: 1.8.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://webperso.easyconnect.fr/om.the/web/cwirc/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://webperso.easyconnect.fr/om.the/web/cwirc/download/cwirc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel

# Screenshot: http://webperso.easyconnect.fr/om.the/web/cwirc/images/screenshot.jpg

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
	TARGET_OS=LINUX \
	PLUGIN_INSTALL_DIRECTORY=/usr/lib/xchat/plugins \
	FRONTEND_INSTALL_DIRECTORY=/usr/bin \
	CWIRC_EXTENSIONS_DIRECTORY=/usr/lib/cwirc/extensions \
	EXTRA_LDFLAGS=

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	TARGET_OS=LINUX \
	PLUGIN_INSTALL_DIRECTORY=%{buildroot}/usr/lib/xchat/plugins \
	FRONTEND_INSTALL_DIRECTORY=%{buildroot}/usr/bin \
	CWIRC_EXTENSIONS_DIRECTORY=%{buildroot}/usr/lib/cwirc/extensions \
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
* Sun May 2 2004 Dries Verachtert <dries@ulyssis.org> 1.8.1-1 
- Initial package.
