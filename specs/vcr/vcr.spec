# $Id$
# Authority: dag
# Upstream: Bram Avontuur <bram$avontuur,org>

Summary: Record a program using a video grabber card
Name: vcr
Version: 1.10
Release: 0.2%{?dist}
Group: Applications/Multimedia
License: GPL
URL: http://www.stack.nl/~brama/vcr/

Source: http://www.stack.nl/~brama/vcr/src/vcr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: avifile-devel
Requires: avifile

%description
VCR is a program which enables you to record a program using a video
grabber card that's supported by the video4linux drivers. It doesn't
require a graphical environment, and you can use all popupular windows
codecs (like DivX, Indeo Video 5, etc) because VCR is built around the
avifile library. Now, you can finally record your favourite program from a
remote place, because Murphy's law dictates that you remember to record it
when you're as far away from your home as possible...

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/vcr/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.10-0.2
- Rebuild for Fedora Core 5.

* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 1.10
- Updated to release 1.10.

* Sun Mar 16 2003 Dag Wieers <dag@wieers.com> - 1.09
- Added avifile0.7 patch to get it to build.

* Fri May 30 2002 Dag Wieers <dag@wieers.com> - 1.07
- Initial package.
