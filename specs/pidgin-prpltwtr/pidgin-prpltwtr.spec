# $Id$
# Authority: shuff
# Upstream: Tan Miaoqing <rabbitrun84$gmail,com>

%define real_name prpltwtr

Summary: libpurple plugin (Pidgin Instant Messenger) for Twitter
Name: pidgin-prpltwtr
Version: 0.5.2
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://code.google.com/p/prpltwtr

Source: http://prpltwtr.googlecode.com/files/prpltwtr-%{version}.tar.gz
Patch0: pidgin-prpltwtr_destdir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: libpurple-devel >= 2
BuildRequires: make
BuildRequires: pkgconfig
Requires: pidgin > 2
Provides: prpltwtr = %{version}-%{release}

%description
This is a libpurple (Pidgin, Finch, Empathy* etc) plugin which treats
microblogging (Twitter, identi.ca, status.net, etc) as IM protocols. 

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

# fix libdir for 64-bitness
%{__perl} -pi -e 's|/lib|/%{_lib}|;' global.mak Makefile gtkprpltwtr/Makefile

%build
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_datadir}/osso-rtcom/twitter.profile
%{_datadir}/pixmaps/pidgin/protocols/*/*.png
%{_iconsbasedir}/*/hildon/*.png
%dir %{_libdir}/purple-2/
%{_libdir}/purple-2/*.so

%changelog
* Mon Nov 01 2010 Steve Huff <shuff@vecna.org> - 0.5.2-1
- Initial package.
