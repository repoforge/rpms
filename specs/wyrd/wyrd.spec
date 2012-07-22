# $Id$
# Authority: shuff
# Upstream: Paul Pelzl <psquared.wyrd$soodonims,com>

Summary: Curses-based frontend to Remind
Name: wyrd
Version: 1.4.5
Release: 1%{?dist}
License: GPL
Group: Applications/Utilities
URL: http://pessimization.com/software/wyrd/

Source: http://pessimization.com/software/wyrd/wyrd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: ocaml >= 3.08
BuildRequires: ocaml-camlp4 >= 3.08
BuildRequires: rpm-macros-rpmforge
Requires: less
Requires: remind >= 3.1.0

%description
Wyrd is a text-based front-end to Remind, a sophisticated calendar and alarm
program. Remind's power lies in its programmability, and Wyrd does not hide
this capability behind flashy GUI dialogs. Rather, Wyrd is designed to make you
more efficient at editing your reminder files directly. It also offers a
scrollable timetable suitable for visualizing your schedule at a glance.

%prep
%setup

%build
%configure
%{__make} opt

%install
%{__rm} -rf %{buildroot}
%{__make} install-opt DESTDIR="%{buildroot}"

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%doc %{_mandir}/man?/*
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/*

%changelog
* Mon Apr 30 2012 Steve Huff <shuff@vecna.org> - 1.4.5-1
- Initial package.
