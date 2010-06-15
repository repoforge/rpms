# $Id$
# Authority: shuff
# Upstream: Enrico Troeger <enrico,troeger$uvena,de>

# update this when a new minor version of Geany comes out
%define geany_basever 0.19

Summary: Collection of plugins for Geany
Name: geany-plugins
Version: 0.19
Release: 1%{?dist}
License: GPL
Group: Applications/Editors
URL: http://plugins.geany.org

Source: http://plugins.geany.org/geany-plugins/geany-plugins-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf, automake
BuildRequires: gcc-c++
# BuildRequires: enchant-devel
# BuildRequires: lua-devel
BuildRequires: geany-devel >= %{geany_basever}
BuildRequires: gettext
BuildRequires: gtk2-devel >= 2.8.0
BuildRequires: gtkspell-devel >= 2.0
BuildRequires: perl(XML::Parser)
BuildRequires: pkgconfig

Requires: geany >= %{geany_basever}

%description
This package is a combined release of the following plugins:

* Addons
* Geanygdb
* Geanylatex
* Geanylipsum
* Geanylua
* Geanysendmail
* Geanyvc
* Shiftcolumn
* Spellcheck

%prep
%setup

%build
export LUA_CFLAGS="-I%{_includedir}" 
export LUA_LIBS="-L%{_libdir}" 
%configure --disable-dependency-tracking \
    --disable-spellcheck \
    --disable-geanylua
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

# put the docs in the right place
%{__mv} %{buildroot}%{_docdir}/geany-plugins geany-plugins-doc

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc NEWS README README.waf
%doc geany-plugins-doc/*
%dir %{_libexecdir}/geany-plugins/
%{_libexecdir}/geany-plugins/*
# %{_libdir}/geany-plugins/*
%{_libdir}/geany/*.so
# %{_datadir}/geany-plugins/*
%{_datadir}/locale/*/LC_MESSAGES/*
%exclude %{_libdir}/geany/*.la
# %exclude %{_libdir}/geany-plugins/*/*.la

%changelog
* Tue Jun 15 2010 Steve Huff <shuff@vecna.org> - 0.19-1
- Updated to version 0.19.

* Thu Mar 18 2010 Steve Huff <shuff@vecna.org> - 0.18-1
- Initial package.
