# $Id$

# Authority: dag
# Upstream: Thierry Godefroy <xdialog@free.fr>

%define real_name Xdialog

Name: xdialog
Summary: X11 drop in replacement for cdialog
Version: 2.1.1
Release: 1
License: GPL
Group: Applications/System
URL: http://xdialog.dyns.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://thgodef.nerim.net/xdialog/Xdialog-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel >= 1.2.0

Provides: Xdialog
Obsoletes: Xdialog

%description
Xdialog is designed to be a drop in replacement for the cdialog program.
It converts any terminal based program into a program with an X-windows
interface. The dialogs are easier to see and use and Xdialog adds even
more functionalities (help button+box, treeview, editbox, file selector,
range box, and much more).

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{real_name}

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}/%{real_name}-%{version}

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README
%doc samples/ doc/*.html doc/*.png
%doc %{_mandir}/man1/*
%{_bindir}/*

%changelog
* Tue Apr 29 2003 Dag Wieers <dag@wieers.com> - 2.1.1-0
- Initial package. (using DAR)
