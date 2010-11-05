# $Id$
# Authority: shuff
# Upstream: Eddie Kohler <ekohler$gmail,com>

Summary: Utilities for Type 1 fonts
Name: t1utils
Version: 1.36
Release: 1%{?dist}
License: Freeware
Group: Applications/Publishing
URL: http://www.lcdf.org/~eddietwo/type/#t1utils

Source: http://www.lcdf.org/~eddietwo/type/t1utils-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: rpm-macros-rpmforge

%description
Six free UNIX/Windows command-line tools for dealing with Type 1 fonts. This is
a revision of I. Lee Hetherington’s beloved t1utils package. t1ascii changes
PFB (binary) fonts into PFA (ASCII) format; t1binary goes the opposite
direction. t1disasm translates PFBs or PFAs into a human-readable and -editable
format; t1asm goes the opposite direction. Finally, t1unmac (formerly unpost)
translates a Macintosh Type 1 font into either PFB or PFA format, and t1mac
goes the opposite direction.

%prep
%setup

%build
%configure \
    --disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Fri Nov 05 2010 Steve Huff <shuff@vecna.org> - 1.36-1
- Initial package.
