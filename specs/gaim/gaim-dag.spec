# $Id$
# Authority: matthias

Summary: multiprotocol instant messaging client
Name: gaim
Version: 0.69
Release: 0%{?dist}
Epoch: 1
License: GPL
Group: Applications/Internet
URL: http://gaim.sourceforge.net/

Source: http://dl.sf.net/gaim/gaim-%{version}.tar.bz2
Patch0: gaim-prefs.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2 >= 2.0, gtkspell-devel, libao-devel
BuildRequires: mozilla-nss, mozilla-nss-devel

%description
Gaim allows you to talk to anyone using a variety of messaging
protocols, including AIM (Oscar and TOC), ICQ, IRC, Yahoo!,
MSN Messenger, Jabber, Gadu-Gadu, Napster, and Zephyr.  These
protocols are implemented using a modular, easy to use design.
To use a protocol, just load the plugin for it.

%prep
%setup
%patch0 -p1 -b .prefs

%{__cat} <<EOF >gaim.desktop
[Desktop Entry]
Name=Gaim Instant Messenger
Comment=Multi-protocol instant messaging client.
Icon=gaim.png
Exec=gaim
Terminal=false
Type=Application
Categories=Application;Network;X-Red-Hat-Base
EOF

%build
%configure \
	--disable-perl
#	--with-perl-lib="%{buildroot}%{_libdir}/perl5/site_perl"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la \
		%{buildroot}%{_libdir}/gaim/*.la
#		%{buildroot}%{_libdir}/perl5/site_perl/*/perllocal.pod \
#		%{buildroot}%{_libdir}/perl5/site_perl/*/auto/Gaim/autosplit.ix \
#		%{buildroot}%{_libdir}/perl5/site_perl/*/auto/Gaim/.packlist

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/CREDITS doc/FAQ doc/PERL_HOWTO.dox NEWS README
%doc doc/gaims_funniest_home_convos.txt doc/the_penguin.txt
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_includedir}/gaim-remote/
%{_libdir}/libgaim-*
%{_libdir}/gaim/
%{_datadir}/applications/*
%{_datadir}/pixmaps/gaim.png
%{_datadir}/pixmaps/gaim/
%{_datadir}/sounds/gaim/
#{_libdir}/perl5/site_perl/

%changelog
* Thu Apr 10 2003 Dag Wieers <dag@wieers.com> - 0.69-0
- Updated to release 0.69.
- Resync with Matthias Saou (FreshRPMS).

* Wed Apr 09 2003 Dag Wieers <dag@wieers.com> - 0.61-0
- Updated to release 0.61.

* Sun Apr 06 2003 Dag Wieers <dag@wieers.com> - 0.60-0
- Initial package. (using DAR)
