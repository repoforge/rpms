# $Id$
# Authority: shuff
# Upstream: David F. Skoll <dfs$roaringpenguin,com>

Summary: Text-based calendar and alarm program
Name: remind
Version: 03.01.12
Release: 1%{?dist}
License: GPL
Group: Applications/Utilities
URL: http://www.roaringpenguin.com/products/remind

Source: http://www.roaringpenguin.com/files/download/remind-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: tk-devel
BuildRequires: rpm-macros-rpmforge

# don't scan the examples for autoreq/prov
%filter_requires_in %{_docdir}
%filter_provides_in %{_docdir}

%filter_setup

%description
Remind is a sophisticated calendar and alarm program. It includes the following
features:

* A sophisticated scripting language and intelligent handling of exceptions and
  holidays.
* Plain-text, PostScript and HTML output.
* Timed reminders and pop-up alarms.
* A friendly graphical front-end for people who don't want to learn the
  scripting language.
* Facilities for both the Gregorian and Hebrew calendars.
* Support for 12 different languages.

%package tk
Summary: Tk/XWindows frontend for %{name}.
Group: Applications/X11
Requires: %{name} = %{version}-%{release}
Requires: tk

%description tk
This package contains tkremind, an XWindows GUI for %{name}.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT MICROSOFT-AND-APPLE README
%doc contrib/ docs/ examples/ www/
%doc %{_mandir}/man?/*
%exclude %{_mandir}/man?/tkremind*
%{_bindir}/*
%exclude %{_bindir}/tkremind

%files tk
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/tkremind*
%{_bindir}/tkremind

%changelog
* Mon Apr 30 2012 Steve Huff <shuff@vecna.org> - 03.01.12-1
- Initial package.
