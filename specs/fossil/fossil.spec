# $Id$
# Authority: shuff
# Upstream: D. Richard Hipp <drh$hwaci,com>

%define datestamp 20110901182519

Summary: Distributed version control with integrated wiki
Name: fossil
Version: 1.19
Release: 1%{?dist}
License: BSD
Group: Development/Tools
URL: http://www.fossil-scm.org.

Source: http://www.fossil-scm.org/download/fossil-src-%{datestamp}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: zlib-devel
BuildRequires: rpm-macros-rpmforge

%description
Features provided by fossil that one does not get with other DVCSes include:

* Integrated wiki.
* Integrated bug tracking
* Immutable artifacts
* Simple, well-defined, enduring file format
* Integrated web interface

%prep
%setup -n %{name}-src-%{datestamp}

%build
CFLAGS="%{optflags} -DFOSSIL_ENABLE_SSL"
%{__make} -f Makefile.classic %{?_smp_mflags} BCC="gcc $CFLAGS" TCC="gcc $CFLAGS"

%install
%{__rm} -rf %{buildroot}
%{__install} -m755 -d %{buildroot}%{_bindir}
%{__install} -m755 fossil %{buildroot}%{_bindir}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc VERSION *.txt
%{_bindir}/*

%changelog
* Fri Sep 16 2011 Steve Huff <shuff@vecna.org> - 1.19-1
- Initial package.
