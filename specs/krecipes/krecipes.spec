# $Id$
# Authority: dries

Summary: Recipe manager
Name: krecipes
Version: 0.9.1
Release: 2%{?dist}
License: GPL
Group: Applications/Databases
URL: http://krecipes.sourceforge.net

Source: http://dl.sf.net/krecipes/krecipes-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, kdelibs-devel, gettext, sqlite-devel

%description
Krecipes is a KDE cooking book that works with either SQLite, MySQL, or
PostgreSQL database backends, and is designed to be highly configurable.
It features configurable ingredients, creation of shopping lists, daily
recipe suggestions based on calories/diets, and much more.

%prep
%setup

%build
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_bindir}/krecipes
%{_datadir}/applnk/Utilities/krecipes.desktop
%{_datadir}/apps/krecipes/
%{_datadir}/doc/HTML/*/krecipes/
%{_datadir}/icons/*/*/*/krecipes*.png
%{_datadir}/mimelnk/application/x-krecipes*.desktop

%changelog
* Tue Apr 24 2007 Dag Wieers <dag@wieers.com> - 0.9.1-2
- Fix group tag.

* Mon Dec 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.1-1
- Initial package.
