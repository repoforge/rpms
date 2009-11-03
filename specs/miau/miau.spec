# $Id$
# Authority: dag
# Upstream: Tommi Saviranta <tsaviran$users,sf,net>

Summary: Full featured IRC bouncer
Name: miau
Version: 0.6.4
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://miau.sourceforge.net/

Source: http://dl.sf.net/miau/miau-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
miau is a smart and versatile irc-bouncing tool for unix. The difference
between miau and other bouncers is that miau will go on irc as soon as
it is launched, guarding or attempting to get your nick. Control over the
session can be taken as with other bouncers, by simply connecting to miau
(and providing a password) like you would connect to a normal irc-server.
On disconnect, miau is able to stay in the channels and to reintroduce
them to your client on your next connect. Other handy features are
message-logging, flood-protection, dcc-bouncing, etc.

%prep
%setup

%build
export OPTIONS="
	--enable-local
	--enable-dccbounce
	--enable-automode
	--enable-releasenick
	--enable-ctcp-replies
	--enable-mkpasswd
	--enable-uptime
	--enable-chanlog
	--enable-privlog
	--enable-onconnect
	--enable-empty-awaymsg
	"
%configure \
	--enable-ipv6 \
	$OPTIONS
%{__make} %{?_smp_mflags}
%{__mv} -f src/miau src/miau-ipv6

%{__make} clean
%configure \
	$OPTIONS
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0755 src/miau-ipv6 %{buildroot}%{_bindir}/miau-ipv6
%{__rm} -f %{buildroot}%{_infodir}/dir

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

%preun
/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL misc/miaurc NEWS README TODO
%doc %{_infodir}/*.info*
%doc %{_mandir}/man1/miau.1*
%{_bindir}/miau*
%exclude %{_datadir}/miaurc

%changelog
* Sun Apr 15 2007 Dag Wieers <dag@wieers.com> - 0.6.4-1
- Updated to release 0.6.4.

* Thu Jan 18 2007 Dag Wieers <dag@wieers.com> - 0.6.3-1
- Updated to release 0.6.3.

* Thu Jul 27 2006 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Updated to release 0.6.2.

* Wed May 17 2006 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Updated to release 0.6.1.

* Sun Jan 01 2006 Dag Wieers <dag@wieers.com> - 0.6.0.2-1
- Updated to release 0.6.0.2.

* Thu Dec 29 2005 Dag Wieers <dag@wieers.com> - 0.6.0.1-1
- Updated to release 0.6.0.1.

* Sun Dec 25 2005 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Updated to release 0.6.0.

* Sat May 21 2005 Dag Wieers <dag@wieers.com> - 0.5.4-1
- Updated to release 0.5.4.

* Mon Nov 15 2004 Dag Wieers <dag@wieers.com> - 0.5.3-2
- Fixed the non-ipv6 build by doing make clean. (Chris Grau)

* Mon Mar 03 2004 Dag Wieers <dag@wieers.com> - 0.5.3-1
- Initial package. (using DAR)
