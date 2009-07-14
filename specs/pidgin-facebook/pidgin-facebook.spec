# $Id$
# Authority: dag

%define real_name pidgin-facebookchat

Summary: Facebook chat plugin for Pidgin Instant Messenger
Name: pidgin-facebook
Version: 1.50
Release: 1
License: GPL
Group: Applications/Internet
URL: http://code.google.com/p/pidgin-facebookchat

Source0: http://pidgin-facebookchat.googlecode.com/files/pidgin-facebookchat-source-%{version}.tar.bz2
Source1: http://pidgin-facebookchat.googlecode.com/files/facebook_icons.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpurple-devel
Requires: pidgin
Obsoletes: pidgin-facebookchat <= %{version}-%{release}
Provides: pidgin-facebookchat = %{version}-%{release}

%description
pidgin-facebook is a Facebook chat plugin for Pidgin and libpurple messengers.
It connects to the new Facebook Chat IM service without the need for an API
key.

%prep
%setup -n %{real_name}

%build
%{__cc} %{optflags} -shared $(pkg-config --cflags purple) -fPIC -DPURPLE_PLUGINS *.c -o libfacebook.so

%install
%{__rm} -rf %{buildroot}
#{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 libfacebook.so %{buildroot}%{_libdir}/purple-2/libfacebook.so
%{__install} -Dp -m0644 facebook16.png %{buildroot}%{_datadir}/pidgin/protocols/16/facebook.png
%{__install} -Dp -m0644 facebook22.png %{buildroot}%{_datadir}/pidgin/protocols/22/facebook.png
%{__install} -Dp -m0644 facebook48.png %{buildroot}%{_datadir}/pidgin/protocols/48/facebook.png

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING
%{_datadir}/pidgin/protocols/*/facebook.png
%dir %{_libdir}/purple-2/
%{_libdir}/purple-2/libfacebook.so

%changelog
* Tue Jul 14 2009 Dag Wieers <dag@wieers.com> - 1.50-1
- Initial package. (using DAR)
