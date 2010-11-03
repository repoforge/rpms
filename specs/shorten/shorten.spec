# $Id$
# Authority: dag

Summary: Low complexity and fast waveform coder
Name: shorten
Version: 3.6.1
Release: 1%{?dist}
License: Distributable
Group: Applications/Multimedia
URL: http://www.etree.org/shnutils/shorten/

Source: http://etree.org/shnutils/shorten/dist/src/shorten-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gawk
BuildRequires: gcc
BuildRequires: make
BuildRequires: rpm-macros-rpmforge

Conflicts: perl-WWW-Shorten

%description
shorten is a low complexity and fast waveform coder (i.e. audio
compressor), originally written by Tony Robinson at SoftSound. It can
operate in both lossy and lossless modes.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/LICENSE doc/TODO doc/tr156.ps NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/shorten

%changelog
* Wed Nov 03 2010 Steve Huff <shuff@vecna.org> - 3.6.1-1
- Updated to version 3.6.1.
- Updated source location.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.6.0-1.2
- Rebuild for Fedora Core 5.

* Wed Jul 14 2004 Dag Wieers <dag@wieers.com> - 3.6.0-1
- Initial package. (using DAR)
