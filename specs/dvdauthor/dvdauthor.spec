# $Id$
# Authority: dag
# Upstream: <dvdauthor-developer$lists,sf,net>

Summary: Set of tools to author a DVD
Name: dvdauthor
Version: 0.6.10
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://dvdauthor.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/dvdauthor/dvdauthor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libxml2-devel >= 2.5.0
#BuildRequires: ImageMagick-devel >= 5.5.7

%description
dvdauthor is a program that will generate a DVD movie from a valid
mpeg2 stream that should play when you put it in a DVD player.

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
%doc COPYING HISTORY README TODO menu.txt doc/*.html doc/*.sgml doc/*.dsl
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 0.6.10-1
- Updated to release 0.6.10.

* Tue Jan 06 2004 Dag Wieers <dag@wieers.com> - 0.6.8-0
- Initial package. (using DAR)
