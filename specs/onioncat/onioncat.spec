# $Id$
# Authority: shuff
# Upstream: bf$abenteuerland,at

# onioncat versions look like 0.2.2.r549
%define vtag 0.2.2
%define rtag_base 549
%define rtag .r%{rtag_base}

Summary: Transparently route IP packets over the Tor network
Name: onioncat
Version: %{vtag}.%{rtag_base}
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.cypherpunk.at/onioncat/

Source: http://www.cypherpunk.at/ocat/download/Source/%{vtag}/onioncat-%{vtag}%{rtag}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: rpm-macros-rpmforge
Requires: tor

%description
OnionCat creates a transparent IP layer on top of Tor's hidden services. It
transmits any kind of IP-based data transparently through the Tor network on a
location hidden basis.

You can think of it as a point-to-multipoint VPN between hidden services. 

%prep
%setup -n %{name}-%{vtag}%{rtag}

%build
%configure \
    --disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# fix gcat
pushd %{buildroot}%{_bindir}
%{__rm} -f gcat
%{__ln_s} ocat gcat
popd

# fix the docs
%{__mv} %{buildroot}%{_docdir}/onioncat/* .
%{__rm} -rf %{buildroot}%{_docdir}/onioncat/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING Garlicat-HOWTO INSTALL NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Mon Dec 20 2010 Steve Huff <shuff@vecna.org> - 0.2.2.549-1
- Initial package.
