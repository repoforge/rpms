# $Id$
# Authority: shuff
# Upstream: Andreas Krennmair <ak$newsbeuter,org>

Summary: The Mutt of news feed readers
Name: newsbeuter
Version: 2.4
Release: 1%{?dist}
License: MIT/X Consortium
Group: Applications/Text
URL: http://newsbeuter.org/

Source: http://newsbeuter.org/downloads/newsbeuter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc-c++, make
BuildRequires: curl-devel
BuildRequires: gettext-devel
BuildRequires: glibc-devel
BuildRequires: libstdc++-devel
BuildRequires: libxml2-devel
BuildRequires: pkgconfig
#BuildRequires: sqlite-devel >= 3.5
BuildRequires: sqlite-devel
BuildRequires: stfl-devel >= 0.21
BuildRequires: zlib-devel

%description
Newsbeuter is an open-source RSS/Atom feed reader for text terminals. It runs
on Linux, FreeBSD, Mac OS X and other Unix-like operating systems. Newsbeuter's
great configurability and vast number of features make it a perfect choice for
people that need a slick and fast feed reader that can be completely controlled
via keyboard.

A summary of some of its features:

* Subscribe to RSS 0.9x, 1.0, 2.0 and Atom feeds
* Download podcasts
* Freely configure your keyboard shortcuts
* Search through all downloaded articles
* Categorize and query your subscriptions with a flexible tag system
* Integrate any data source through a flexible filter and plugin system
* Automatically remove unwanted articles through a "killfile"
* Define "meta feeds" using a powerful query language
* Synchronize newsbeuter with your bloglines.com account
* Import and exporting your subscriptions with the widely used OPML format
* Freely define newsbeuter's look'n'feel through free color configurability and
  format strings

%prep
%setup

%build
CFLAGS="%{optflags}" %{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install prefix=%{_prefix} DESTDIR=%{buildroot}

# the RPM handles docfiles installation
%{__rm} -rf %{buildroot}%{_datadir}/doc/newsbeuter

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGES LICENSE README TODO
%doc doc/ contrib/
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/locale/*/LC_MESSAGES/*

%changelog
* Thu Mar 31 2011 Steve Huff <shuff@vecna.org> - 2.4-1
- Updated to versionm 2.4.

* Mon Sep 13 2010 Steve Huff <shuff@vecna.org> - 2.3-1
- Updated to version 2.3, removed newsbeuter-2.2_el5libcurl.patch 
  (in upstream now)
- Thanks to Philip Durbin for the patch!

* Fri May 28 2010 Steve Huff <shuff@vecna.org> - 2.2-1
- Initial package.
