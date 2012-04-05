# $Id$
# Authority: shuff
# Upstream: http://swish-e.org/discuss.html

Summary: Simple Web Indexing for Humans - Enhanced
Name: swish-e
Version: 2.4.7
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://swish-e.org/

Source: http://swish-e.org/distribution/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: libxml2-devel
BuildRequires: make
BuildRequires: pcre-devel
BuildRequires: zlib-devel
BuildRequires: rpm-macros-rpmforge
Requires: catdoc
Requires: perl(HTML::Parser)
Requires: perl(HTML::Entities)
Requires: perl(HTML::FillInForm)
Requires: perl(HTML::Tagset)
Requires: perl(HTML::Template)
Requires: perl(LWP)
Requires: perl(MIME::Types)
Requires: perl(MP3::Tag)
Requires: perl(Spreadsheet::ParseExcel)
Requires: perl(Template)
Requires: perl(URI)
Requires: vixie-cron
Requires: xpdf

# filter some bogus autoreq/prov
%filter_from_requires /^perl(SWISH.*)/d
%filter_from_provides /^perl/d

# don't scan the examples for autoreq/prov
%filter_requires_in %{_docdir}
%filter_provides_in %{_docdir}

%filter_setup

%description
Swish-e is a fast, flexible, and free open source system for indexing
collections of Web pages or other files. Swish-e is ideally suited for
collections of a million documents or smaller. Using the GNOME libxml2 parser
and a collection of filters, Swish-e can index plain text, e-mail, PDF, HTML,
XML, Microsoft Word/PowerPoint/Excel, and just about any file that can be
converted to XML or HTML text.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.


%prep
%setup

%build
%configure \
    --disable-dependency-tracking \
    --disable-static \
    --with-pcre
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# let rpm handle the docs
%{__rm} -rf %{buildroot}%{_docdir}/swish-e/

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL README* TODO example/ html/ pod/
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/swish-e/
%{_datadir}/swish-e/

%files devel
%doc src/libtest.c
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Tue Feb 21 2012 Steve Huff <shuff@vecna.org> - 2.4.7-1
- Initial package.
