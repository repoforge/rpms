# $Id$
# Authority: dag
# Upstream: Jens Reimann <ctron$dentrassi,de>

Summary: Graphical regular expression explorer
Name: gregexp
Version: 0.3
Release: 1
License: GPL
Group: Development/Tools
URL: http://dentrassi.de/download/gregexp

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dentrassi.de/download/gregexp/0.3/gregexp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: intltool, pcre-devel, gtk2-devel >= 2.0.0, libglade2-devel >= 2.0.0

%description
A graphical regular expression explorer which uses PCRE as regular expression
engine. Therefore UTF-8 strings are supported out of the box.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor gnome --delete-original \
       --add-category X-Red-Hat-Base                  \
       --add-category Development                     \
       --dir %{buildroot}%{_datadir}/applications     \
       %{buildroot}%{_datadir}/applications/gregexp.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS TODO README COPYING INSTALL
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/gregexp/glade/*.glade
%{_datadir}/pixmaps/*.png

%changelog
* Fri Apr 23 2004 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
