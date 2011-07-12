# $Id$
# Authority: shuff
# Upstream: Andre Simon <andre.simon1$gmx,de>

Summary: Universal source code to formatted text converter
Name: highlight
Version: 3.5
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://www.andre-simon.de/

Source: http://www.andre-simon.de/zip/highlight-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc-c++
BuildRequires: lua-devel >= 5.1
BuildRequires: make
BuildRequires: qt-devel >= 4
BuildRequires: rpm-macros-rpmforge

# don't scan the examples for autoreq/prov
%filter_requires_in %{_docdir}
%filter_provides_in %{_docdir}

%filter_setup

%description
Highlight converts source code to formatted text with syntax highlighting.

* Coloured output in HTML, XHTML, RTF, TeX, LaTeX, SVG, BBCode and XML format
* Supports 160 programming languages
* Includes 80 color themes
* Recognizes nested languages
* Language definitions and themes are Lua scripts
* Plug-In interface to tweak syntax parsing and coloring

%package gui
Summary: Graphical tools for %{name}.
Group: Development/Tools
Requires: %{name} = %{version}-%{release}

%description gui
A graphical interface to the highlight tool.

%prep
%setup

%build
%{__make} %{?_smp_mflags} lib-shared
%{__make} %{?_smp_mflags} cli
%{__make} %{?_smp_mflags} gui QMAKE='qmake-qt4'

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__make} install-gui DESTDIR="%{buildroot}"

# we will handle the desktop file ourselves
%{__rm} -rf %{buildroot}%{_datadir}/applications/*.desktop
%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor net                  \
    --add-category X-Red-Hat-Base              \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop

# we will handle the docs ourselves
%{__rm} -rf %{buildroot}%{_datadir}/doc/highlight

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README* TODO examples/
%doc %{_mandir}/man?/*
%{_bindir}/highlight
%{_datadir}/highlight/langDefs/
%{_datadir}/highlight/plugins/
%{_datadir}/highlight/themes/
%config(noreplace) %{_sysconfdir}/highlight/*.conf

%files gui
%defattr(-, root, root, 0755)
%{_bindir}/highlight-gui
%{_datadir}/highlight/gui_files/
%{_datadir}/pixmaps/*.xpm
%{_datadir}/applications/*.desktop

%changelog
* Tue Jul 12 2011 Steve Huff <shuff@vecna.org> - 3.5-1
- Initial package.
