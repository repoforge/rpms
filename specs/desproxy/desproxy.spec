# $Id$

# Authority: dag

# Upstream: Miguelanxo Otero Salgueiro <miguelanxotero@hotmail.com>

%define rversion 0.1.0-pre2

Summary: A TCP tunnel for HTTP proxies.
Name: desproxy
Version: 0.1.0
Release: 0.pre2
License: GPL
Group: Applications/Internet
URL: http://desproxy.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/desproxy/%{name}-%{rversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
desproxy allows you to establish TCP connections through HTTP proxies.

With desproxy you can use every application you got used to work with:
your favourite browser (MSIE, Mozilla...), your mailer (Outlook Express,
Pine, Mutt, Eudora), your news reader (Netscape News...)... without
having to worry whether they have HTTP support or not.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{rversion}

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e 's|^localedir = \@prefix\@/share/locale$|datadir = \@datadir\@\nlocaledir = \$(datadir)/locale|' Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
### FIXME: Makefile doesn't create target directories (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_bindir}
#makeinstall
%{__install} -m0755 src/desproxy src/desproxy-inetd src/desproxy-dns %{buildroot}%{_bindir}
%{__install} -m0755 src/desproxy-socksserver src/socket2socket %{buildroot}%{_bindir}


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Changes COPYING doc/*.html
%{_bindir}/*

%changelog
* Wed Sep 24 2003 Dag Wieers <dag@wieers.com> - 0.1.0-0.pre2
- Initial package. (using DAR)
