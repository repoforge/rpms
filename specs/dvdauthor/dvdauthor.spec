# $Id$
# Authority: dag
# Upstream: <dvdauthor-developer$lists,sf,net>

Summary: Set of tools to author a DVD
Name: dvdauthor
Version: 0.6.10
Release: 2
License: GPL
Group: Applications/Multimedia
URL: http://dvdauthor.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/dvdauthor/dvdauthor-%{version}.tar.gz
Patch0: dvdauthor-0.6.10-gcc34.patch
Patch1: dvdauthor-0.6.10-readxml.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libxml2-devel >= 2.5.0, libdvdread-devel
BuildRequires: libpng-devel
#BuildRequires: ImageMagick-devel >= 5.5.7

%description
dvdauthor is a program that will generate a DVD movie from a valid
mpeg2 stream that should play when you put it in a DVD player.

%prep 
%setup
%patch0
%patch1

%{__perl} -pi.orig -e 's|(-ldvdread)|$1 -ldl|g' configure

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
%doc COPYING HISTORY README TODO menu.txt doc/*.html doc/*.sgml doc/*.dsl
%doc %{_mandir}/man1/*
%{_bindir}/*

%changelog
* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 0.6.10-2
- Added readxml patch. (John Veysey)

* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 0.6.10-1
- Updated to release 0.6.10.

* Tue Jan 06 2004 Dag Wieers <dag@wieers.com> - 0.6.8-0
- Initial package. (using DAR)
