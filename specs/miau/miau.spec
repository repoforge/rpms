# $Id: _template.spec 219 2004-04-09 06:21:45Z dag $
# Authority: dag
# Upstream: Tommi Saviranta <tsaviran@users.sf.net>

Summary: Full featured IRC bouncer
Name: miau
Version: 0.5.3
Release: 1
License: GPL
Group: Applications/Internet
URL: http://miau.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

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
	--disable-dependency-tracking
	"
%configure \
	--enable-ipv6 \
	$OPTIONS
%{__make} %{?_smp_mflags}
%{__mv} -f src/miau src/miau-ipv6

%configure \
	$OPTIONS
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -D -m0755 src/miau-ipv6 %{buildroot}%{_bindir}/miau-ipv6

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

%preun
/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO misc/miaurc
%doc %{_infodir}/*.info*
%{_bindir}/*
%exclude %{_datadir}/miaurc

%changelog
* Mon Mar 03 2004 Dag Wieers <dag@wieers.com> - 0.5.3-1
- Initial package. (using DAR)
