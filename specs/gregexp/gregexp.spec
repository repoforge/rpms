# $Id$
# Authority: dag
# Upstream: Jens Reimann <ctron$dentrassi,de>

Summary: Graphical regular expression explorer
Name: gregexp
Version: 0.3
Release: 1.2%{?dist}
License: GPL
Group: Development/Tools
URL: http://dentrassi.de/download/gregexp

Source: http://dentrassi.de/download/gregexp/0.3/gregexp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: intltool, pcre-devel, gtk2-devel >= 2.0.0, libglade2-devel >= 2.0.0
BuildRequires: libgnomeui-devel, desktop-file-utils

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
%doc AUTHORS COPYING INSTALL README TODO
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/gregexp/glade/*.glade
%{_datadir}/pixmaps/*.png

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1.2
- Rebuild for Fedora Core 5.

* Fri Apr 23 2004 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
