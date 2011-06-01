# $Id$
# Authority: shuff
# Upstream: Danny Sadinoff <hebcal$sadinoff,com>

%define default_city New York

Summary: perpetual Jewish calendar
Name: hebcal
Version: 3.9.1
Release: 1%{?dist}
License: GPL
Group: Applications/Utilities
URL: http://danny.sadinoff.com/hebcal/

Source: https://downloads.sourceforge.net/project/hebcal/hebcal-c/%{version}/hebcal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# Buildarch: noarch
BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: rpm-macros-rpmforge
Requires: info

%description
Hebcal is a perpetual Jewish calendar program, implemented in C. The key
routines are translations of Dershowitz & Reingold's lisp code in GNU-Emacs 18.
Hebcal offers several convenience routines that make it a good fit for
generating calendars for PDAs and personal calendars.

Hebcal has been successfully ported to Perl, C, and Javascript, but I'm
currently only maintaining the C implementation. 

%prep
%setup

%build
%configure \
    --disable-dependency-tracking \
    --with-default-city="%{default_city}"

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING HACKING INSTALL NEWS OLD_NEWS README TODO
%doc %{_mandir}/man?/*
%doc %{_infodir}/*.info.gz
%{_bindir}/*
%exclude %{_infodir}/dir

%changelog
* Wed Jun 01 2011 Steve Huff <shuff@vecna.org> - 3.9.1-1
- Initial package.
